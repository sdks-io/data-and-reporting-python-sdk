
# Update Odometer Response

## Structure

`UpdateOdometerResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_reference` | `int` | Optional | Main reference number for tracking. |
| `update_odometer_references` | [`List[UpdateOdometerReference]`](../../doc/models/update-odometer-reference.md) | Optional | - |

## Example (as JSON)

```json
{
  "ServiceReference": 140,
  "UpdateOdometerReferences": [
    {
      "SalesItemId": 206,
      "UpdateOdometerReferenceId": 242
    },
    {
      "SalesItemId": 206,
      "UpdateOdometerReferenceId": 242
    },
    {
      "SalesItemId": 206,
      "UpdateOdometerReferenceId": 242
    }
  ]
}
```

