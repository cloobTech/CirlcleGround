import httpx
from src.core.pydantic_confirguration import config
from src.schemas.paystack_client_schema import PaystackBankResolveResponseSchema
from src.schemas.bank_schema import CreateBank
from src.core.exceptions import FetchBankError, PaystackConnectionError, PaystackResponseError, PaystackTimeoutError, BankResolveError


class PaystackClient:

    def headers(self):
        return{
            "Authorization": f"Bearer {config.PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json"
        }
    
    async def get_banks(self, currency: str = "NGN"):
        url = config.PAYSTACK_BANK_CODES_URL

        try:
            async with httpx.AsyncClient(timeout=20) as client:
                response = await client.get(
                    url=url,
                    params={"currency": currency},
                    headers=self.headers(),
                )

                response.raise_for_status()

                data: dict = response.json()

        except httpx.TimeoutException as exc:
            raise PaystackTimeoutError(
                message="Fetching banks timed out."
            ) from exc

        except httpx.HTTPStatusError as exc:
            raise FetchBankError(
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
            raise FetchBankError(
                message= "Error while fetching banks."  
            )

        banks = data["data"]

        return [
            CreateBank(
                name=bank["name"],
                code=bank["code"],
                currency=bank["currency"],
            )
            for bank in banks
        ]
    
    async def resolve_bank(self, account_number: str, bank_code: str):
        url = config.PAYSTACK_BANK_RESOLVE_URL
        params = {
            "account_number": account_number,
            "bank_code": bank_code
        }
        try:
            async with httpx.AsyncClient(timeout=20) as client:
                response = await client.get(
                    url=url,
                    params=params,
                    headers=self.headers(),
                )

                response.raise_for_status()

                data: dict = response.json()

        except httpx.TimeoutException as exc:
            raise PaystackTimeoutError(
                message="Bank resolution request timed out."
            ) from exc

        except httpx.HTTPStatusError as exc:
            raise BankResolveError(
                message=f"Unable to resolve bank"
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
            raise BankResolveError(
                message=data.get(
                    "message",
                    "Failed to resolve bank account.",
                )
            )

        account_data = data["data"]

        return PaystackBankResolveResponseSchema(
            account_name=account_data["account_name"],
            account_number=account_data["account_number"],
        )


paystack_bank_client = PaystackClient()