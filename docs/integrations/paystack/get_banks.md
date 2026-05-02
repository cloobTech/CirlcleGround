# Get Supported Banks (Paystack)

- **Module:** `integrations/paystack/banks.py`


- **Description:**
This internal Paystack client method retrieves all Paystack-supported banks for a specified currency. It is commonly used for bank account onboarding, withdrawal setup, and bank code validation.

- **Type:** Internal Integration Call (Not a public API route)


## Request Parameters

| Name          | Type   | Required | Description                                     |
|---------------| ------ | -------- | ----------------------------------------------- |
| `currency`  | string | Yes      | Currency code used to filter supported banks         |


## Internal Request Sent to Paystack
- **Query Parameters**
```json
{
  "currency": "NGN"
}
```


## Success Response
- **Status Code:** `200 OK`
```json
[
  {
    "name": "Access Bank",
    "code": "044",
    "currency": "NGN"
  },
  {
    "name": "Zenith Bank",
    "code": "057",
    "currency": "NGN"
  }
]
```

## Possible Exceptions
### Timeout Error
- **Status Code:** `504 Gateway Timeout`
```json
{
  "detail": "Fetching banks timed out."
}
```

### HTTP Error
- **Status Code:** `502 Bad Gateway`
```json
{
  "detail": "Paystack HTTP error: <response text>"
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

### Fetch Failed
- **Status Code:** `400 Bad Request`
```json
{
  "detail": "Error while fetching banks."
}
```