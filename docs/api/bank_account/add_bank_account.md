# Add Bank Account
**Endpoint:** `POST /api/v1/bank_accounts/`
**Description:** This endpoint allows an authenticated user to add and save a bank account to their profile. The bank account is validated before being stored for future withdrawals.

**Content-Type:** `application/json`

## Headers

| Name            | Required | Description                      |
|-----------------|----------|----------------------------------|
| Authorization   | Yes      | Bearer access token              |


## Request Parameters
| Name          | Type   | Required | Description                                     |
|---------------| ------ | -------- | ----------------------------------------------- |
| `currency`  | string | Yes      | Currency type (default: NGN)         |
| `bank_code`  | string | Yes      | Bank identification code         |
| `account_name`  | string | Yes      | Name on the account        |
| `account_number`  | string | Yes      | Bank account number        |



## Response
### Success Response
- **Status Code:** `200 OK`
```json
{
  "bank_account_id": "ba_12345",
  "user_id": "usr_001",
  "account_name": "John Doe",
  "account_number": "0123456789",
  "bank_code": "044",
  "currency": "NGN",
  "is_verified": true
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

#### Invalid Bank Details
- **Status Code:** `400 Bad Request`
```json
{
  "detail": "Invalid bank account details"
}
```

#### Bank Resolution Failed
- **Status Code:** `400 Bad Request`
```json
{
  "detail": "Unable to resolve bank account"
}
```

#### Duplicate Account
- **Status Code:** `409 Conflict`
```json
{
  "detail": "Bank account already exists"
}
```

#### Forbidden
- **Status Code:** `403 Forbidden`
```json
{
  "detail": "You are not allowed to perform this action"
}
```

#### Internal Server Error
- **Status Code:** `500 Internal Server Error`
```json
{
  "detail": "An error occurred while adding bank account"
}
```