import httpx
from decimal import Decimal
from pydantic import EmailStr
from src.core.pydantic_confirguration import config
from src.schemas.paystack_client_schema import InitializePaymentResponseSchema, PaymentStatusResponseSchema
from src.core.exceptions import  PaystackVerificationError, PaystackConnectionError, PaystackPaymentInitializationError, PaystackResponseError, PaystackTimeoutError
from src.enums.enums import PaymentMethod, Currency





class PaystackClient:  

    def headers(self):
        return{
            "Authorization": f"Bearer {config.PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json"
        }
    
    async def create_customer(self, email: str, first_name: str, last_name: str, phone_number: str):
        payload={
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number
        }
        url= config.PAYSTACK_CUSTOMER_URL
        try:
            async with httpx.AsyncClient(timeout=20) as client:
                response = await client.post(
                    url=url,
                    json=payload,
                    headers=self.headers()
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
        
        customer_code = data["data"]["customer_code"]
        return customer_code



    
    async def initialize_card_authorization(self, email: str, customer_code: str, currency: Currency):
        payload={
            "email": email,
            "customer_code": customer_code,
            "channel": PaymentMethod.CARD,
            "currency": currency
            
        }

        try:
            async with httpx.AsyncClient(timeout=20) as client:

                response = await client.post(
                    url=config.PAYSTACK_AUTHORIZATION_URL,
                    json=payload,
                    headers=self.headers()
                )
                # print(f"Status: {response.status_code}")
                # print(f"Body: {response.text}") 
                response.raise_for_status()
                 
                data: dict = response.json()
        
        except httpx.TimeoutException as exc:
            raise PaystackTimeoutError(message="Paystack request timed out.") from exc

        except httpx.HTTPStatusError as exc:
            print(exc.response.status_code)
            print(exc.response.text)  
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
        

        return payment_data["authorization_url"]


paystack_customer_client = PaystackClient()