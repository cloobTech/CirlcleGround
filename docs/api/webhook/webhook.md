# Paystack Webhook Handler
**Endpoint:** `POST /api/v1/webhook/`

**Description:** This endpoint receives event notifications from Paystack and updates internal payment, booking, and wallet transaction states accordingly. It is the core mechanism for confirming asynchronous payment and transfer outcomes.

**Content-Type:** `application/json`

## Headers
| Header Name          | Required | Description                                        |
| -------------------- | -------- | -------------------------------------------------- |
| x-paystack-signature | Yes      | HMAC signature used to verify request authenticity |

This request can fail if signature verification is rejected

## Example of event payload
Paystack sends event-based payloads in the following structure:
```json
{
  "event": "charge.success",
  "data": {
    "reference": "WT_12345",
    "status": "success",
    "amount": 5000,
    "id": 987654321
  }
}
```

## Supported Events
### Charge Success
**Event:** charge.success
**Behavior:** 
If reference starts with WT → wallet top-up success handler is triggered,
If reference starts with BP → booking payment success handler is triggered.

**Internal Actions:**
Update wallet balance OR booking payment status,
Mark transaction as successful.


### Charge Failed
**Event:** charge.failed
**Behavior:**
If reference starts with WT → wallet top-up failure handler is triggered or
If reference starts with BP → booking payment failure handler is triggered

**Internal Actions:**
Mark transaction as failed and
Prevent wallet credit or booking confirmation

### Transfer Success
**Event:** transfer.success
**Behavior:**
Used for wallet withdrawal payouts and
calls transfer success handler in wallet service

**Internal Actions:**
Mark withdrawal as successful,
Update transaction status,
Finalize payout record.

### Transfer Failure
**Event:** transfer.failure
**Behavior:**
Handles failed payout or transfer attempts

**Internal Actions:**
Mark transfer as failed



## Response
### Success Response
- **Status Code:** `200 OK`
```json
{
  "status": "success"
}
```

### Error Responses
#### Invalid Signature
- **Status Code:** `400 Bad Request`
```json
{
  "detail": "Invalid signature"
}
```

#### Invalid Payload
- **Status Code:** `400 Bad Request`
```json
{
  "detail": "Invalid webhook payload"
}
```

#### Internal Server Error
- **Status Code:** `500 Internal Server Error`
```json
{
  "detail": "An error occurred while processing webhook"
}