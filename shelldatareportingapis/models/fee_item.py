# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper
from shelldatareportingapis.models.fees_fee_rule_tiers import FeesFeeRuleTiers


class FeeItem(object):

    """Implementation of the 'FeeItem' model.

    TODO: type model description here.

    Attributes:
        fee_item_id (int): Fee Item unique identifier in the H3 Cards
            Platform
        account_id (int): Account Id
        account_number (str): Account Number
        account_short_name (str): Account short Number
        invoice_account_id (int): Invoice Account Id
        invoice_account_number (str): Invoice Account Number
        invoice_account_short_name (str): Invoice Account short Name
        payer_id (int): Payer Id
        payer_number (str): Payer Number
        payer_short_name (str): Payer short Name
        card_id (int): Unique Card Id
        pan (str): Card PAN
        card_group_id (int): Card Group Id
        card_group_name (str): Card Group Name
        fee_type_id (int): Fee type identifier.
        fee_type (str): Fee type description
        fee_type_group (str): Fee type group in under which the Fee item is
            generated.  Example:   Account  Card  Others
        fee_rule_id (int): Fee rule identifier
        fee_rule_description (str): Fee rule description
        fee_rule_tiers (List[FeesFeeRuleTiers]): TODO: type description here.
        fee_item_date (str): Local Fee Item Date of when the transaction took
            place  Format: yyyyMMdd
        fee_item_time (str): Local Fee Item Time of where the transaction took
            place  Format: HH:mm:ss (24 hours format)
        is_manual (bool): True/False.  Is manual
        is_cancelled (bool): True/False.  Is cancelled
        customer_currency_code (str): ISO currency code   Example: GBP
        customer_currency_symbol (str): Currency symbol of the Currency Code  
            Example: £, $
        product_id (int): Product Id  Example: Sample list of product ids and
            description.  100 Service fee  102 Invoice production fee  103
            Account fee  104 Transaction fee  105 Card membership fee
        product_code (str): Product Code – Global as per GFN configuration  
            Example:   2 Service fee  4 Invoice production fee  5 Account fee 
            6 Transaction fee  7 Card membership fee
        product_name (str): Product Name  Example: Sample list of product ids
            and description.  Service fee  Invoice production fee
        product_group_id (int): Product Group Id  Example: Sample list  22
            Card related fees  23 Monetary Adjustment
        product_group_name (str): Product Group Name  Example: Sample list  22
            Card related fees  23 Monetary Adjustment
        line_item_description (str): Line Item Description generally the
            quantity as printed on Invoice or the manually keyed in
            description for manual fees
        quantity (int): Quantity
        is_invoiced (bool): True/False.  Is fee item invoiced
        vat_country_code (str): VAT country ISO code
        vat_country_name (str): VAT country name
        vat_percentage (float): VAT percentage
        vat_category_id (int): VAT Category identifier
        vat_category_description (str): VAT Category description
        legislative_region_id (int): Legislative region id
        legislative_region_name (str): Legislative region name
        system_entry_date (str): System entry date
        system_entry_time (str): System entry time
        col_co_net_amount (float): ColCo net amount
        col_co_vat_amount (float): ColCoVAT amount
        col_co_gross_amount (float): ColCo gross amount
        interim_invoice_id (int): Interim invoice id
        interim_invoice_number (str): Interim invoice number
        invoice_id (int): Invoice id
        invoice_number (str): Invoice number
        invoice_date (str): Invoice date   Format: yyyyMMdd
        customer_exchange_rate (float): Customer exchange rate
        invoice_net_amount (float): Invoice net amount
        invoice_gross_amount (float): Invoice gross amount
        invoice_vat_amount (float): Invoice VAT amount
        reverse_charge (bool): True/False.  Reverse charge.
        original_fee_item_id (int): Original Fee Item id.
        original_currency_code (str): Original FeeItem Currency ISO code.
        original_currency_symbol (str): Original FeeItem currency symbol
        original_unit_price (float): Original FeeItem unit price
        original_net_amount (float): Original FeeItem net amount
        original_vat_amount (float): Original FeeItem VAT amount
        original_gross_amount (float): Original FeeItem gross amount
        original_exchange_rate (float): Original FeeItem exchange rate
        original_legislative_region_id (int): Original legislative region id
        original_legislative_region_name (str): Original legislative region
            name
        frequency (str): Fee frequency derived from Fee rules if applicable 
            Returns ID-Description in one field  Example:   1- Daily (all
            days)  2-Daily (only working days)  3-Weekly – Monday  4-Weekly -
            Tuesday
        fee_item_card_level_breakup (str): Fee breakup at card level for Fee
            Items where applicable.
        original_fee_item_invoice_id (int): Invoice Id/ Billing Document Id of
            the original fee item (when not null).  Applicable only for fee
            items that are refund to an original fee item that is already
            invoiced.
        original_fee_item_invoice_number (str): Invoice Number of the original
            fee item (when not null).  Applicable only for fee items that are
            refund to an original fee item that is already invoiced.
        original_fee_item_invoice_date (str): Invoice Date of the original fee
            item (when not null).  Applicable only for fee items that are
            refund to an original fee item that is already invoiced.  Format:
            yyyyMMdd
        driver_name (str): Driver name embossed on the Card
        emboss_text (str): Text embossed on the Card
        vrn (str): Reg. Number embossed on the Card

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "fee_item_id": 'FeeItemId',
        "account_id": 'AccountId',
        "account_number": 'AccountNumber',
        "account_short_name": 'AccountShortName',
        "invoice_account_id": 'InvoiceAccountId',
        "invoice_account_number": 'InvoiceAccountNumber',
        "invoice_account_short_name": 'InvoiceAccountShortName',
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber',
        "payer_short_name": 'PayerShortName',
        "card_id": 'CardId',
        "pan": 'PAN',
        "card_group_id": 'CardGroupId',
        "card_group_name": 'CardGroupName',
        "fee_type_id": 'FeeTypeId',
        "fee_type": 'FeeType',
        "fee_type_group": 'FeeTypeGroup',
        "fee_rule_id": 'FeeRuleId',
        "fee_rule_description": 'FeeRuleDescription',
        "fee_rule_tiers": 'FeeRuleTiers',
        "fee_item_date": 'FeeItemDate',
        "fee_item_time": 'FeeItemTime',
        "is_manual": 'IsManual',
        "is_cancelled": 'IsCancelled',
        "customer_currency_code": 'CustomerCurrencyCode',
        "customer_currency_symbol": 'CustomerCurrencySymbol',
        "product_id": 'ProductId',
        "product_code": 'ProductCode',
        "product_name": 'ProductName',
        "product_group_id": 'ProductGroupId',
        "product_group_name": 'ProductGroupName',
        "line_item_description": 'LineItemDescription',
        "quantity": 'Quantity',
        "is_invoiced": 'IsInvoiced',
        "vat_country_code": 'VATCountryCode',
        "vat_country_name": 'VATCountryName',
        "vat_percentage": 'VATPercentage',
        "vat_category_id": 'VATCategoryID',
        "vat_category_description": 'VATCategoryDescription',
        "legislative_region_id": 'LegislativeRegionId',
        "legislative_region_name": 'LegislativeRegionName',
        "system_entry_date": 'SystemEntryDate',
        "system_entry_time": 'SystemEntryTime',
        "col_co_net_amount": 'ColCoNetAmount',
        "col_co_vat_amount": 'ColCoVATAmount',
        "col_co_gross_amount": 'ColCoGrossAmount',
        "interim_invoice_id": 'InterimInvoiceId',
        "interim_invoice_number": 'InterimInvoiceNumber',
        "invoice_id": 'InvoiceId',
        "invoice_number": 'InvoiceNumber',
        "invoice_date": 'InvoiceDate',
        "customer_exchange_rate": 'CustomerExchangeRate',
        "invoice_net_amount": 'InvoiceNetAmount',
        "invoice_gross_amount": 'InvoiceGrossAmount',
        "invoice_vat_amount": 'InvoiceVATAmount',
        "reverse_charge": 'ReverseCharge',
        "original_fee_item_id": 'OriginalFeeItemId',
        "original_currency_code": 'OriginalCurrencyCode',
        "original_currency_symbol": 'OriginalCurrencySymbol',
        "original_unit_price": 'OriginalUnitPrice',
        "original_net_amount": 'OriginalNetAmount',
        "original_vat_amount": 'OriginalVATAmount',
        "original_gross_amount": 'OriginalGrossAmount',
        "original_exchange_rate": 'OriginalExchangeRate',
        "original_legislative_region_id": 'OriginalLegislativeRegionId',
        "original_legislative_region_name": 'OriginalLegislativeRegionName',
        "frequency": 'Frequency',
        "fee_item_card_level_breakup": 'FeeItemCardLevelBreakup',
        "original_fee_item_invoice_id": 'OriginalFeeItemInvoiceId',
        "original_fee_item_invoice_number": 'OriginalFeeItemInvoiceNumber',
        "original_fee_item_invoice_date": 'OriginalFeeItemInvoiceDate',
        "driver_name": 'DriverName',
        "emboss_text": 'EmbossText',
        "vrn": 'VRN'
    }

    _optionals = [
        'fee_item_id',
        'account_id',
        'account_number',
        'account_short_name',
        'invoice_account_id',
        'invoice_account_number',
        'invoice_account_short_name',
        'payer_id',
        'payer_number',
        'payer_short_name',
        'card_id',
        'pan',
        'card_group_id',
        'card_group_name',
        'fee_type_id',
        'fee_type',
        'fee_type_group',
        'fee_rule_id',
        'fee_rule_description',
        'fee_rule_tiers',
        'fee_item_date',
        'fee_item_time',
        'is_manual',
        'is_cancelled',
        'customer_currency_code',
        'customer_currency_symbol',
        'product_id',
        'product_code',
        'product_name',
        'product_group_id',
        'product_group_name',
        'line_item_description',
        'quantity',
        'is_invoiced',
        'vat_country_code',
        'vat_country_name',
        'vat_percentage',
        'vat_category_id',
        'vat_category_description',
        'legislative_region_id',
        'legislative_region_name',
        'system_entry_date',
        'system_entry_time',
        'col_co_net_amount',
        'col_co_vat_amount',
        'col_co_gross_amount',
        'interim_invoice_id',
        'interim_invoice_number',
        'invoice_id',
        'invoice_number',
        'invoice_date',
        'customer_exchange_rate',
        'invoice_net_amount',
        'invoice_gross_amount',
        'invoice_vat_amount',
        'reverse_charge',
        'original_fee_item_id',
        'original_currency_code',
        'original_currency_symbol',
        'original_unit_price',
        'original_net_amount',
        'original_vat_amount',
        'original_gross_amount',
        'original_exchange_rate',
        'original_legislative_region_id',
        'original_legislative_region_name',
        'frequency',
        'fee_item_card_level_breakup',
        'original_fee_item_invoice_id',
        'original_fee_item_invoice_number',
        'original_fee_item_invoice_date',
        'driver_name',
        'emboss_text',
        'vrn',
    ]

    _nullables = [
        'fee_item_id',
        'account_id',
        'account_number',
        'account_short_name',
        'invoice_account_id',
        'invoice_account_number',
        'invoice_account_short_name',
        'payer_id',
        'payer_number',
        'payer_short_name',
        'card_id',
        'pan',
        'card_group_id',
        'card_group_name',
        'fee_type_id',
        'fee_type',
        'fee_type_group',
        'fee_rule_id',
        'fee_rule_description',
        'fee_item_date',
        'fee_item_time',
        'is_manual',
        'is_cancelled',
        'customer_currency_code',
        'customer_currency_symbol',
        'product_id',
        'product_code',
        'product_name',
        'product_group_id',
        'product_group_name',
        'line_item_description',
        'quantity',
        'is_invoiced',
        'vat_country_code',
        'vat_country_name',
        'vat_percentage',
        'vat_category_id',
        'vat_category_description',
        'legislative_region_id',
        'legislative_region_name',
        'system_entry_date',
        'system_entry_time',
        'col_co_net_amount',
        'col_co_vat_amount',
        'col_co_gross_amount',
        'interim_invoice_id',
        'interim_invoice_number',
        'invoice_id',
        'invoice_number',
        'invoice_date',
        'customer_exchange_rate',
        'invoice_net_amount',
        'invoice_gross_amount',
        'invoice_vat_amount',
        'reverse_charge',
        'original_fee_item_id',
        'original_currency_code',
        'original_currency_symbol',
        'original_unit_price',
        'original_net_amount',
        'original_vat_amount',
        'original_gross_amount',
        'original_exchange_rate',
        'original_legislative_region_id',
        'original_legislative_region_name',
        'frequency',
        'fee_item_card_level_breakup',
        'original_fee_item_invoice_id',
        'original_fee_item_invoice_number',
        'original_fee_item_invoice_date',
        'driver_name',
        'emboss_text',
        'vrn',
    ]

    def __init__(self,
                 fee_item_id=APIHelper.SKIP,
                 account_id=APIHelper.SKIP,
                 account_number=APIHelper.SKIP,
                 account_short_name=APIHelper.SKIP,
                 invoice_account_id=APIHelper.SKIP,
                 invoice_account_number=APIHelper.SKIP,
                 invoice_account_short_name=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 payer_short_name=APIHelper.SKIP,
                 card_id=APIHelper.SKIP,
                 pan=APIHelper.SKIP,
                 card_group_id=APIHelper.SKIP,
                 card_group_name=APIHelper.SKIP,
                 fee_type_id=APIHelper.SKIP,
                 fee_type=APIHelper.SKIP,
                 fee_type_group=APIHelper.SKIP,
                 fee_rule_id=APIHelper.SKIP,
                 fee_rule_description=APIHelper.SKIP,
                 fee_rule_tiers=APIHelper.SKIP,
                 fee_item_date=APIHelper.SKIP,
                 fee_item_time=APIHelper.SKIP,
                 is_manual=APIHelper.SKIP,
                 is_cancelled=APIHelper.SKIP,
                 customer_currency_code=APIHelper.SKIP,
                 customer_currency_symbol=APIHelper.SKIP,
                 product_id=APIHelper.SKIP,
                 product_code=APIHelper.SKIP,
                 product_name=APIHelper.SKIP,
                 product_group_id=APIHelper.SKIP,
                 product_group_name=APIHelper.SKIP,
                 line_item_description=APIHelper.SKIP,
                 quantity=APIHelper.SKIP,
                 is_invoiced=APIHelper.SKIP,
                 vat_country_code=APIHelper.SKIP,
                 vat_country_name=APIHelper.SKIP,
                 vat_percentage=APIHelper.SKIP,
                 vat_category_id=APIHelper.SKIP,
                 vat_category_description=APIHelper.SKIP,
                 legislative_region_id=APIHelper.SKIP,
                 legislative_region_name=APIHelper.SKIP,
                 system_entry_date=APIHelper.SKIP,
                 system_entry_time=APIHelper.SKIP,
                 col_co_net_amount=APIHelper.SKIP,
                 col_co_vat_amount=APIHelper.SKIP,
                 col_co_gross_amount=APIHelper.SKIP,
                 interim_invoice_id=APIHelper.SKIP,
                 interim_invoice_number=APIHelper.SKIP,
                 invoice_id=APIHelper.SKIP,
                 invoice_number=APIHelper.SKIP,
                 invoice_date=APIHelper.SKIP,
                 customer_exchange_rate=APIHelper.SKIP,
                 invoice_net_amount=APIHelper.SKIP,
                 invoice_gross_amount=APIHelper.SKIP,
                 invoice_vat_amount=APIHelper.SKIP,
                 reverse_charge=APIHelper.SKIP,
                 original_fee_item_id=APIHelper.SKIP,
                 original_currency_code=APIHelper.SKIP,
                 original_currency_symbol=APIHelper.SKIP,
                 original_unit_price=APIHelper.SKIP,
                 original_net_amount=APIHelper.SKIP,
                 original_vat_amount=APIHelper.SKIP,
                 original_gross_amount=APIHelper.SKIP,
                 original_exchange_rate=APIHelper.SKIP,
                 original_legislative_region_id=APIHelper.SKIP,
                 original_legislative_region_name=APIHelper.SKIP,
                 frequency=APIHelper.SKIP,
                 fee_item_card_level_breakup=APIHelper.SKIP,
                 original_fee_item_invoice_id=APIHelper.SKIP,
                 original_fee_item_invoice_number=APIHelper.SKIP,
                 original_fee_item_invoice_date=APIHelper.SKIP,
                 driver_name=APIHelper.SKIP,
                 emboss_text=APIHelper.SKIP,
                 vrn=APIHelper.SKIP):
        """Constructor for the FeeItem class"""

        # Initialize members of the class
        if fee_item_id is not APIHelper.SKIP:
            self.fee_item_id = fee_item_id 
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if account_short_name is not APIHelper.SKIP:
            self.account_short_name = account_short_name 
        if invoice_account_id is not APIHelper.SKIP:
            self.invoice_account_id = invoice_account_id 
        if invoice_account_number is not APIHelper.SKIP:
            self.invoice_account_number = invoice_account_number 
        if invoice_account_short_name is not APIHelper.SKIP:
            self.invoice_account_short_name = invoice_account_short_name 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 
        if payer_short_name is not APIHelper.SKIP:
            self.payer_short_name = payer_short_name 
        if card_id is not APIHelper.SKIP:
            self.card_id = card_id 
        if pan is not APIHelper.SKIP:
            self.pan = pan 
        if card_group_id is not APIHelper.SKIP:
            self.card_group_id = card_group_id 
        if card_group_name is not APIHelper.SKIP:
            self.card_group_name = card_group_name 
        if fee_type_id is not APIHelper.SKIP:
            self.fee_type_id = fee_type_id 
        if fee_type is not APIHelper.SKIP:
            self.fee_type = fee_type 
        if fee_type_group is not APIHelper.SKIP:
            self.fee_type_group = fee_type_group 
        if fee_rule_id is not APIHelper.SKIP:
            self.fee_rule_id = fee_rule_id 
        if fee_rule_description is not APIHelper.SKIP:
            self.fee_rule_description = fee_rule_description 
        if fee_rule_tiers is not APIHelper.SKIP:
            self.fee_rule_tiers = fee_rule_tiers 
        if fee_item_date is not APIHelper.SKIP:
            self.fee_item_date = fee_item_date 
        if fee_item_time is not APIHelper.SKIP:
            self.fee_item_time = fee_item_time 
        if is_manual is not APIHelper.SKIP:
            self.is_manual = is_manual 
        if is_cancelled is not APIHelper.SKIP:
            self.is_cancelled = is_cancelled 
        if customer_currency_code is not APIHelper.SKIP:
            self.customer_currency_code = customer_currency_code 
        if customer_currency_symbol is not APIHelper.SKIP:
            self.customer_currency_symbol = customer_currency_symbol 
        if product_id is not APIHelper.SKIP:
            self.product_id = product_id 
        if product_code is not APIHelper.SKIP:
            self.product_code = product_code 
        if product_name is not APIHelper.SKIP:
            self.product_name = product_name 
        if product_group_id is not APIHelper.SKIP:
            self.product_group_id = product_group_id 
        if product_group_name is not APIHelper.SKIP:
            self.product_group_name = product_group_name 
        if line_item_description is not APIHelper.SKIP:
            self.line_item_description = line_item_description 
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity 
        if is_invoiced is not APIHelper.SKIP:
            self.is_invoiced = is_invoiced 
        if vat_country_code is not APIHelper.SKIP:
            self.vat_country_code = vat_country_code 
        if vat_country_name is not APIHelper.SKIP:
            self.vat_country_name = vat_country_name 
        if vat_percentage is not APIHelper.SKIP:
            self.vat_percentage = vat_percentage 
        if vat_category_id is not APIHelper.SKIP:
            self.vat_category_id = vat_category_id 
        if vat_category_description is not APIHelper.SKIP:
            self.vat_category_description = vat_category_description 
        if legislative_region_id is not APIHelper.SKIP:
            self.legislative_region_id = legislative_region_id 
        if legislative_region_name is not APIHelper.SKIP:
            self.legislative_region_name = legislative_region_name 
        if system_entry_date is not APIHelper.SKIP:
            self.system_entry_date = system_entry_date 
        if system_entry_time is not APIHelper.SKIP:
            self.system_entry_time = system_entry_time 
        if col_co_net_amount is not APIHelper.SKIP:
            self.col_co_net_amount = col_co_net_amount 
        if col_co_vat_amount is not APIHelper.SKIP:
            self.col_co_vat_amount = col_co_vat_amount 
        if col_co_gross_amount is not APIHelper.SKIP:
            self.col_co_gross_amount = col_co_gross_amount 
        if interim_invoice_id is not APIHelper.SKIP:
            self.interim_invoice_id = interim_invoice_id 
        if interim_invoice_number is not APIHelper.SKIP:
            self.interim_invoice_number = interim_invoice_number 
        if invoice_id is not APIHelper.SKIP:
            self.invoice_id = invoice_id 
        if invoice_number is not APIHelper.SKIP:
            self.invoice_number = invoice_number 
        if invoice_date is not APIHelper.SKIP:
            self.invoice_date = invoice_date 
        if customer_exchange_rate is not APIHelper.SKIP:
            self.customer_exchange_rate = customer_exchange_rate 
        if invoice_net_amount is not APIHelper.SKIP:
            self.invoice_net_amount = invoice_net_amount 
        if invoice_gross_amount is not APIHelper.SKIP:
            self.invoice_gross_amount = invoice_gross_amount 
        if invoice_vat_amount is not APIHelper.SKIP:
            self.invoice_vat_amount = invoice_vat_amount 
        if reverse_charge is not APIHelper.SKIP:
            self.reverse_charge = reverse_charge 
        if original_fee_item_id is not APIHelper.SKIP:
            self.original_fee_item_id = original_fee_item_id 
        if original_currency_code is not APIHelper.SKIP:
            self.original_currency_code = original_currency_code 
        if original_currency_symbol is not APIHelper.SKIP:
            self.original_currency_symbol = original_currency_symbol 
        if original_unit_price is not APIHelper.SKIP:
            self.original_unit_price = original_unit_price 
        if original_net_amount is not APIHelper.SKIP:
            self.original_net_amount = original_net_amount 
        if original_vat_amount is not APIHelper.SKIP:
            self.original_vat_amount = original_vat_amount 
        if original_gross_amount is not APIHelper.SKIP:
            self.original_gross_amount = original_gross_amount 
        if original_exchange_rate is not APIHelper.SKIP:
            self.original_exchange_rate = original_exchange_rate 
        if original_legislative_region_id is not APIHelper.SKIP:
            self.original_legislative_region_id = original_legislative_region_id 
        if original_legislative_region_name is not APIHelper.SKIP:
            self.original_legislative_region_name = original_legislative_region_name 
        if frequency is not APIHelper.SKIP:
            self.frequency = frequency 
        if fee_item_card_level_breakup is not APIHelper.SKIP:
            self.fee_item_card_level_breakup = fee_item_card_level_breakup 
        if original_fee_item_invoice_id is not APIHelper.SKIP:
            self.original_fee_item_invoice_id = original_fee_item_invoice_id 
        if original_fee_item_invoice_number is not APIHelper.SKIP:
            self.original_fee_item_invoice_number = original_fee_item_invoice_number 
        if original_fee_item_invoice_date is not APIHelper.SKIP:
            self.original_fee_item_invoice_date = original_fee_item_invoice_date 
        if driver_name is not APIHelper.SKIP:
            self.driver_name = driver_name 
        if emboss_text is not APIHelper.SKIP:
            self.emboss_text = emboss_text 
        if vrn is not APIHelper.SKIP:
            self.vrn = vrn 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        fee_item_id = dictionary.get("FeeItemId") if "FeeItemId" in dictionary.keys() else APIHelper.SKIP
        account_id = dictionary.get("AccountId") if "AccountId" in dictionary.keys() else APIHelper.SKIP
        account_number = dictionary.get("AccountNumber") if "AccountNumber" in dictionary.keys() else APIHelper.SKIP
        account_short_name = dictionary.get("AccountShortName") if "AccountShortName" in dictionary.keys() else APIHelper.SKIP
        invoice_account_id = dictionary.get("InvoiceAccountId") if "InvoiceAccountId" in dictionary.keys() else APIHelper.SKIP
        invoice_account_number = dictionary.get("InvoiceAccountNumber") if "InvoiceAccountNumber" in dictionary.keys() else APIHelper.SKIP
        invoice_account_short_name = dictionary.get("InvoiceAccountShortName") if "InvoiceAccountShortName" in dictionary.keys() else APIHelper.SKIP
        payer_id = dictionary.get("PayerId") if "PayerId" in dictionary.keys() else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if "PayerNumber" in dictionary.keys() else APIHelper.SKIP
        payer_short_name = dictionary.get("PayerShortName") if "PayerShortName" in dictionary.keys() else APIHelper.SKIP
        card_id = dictionary.get("CardId") if "CardId" in dictionary.keys() else APIHelper.SKIP
        pan = dictionary.get("PAN") if "PAN" in dictionary.keys() else APIHelper.SKIP
        card_group_id = dictionary.get("CardGroupId") if "CardGroupId" in dictionary.keys() else APIHelper.SKIP
        card_group_name = dictionary.get("CardGroupName") if "CardGroupName" in dictionary.keys() else APIHelper.SKIP
        fee_type_id = dictionary.get("FeeTypeId") if "FeeTypeId" in dictionary.keys() else APIHelper.SKIP
        fee_type = dictionary.get("FeeType") if "FeeType" in dictionary.keys() else APIHelper.SKIP
        fee_type_group = dictionary.get("FeeTypeGroup") if "FeeTypeGroup" in dictionary.keys() else APIHelper.SKIP
        fee_rule_id = dictionary.get("FeeRuleId") if "FeeRuleId" in dictionary.keys() else APIHelper.SKIP
        fee_rule_description = dictionary.get("FeeRuleDescription") if "FeeRuleDescription" in dictionary.keys() else APIHelper.SKIP
        fee_rule_tiers = None
        if dictionary.get('FeeRuleTiers') is not None:
            fee_rule_tiers = [FeesFeeRuleTiers.from_dictionary(x) for x in dictionary.get('FeeRuleTiers')]
        else:
            fee_rule_tiers = APIHelper.SKIP
        fee_item_date = dictionary.get("FeeItemDate") if "FeeItemDate" in dictionary.keys() else APIHelper.SKIP
        fee_item_time = dictionary.get("FeeItemTime") if "FeeItemTime" in dictionary.keys() else APIHelper.SKIP
        is_manual = dictionary.get("IsManual") if "IsManual" in dictionary.keys() else APIHelper.SKIP
        is_cancelled = dictionary.get("IsCancelled") if "IsCancelled" in dictionary.keys() else APIHelper.SKIP
        customer_currency_code = dictionary.get("CustomerCurrencyCode") if "CustomerCurrencyCode" in dictionary.keys() else APIHelper.SKIP
        customer_currency_symbol = dictionary.get("CustomerCurrencySymbol") if "CustomerCurrencySymbol" in dictionary.keys() else APIHelper.SKIP
        product_id = dictionary.get("ProductId") if "ProductId" in dictionary.keys() else APIHelper.SKIP
        product_code = dictionary.get("ProductCode") if "ProductCode" in dictionary.keys() else APIHelper.SKIP
        product_name = dictionary.get("ProductName") if "ProductName" in dictionary.keys() else APIHelper.SKIP
        product_group_id = dictionary.get("ProductGroupId") if "ProductGroupId" in dictionary.keys() else APIHelper.SKIP
        product_group_name = dictionary.get("ProductGroupName") if "ProductGroupName" in dictionary.keys() else APIHelper.SKIP
        line_item_description = dictionary.get("LineItemDescription") if "LineItemDescription" in dictionary.keys() else APIHelper.SKIP
        quantity = dictionary.get("Quantity") if "Quantity" in dictionary.keys() else APIHelper.SKIP
        is_invoiced = dictionary.get("IsInvoiced") if "IsInvoiced" in dictionary.keys() else APIHelper.SKIP
        vat_country_code = dictionary.get("VATCountryCode") if "VATCountryCode" in dictionary.keys() else APIHelper.SKIP
        vat_country_name = dictionary.get("VATCountryName") if "VATCountryName" in dictionary.keys() else APIHelper.SKIP
        vat_percentage = dictionary.get("VATPercentage") if "VATPercentage" in dictionary.keys() else APIHelper.SKIP
        vat_category_id = dictionary.get("VATCategoryID") if "VATCategoryID" in dictionary.keys() else APIHelper.SKIP
        vat_category_description = dictionary.get("VATCategoryDescription") if "VATCategoryDescription" in dictionary.keys() else APIHelper.SKIP
        legislative_region_id = dictionary.get("LegislativeRegionId") if "LegislativeRegionId" in dictionary.keys() else APIHelper.SKIP
        legislative_region_name = dictionary.get("LegislativeRegionName") if "LegislativeRegionName" in dictionary.keys() else APIHelper.SKIP
        system_entry_date = dictionary.get("SystemEntryDate") if "SystemEntryDate" in dictionary.keys() else APIHelper.SKIP
        system_entry_time = dictionary.get("SystemEntryTime") if "SystemEntryTime" in dictionary.keys() else APIHelper.SKIP
        col_co_net_amount = dictionary.get("ColCoNetAmount") if "ColCoNetAmount" in dictionary.keys() else APIHelper.SKIP
        col_co_vat_amount = dictionary.get("ColCoVATAmount") if "ColCoVATAmount" in dictionary.keys() else APIHelper.SKIP
        col_co_gross_amount = dictionary.get("ColCoGrossAmount") if "ColCoGrossAmount" in dictionary.keys() else APIHelper.SKIP
        interim_invoice_id = dictionary.get("InterimInvoiceId") if "InterimInvoiceId" in dictionary.keys() else APIHelper.SKIP
        interim_invoice_number = dictionary.get("InterimInvoiceNumber") if "InterimInvoiceNumber" in dictionary.keys() else APIHelper.SKIP
        invoice_id = dictionary.get("InvoiceId") if "InvoiceId" in dictionary.keys() else APIHelper.SKIP
        invoice_number = dictionary.get("InvoiceNumber") if "InvoiceNumber" in dictionary.keys() else APIHelper.SKIP
        invoice_date = dictionary.get("InvoiceDate") if "InvoiceDate" in dictionary.keys() else APIHelper.SKIP
        customer_exchange_rate = dictionary.get("CustomerExchangeRate") if "CustomerExchangeRate" in dictionary.keys() else APIHelper.SKIP
        invoice_net_amount = dictionary.get("InvoiceNetAmount") if "InvoiceNetAmount" in dictionary.keys() else APIHelper.SKIP
        invoice_gross_amount = dictionary.get("InvoiceGrossAmount") if "InvoiceGrossAmount" in dictionary.keys() else APIHelper.SKIP
        invoice_vat_amount = dictionary.get("InvoiceVATAmount") if "InvoiceVATAmount" in dictionary.keys() else APIHelper.SKIP
        reverse_charge = dictionary.get("ReverseCharge") if "ReverseCharge" in dictionary.keys() else APIHelper.SKIP
        original_fee_item_id = dictionary.get("OriginalFeeItemId") if "OriginalFeeItemId" in dictionary.keys() else APIHelper.SKIP
        original_currency_code = dictionary.get("OriginalCurrencyCode") if "OriginalCurrencyCode" in dictionary.keys() else APIHelper.SKIP
        original_currency_symbol = dictionary.get("OriginalCurrencySymbol") if "OriginalCurrencySymbol" in dictionary.keys() else APIHelper.SKIP
        original_unit_price = dictionary.get("OriginalUnitPrice") if "OriginalUnitPrice" in dictionary.keys() else APIHelper.SKIP
        original_net_amount = dictionary.get("OriginalNetAmount") if "OriginalNetAmount" in dictionary.keys() else APIHelper.SKIP
        original_vat_amount = dictionary.get("OriginalVATAmount") if "OriginalVATAmount" in dictionary.keys() else APIHelper.SKIP
        original_gross_amount = dictionary.get("OriginalGrossAmount") if "OriginalGrossAmount" in dictionary.keys() else APIHelper.SKIP
        original_exchange_rate = dictionary.get("OriginalExchangeRate") if "OriginalExchangeRate" in dictionary.keys() else APIHelper.SKIP
        original_legislative_region_id = dictionary.get("OriginalLegislativeRegionId") if "OriginalLegislativeRegionId" in dictionary.keys() else APIHelper.SKIP
        original_legislative_region_name = dictionary.get("OriginalLegislativeRegionName") if "OriginalLegislativeRegionName" in dictionary.keys() else APIHelper.SKIP
        frequency = dictionary.get("Frequency") if "Frequency" in dictionary.keys() else APIHelper.SKIP
        fee_item_card_level_breakup = dictionary.get("FeeItemCardLevelBreakup") if "FeeItemCardLevelBreakup" in dictionary.keys() else APIHelper.SKIP
        original_fee_item_invoice_id = dictionary.get("OriginalFeeItemInvoiceId") if "OriginalFeeItemInvoiceId" in dictionary.keys() else APIHelper.SKIP
        original_fee_item_invoice_number = dictionary.get("OriginalFeeItemInvoiceNumber") if "OriginalFeeItemInvoiceNumber" in dictionary.keys() else APIHelper.SKIP
        original_fee_item_invoice_date = dictionary.get("OriginalFeeItemInvoiceDate") if "OriginalFeeItemInvoiceDate" in dictionary.keys() else APIHelper.SKIP
        driver_name = dictionary.get("DriverName") if "DriverName" in dictionary.keys() else APIHelper.SKIP
        emboss_text = dictionary.get("EmbossText") if "EmbossText" in dictionary.keys() else APIHelper.SKIP
        vrn = dictionary.get("VRN") if "VRN" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(fee_item_id,
                   account_id,
                   account_number,
                   account_short_name,
                   invoice_account_id,
                   invoice_account_number,
                   invoice_account_short_name,
                   payer_id,
                   payer_number,
                   payer_short_name,
                   card_id,
                   pan,
                   card_group_id,
                   card_group_name,
                   fee_type_id,
                   fee_type,
                   fee_type_group,
                   fee_rule_id,
                   fee_rule_description,
                   fee_rule_tiers,
                   fee_item_date,
                   fee_item_time,
                   is_manual,
                   is_cancelled,
                   customer_currency_code,
                   customer_currency_symbol,
                   product_id,
                   product_code,
                   product_name,
                   product_group_id,
                   product_group_name,
                   line_item_description,
                   quantity,
                   is_invoiced,
                   vat_country_code,
                   vat_country_name,
                   vat_percentage,
                   vat_category_id,
                   vat_category_description,
                   legislative_region_id,
                   legislative_region_name,
                   system_entry_date,
                   system_entry_time,
                   col_co_net_amount,
                   col_co_vat_amount,
                   col_co_gross_amount,
                   interim_invoice_id,
                   interim_invoice_number,
                   invoice_id,
                   invoice_number,
                   invoice_date,
                   customer_exchange_rate,
                   invoice_net_amount,
                   invoice_gross_amount,
                   invoice_vat_amount,
                   reverse_charge,
                   original_fee_item_id,
                   original_currency_code,
                   original_currency_symbol,
                   original_unit_price,
                   original_net_amount,
                   original_vat_amount,
                   original_gross_amount,
                   original_exchange_rate,
                   original_legislative_region_id,
                   original_legislative_region_name,
                   frequency,
                   fee_item_card_level_breakup,
                   original_fee_item_invoice_id,
                   original_fee_item_invoice_number,
                   original_fee_item_invoice_date,
                   driver_name,
                   emboss_text,
                   vrn)
