from decimal import Decimal
from uuid import uuid4
from pydantic import EmailStr
from src.unit_of_work.unit_of_work import UnitOfWork
from src.integrations.paystack.transfer import paystack_transfer_client
from src.enums.enums import PaymentStatus, WalletTransactionPurpose, WalletTransactionStatus, TransactionType
from src.schemas.paystack_client_schema import InitializeTransfer
from src.schemas.wallet_transaction import Withdraw, TopUpWallet
from src.integrations.paystack.payment import paystack_payment_client
from src.core.exceptions import EntityNotFound




class WalletTransactionService:
    def __init__(self, uow_factory: UnitOfWork):
        self.uow_factory = uow_factory
    
    async def top_up_account(self, user_id: str, email: EmailStr, top_up_data: TopUpWallet):
        reference = f"WT-{uuid4().hex[:12].upper()}"

        async with self.uow_factory as uow:
            wallet = await uow.wallet_repo.get_wallet_by_user_id(user_id)
            

            await uow.wallet_transaction_repo.create_wallet_transaction(
                payload= {
                    "wallet_id": wallet.id,
                    "amount": top_up_data.amount,
                    "type": TransactionType.CREDIT,
                    "purpose": WalletTransactionPurpose.TOP_UP,
                    "status": WalletTransactionStatus.PENDING,
                    "reference": reference
                }
            )
            result = await paystack_payment_client.initialize_payment(reference=reference, email=email, amount=top_up_data.amount)

            return result["authorization_url"]
            
    
    async def withdraw(self, user_id: str, withdrawal_data: Withdraw):
        print(user_id)
        async with self.uow_factory as uow:
            reference = f"BP-{uuid4().hex[:12].upper()}"
            wallet = await uow.wallet_repo.get_wallet_by_user_id(user_id)
            bank_account = await uow.bank_account_repo.get_account_by_user_id(user_id)
            if not bank_account:
                raise EntityNotFound(message="No bank account for this user", details={
                    "recommendation": "Please add a bank account to your profile before initiating withdrawal"
                })


            if wallet.balance < withdrawal_data.amount:
                raise Exception("Insufficient balance")
            
            wallet.balance -= withdrawal_data.amount
            
            await uow.wallet_transaction_repo.create_wallet_transaction(
                 payload= {
                    "wallet_id": wallet.id,
                    "amount": withdrawal_data.amount,
                    "type": TransactionType.DEBIT,
                    "purpose": WalletTransactionPurpose.WITHDRAWAL,
                    "status": WalletTransactionStatus.PENDING,
                    "reference": reference
                }
            )
        result = await paystack_transfer_client.initialize_transfer(
            InitializeTransfer(
                amount=withdrawal_data.amount,
                recipient=bank_account.recipient,
                reference=reference
            )
        )
        return result 
    
    async def handle_top_up_success(self, reference: str):

        async with self.uow_factory as uow:
            transaction = await uow.wallet_transaction_repo.get_transaction_by_reference(reference)
            if not transaction:
                return None
            
            transaction.status = WalletTransactionStatus.SUCCESS

            wallet = await uow.wallet_repo.get_by_id(transaction.wallet_id)
            
            wallet.balance += transaction.amount
        
        return {
            "status": "success",
            "message": "Wallet top-up successful"
        }
        
    async def handle_top_up_failed(self, reference: str):

       async with self.uow_factory as uow:
            transaction = await uow.wallet_transaction_repo.get_transaction_by_reference(reference)
            if not transaction:
                return None
            
            transaction.status = WalletTransactionStatus.FAILED
        
        

    async def handle_transfer_success(self, reference: str):
        async with self.uow_factory as uow:
            transaction = await uow.wallet_transaction_repo.get_transaction_by_reference(reference)
            
            if not transaction:
                return None
            
            transaction.status = WalletTransactionStatus.SUCCESS



    async def handle_transfer_failed(self, reference: str):
        async with self.uow_factory as uow:
            payment = await uow.payment_repo.get_payment_by_reference(reference)
            if not payment:
                return None
            
            payment.payment_status = PaymentStatus.FAILED
            

