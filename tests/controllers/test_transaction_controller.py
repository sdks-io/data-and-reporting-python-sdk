# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json

from tests.controllers.controller_test_base import ControllerTestBase
from apimatic_core.utilities.comparison_helper import ComparisonHelper
from shelldatareportingapis.api_helper import APIHelper
from shelldatareportingapis.models.recent_transaction_request import RecentTransactionRequest
from shelldatareportingapis.models.priced_transaction_request_v_2 import PricedTransactionRequestV2


class TransactionControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(TransactionControllerTests, cls).setUpClass()
        cls.controller = cls.client.transaction
        cls.response_catcher = cls.controller.http_call_back

    # This endpoint allows querying last 48 hours of transaction data of Shell Card (i.e. Priced, Billed, Unbilled etc. sales items). It provides a flexible search criteria and supports pagination. E.g., if the request is made at 08:30 AM on 18 Aug 2022 then transactions until 16 Aug 2022 08:30 AM (including) can be retrieved.
    #
    #
    ##### Supported operations
    #
    #    * Search by Date and Time range (within the last 48 hours only)
    #
    #    * Search by Payer and/or Account number
    #
    #    * Search by Card
    #
    #    * Search by Purchased Country
    #
    #    * Search by Transaction posting date
    #
    #    * Search by Driver Name or Vehicle registration number
    #
    #    * Search by Fuel only transactions
    #
    #    * Search by Product and/or Product group
    def test_recent_transactions_new(self):
        # Parameters for the API call
        request_id = '2b0cbe11-f109-4c43-9201-49af0370df1c'
        body = APIHelper.json_deserialize('{"PageSize":1,"Page":1,"Filters":{"ColCoCode":14,"PayerNumber":"GB'
            '00001232","AccountNumber":"GB00001233","ProductCode":"22","Purchas'
            'edInCountry":"GB","CardPAN":"700205******890645","FromDateTime":"2'
            '020-11-09 13:56:03.000","ToDateTime":"2020-12-09 13:56:03.000","Tr'
            'ansactionStatus":"APPROVED","FuelOnly":"False","ProductGroupName":'
            '"Motor gasoline","VehicleRegistrationNumber":"YG67OUM","IncludeDec'
            'lines":true,"CardIssuerName":"Mathew","ColumnList":"PayerNumber,Ac'
            'countNumber,ProductName,FuelVolume,PAN"}}', RecentTransactionRequest.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.recent_transactions_new(request_id, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"RequestId":"9d2dee33-7803-485a-a2b1-2c7538e597ee","Status":"SUCC'
            'ESS","Page":1,"RowCount":2,"TotalPages":1,"Data":[{"ColCoCode":84,'
            '"PayerNumber":"MY00200653","AccountNumber":"MY00200653","CardIssue'
            'Number":"1","CollectingCompanyCurrencyCode":"MYR","CustDataCustome'
            'rEntered":"PartnerId","CustDataDriverId":"D123","CustDataFleetDesc'
            'ription":"Fleet-Truck","FleetIdInput":"AS2344","Amount":62.47,"Eur'
            'oshellSiteNumber":"1231","IncomingProductCode":"10","ProductCode":'
            '"23","ProductName":"Unleaded - Low octane","SiteCode":3350,"Hostin'
            'gCollectingCompanyName":"Shell Malaysia Trading Sdn Bhd","HostingC'
            'ollectingCompanyNumber":"84","IccdataTranTypeCode":"1","Transactio'
            'nType":"Transaction Type description","Latitude":"52.143814","Long'
            'itude":"101.72869","MerchantCategory":"5542","MerchantCategoryDesc'
            'ription":"Description","PurchasedInCountry":"MY","MerchantId":"MY1'
            '737000000000","SiteName":"ShellPT3895 BATU 4    KUALA LUMPUR MY","'
            'Network":"458","DelcoCode":"084","OdometerInput":"201620","Odomete'
            'rReadingKm":"201620","OdometerReadingMiles":"201620","CardPAN":"70'
            '0214*******780061","PINIndicator":"Y","POIReceiptNumber":"417662",'
            '"ProductsCodeAdditional":"Additional Code","ProductsTaxCode":"0","'
            'FuelVolume":34.15,"SfgwCardDateOfExpiry":"2024-12","SiteCurrencyIS'
            'OCode":"MYR","CardId":"330743","TransactionDate":"2021-11-11","Tra'
            'nsactionDateTime":"2021-11-11 16:32:09.000","TransactionId":"86422'
            '0307","TransactionStatus":"Approved","UnitOfMeasure":"L","VehicleR'
            'egistrationNumber":"WD33637","NetworkDelcoName":"Shell Malaysia Tr'
            'ading Sdn Bhd","ProductGroupName":"Motor gasoline","FuelProduct":"'
            'All Fuels","AccountCustomerName":"WCT BERHAD","PayerName":"WCT BER'
            'HAD","TransactionTime":"2021-11-11","TransactionCurrency":"RM","Un'
            'itPrice":0.02050073206442167,"AuthorisedFlag":"Y","TransactionTime'
            'GMT":"08:41:02","ReasonCode":"10","IssuerActionCode":"2","IssuerAc'
            'tionCodeDescription":"Approved, partial","DeclinedReason":"partial'
            '","CardStatusReasonDescription":"Approved, partial","TransactionCo'
            'untry":"458","IssuingCollectingCompanyName":"Partner Name","CardIs'
            'suerName":"John","DriverName":"PAK PAK","BearerDescription":"Descr'
            'iption","CardCategoryDescription":"Driver Card","CardTypeDescripti'
            'on":"SHELL FLEET- HONG KONG 7002821","CardTokenTypeDescription":"H'
            'K FLE NAT SIN R1 - CHIP","EmbossType":"Driver","EVPrintedNumber":"'
            'NL-TNM-C00122045-K","IsRFID":false}]}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # This API allows querying transaction data (i.e. Priced, Billed and Unbilled sales items). It provides a flexible search criteria and supports paging. 
    #The version 2 is an enhancement to the version 1 where EV transactions and their details are added in the response. 
    #
    #Transactions that are posted but not yet priced, billed or that are in error will not be returned by this API. The API also supports returning Fee Items.
    #
    ##### Supported operations
    #  * Get sales items and fee transactions
    #    * Search by invoice status
    #    * Search by fixed date period
    #    * Search by date range
    #    * Search by account
    #    * Search by card
    #  * Get sales items only
    #    * Search by transaction Id or location
    #    * Search by transaction posting date
    #    * Search by invoice number or date
    #    * Search by driver name or vehicle registration number
    #    * Search by card group
    #    * Search by fuel only transactions
    #    * Search by product
    # * EV transaction details - Below are EV specific parameters
    #    * EVOperator
    #    * EVSerialId
    #    * EVChargePointSerial
    #    * EVChargePointConnectorType
    #    * EVChargePointConnectorTypeDescription
    #    * EVChargeDuration
    #    * EVChargeStartDate
    #    * EVChargeStartTime
    #    * EVChargeEndDate
    #    * EVChargeEndTime
    def test_priced_transactions_v_2(self):
        # Parameters for the API call
        request_id = '2b0cbe11-f109-4c43-9201-49af0370df1c'
        body = APIHelper.json_deserialize('{"PageSize":1,"Page":1,"Filters":{"ColCoCode":"032","InvoiceStatus'
            '":"A","PayerNumber":"DE26685263","AccountId":29484,"AccountNumber"'
            ':"DE26667080","DriverName":"HH NX 508","CardGroupId":40000,"CardPA'
            'N":"7002051006629890645","ProductCode":"10","ProductName":"Diesel '
            'AGO","SiteCode":"05000100","IncomingSiteNumber":"100021","InvoiceD'
            'ate":"2021-01-01","InvoiceNumber":"3201016193","PurchasedInCountry'
            'Code":"GB","PurchasedInCountry":"United Kingdom","SiteGroupId":202'
            ',"VehicleRegistrationNumber":"4K46801","FeeTypeId":275549,"LineIte'
            'mDescription":"ABC3","Cards":[0],"SortOrder":"5","FromDate":"2022-'
            '01-01 00:00:00","ToDate":"2022-01-01 00:00:00","Period":3,"Posting'
            'DateFrom":"2022-01-01 00:00:00","PostingDateTo":"2022-01-01 00:00:'
            '00","TransactionItemId":"1208176398","FuelOnly":false,"IncludeFees'
            '":true,"IsMultipayer":true,"ValidInvoiceDateOnly":false,"InvoiceFr'
            'omDate":"2022-01-01 00:00:00","InvoiceToDate":"2022-01-01 00:00:00'
            '","HostingCollectingCompanyNumber":"032","Search":"2K89909","Trans'
            'actionId":"io9KVXk1UkW57XWKyeaHHg"}}', PricedTransactionRequestV2.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.priced_transactions_v_2(request_id, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"RequestId":"9d2dee33-7803-485a-a2b1-2c7538e597ee","Status":"SUCC'
            'ESS","Data":[{"AccountName":"Blue Colour Ltd","AccountId":29484,"A'
            'ccountNumber":"DE26667080","AccountShortName":"Mathew","Additional'
            '1":"GBALLEGO0002452","Additional2":"GBALLEGO0002452","Additional3"'
            ':"GBALLEGO0002452","Additional4":"GBALLEGO0002452","AllowClearing"'
            ':"Null","AuthorisationCode":300796,"TransactionStatus":"Y","Driver'
            'Name":"SATTY BHAMRA","CardExpiryPeriod":2204,"CardExpiry":"2022010'
            '1","CardGroupId":40000,"CardGroupName":"006240 FIRE BRIGHT SOLUTIO'
            'NS","IssuerCode":7002,"CardPAN":"7002053465789891000","ReleaseCode'
            '":9,"CardSequenceNumber":617,"CardType":"GB STD FLT NAT SINGLE R9"'
            ',"ColCoCode":"014","UnitDiscountInvoiceCurrency":-0.0051,"ColCoExc'
            'hangeRate":0.851858,"InvoiceCurrencySymbol":"GBP","CorrectionFlag"'
            ':true,"CRMNumber":10,"CustomerCountry":"United Kingdom","CustomerC'
            'urrencyCode":"GBP","CustomerCurrencySymbol":"£","RebateonNetAmount'
            'InCustomerCurrency":0,"EffectiveDiscountInCustomerCurrency":-0.22,'
            '"EffectiveUnitDiscountInCustomerCurrency":-0.0051,"UnitPriceInInvo'
            'iceCurrency":1.1024,"InvoiceTax":0,"InvoiceGrossAmount":57.25,"Inv'
            'oiceNetAmount":47.71,"VATonNetAmountInCustomerCurrency":9.54,"Cust'
            'omerRetailPriceUnitGross":0,"CustomerRetailValueTotalGross":57.52,'
            '"CustomerRetailValueTotalNet":47.93,"TransactionTypeDescription":9'
            '.59,"RebateonNetAmountInTransactionCurrency":-0.22,"EffectiveDisco'
            'untInTrxCurrency":-0.22,"DelCoToColCoExchangeRate":0,"Cards":[2755'
            '49],"UnitDiscountTransactionCurrency":-0.005,"TransactionGrossAmou'
            'nt":57.25,"TransactionNetAmount":47.71,"TransactionTax":9.54,"VATo'
            'nNetAmount":9.54,"DelcoListPriceUnitNet":0,"DelcoRetailPriceUnitGr'
            'oss":1.32888,"UnitPriceInTransactionCurrency":1.1074,"DelcoRetailP'
            'riceUnitNet":1.1074,"DelcoRetailValueTotalGross":57.52,"DelcoRetai'
            'lValueTotalNet":47.93,"TransactionCurrencySymbol":"$","DiscountTyp'
            'e":"Retail","DisputeStatus":false,"IsShellSite":false,"FleetIdInpu'
            't":"YG67OUM","IncomingProductCode":23,"PostingDate":"20210802","Po'
            'stingTime":"14:15:22","ProductCode":30,"ProductName":"Unleaded - M'
            'edium octane","ProductGroupId":22,"IncomingCurrencyCode":"GBP","In'
            'comingSiteDescription":"Shell Broadway Ring","Location":"Shell Bro'
            'adway Ring","SiteName":"Shell Broadway Ring","SiteCode":32,"Incomi'
            'ngSiteNumber":15,"InvoiceCurrencyCode":"GBP","InvoiceDate":"202108'
            '02","InvoiceNumber":3201016193,"FuelProduct":true,"VATApplicable":'
            '"Y","PayerName":"Colours Services Ltd","PayerNumber":"GB12121212",'
            '"ParentCustomerNumber":"GB12121212","PayerGroup":"H312066","PayerG'
            'roupName":"12162566 - FUEL CARD SERVICE","CheckDigit":6,"NetInvoic'
            'eIndicator":"Y","DelcoCode":5,"NetworkCode":3,"PurchasedInCountry"'
            ':"United Kingdom","SiteCountry":"United Kingdom","VATCountry":"Uni'
            'ted Kingdom","DelcoName":"Shell U.K. Oil Products Limited","Networ'
            'k":"Shell","OdometerInput":0,"OriginalSalesItemId":"Null","FleetID'
            'Description":"YG67OUM","ParentCustomerId":6494,"PINIndicator":"Y, '
            'N","ProductGroupName":"Fees","PurchasedInCountryCode":"GB","Quanti'
            'ty":43.28,"RebateRate":0.0022,"ReceiptNumber":6803,"RefundFlag":"Y'
            '","SiteGroupId":202,"SiteGroupName":"CZ 9100 ECONOMY NETWORK","Lat'
            'itude":53.83606,"Longitude":-1.61854,"DelCoExchangeRate":0.851858,'
            '"EuroRebateAmount":-0.258259,"NetEuroAmount":56.01,"EuroVATAmount"'
            ':11.2,"ParentCustomerName":"FUEL CARD SERVICES LTD","IsInvoiced":f'
            'alse,"TransactionCurrencyCode":"GBP","CreditDebitCode":"D or C","T'
            'ransactionDate":"20210801","TransactionTime":"12:16:58","Transacti'
            'onItemId":"H305908971030","TrnIdentifier":"H305908971030","Type":"'
            'SALE","TransactionLine":1,"TransactionType":"Purchase","UTCOffset"'
            ':"Europe/London","VATCategory":"United Kingdom Standard VAT Rate",'
            '"VATRate":0.2,"VehicleRegistration":"YG67OUM","IsCancelled":"Y","C'
            'olCoGrossAmount":57.25,"ColCoNetAmount":47.71,"ColCoVATAmount":9.5'
            '4,"OriginalCurrencySymbol":"$","OriginalCurrencyCode":"$","Origina'
            'lVATAmount":0,"EmbossText":"PARKLANE PROPERTIES LTD","OriginalExch'
            'angeRate":0,"OriginalTransactionItemInvoiceDate":"20220202","FeeTy'
            'peId":1,"LineItemDescription":true,"FeeRuleDescription":"Simple Fe'
            'e","Frequency":1,"FeeRuleId":1,"SystemEntryDate":"20210828","Syste'
            'mEntryTime":"20:21:08","IsManual":"Y","OriginalTransactionItemId":'
            '"Y","OriginalTransactionItemInvoiceNumber":6750802,"OriginalTransa'
            'ctionItemInvoiceId":234,"PayerShortName":"FUEL CARD SERVICES LTD",'
            '"ReverseCharge":"Y","OriginalGrossAmount":57.25,"OriginalNetAmount'
            '":57.25,"UnitOfMeasure":"L","RoadType":"National Road","CustomerCo'
            'untryIsoCode":"DE","EVOperator":"Shell Recharge","EVSerialId":"GBA'
            'LLEGO0002452","EVChargePointSerial":"GBALLEGO0002452","EVChargePoi'
            'ntConnectorType":5,"EVChargePointConnectorTypeDescription":"DC 50 '
            'kW","EVChargeDuration":"PT3205S","EVChargeStartDate":"2021-08-01",'
            '"EVChargeStartTime":"20:08:01","EVChargeEndDate":"2022-08-01","EVC'
            'hargeEndTime":"20:08:01","HostingCollectingCompanyNumber":0,"Trans'
            'actionId":0,"FuelOnly":true}],"Page":3,"PageSize":30,"TotalPages":'
            '5}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

