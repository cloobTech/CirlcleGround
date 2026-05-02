# Initiate payment (Paystack)
- **Module:** `integrations/paystack/payment.py`
- **Description:** This internal Paystack client method initializes a payment transaction with Paystack and returns authorization url required for customer checkout.

This method in this system is used for:

Booking payments
Wallet top-ups

## Request Parameters
| Name          | Type   | Required | Description                                     |
|---------------| ------ | -------- | ----------------------------------------------- |
| `reference`  | string | Yes      | Unique internal transaction reference         |
| `email`  | string | Yes      | Customer email address         |
| `amount`  | Decimal | Yes      | Payment amount in major unit (e.g. NGN)         |

## Internal Processing Flow
### Payload Preparation
**The method:**

- converts amount to Paystack subunit (kobo)
- attaches unique reference
- sends request to paystack with the url provided

**Example Payload Sent to Paystack**
```json
{
  "email": "user@email.com",
  "amount": 500000,
  "reference": "WT_12345"
}
```

## Response
### Success Response
```json
{
  "authorization_url": "https://checkout.paystack.com/xyz",
  "reference": "WT_12345",
  "access_code": "ACCESS_67890"
}
```

### Possible Exceptions
#### Timeout Error
- **Status Code:** `504 Gateway Timeout`
```json
{
  "detail": "Paystack request timed out."
}
```
#### HTTP Error
- **Status Code:** `502 Bad Gateway`
```json
{
  "detail": "Paystack HTTP error: <response text>"
}
```

#### Connection Error
- **Status Code:** `503 Service Unavailable`
```json
{
  "detail": "Unable to connect to Paystack."
}
```

#### Invalid Response
- **Status Code:** `502 Bad Gateway`
```json
{
  "detail": "Invalid response received from Paystack."
}
```

#### Payment Initialization Failed
- **Status Code:** `400 Bad Request`
```json
{
  "detail": "Payment initialization failed."
}
```
