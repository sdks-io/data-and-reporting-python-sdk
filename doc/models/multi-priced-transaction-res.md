
# Multi Priced Transaction Res

## Structure

`MultiPricedTransactionRes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | Unique identifier for the request. This will be played back in the response from the request. |
| `status` | `str` | Optional | Status of the request |
| `data` | [`List[MultiPricedTransactionResponse]`](../../doc/models/multi-priced-transaction-response.md) | Optional | - |
| `page` | `int` | Optional | Current Page |
| `total_records` | `int` | Optional | Total row count matched for the given input criteria |
| `total_pages` | `int` | Optional | Calculated page count based on page size from the incoming API request and total number of rows matched for the given input criteria. Return 1 if the page size is -1 as all records are returned. |
| `page_size` | `int` | Optional | Page Size – Number of records to show on current page. |
| `warnings` | [`List[Warning]`](../../doc/models/warning.md) | Optional | A list of Warning entity.<br>This entity will hold the details of the scheduled System Outages of any dependent applications of this service.<br>Note: If there is no scheduled outage information available, in the configuration in AMS, for this service, this parameter won’t be present in output. |

## Example (as JSON)

```json
{
  "RequestId": "0e6fb42a-51b0-43b2-f010-92f822657f6a",
  "Status": "SUCCESS",
  "Page": 1,
  "TotalRecords": 100,
  "TotalPages": 100,
  "PageSize": 100,
  "Data": [
    {
      "Transactions": [
        {
          "Type": "Type2",
          "CardId": 86,
          "CardPAN": "CardPAN4",
          "CardExpiry": "CardExpiry0",
          "TransactionDate": "TransactionDate0"
        }
      ]
    },
    {
      "Transactions": [
        {
          "Type": "Type2",
          "CardId": 86,
          "CardPAN": "CardPAN4",
          "CardExpiry": "CardExpiry0",
          "TransactionDate": "TransactionDate0"
        }
      ]
    }
  ]
}
```

