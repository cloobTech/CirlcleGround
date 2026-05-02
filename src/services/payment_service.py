from uuid import uuid4
from decimal import Decimal
from src.core.exceptions import EntityNotFound, PermissionDeniedError, ValidationError
from src.enums.enums import PaymentAction, BookingStatus, PaymentStatus, WalletTransactionPurpose, BookingPaymentStatus, WalletTransactionStatus, TransactionType
from src.unit_of_work.unit_of_work import UnitOfWork
from src.integrations.paystack.payment import paystack_payment_client

from src.utils.payment_logic import decide_payment_action



class PaymentService:
    def __init__(self, uow_factory: UnitOfWork) -> None:
        self.uow_factory = uow_factory
    
    async def initialize_booking_payment(self, user_id: str, email: str, amount_paid: Decimal, booking_id: str):
        reference = f"BP-{uuid4().hex[:12].upper()}"
        
        async with self.uow_factory as uow:
            booking = await uow.booking_repo.get_booking(booking_id)
            
            if not booking:
                raise EntityNotFound(
                    message="Booking not found",
                    details={"recommendation": "Pass the correct booking_id"}
                )
            
            if booking.status != BookingStatus.PENDING:
                raise Exception("Booking is not payable")
            
            if booking.guest_id != user_id:
                raise PermissionDeniedError(
                    message="Only the guest user can initiate payment for this booking",
                    details={"recommendation": "Pass the correct guest id"}
                )

            latest_payment = booking.payments[0] if booking.payments else None

            if latest_payment and latest_payment.payment_status == PaymentStatus.PENDING:
                raise Exception("You have a pending transaction, please wait for it to complete")
            
            total_price = booking.total_price
            minimum_payable_price = total_price / 2

            if amount_paid < minimum_payable_price:
                raise ValidationError(
                    message="Amount is below minimum allowed value",
                    details={"recommendation": f"Minimum payable price is {minimum_payable_price}"}
                )
            if amount_paid > booking.total_price:
                raise ValidationError(
                    message="Amount is above booking price",
                    details={"recommendation": f"Total booking price is {booking.total_price}"}
                )

            payment_action = decide_payment_action(booking.payment_status)

            if payment_action == PaymentAction.STOP:
                return {
                    "status": "skipped",
                    "message": "Payment already completed"
                }
            print("Got here")
            if payment_action == PaymentAction.CREATE_NEW:
                payment = await uow.payment_repo.create_payment(
                    payload={
                        "booking_id": booking_id,
                        "reference": reference,
                        "user_id": user_id,
                        "amount": amount_paid,
                    }
                )
                print("Payment created")
                amount = amount_paid

            elif payment_action == PaymentAction.CREATE_BALANCE:
                if not latest_payment:
                    raise ValueError("Cannot create balance payment: no existing payment record found")
                
                payment = latest_payment
                payment.reference = reference
                amount = booking.total_price - booking.amount_paid

            else:
                raise ValueError(f"Unhandled payment action: {payment_action}")
        print("About to return url")

        result = await paystack_payment_client.initialize_payment(reference, email, amount)
        
        return result["authorization_url"]
        

    async def handle_booking_success(self, reference: str):
        async with self.uow_factory as uow:
            
            payment = await uow.payment_repo.get_payment_by_reference(reference)
            
            
            if not payment:
                return None     
            
            wallet = await uow.wallet_repo.get_wallet_by_user_id(payment.booking.space.host_id)
            wallet.balance += payment.amount
            
            await uow.wallet_transaction_repo.create_wallet_transaction(
                payload = {
                "wallet_id": wallet.id,
                "amount": payment.amount,
                "type": TransactionType.CREDIT,
                "purpose": WalletTransactionPurpose.BOOKING_PAYMENT,
                "status": WalletTransactionStatus.SUCCESS,
                "reference": reference
            })
            
            if payment.booking.total_price == payment.amount:
                payment.booking.status = BookingStatus.CONFIRMED
                payment.booking.payment_status = BookingPaymentStatus.PAID
                payment.booking.amount_paid = payment.amount
            elif payment.booking.total_price > payment.amount:
                payment.booking.status = BookingStatus.PENDING
                payment.booking.payment_status = BookingPaymentStatus.PARTIALLY_PAID
                payment.booking.amount_paid = payment.amount

            payment.payment_status = PaymentStatus.SUCCESS

            return{
                "status": "success"
            }
            


    async def handle_booking_failed(self, reference):
        async with self.uow_factory as uow:
            payment = await uow.payment_repo.get_payment_by_reference(reference)
            if not payment:
                return None
            
            payment.booking.status = BookingStatus.PENDING
            payment.payment_status = PaymentStatus.FAILED

            return payment