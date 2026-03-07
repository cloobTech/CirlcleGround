# Update User Notification
## Endpoint
1`POST /api/v1/notification_recipient`

## Description

This endpoint allows the backend to update a notification whenever the user views it.

## Request
This should be made with `Content-Type: application/json` and include the following parameters:


| Parameter               | Type   | Required | Description                             |Example/Notes          |
|-------------------------|--------|----------|-----------------------------------------|-----------------------|
|`notification_id`        |string  |Yes       |Country of the location                  |`"Nigeria"`            |
|`recipient_id`           |string  |Yes        |City of the location                    |`"kano"`               |
|`state`                  |string  |Yes       |State of the location                    |`"state"`              |
