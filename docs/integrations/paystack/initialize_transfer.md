# Initialize Transfer (Paystack)

- **Module:** `integrations/paystack/transfer.py`

- **Description:**
This internal Paystack client method initializes a transfer from your Paystack balance to a recipient account. It is primarily used for wallet withdrawals or payout-related transactions.

- **Type:** Internal Integration Call (Not a public API route)


## Request Parameters

| Name          | Type   | Required | Description                                     |
|---------------| ------ | -------- | ----------------------------------------------- |
| `reference`  | string | Yes      | Unique withdrawal or transfer reference         |
| `amount`  | Decimal | Yes      |Transfer amount          |
| `recipient`  | String | Yes      |Paystack recipient code          |



## Internal Payload Sent to Paystack
```json
{
  "source": "balance",
  "reason": "withdrawal",
  "reference": "WD_12345",
  "amount": 500000,
  "recipient": "RCP_123456"
}
```

## Payload Notes
- source is always "balance" (Paystack balance)
- reason is mapped from:
WalletTransactionPurpose.WITHDRAWAL
- amount is converted to Paystack subunit internally
- recipient must be a valid Paystack recipient code

## Success Response
- **Status Code:** `200 OK`
```json
{
  "transfer_code": "TRF_123456789",
  "reference": "WD_12345",
  "status": "pending",
  "paystack_id": 987654321
}
```


## Possible Exceptions
### Transfer Initialization Failed
- **Status Code:** `400 Bad Request`
```json
{
  "detail": "Failed to initialize transfer: <paystack response>"
}
```

### HTTP Error
- **Status Code:** `502 Bad Gateway`
```json
{
  "detail": "Paystack HTTP error: <response text>"
}
```

### Network Error
- **Status Code:** `503 Service Unavailable`
```json
{
  "detail": "Network error while initializing transfer: <error details>"
}