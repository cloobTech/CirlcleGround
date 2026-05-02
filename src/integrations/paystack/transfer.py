import httpx
from decimal import Decimal
from pydantic import EmailStr
from src.core.pydantic_confirguration import config
from src.schemas.paystack_client_schema import CreateRecipient, InitializeTransfer, InitializePaymentResponseSchema, PaymentStatusResponseSchema, PaystackBankResolveResponseSchema
from src.schemas.bank_schema import CreateBank
from src.enums.enums import WalletTransactionPurpose
from src.core.exceptions import PaystackTransferInitializationError, PaystackVerificationError, FetchBankError, PaystackConnectionError, PaystackPaymentInitializationError, PaystackResponseError, PaystackTimeoutError, BankResolveError



class PaystackClient:

    def headers(self):
        return{
            "Authorization": f"Bearer {config.PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json"
        }
    
    def to_subunit(self, amount: Decimal):
        return int(amount * 100)
    
    async def initialize_transfer(self, transfer_data: InitializeTransfer) -> dict:
            try:
                async with httpx.AsyncClient(timeout=20) as client:
                    response = await client.post(
                        url=config.PAYSTACK_TRANSFER_URL,
                        headers=self.headers(),
                        json={
                            "source": "balance",
                            "reason": WalletTransactionPurpose.WITHDRAWAL.value,
                            "reference": transfer_data.reference,
                            "amount": self.to_subunit(transfer_data.amount),
                            "recipient": transfer_data.recipient,
                        }
                    )

                    response.raise_for_status()

                    data: dict = response.json()

                    if not data.get("status"):
                        raise PaystackTransferInitializationError(
                        message= f"Failed to initialize transfer: {data}"
                        )

                    transfer = data["data"]

                    return {
                        "transfer_code": transfer["transfer_code"],
                        "reference": transfer["reference"],
                        "status": transfer["status"],
                        "paystack_id": transfer["id"],
                    }

            except httpx.HTTPStatusError as exc:
                raise PaystackTransferInitializationError(
                    f"Paystack HTTP error: {exc.response.text}"
                ) from exc

            except httpx.RequestError as exc:
                raise PaystackTransferInitializationError(
                    f"Network error while initializing transfer: {str(exc)}"
                ) from exc
                
paystack_transfer_client = PaystackClient()
