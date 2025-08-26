
# Payer Request

## Structure

`PayerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payers` | [`List[Payers]`](../../doc/models/payers.md) | Optional | List of Payer entity.<br>Optional.<br>Note:<br>•    Max number of payers allowed in the input is 10, if it exceeds in the input it will throw an error.<br>•    This value is configurable. Initial configuration will be 1000 and will change to 10 once SFH changes are integrated. |
| `return_basic_details_only` | `bool` | Optional | Returns only the high-level basic details of payers. Set this field to ‘true’ when only the basic details are required to get the result quicker.<br><br>**Default**: `False` |
| `include_addresses` | `bool` | Optional | Include address related fields on the response. Set this field to ‘False’ when Address fields are not required to get the result quicker.<br><br>**Default**: `False` |
| `include_bonus_parameters` | `bool` | Optional | Include the Finance Currency, used for Finance Widget, in the response<br><br>**Default**: `False` |

## Example (as JSON)

```json
{
  "ReturnBasicDetailsOnly": false,
  "IncludeAddresses": false,
  "IncludeBonusParameters": false,
  "Payers": [
    {
      "ColCoId": 78,
      "ColCoCode": 92,
      "PayerId": 126,
      "PayerNumber": "PayerNumber0",
      "PayerName": "PayerName0"
    }
  ]
}
```

