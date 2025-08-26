
# Fuel Consumption Response

## Structure

`FuelConsumptionResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | Unique identifier for the request. This will be played back in the response from the request. |
| `status` | `str` | Optional | Status of the request |
| `data` | [`List[FuelConsumptionData]`](../../doc/models/fuel-consumption-data.md) | Optional | - |
| `warnings` | [`List[Warning]`](../../doc/models/warning.md) | Optional | A list of Warning entity.<br>This entity will hold the details of the scheduled System Outages of any dependent applications of this service.<br>Note: If there is no scheduled outage information available, in the configuration in AMS, for this service, this parameter won’t be present in output. |

## Example (as JSON)

```json
{
  "RequestId": "0e6fb42a-51b0-43b2-f010-92f822657f6a",
  "Status": "SUCCESS",
  "Data": [
    {
      "AccountName": "AccountName4",
      "AccountNumber": "AccountNumber8",
      "PayerName": "PayerName4",
      "PayerNumber": "PayerNumber6",
      "CardNumber": "CardNumber6"
    },
    {
      "AccountName": "AccountName4",
      "AccountNumber": "AccountNumber8",
      "PayerName": "PayerName4",
      "PayerNumber": "PayerNumber6",
      "CardNumber": "CardNumber6"
    },
    {
      "AccountName": "AccountName4",
      "AccountNumber": "AccountNumber8",
      "PayerName": "PayerName4",
      "PayerNumber": "PayerNumber6",
      "CardNumber": "CardNumber6"
    }
  ],
  "Warnings": [
    {
      "Message": "Message0",
      "Type": "Type4"
    },
    {
      "Message": "Message0",
      "Type": "Type4"
    }
  ]
}
```

