from fastapi import APIRouter, Depends
from src.schemas.wallet_transaction import TopUpWallet, Withdraw
from src.models.user import User
from src.api.v1.dependencies import get_wallet_transaction_service, get_current_user
from src.services.wallet_transaction_service import WalletTransactionService



wallet_transaction_router = APIRouter(prefix="/api/v1/wallet_transactions", tags=["Wallet"])

@wallet_transaction_router.post("/me/transaction/top-up")
async def top_up_wallet(top_up_data: TopUpWallet, user: User = Depends(get_current_user), wallet_transaction_service: WalletTransactionService = Depends(get_wallet_transaction_service)):
    response = await wallet_transaction_service.top_up_account(user_id= user.id, email=user.email, top_up_data=top_up_data)
    return response



@wallet_transaction_router.post("/me/transaction/withdraw")
async def withdraw(withdrawal_data: Withdraw, user: User = Depends(get_current_user), wallet_transaction_service: WalletTransactionService = Depends(get_wallet_transaction_service)):
    response = await wallet_transaction_service.withdraw(user_id=user.id, withdrawal_data=withdrawal_data)
    return response
