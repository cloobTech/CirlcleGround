import httpx
from decimal import Decimal
from pydantic import EmailStr
from src.core.pydantic_confirguration import config
from src.schemas.paystack_client_schema import InitializePaymentResponseSchema, PaymentStatusResponseSchema
from src.core.exceptions import  PaystackVerificationError, PaystackConnectionError, PaystackPaymentInitializationError, PaystackResponseError, PaystackTimeoutError,





class PaystackClient:  

    def headers(self):
        return{
            "Authorization": f"Bearer {config.PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json"
        }
    
    def to_subunit(self, amount: Decimal):
        return int(amount * 100)

    async def initialize_payment(self, reference: str, email: EmailStr, amount: Decimal,
) -> InitializePaymentResponseSchema:
    

        payload = {
            "email": str(email),
            "amount": self.to_subunit(amount),
            "reference": reference,
        }

        try:
            async with httpx.AsyncClient(timeout=20) as client:
                response = await client.post(
                    url=config.PAYSTACK_PAYMENT_URL,
                    json=payload,
                    headers=self.headers(),
                )

                response.raise_for_status()

                data: dict = response.json()

        except httpx.TimeoutException as exc:
            raise PaystackTimeoutError(message="Paystack request timed out.") from exc

        except httpx.HTTPStatusError as exc:
            raise PaystackPaymentInitializationError(
               message= f"Paystack HTTP error: {exc.response.text}"
            ) from exc

        except httpx.RequestError as exc:
            raise PaystackConnectionError(
                message="Unable to connect to Paystack."
            ) from exc

        except ValueError as exc:
            raise PaystackResponseError(
               message= "Invalid response received from Paystack."
            ) from exc

        if not data.get("status"):
            raise PaystackPaymentInitializationError(
                data.get("message", "Payment initialization failed.")
            )

        payment_data = data["data"]

        return InitializePaymentResponseSchema(
            authorization_url=payment_data["authorization_url"],
            reference=payment_data["reference"],
            access_code=payment_data["access_code"],
        )
    


    async def get_payment_status(self, reference: str):
        url = config.PAYSTACK_PAYMENT_URL/{reference}
        
            try:
                async with httpx.AsyncClient(timeout=20) as client:
                    response = await client.get(
                        url=url,
                        headers=self.headers(),
                    )

                    response.raise_for_status()

                    data: dict = response.json()

            except httpx.TimeoutException as exc:
                raise PaystackTimeoutError(
                    message="Paystack verification request timed out."
                ) from exc

            except httpx.HTTPStatusError as exc:
                raise PaystackVerificationError(
                    message=f"Paystack HTTP error: {exc.response.text}"
                ) from exc

            except httpx.RequestError as exc:
                raise PaystackConnectionError(
                    message="Unable to connect to Paystack."
                ) from exc

            except ValueError as exc:
                raise PaystackResponseError(
                    message="Invalid response received from Paystack."
                ) from exc

            if not data.get("status"):
                raise PaystackVerificationError(
                    message=data.get(
                        "message",
                        "Paystack payment verification failed.",
                    )
                )

            payment_data = data["data"]

            return PaymentStatusResponseSchema(
                status=payment_data["status"],
                email=payment_data["customer"]["email"],
                reference=payment_data["reference"],
                amount=Decimal(payment_data["amount"]) / 100,
            )

paystack_payment_client = PaystackClient()