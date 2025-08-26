
# Card Group Req

## Structure

`CardGroupReq`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filters` | [`CardGroupRequest`](../../doc/models/card-group-request.md) | Optional | - |
| `page` | `int` | Optional | Page Number (as shown to the users)<br><br>**Default**: `1` |
| `page_size` | `int` | Optional | Page Size – Number of records to show on a page.<br><br>**Default**: `50` |

## Example (as JSON)

```json
{
  "Page": 1,
  "PageSize": 100,
  "Filters": {
    "ColCoId": 0,
    "ColCoCode": 14,
    "PayerId": 48,
    "PayerNumber": "PayerNumber0",
    "Account": [
      {
        "AccountId": 66,
        "AccountNumber": "AccountNumber2"
      },
      {
        "AccountId": 66,
        "AccountNumber": "AccountNumber2"
      }
    ]
  }
}
```

