
# Finance Currency 2

## Structure

`FinanceCurrency2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_code` | `str` | Optional | Currency ISO Code used for the Finance Widget. |
| `currency_symbol` | `str` | Optional | Currency Symbol |
| `invoice_exchange_rate` | `float` | Optional | Factor to be used for converting the amounts in invoice currency to finance widget currency. (If finance currency is same as invoice currency, then the value of this field will be “1” so that the value does not change) |
| `credit_limit_exchange_rate` | `float` | Optional | Factor to be used for converting the amounts in credit limit currency to finance widget currency. (If finance currency is same as credit limit currency, then the value of this field will be “1” so that the value does not change) |

## Example (as JSON)

```json
{
  "CurrencyCode": "EUR",
  "CurrencySymbol": "€",
  "Invoice_ExchangeRate": 1.0,
  "CreditLimit_ExchangeRate": 1.0
}
```

