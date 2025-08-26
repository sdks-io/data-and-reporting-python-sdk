
# Customer Price List Res

## Structure

`CustomerPriceListRes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | Unique identifier for the request. This will be played back in the response from the request. |
| `status` | `str` | Optional | Status of the request |
| `data` | [`List[CustomerPriceListResponse]`](../../doc/models/customer-price-list-response.md) | Optional | - |

## Example (as JSON)

```json
{
  "RequestId": "0e6fb42a-51b0-43b2-f010-92f822657f6a",
  "Status": "SUCCESS",
  "Data": [
    {
      "PriceList": [
        {
          "Date": "Date8",
          "Day": "Day4",
          "Type": "Type0",
          "PriceListId": 210,
          "PriceListDescription": "PriceListDescription0"
        },
        {
          "Date": "Date8",
          "Day": "Day4",
          "Type": "Type0",
          "PriceListId": 210,
          "PriceListDescription": "PriceListDescription0"
        }
      ]
    }
  ]
}
```

