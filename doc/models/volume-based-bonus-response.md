
# Volume Based Bonus Response

## Structure

`VolumeBasedBonusResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `configuration` | [`List[BonusConfiguration]`](../../doc/models/bonus-configuration.md) | Optional | - |
| `current_period_consumption` | [`List[CurrentVolume]`](../../doc/models/current-volume.md) | Optional | - |
| `historical_bonus_paid` | [`List[BonusHistory]`](../../doc/models/bonus-history.md) | Optional | - |

## Example (as JSON)

```json
{
  "Configuration": [
    {
      "PricingAccountId": 94,
      "PricingAccountNumber": "PricingAccountNumber0",
      "PricingAccountShortName": "PricingAccountShortName2",
      "PricingAccountFullName": "PricingAccountFullName8",
      "FeeRuleId": 254
    },
    {
      "PricingAccountId": 94,
      "PricingAccountNumber": "PricingAccountNumber0",
      "PricingAccountShortName": "PricingAccountShortName2",
      "PricingAccountFullName": "PricingAccountFullName8",
      "FeeRuleId": 254
    },
    {
      "PricingAccountId": 94,
      "PricingAccountNumber": "PricingAccountNumber0",
      "PricingAccountShortName": "PricingAccountShortName2",
      "PricingAccountFullName": "PricingAccountFullName8",
      "FeeRuleId": 254
    }
  ],
  "CurrentPeriodConsumption": [
    {
      "FeeRuleId": 146,
      "FeeRuleDescription": "FeeRuleDescription8",
      "Month": 174,
      "Year": "Year2",
      "TotalVolume": 254.28
    },
    {
      "FeeRuleId": 146,
      "FeeRuleDescription": "FeeRuleDescription8",
      "Month": 174,
      "Year": "Year2",
      "TotalVolume": 254.28
    }
  ],
  "HistoricalBonusPaid": [
    {
      "PayerId": 156,
      "PayerNumber": "PayerNumber0",
      "PayerShortName": "PayerShortName4",
      "PayerFullName": "PayerFullName0",
      "AccountId": 216
    }
  ]
}
```

