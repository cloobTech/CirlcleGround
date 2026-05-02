from fastapi import APIRouter, Request, HTTPException
from src.auth.security import verify_signature
from src.storage import db
from src.unit_of_work.unit_of_work import UnitOfWork
from src.services.payment_service import PaymentService
from src.services.wallet_transaction_service import WalletTransactionService


wb_router = APIRouter(prefix="/api/v1/webhook", tags=["Webhook"])


@wb_router.post("/")
async def webhook_enpoint(request: Request):
    print("web hook hit")
    raw_body = await request.body()
    payload: dict = await request.json()


    signature = request.headers.get("x-paystack-signature")
    if not verify_signature(raw_body, signature):
        raise HTTPException(status_code=400, detail="Invalid signature")
    
    event = payload["event"]
    reference: str = payload["data"]["reference"]


    async with db.get_session() as session:
        uow = UnitOfWork(session)
        payment_service = PaymentService(uow)
        wallet_transaction_service = WalletTransactionService(uow)
        


        
        if event == "charge.success":
            if reference.startswith("WT"):
                await wallet_transaction_service.handle_top_up_success(reference)
            elif reference.startswith("BP"):
                await payment_service.handle_booking_success(reference)

        elif event == "charge.failed":
            if reference.startswith("WT"):
                await wallet_transaction_service.handle_top_up_failed(reference)
            elif reference.startswith("BP"):
                await payment_service.handle_booking_failed(reference)
        
        elif event == "transfer.success":
            await wallet_transaction_service.handle_transfer_success(reference)
        
        elif event == "transaction.failure":
            await wallet_transaction_service.handle_transfer_failed(reference)
            
            

        return {
            "status": "success"
        }