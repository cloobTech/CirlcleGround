# Resolve Bank Account (Paystack)

- **Module:** `integrations/paystack/banks.py`

- **Description:**
This internal Paystack client method validates a bank account number against a provided bank code and returns the official account holder name. It is primarily used before bank account creation, recipient creation, or withdrawals.

- **Type:** Internal Integration Call (Not a public API route)


## Request Parameters

| Name          | Type   | Required | Description                                     |
|---------------| ------ | -------- | ----------------------------------------------- |
| `account_number`  | string | Yes      | Bank account number to validate         |
| `bank_code`  | string | Yes      | Paystack-supported bank code         |



## Internal Request Sent to Paystack
**Query Parameters:**
```json
{
  "account_number": "0123456789",
  "bank_code": "044"
}
```

## Success Response
- **Status Code:** `200 OK`
```json
{
  "account_name": "John Doe",
  "account_number": "0123456789"
}
```

## Possible Exceptions
### Timeout Error
- **Status Code:** `504 Gateway Timeout`
```json
{
  "detail": "Bank resolution request timed out."
}
```

### Bank Resolution Failed
- **Status Code:** `400 Bad Request`
```json
{
  "detail": "Unable to resolve bank"
}
```

### Connection Error
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

