from fastapi import APIRouter, Depends
from src.models.user import User
from src.api.v1.dependencies import get_current_user, get_bank_service
from src.schemas.bank_schema import CreateBank
from src.services.bank_service import BankService


bank_router = APIRouter(prefix="/api/v1/banks", tags=["Banks"])

@bank_router.get("/")
async def get_banks(
    currency: str,
    bank_service: BankService = Depends(get_bank_service)
):
    response = await bank_service.get_banks(currency)
    return response