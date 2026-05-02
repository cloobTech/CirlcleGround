from src.enums.enums import PaymentAction
from src.enums.enums import BookingPaymentStatus



def decide_payment_action(status: BookingPaymentStatus):
    if status == BookingPaymentStatus.PAID  :
        return PaymentAction.STOP

    if status in (BookingPaymentStatus.UNPAID, BookingPaymentStatus.REFUNDED, BookingPaymentStatus.DECLINED):
        return PaymentAction.CREATE_NEW
    
    if status == BookingPaymentStatus.PARTIALLY_PAID:
        return PaymentAction.CREATE_BALANCE
    
    
    else: 
        raise ValueError(f"Unhandled booking payment status: {status}")