import httpx
from src.core.pydantic_confirguration import config
from src.schemas.paystack_client_schema import CreateRecipient


class PaystackClient:   
    
    def headers(self):
        return{
            "Authorization": f"Bearer {config.PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json"
        } 
    
    async def create_recipient(self, recipient_data: CreateRecipient):
        async with httpx.AsyncClient(timeout=20) as client:
            url = config.PAYSTACK_RECIPIENT_URL

            response = await client.post(url=url, json={
                "type": "nuban",
                "name": recipient_data.account_name,
                "bank_code": recipient_data.bank_code,
                "currency": recipient_data.currency,
                "account_number": recipient_data.account_number
            }, headers=self.headers())
            data: dict = response.json()

            if not data.get("status"):
                raise Exception(f"Failed to create recipient: {data}")
            c = data["data"]

            return{
                "recipient_code": c["recipient_code"]
            }
        

paystack_recipient_client = PaystackClient()