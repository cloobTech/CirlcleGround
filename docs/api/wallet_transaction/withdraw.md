# Withdraw
**Endpoint:** `POST /api/v1/wallet_transactions/me/transaction/withdraw`
**Description:** This endpoint allows an authenticated user to withdraw funds from their wallet to a linked bank account. It initiates a withdrawal transaction with paystack and processes payout through the wallet transaction service.
**Content-Type:** `application/json`

### Headers

| Name            | Required | Description                      |
|-----------------|----------|----------------------------------|
| Authorization   | Yes      | Bearer access token              |


### Request Parameters

| Name          | Type   | Required | Description                                     |
|---------------| ------ | -------- | ----------------------------------------------- |
| `amount`  | string | Yes      | Unique ID of the booking being paid for         |


## Response
### Success Response
- **Status Code:** `200 OK`
```json
{
  "transfer_code": "TRF_123456789",
  "reference": "WD_REF_98765",
  "status": "pending",
  "paystack_id": 987654321    
}
```

### Error Response
#### Unauthorized
- **Status Code:** `401 Unauthorized`
```json
{
  "detail": "Could not validate credentials"
}
```

#### Insufficient Balance
- **Status Code:** `400 Bad Request`
```json
{
  "detail": "Insufficient wallet balance"
}
```

#### Invalid Withdrawal Data
- **Status Code:** `400 Bad Request`
```json
{
  "detail": "Invalid withdrawal request data"
}
```

#### Bank Resolution Failed
- **Status Code:** `400 Bad Request`
```json
{
  "detail": "Unable to resolve bank account"
}
```

#### Forbidden
- **Status Code:** `403 Forbidden`
```json
{
  "detail": "You are not allowed to perform this withdrawal"
}
```

#### Internal Server Error
- **Status Code:** `500 Internal Server Error`
```json
{
  "detail": "An error occurred while processing withdrawal"
}
```