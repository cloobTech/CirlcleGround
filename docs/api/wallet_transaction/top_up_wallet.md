# Top-up Wallet
**Endpoint:** `POST /api/v1/wallet_transactions/me/transaction/top-up`
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
  "authorization_url": "https://checkout.paystack.com/xyz"
}
```

### Error Responses
#### Unauthorized

- **Status Code:** `401 Unauthorized`
```json
{
  "detail": "Could not validate credentials"
}
```

#### Wallet Not Found
- **Status Code:** `404 Not Found`
```json
{
  "detail": "Wallet not found for user"
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
  "detail": "An error occurred while processing wallet top-up"
}