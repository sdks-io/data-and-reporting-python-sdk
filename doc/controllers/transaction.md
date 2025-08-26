# Transaction

APIs for Retrieve Transaction details about the shell cards

```python
transaction_controller = client.transaction
```

## Class Name

`TransactionController`

## Methods

* [Priced Transactions](../../doc/controllers/transaction.md#priced-transactions)
* [Priced Transactions Summary](../../doc/controllers/transaction.md#priced-transactions-summary)
* [Multipriced Transactions](../../doc/controllers/transaction.md#multipriced-transactions)
* [Card Usage Summary](../../doc/controllers/transaction.md#card-usage-summary)
* [Volume Based Bonus](../../doc/controllers/transaction.md#volume-based-bonus)
* [Volume Based Pricing](../../doc/controllers/transaction.md#volume-based-pricing)
* [Fees](../../doc/controllers/transaction.md#fees)
* [Fee Summary Response](../../doc/controllers/transaction.md#fee-summary-response)
* [Fuel Consumption](../../doc/controllers/transaction.md#fuel-consumption)
* [Update Odometer](../../doc/controllers/transaction.md#update-odometer)
* [Transaction Exceptions](../../doc/controllers/transaction.md#transaction-exceptions)
* [Recent Transactions New](../../doc/controllers/transaction.md#recent-transactions-new)
* [Priced Transactions V2](../../doc/controllers/transaction.md#priced-transactions-v2)


# Priced Transactions

This API allows querying transaction data (i.e. Priced, Billed and Unbilled sales items). It provides a flexible search criteria and supports paging.

Transactions that are posted but not yet priced, billed or that are in error will not be returned by this API. The API also supports returning Fee Items.

#### Supported operations

* Get sales items and fee transactions
  * Search by invoice status
  * Search by fixed date period
  * Search by date range
  * Search by account
  * Search by card
* Get sales items only
  * Search by transaction Id or location
  * Search by transaction posting date
  * Search by invoice number or date
  * Search by driver name or vehicle registration number
  * Search by card group
  * Search by fuel only transactions
  * Search by product

This API fetches transactions for a period based on the below parameters and priority order:

1. InvoiceNumber
2. InvoiceDate
3. FromDate, ToDate
4. PostingFromDate, PostingToDate (Can be used only when IncludeFees = false)
5. InvoiceDateFrom, InvoiceDateTo
6. Period

This API considers only one of the above set of parameters at a time. For example, if InvoiceNumber and Period are provided in the input then Period is ignored and transactions associated to the given invoice number are returned.

If none of the above parameters are provided then last 7 days transactions will be fetched.

This operation can fetch transactions that are old up to 24 (configurable) months. However, the date range between any of the ‘From’ and ‘To’ dates in the above combination cannot be more than 210 (configurable) days.

```python
def priced_transactions(self,
                       request_id,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`PriceTransactionReq`](../../doc/models/price-transaction-req.md) | Body, Optional | Priced Transaction Request Body |

## Response Type

[`PricedTransactionRes`](../../doc/models/priced-transaction-res.md)

## Example Usage

```python
request_id = 'RequestId8'

body = PriceTransactionReq(
    page=1,
    page_size=100
)

result = transaction_controller.priced_transactions(
    request_id,
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Priced Transactions Summary

This API returns the transaction summary data (i.e. Priced, Billed and Unbilled sales items). It provides a flexible search criteria.
The API also supports returning Fee Items. Transactions posted for fee items that are in error are not included in the summary.

The endpoint supports the exact same search criteria as the endpoint *transaction/prciedtransactions*.

#### Supported operations

* Get sales items and fee transactions
  * Search by invoice status
  * Search by fixed date period
  * Search by date range
  * Search by account
  * Search by card
* Get sales items only
  * Search by transaction Id or location
  * Search by transaction posting date
  * Search by invoice number or date
  * Search by driver name or vehicle registration number
  * Search by card group
  * Search by fuel only transactions
  * Search by product

This API fetches transactions for a period based on the below parameters and priority order:

1. InvoiceNumber
2. InvoiceDate
3. FromDate, ToDate
4. PostingFromDate, PostingToDate (Can be used only when IncludeFees = false)
5. InvoiceDateFrom, InvoiceDateTo
6. Period

This API considers only one of the above set of parameters at a time. For example, if InvoiceNumber and Period are provided in the input then Period is ignored and transactions associated to the given invoice number are returned.

If none of the above parameters are provided then last 7 days transactions will be fetched.

```python
def priced_transactions_summary(self,
                               request_id,
                               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`PriceTransSummaryReq`](../../doc/models/price-trans-summary-req.md) | Body, Optional | PricedSummary RequestBody |

## Response Type

[`PricedTransSummaryResp`](../../doc/models/priced-trans-summary-resp.md)

## Example Usage

```python
request_id = 'RequestId8'

result = transaction_controller.priced_transactions_summary(request_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Multipriced Transactions

This API allows querying transaction data (i.e. Priced, Billed and Unbilled sales items) for multiple payers. It provides a flexible search criteria and supports paging.

Transactions that are posted but not yet priced, billed or that are in error will not be returned by this API. The API also supports returning Fee Items.

At least one payer should be provided. Multiple payers must belong to the same payer group.

#### Supported operations

* Get sales items and fee transactions for multiple payers
  * Search by invoice status
  * Search by fixed date period
  * Search by date range
* Get sales items only for multiple payers
  * Search by transaction location
  * Search by transaction posting date
  * Search by invoice number or date
  * Search by fuel only transactions

This API fetches transactions for a period based on the below parameters and priority order:

1. InvoiceNumber
2. InvoiceDate
3. FromDate, ToDate
4. PostingFromDate, PostingToDate (Can be used only when IncludeFees = false)
5. InvoiceDateFrom, InvoiceDateTo
6. Period

This API considers only one of the above set of parameters at a time. For example, if InvoiceNumber and Period are provided in the input then Period is ignored and transactions associated to the given invoice number are returned.

If none of the above parameters are provided then last 7 days transactions will be fetched.

```python
def multipriced_transactions(self,
                            request_id,
                            body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`MultiPricedTransactionReq`](../../doc/models/multi-priced-transaction-req.md) | Body, Optional | MultiPayer RequestBody |

## Response Type

[`MultiPricedTransactionRes`](../../doc/models/multi-priced-transaction-res.md)

## Example Usage

```python
request_id = 'RequestId8'

body = MultiPricedTransactionReq(
    page=1,
    page_size=100
)

result = transaction_controller.multipriced_transactions(
    request_id,
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Card Usage Summary

This operation is to provide the expenditure analysis for a card for the past 7 months.
The response contains a daily summary of the transactions (billed & unbilled) from 1st of the last 7 months for the requested card grouped by card, site-group and product.

```python
def card_usage_summary(self,
                      request_id,
                      body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`CardUsageSummaryReq`](../../doc/models/card-usage-summary-req.md) | Body, Optional | Card Usage Summary RequestBody |

## Response Type

[`CardUsageSummaryRes`](../../doc/models/card-usage-summary-res.md)

## Example Usage

```python
request_id = 'RequestId8'

result = transaction_controller.card_usage_summary(request_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "eb621f45-a543-4d9a-a934-2f223b263c42",
  "Status": "SUCCESS",
  "Data": [
    {
      "UsageSummary": [
        {
          "Date": "20170930",
          "ProductId": 1,
          "ProductCode": "2",
          "ProductName": "Diesel AGO",
          "IsFuelProduct": true,
          "SiteGroupId": 1234,
          "SiteGroupName": "UK 9500 MOTORWAY NETWORK",
          "TotalVolume": 123.12,
          "TotalGross": 123.12,
          "TotalNet": 123.12,
          "CurrencyCode": "GBP",
          "CurrencySymbol": "£",
          "ProductGroupId": 1234,
          "ProductGroupName": "Motor gasoline"
        }
      ]
    }
  ],
  "Warnings": [
    {
      "Message": "System is down for upgradation.",
      "Type": "System Outage"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Volume Based Bonus

- This API provides the details of the bonus and/or association bonus rules setup for the given payer and that are active on the current date.
- This API also returns the details of the monthly breakup of current period consumption as well as the details of the previously calculated bonus and consumption of the applicable payers.

```python
def volume_based_bonus(self,
                      request_id,
                      body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`VolumeBasedBonusReq`](../../doc/models/volume-based-bonus-req.md) | Body, Optional | VolumeBasedBonus RequestBody |

## Response Type

[`VolumeBasedBonusRes`](../../doc/models/volume-based-bonus-res.md)

## Example Usage

```python
request_id = 'RequestId8'

result = transaction_controller.volume_based_bonus(request_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "eb621f45-a543-4d9a-a934-2f223b263c42",
  "Status": "SUCCESS",
  "Data": [
    {
      "Configuration": [
        {
          "PricingAccountId": 123456,
          "PricingAccountNumber": "GB000000123",
          "PricingAccountShortName": "MATTHEW",
          "PricingAccountFullName": "MATTHEW",
          "FeeRuleId": 1,
          "FeeRuleDescription": "NL/GAGO/D018/UP0.0120>1",
          "FeeRuleDateEffective": "20231223",
          "FeeRuleDateTerminated": "20231223",
          "BonusPaidTo": "1-Pay to Payer",
          "BonusPaidToAccountId": 123456,
          "BonusPaidToAccountNumber": "GB000000123",
          "BonusPaidToAccountShortName": "12345",
          "BonusPaidToAccountFullName": "GB000000123",
          "Frequency": "3-Weekly – Monday",
          "NextCalculationDate": "20231223",
          "PreviousCalculatedDate": "20231223",
          "FeeRuleBasis": "3-Lump Sum",
          "FeeRuleCurrencyCode": "GBP",
          "FeeRuleCurrencySymbol": "£",
          "FeeRuleAvailableFrom": "20231223",
          "FeeRuleAvailableTo": "20231223",
          "FeeRuleLocations": [
            {
              "DelcoId": "866",
              "Country": "United Kingdom",
              "CountryCode": "UK",
              "FuelNetworkId": 100007,
              "NetworkName": "VALERO",
              "SiteGroupId": 100007,
              "SiteGroupName": "VALERO ENERGY LTD",
              "SiteCode": 999493,
              "SiteId": 100007,
              "SiteName": "VALERO ENERGY LTD"
            }
          ],
          "FeeRuleProducts": [
            {
              "ProductGroupID": 3,
              "ProductGroupName": "Motor gasoline",
              "ProductCode": "30 for Diesel AGO",
              "ProductId": 30,
              "ProductName": "Diesel AGO"
            }
          ],
          "FeeRuleTiers": [
            {
              "TierMinimum": 1234,
              "TierMaximum": 1234,
              "Value": 1234.12
            }
          ],
          "AssociatedAccounts": [
            {
              "AssociatedAccountId": 12345,
              "AssociatedAccountNumber": "GB000000123",
              "AssociatedAccountShortName": "Account short name",
              "AssociatedAccountFullName": "Account Full name"
            }
          ]
        }
      ],
      "CurrentPeriodConsumption": [
        {
          "FeeRuleId": 12345,
          "FeeRuleDescription": "NL/GAGO/D018/UP0.0120>1",
          "Month": 1,
          "Year": "2018",
          "TotalVolume": 10000.78
        }
      ],
      "HistoricalBonusPaid": [
        {
          "PayerId": 12345,
          "PayerNumber": "GB000000123",
          "PayerShortName": "Jorden",
          "PayerFullName": "MATTHEW",
          "AccountId": 123456,
          "AccountNumber": "GB000000123",
          "AccountShortName": "SALT",
          "AccountFullName": "ABCD1234",
          "InvoiceAccountId": 12345,
          "InvoiceAccountNumber": "GB000000123",
          "InvoiceAccountShortName": "DFE1234",
          "InvoiceAccountFullName": "AZAD PVT LMT",
          "FeeRuleId": "12345",
          "FeeRuleDescription": "NL/GAGO/D018/UP0.0120>1",
          "FromDate": "20231223",
          "ToDate": "20231223",
          "BonusPaidTo": "5-Pay to Associated Customers",
          "FeeItemId": 12345,
          "FeeRuleBasis": "2-Percentage of Uplift",
          "FeeItemCurrencyCode": "GBP",
          "FeeItemCurrencySymbol": "$",
          "ProratedVolume": 123.12,
          "TotalVolume": 123.12,
          "FeeProduct": "1562-Bonus diesel Shell",
          "InvoiceGrossAmount": 123.12,
          "InvoiceNetAmount": 123.12,
          "InvoiceVATAmount": 123.12,
          "IsFeeCancelled": true,
          "FeeItemTierProratedVolume": 123.12,
          "FeeItemTierTotalVolume": 123.12,
          "TierMinimum": 123,
          "TierRate": 123.12
        }
      ]
    }
  ],
  "Warnings": [
    {
      "Message": "System is down for upgradation.",
      "Type": "System Outage"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Volume Based Pricing

- This API will return the details of the in arrear fee rule applied to the payer along with details of locations, products, tiers as applied.
- It will also show historical and current volume consumption and related tier applied for the following month.

```python
def volume_based_pricing(self,
                        request_id,
                        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`VolumeBasedPricingReq`](../../doc/models/volume-based-pricing-req.md) | Body, Optional | VolumeBasedPricing RequestBody |

## Response Type

[`VolumeBasedPricingRes`](../../doc/models/volume-based-pricing-res.md)

## Example Usage

```python
request_id = 'RequestId8'

result = transaction_controller.volume_based_pricing(request_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "eb621f45-a543-4d9a-a934-2f223b263c42",
  "Status": "SUCCESS",
  "Data": [
    {
      "Configuration": [
        {
          "PricingAccountId": 123456,
          "PricingAccountNumber": "GB000000123",
          "PricingAccountShortName": "ABCD1234",
          "PricingAccountFullName": "ABCD1234",
          "FeeRuleId": 12345,
          "FeeRuleDescription": "NL/GAGO/D018/UP0.0120>1",
          "FeeRuleDateEffective": "20231223",
          "FeeRuleDateTerminated": "20231223",
          "BonusPaidTo": "1-Pay to Payer",
          "BonusPaidToAccountId": 123456,
          "BonusPaidToAccountNumber": "GB000000123",
          "BonusPaidToAccountShortName": "12345",
          "BonusPaidToAccountFullName": "GB000000123",
          "Frequency": "3-Weekly – Monday",
          "NextCalculationDate": "20231223",
          "PreviousCalculatedDate": "20231223",
          "FeeRuleBasis": "3-Lump Sum",
          "FeeRuleCurrencyCode": "GBP",
          "FeeRuleCurrencySymbol": "£",
          "FeeRuleAvailableFrom": "20231223",
          "FeeRuleAvailableTo": "20231223",
          "FeeRuleLocations": [
            {
              "DelcoId": "866",
              "Country": "United Kingdom",
              "CountryCode": "UK",
              "FuelNetworkId": 100007,
              "NetworkName": "VALERO",
              "SiteGroupId": 100007,
              "SiteGroupName": "VALERO ENERGY LTD",
              "SiteCode": 999493,
              "SiteId": 100007,
              "SiteName": "VALERO ENERGY LTD"
            }
          ],
          "FeeRuleProducts": [
            {
              "ProductGroupID": 3,
              "ProductGroupName": "Motor gasoline",
              "ProductCode": "30 for Diesel AGO",
              "ProductId": 30,
              "ProductName": "Diesel AGO"
            }
          ],
          "FeeRuleTiers": [
            {
              "TierMinimum": 1234,
              "TierMaximum": 1234,
              "Value": 1234.12
            }
          ]
        }
      ],
      "CurrentPeriodConsumption": [
        {
          "FeeRuleId": 12345,
          "FeeRuleDescription": "NL/GAGO/D018/UP0.0120>1",
          "PriceRuleID": 100005,
          "PriceRuleDescription": "PL/GAGO/GMOT/UL0.055",
          "TotalVolume": 10000.78,
          "NextFeeCreationDate": "20231223"
        }
      ],
      "History": [
        {
          "FromDate": "20231223",
          "ToDate": "20231223",
          "FeesRuleID": 8081,
          "FeesRuleDescription": "PT/P067/D120/P4.0",
          "TotalVolume": 12356.66
        }
      ],
      "Warnings": [
        {
          "Message": "System is down for upgradation.",
          "Type": "System Outage"
        }
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Fees

This API returns the fee/charges levied from a  customer's account in a billing period or date range. The API returns both billed and unbilled fee items.

To get the summary of charges, the endpoint *transaction/feessummary* should be called with the same input criteria.

#### Supported operations

* Get fees by invoice status
* Get fees by date period
* Get fees by account
* Get fees by card Id or PAN
* Get fees by fee type charges
* Get fees including cancelled items
* Get fees by line item description
* Get fees by product

```python
def fees(self,
        request_id,
        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`TransactionFeesReq`](../../doc/models/transaction-fees-req.md) | Body, Optional | Transaction Fees RequestBody |

## Response Type

[`TransactionFeesRes`](../../doc/models/transaction-fees-res.md)

## Example Usage

```python
request_id = 'RequestId8'

body = TransactionFeesReq(
    page=1,
    page_size=100
)

result = transaction_controller.fees(
    request_id,
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Fee Summary Response

This API returns the summary data of the fee/charges levied from a customer's account in a billing period or date range. The API returns both billed and unbilled fee items.

The endpoint supports the exact same search criteria as the endpoint *transaction/feessummary*.

#### Supported operations

* Get fees by invoice status
* Get fees by date period
* Get fees by account
* Get fees by card Id or PAN
* Get fees by fee type charges
* Get fees including cancelled items
* Get fees by line item description
* Get fees by product

```python
def fee_summary_response(self,
                        request_id,
                        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`TransactionFeesSummaryReq`](../../doc/models/transaction-fees-summary-req.md) | Body, Optional | FeeSummary RequestBody |

## Response Type

[`FeeSummaryResponse`](../../doc/models/fee-summary-response.md)

## Example Usage

```python
request_id = 'RequestId8'

result = transaction_controller.fee_summary_response(request_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Fuel Consumption

- This API returns the customer an overview of how many transactions, how much fuel volume used over a given period and the total volume used by a card
- This operation response will contains card & transaction details for given period aggregated by payer, account, cardGroup, PAN, DriverName and VRN

```python
def fuel_consumption(self,
                    request_id,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`FuelConsumptionReq`](../../doc/models/fuel-consumption-req.md) | Body, Optional | FuelConsumption RequestBody |

## Response Type

[`FuelConsumptionResponse`](../../doc/models/fuel-consumption-response.md)

## Example Usage

```python
request_id = 'RequestId8'

result = transaction_controller.fuel_consumption(request_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Update Odometer

- This API allows the users to update the odometer readings on the sales items (transaction data)
- This is an asynchronous operation. If opted, the user will be notified on completion of processing.

```python
def update_odometer(self,
                   request_id,
                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`UpdateOdometerRequest`](../../doc/models/update-odometer-request.md) | Body, Optional | updateOdometer RequestBody |

## Response Type

[`UpdateOdometerResp`](../../doc/models/update-odometer-resp.md)

## Example Usage

```python
request_id = 'RequestId8'

result = transaction_controller.update_odometer(request_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Transaction Exceptions

- This API provides the details of the Cards or Transaction related exceptions based on the given conditions for the Requested period.
- This API will return the Transactions related exceptions when the OutputType input parameter is passed as ‘Transaction’ else will return the Cards related exceptions.

```python
def transaction_exceptions(self,
                          request_id,
                          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`TransactionExceptionsReq`](../../doc/models/transaction-exceptions-req.md) | Body, Optional | Transaction Exceptions RequestBody |

## Response Type

[`TransactionExceptionsRes`](../../doc/models/transaction-exceptions-res.md)

## Example Usage

```python
request_id = 'RequestId8'

result = transaction_controller.transaction_exceptions(request_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Recent Transactions New

This endpoint allows querying last 48 hours of transaction data of Shell Card (i.e. Priced, Billed, Unbilled etc. sales items). It provides a flexible search criteria and supports pagination. E.g., if the request is made at 08:30 AM on 18 Aug 2022 then transactions until 16 Aug 2022 08:30 AM (including) can be retrieved.

#### Supported operations

    * Search by Date and Time range (within the last 48 hours only)
    
    * Search by Payer and/or Account number
    
    * Search by Card
    
    * Search by Purchased Country
    
    * Search by Transaction posting date
    
    * Search by Driver Name or Vehicle registration number
    
    * Search by Fuel only transactions
    
    * Search by Product and/or Product group

```python
def recent_transactions_new(self,
                           request_id,
                           body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request.<br><br>**Constraints**: *Minimum Length*: `36`, *Maximum Length*: `36`, *Pattern*: `^[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?$` |
| `body` | [`RecentTransactionRequest`](../../doc/models/recent-transaction-request.md) | Body, Optional | New Recent Transaction RequestBody |

## Response Type

[`RecentTransactionsResponse`](../../doc/models/recent-transactions-response.md)

## Example Usage

```python
request_id = '2b0cbe11-f109-4c43-9201-49af0370df1c'

body = RecentTransactionRequest(
    page_size=1,
    page=1,
    filters=RecentTransactionReq(
        col_co_code=14,
        payer_number='GB00001232',
        account_number='GB00001233',
        product_code='22',
        purchased_in_country='GB',
        card_pan='700205******890645',
        from_date_time='2020-11-09 13:56:03.000',
        to_date_time='2020-12-09 13:56:03.000',
        transaction_status='APPROVED',
        fuel_only='False',
        product_group_name='Motor gasoline',
        vehicle_registration_number='YG67OUM',
        include_declines=True,
        card_issuer_name='Mathew',
        column_list='PayerNumber,AccountNumber,ProductName,FuelVolume,PAN'
    )
)

result = transaction_controller.recent_transactions_new(
    request_id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "9d2dee33-7803-485a-a2b1-2c7538e597ee",
  "Status": "SUCCESS",
  "Page": 1,
  "RowCount": 2,
  "TotalPages": 1,
  "Data": [
    {
      "ColCoCode": 84,
      "PayerNumber": "MY00200653",
      "AccountNumber": "MY00200653",
      "CardIssueNumber": "1",
      "CollectingCompanyCurrencyCode": "MYR",
      "CustDataCustomerEntered": "PartnerId",
      "CustDataDriverId": "D123",
      "CustDataFleetDescription": "Fleet-Truck",
      "FleetIdInput": "AS2344",
      "Amount": 62.47,
      "EuroshellSiteNumber": "1231",
      "IncomingProductCode": "10",
      "ProductCode": "23",
      "ProductName": "Unleaded - Low octane",
      "SiteCode": 3350,
      "HostingCollectingCompanyName": "Shell Malaysia Trading Sdn Bhd",
      "HostingCollectingCompanyNumber": "84",
      "IccdataTranTypeCode": "1",
      "TransactionType": "Transaction Type description",
      "Latitude": "52.143814",
      "Longitude": "101.72869",
      "MerchantCategory": "5542",
      "MerchantCategoryDescription": "Description",
      "PurchasedInCountry": "MY",
      "MerchantId": "MY1737000000000",
      "SiteName": "ShellPT3895 BATU 4    KUALA LUMPUR MY",
      "Network": "458",
      "DelcoCode": "084",
      "OdometerInput": "201620",
      "OdometerReadingKm": "201620",
      "OdometerReadingMiles": "201620",
      "CardPAN": "700214*******780061",
      "PINIndicator": "Y",
      "POIReceiptNumber": "417662",
      "ProductsCodeAdditional": "Additional Code",
      "ProductsTaxCode": "0",
      "FuelVolume": 34.15,
      "SfgwCardDateOfExpiry": "2024-12",
      "SiteCurrencyISOCode": "MYR",
      "CardId": "330743",
      "TransactionDate": "2021-11-11",
      "TransactionDateTime": "2021-11-11 16:32:09.000",
      "TransactionId": "864220307",
      "TransactionStatus": "Approved",
      "UnitOfMeasure": "L",
      "VehicleRegistrationNumber": "WD33637",
      "NetworkDelcoName": "Shell Malaysia Trading Sdn Bhd",
      "ProductGroupName": "Motor gasoline",
      "FuelProduct": "All Fuels",
      "AccountCustomerName": "WCT BERHAD",
      "PayerName": "WCT BERHAD",
      "TransactionTime": "2021-11-11",
      "TransactionCurrency": "RM",
      "UnitPrice": 0.02050073206442167,
      "AuthorisedFlag": "Y",
      "TransactionTimeGMT": "08:41:02",
      "ReasonCode": "10",
      "IssuerActionCode": "2",
      "IssuerActionCodeDescription": "Approved, partial",
      "DeclinedReason": "partial",
      "CardStatusReasonDescription": "Approved, partial",
      "TransactionCountry": "458",
      "IssuingCollectingCompanyName": "Partner Name",
      "CardIssuerName": "John",
      "DriverName": "PAK PAK",
      "BearerDescription": "Description",
      "CardCategoryDescription": "Driver Card",
      "CardTypeDescription": "SHELL FLEET- HONG KONG 7002821",
      "CardTokenTypeDescription": "HK FLE NAT SIN R1 - CHIP",
      "EmbossType": "Driver",
      "EVPrintedNumber": "NL-TNM-C00122045-K",
      "IsRFID": false
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Priced Transactions V2

This API allows querying transaction data (i.e. Priced, Billed and Unbilled sales items). It provides a flexible search criteria and supports paging.
The version 2 is an enhancement to the version 1 where EV transactions and their details are added in the response.

Transactions that are posted but not yet priced, billed or that are in error will not be returned by this API. The API also supports returning Fee Items.

#### Supported operations

* Get sales items and fee transactions
  * Search by invoice status
  * Search by fixed date period
  * Search by date range
  * Search by account
  * Search by card
* Get sales items only
  * Search by transaction Id or location
  * Search by transaction posting date
  * Search by invoice number or date
  * Search by driver name or vehicle registration number
  * Search by card group
  * Search by fuel only transactions
  * Search by product
* EV transaction details - Below are EV specific parameters
  * EVOperator
  * EVSerialId
  * EVChargePointSerial
  * EVChargePointConnectorType
  * EVChargePointConnectorTypeDescription
  * EVChargeDuration
  * EVChargeStartDate
  * EVChargeStartTime
  * EVChargeEndDate
  * EVChargeEndTime

```python
def priced_transactions_v_2(self,
                           request_id,
                           body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request.<br><br>**Constraints**: *Minimum Length*: `36`, *Maximum Length*: `36`, *Pattern*: `^[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?$` |
| `body` | [`PricedTransactionRequestV2`](../../doc/models/priced-transaction-request-v2.md) | Body, Optional | Priced TransactionV2 RequestBody |

## Response Type

[`PricedTransactionResponseV2`](../../doc/models/priced-transaction-response-v2.md)

## Example Usage

```python
request_id = '2b0cbe11-f109-4c43-9201-49af0370df1c'

body = PricedTransactionRequestV2(
    filters=Filters(
        col_co_code='032',
        invoice_status=PricedTransactionReqV2InvoiceStatusEnum.A,
        payer_number='DE26685263',
        account_id=29484,
        account_number='DE26667080',
        driver_name='HH NX 508',
        card_group_id=40000,
        card_pan='7002051006629890645',
        product_code='10',
        product_name='Diesel AGO',
        site_code='05000100',
        incoming_site_number='100021',
        invoice_date='2021-01-01',
        invoice_number='3201016193',
        purchased_in_country_code='GB',
        purchased_in_country='United Kingdom',
        site_group_id=202,
        vehicle_registration_number='4K46801',
        fee_type_id=275549,
        line_item_description='ABC3',
        cards=[
            0
        ],
        sort_order=PricedTransactionReqV2SortOrderEnum.ENUM_5,
        from_date='2022-01-01 00:00:00',
        to_date='2022-01-01 00:00:00',
        period=PricedTransactionReqV2PeriodEnum.ENUM_3,
        posting_date_from='2022-01-01 00:00:00',
        posting_date_to='2022-01-01 00:00:00',
        transaction_item_id='1208176398',
        fuel_only=False,
        include_fees=True,
        is_multipayer=True,
        valid_invoice_date_only=False,
        invoice_from_date='2022-01-01 00:00:00',
        invoice_to_date='2022-01-01 00:00:00',
        hosting_collecting_company_number='032',
        search='2K89909',
        transaction_id='io9KVXk1UkW57XWKyeaHHg'
    ),
    page=1,
    page_size=1
)

result = transaction_controller.priced_transactions_v_2(
    request_id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "9d2dee33-7803-485a-a2b1-2c7538e597ee",
  "Status": "SUCCESS",
  "Data": [
    {
      "AccountName": "Blue Colour Ltd",
      "AccountId": 29484,
      "AccountNumber": "DE26667080",
      "AccountShortName": "Mathew",
      "Additional1": "GBALLEGO0002452",
      "Additional2": "GBALLEGO0002452",
      "Additional3": "GBALLEGO0002452",
      "Additional4": "GBALLEGO0002452",
      "AllowClearing": "Null",
      "AuthorisationCode": 300796,
      "TransactionStatus": "Y",
      "DriverName": "SATTY BHAMRA",
      "CardExpiryPeriod": 2204,
      "CardExpiry": "20220101",
      "CardGroupId": 40000,
      "CardGroupName": "006240 FIRE BRIGHT SOLUTIONS",
      "IssuerCode": 7002,
      "CardPAN": "7002053465789891000",
      "ReleaseCode": 9,
      "CardSequenceNumber": 617,
      "CardType": "GB STD FLT NAT SINGLE R9",
      "ColCoCode": "014",
      "UnitDiscountInvoiceCurrency": -0.0051,
      "ColCoExchangeRate": 0.851858,
      "InvoiceCurrencySymbol": "GBP",
      "CorrectionFlag": true,
      "CRMNumber": 10,
      "CustomerCountry": "United Kingdom",
      "CustomerCurrencyCode": "GBP",
      "CustomerCurrencySymbol": "£",
      "RebateonNetAmountInCustomerCurrency": 0,
      "EffectiveDiscountInCustomerCurrency": -0.22,
      "EffectiveUnitDiscountInCustomerCurrency": -0.0051,
      "UnitPriceInInvoiceCurrency": 1.1024,
      "InvoiceTax": 0,
      "InvoiceGrossAmount": 57.25,
      "InvoiceNetAmount": 47.71,
      "VATonNetAmountInCustomerCurrency": 9.54,
      "CustomerRetailPriceUnitGross": 0,
      "CustomerRetailValueTotalGross": 57.52,
      "CustomerRetailValueTotalNet": 47.93,
      "TransactionTypeDescription": 9.59,
      "RebateonNetAmountInTransactionCurrency": -0.22,
      "EffectiveDiscountInTrxCurrency": -0.22,
      "DelCoToColCoExchangeRate": 0,
      "Cards": [
        275549
      ],
      "UnitDiscountTransactionCurrency": -0.005,
      "TransactionGrossAmount": 57.25,
      "TransactionNetAmount": 47.71,
      "TransactionTax": 9.54,
      "VATonNetAmount": 9.54,
      "DelcoListPriceUnitNet": 0,
      "DelcoRetailPriceUnitGross": 1.32888,
      "UnitPriceInTransactionCurrency": 1.1074,
      "DelcoRetailPriceUnitNet": 1.1074,
      "DelcoRetailValueTotalGross": 57.52,
      "DelcoRetailValueTotalNet": 47.93,
      "TransactionCurrencySymbol": "$",
      "DiscountType": "Retail",
      "DisputeStatus": false,
      "IsShellSite": false,
      "FleetIdInput": "YG67OUM",
      "IncomingProductCode": 23,
      "PostingDate": "20210802",
      "PostingTime": "14:15:22",
      "ProductCode": 30,
      "ProductName": "Unleaded - Medium octane",
      "ProductGroupId": 22,
      "IncomingCurrencyCode": "GBP",
      "IncomingSiteDescription": "Shell Broadway Ring",
      "Location": "Shell Broadway Ring",
      "SiteName": "Shell Broadway Ring",
      "SiteCode": 32,
      "IncomingSiteNumber": 15,
      "InvoiceCurrencyCode": "GBP",
      "InvoiceDate": "20210802",
      "InvoiceNumber": 3201016193,
      "FuelProduct": true,
      "VATApplicable": "Y",
      "PayerName": "Colours Services Ltd",
      "PayerNumber": "GB12121212",
      "ParentCustomerNumber": "GB12121212",
      "PayerGroup": "H312066",
      "PayerGroupName": "12162566 - FUEL CARD SERVICE",
      "CheckDigit": 6,
      "NetInvoiceIndicator": "Y",
      "DelcoCode": 5,
      "NetworkCode": 3,
      "PurchasedInCountry": "United Kingdom",
      "SiteCountry": "United Kingdom",
      "VATCountry": "United Kingdom",
      "DelcoName": "Shell U.K. Oil Products Limited",
      "Network": "Shell",
      "OdometerInput": 0,
      "OriginalSalesItemId": "Null",
      "FleetIDDescription": "YG67OUM",
      "ParentCustomerId": 6494,
      "PINIndicator": "Y, N",
      "ProductGroupName": "Fees",
      "PurchasedInCountryCode": "GB",
      "Quantity": 43.28,
      "RebateRate": 0.0022,
      "ReceiptNumber": 6803,
      "RefundFlag": "Y",
      "SiteGroupId": 202,
      "SiteGroupName": "CZ 9100 ECONOMY NETWORK",
      "Latitude": 53.83606,
      "Longitude": -1.61854,
      "DelCoExchangeRate": 0.851858,
      "EuroRebateAmount": -0.258259,
      "NetEuroAmount": 56.01,
      "EuroVATAmount": 11.2,
      "ParentCustomerName": "FUEL CARD SERVICES LTD",
      "IsInvoiced": false,
      "TransactionCurrencyCode": "GBP",
      "CreditDebitCode": "D or C",
      "TransactionDate": "20210801",
      "TransactionTime": "12:16:58",
      "TransactionItemId": "H305908971030",
      "TrnIdentifier": "H305908971030",
      "Type": "SALE",
      "TransactionLine": 1,
      "TransactionType": "Purchase",
      "UTCOffset": "Europe/London",
      "VATCategory": "United Kingdom Standard VAT Rate",
      "VATRate": 0.2,
      "VehicleRegistration": "YG67OUM",
      "IsCancelled": "Y",
      "ColCoGrossAmount": 57.25,
      "ColCoNetAmount": 47.71,
      "ColCoVATAmount": 9.54,
      "OriginalCurrencySymbol": "$",
      "OriginalCurrencyCode": "$",
      "OriginalVATAmount": 0,
      "EmbossText": "PARKLANE PROPERTIES LTD",
      "OriginalExchangeRate": 0,
      "OriginalTransactionItemInvoiceDate": "20220202",
      "FeeTypeId": 1,
      "LineItemDescription": true,
      "FeeRuleDescription": "Simple Fee",
      "Frequency": 1,
      "FeeRuleId": 1,
      "SystemEntryDate": "20210828",
      "SystemEntryTime": "20:21:08",
      "IsManual": "Y",
      "OriginalTransactionItemId": "Y",
      "OriginalTransactionItemInvoiceNumber": 6750802,
      "OriginalTransactionItemInvoiceId": 234,
      "PayerShortName": "FUEL CARD SERVICES LTD",
      "ReverseCharge": "Y",
      "OriginalGrossAmount": 57.25,
      "OriginalNetAmount": 57.25,
      "UnitOfMeasure": "L",
      "RoadType": "National Road",
      "CustomerCountryIsoCode": "DE",
      "EVOperator": "Shell Recharge",
      "EVSerialId": "GBALLEGO0002452",
      "EVChargePointSerial": "GBALLEGO0002452",
      "EVChargePointConnectorType": 5,
      "EVChargePointConnectorTypeDescription": "DC 50 kW",
      "EVChargeDuration": "PT3205S",
      "EVChargeStartDate": "2021-08-01",
      "EVChargeStartTime": "20:08:01",
      "EVChargeEndDate": "2022-08-01",
      "EVChargeEndTime": "20:08:01",
      "HostingCollectingCompanyNumber": 0,
      "TransactionId": 0,
      "FuelOnly": true
    }
  ],
  "Page": 3,
  "PageSize": 30,
  "TotalPages": 5
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |

