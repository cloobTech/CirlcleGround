# Initialize booking payment

**Enpoint:** `POST /api/v1/payments/initialize-booking-payment`

**Description:** This endpoint initializes a payment for a booking. It creates a Paystack transaction linked to a specific booking and returns payment authorization url to proceed with the transaction.

**Content-Type:** `application/json`

### Headers

| Name            | Required | Description                      |
|-----------------|----------|----------------------------------|
| Authorization   | Yes      | Bearer access token              |


### Request Parameters

| Name          | Type   | Required | Description                                     |
|---------------| ------ | -------- | ----------------------------------------------- |
| `booking_id`  | string | Yes      | Unique ID of the booking being paid for         |
| `amount_paid`  | string | Yes      | Amount the user is paying for the booking        |



## Response
### Success Response
- **Status Code:** `200 OK`
```json
{
    "authorization_url": "https://checkout.paystack.com/xyz",
    
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

#### Bad Request
- **Status Code:** `404 Bad Request`

```json
{
  "detail": "booking_id cannot be empty"
}
```

#### Booking Not Found
- **Status Code:** `404 Not Found`
```json
{
  "detail": "Booking not found"
}
```

#### Forbidden
- **Status Code:** `403 Forbidden`
```json
{
  "detail": "Only guest_user can pay for this booking"
}
```

#### Internal Server Error
- **Status Code:** `500 Internal Server Error`
```json
{
  "detail": "An error occurred while initializing booking payment"
}
```

