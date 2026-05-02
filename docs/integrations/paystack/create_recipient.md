# Create Transfer Recipient (Paystack)

- **Module:** `integrations/paystack/recipient.py`

- **Description:**
This internal Paystack client method creates a transfer recipient for bank payouts. A recipient must exist before initiating transfers or wallet withdrawals to a bank account.

- **Type:** Internal Integration Call (Not a public API route)


## Request Parameters

| Name          | Type   | Required | Description                                     |
|---------------| ------ | -------- | ----------------------------------------------- |
| `account_name`  | string | Yes      | Name on the account         |
| `bank_code`  | string | Yes      | Paystack-supported bank code         |
| `currency`  | string | Yes      | Currency code (e.g. NGN)         |
| `account_number`  | string | Yes      | 	Bank account number         |




## Internal Payload Sent to Paystack
```json
{
  "type": "nuban",
  "name": "John Doe",
  "bank_code": "044",
  "currency": "NGN",
  "account_number": "0123456789"
}
```

## Payload Notes
- type is fixed as "nuban" for Nigerian bank accounts
- bank_code must match Paystack-supported bank codes
- account_number should be validated before submission when possible

## Success Response
- **Status Code:** `200 OK`
```json
{
  "recipient_code": "RCP_123456789"
}
```

## Possible Exceptions
### Recipient Creation Failed
- **Status Code:** ` 400 Bad Request`
```json
{
  "detail": "Failed to create recipient: <paystack response>"
}
```

### HTTP Error
- **Status Code:** `502 Bad Gateway`
```json
{
  "detail": "Paystack HTTP error: <response text>"
}
```

### Timeout Error
- **Status Code:** `504 Gateway Timeout`
```json
{
  "detail": "Paystack request timed out."
}
```


### Network Error
- **Status Code:** `503 Service Unavailable`
```json
{
  "detail": "Unable to connect to Paystack."
}
```

### Invalid Response
- **Status Code:** `502 Bad Gateway`
```json
{
  "detail": "Invalid response received from Paystack."
}
```