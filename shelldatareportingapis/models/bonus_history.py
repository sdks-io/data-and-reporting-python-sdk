# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper


class BonusHistory(object):

    """Implementation of the 'BonusHistory' model.

    TODO: type model description here.

    Attributes:
        payer_id (int): Payer Id
        payer_number (str): Payer Number of the selected payer
        payer_short_name (str): Payer short name.
        payer_full_name (str): Payer full name.
        account_id (int): Account Id
        account_number (str): Account Number of the selected payer.
        account_short_name (str): Account short name.
        account_full_name (str): Account full name.
        invoice_account_id (int): Invoice Account Id
        invoice_account_number (str): Invoice Account Number of the selected
            payer.
        invoice_account_short_name (str): Invoice Account short name.
        invoice_account_full_name (str): Invoice Account full name.
        fee_rule_id (str): Bonus or association bonus configuration identifier
        fee_rule_description (str): Bonus or association bonus configuration
            description that is associated to the bonus fee item
        from_date (str): Bonus was calculated from this date. Format: YYYYMMDD
        to_date (str): Bonus was calculated till this date. Format: YYYYMMDD
        bonus_paid_to (str): Specifies how the bonus was paid back.  Format:
            ID-Description  Example:   1-Pay to Payer  2-Pay to invoice levels
            before the payer  3-Pay to specific customer  4-Pay to Association
            Customer  5-Pay to Associated Customers
        fee_item_id (int): Bonus fee item identifier.
        fee_rule_basis (str): Fee Rule Basis of the bonus fee item. Format:
            ID-Description Example: 1-Currency Per Unit 2-Percentage of Uplift
            3-Lump Sum
        fee_item_currency_code (str): ISO currency code of the currency in
            which Bonus is paid. Example: GBP
        fee_item_currency_symbol (str): Currency symbol of the currency in
            which Bonus is paid.
        prorated_volume (float): Prorated volume considered under the account
            as  configured for the bonus association.
        total_volume (float): Total volume considered for calculating the
            bonus.
        fee_product (str): Product as shown in the invoice for the bonus paid.
            Format: ID-Description Example: 1562-Bonus diesel Shell
            Netherlands on agreed site(s)
        invoice_gross_amount (float): Gross Amount – Bonus Paid including VAT
            as shown on the Invoice
        invoice_net_amount (float): Net Amount – Bonus Paid excluding VAT as
            shown on the Invoice
        invoice_vat_amount (float): VAT calculated for the bonus paid as shown
            on the Invoice
        is_fee_cancelled (bool): True/False True if bonus is generated but
            cancelled. When true, consider this as not paid.
        fee_item_tier_prorated_volume (float): Prorated volume in the bonus
            fee item tier.
        fee_item_tier_total_volume (float): Total volume in the bonus fee item
            tier.
        tier_minimum (int): Tier minimum value considered for calculation
        tier_rate (float): Tier rate considered for calculation

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber',
        "payer_short_name": 'PayerShortName',
        "payer_full_name": 'PayerFullName',
        "account_id": 'AccountId',
        "account_number": 'AccountNumber',
        "account_short_name": 'AccountShortName',
        "account_full_name": 'AccountFullName',
        "invoice_account_id": 'InvoiceAccountId',
        "invoice_account_number": 'InvoiceAccountNumber',
        "invoice_account_short_name": 'InvoiceAccountShortName',
        "invoice_account_full_name": 'InvoiceAccountFullName',
        "fee_rule_id": 'FeeRuleId',
        "fee_rule_description": 'FeeRuleDescription',
        "from_date": 'FromDate',
        "to_date": 'ToDate',
        "bonus_paid_to": 'BonusPaidTo',
        "fee_item_id": 'FeeItemId',
        "fee_rule_basis": 'FeeRuleBasis',
        "fee_item_currency_code": 'FeeItemCurrencyCode',
        "fee_item_currency_symbol": 'FeeItemCurrencySymbol',
        "prorated_volume": 'ProratedVolume',
        "total_volume": 'TotalVolume',
        "fee_product": 'FeeProduct',
        "invoice_gross_amount": 'InvoiceGrossAmount',
        "invoice_net_amount": 'InvoiceNetAmount',
        "invoice_vat_amount": 'InvoiceVATAmount',
        "is_fee_cancelled": 'IsFeeCancelled',
        "fee_item_tier_prorated_volume": 'FeeItemTierProratedVolume',
        "fee_item_tier_total_volume": 'FeeItemTierTotalVolume',
        "tier_minimum": 'TierMinimum',
        "tier_rate": 'TierRate'
    }

    _optionals = [
        'payer_id',
        'payer_number',
        'payer_short_name',
        'payer_full_name',
        'account_id',
        'account_number',
        'account_short_name',
        'account_full_name',
        'invoice_account_id',
        'invoice_account_number',
        'invoice_account_short_name',
        'invoice_account_full_name',
        'fee_rule_id',
        'fee_rule_description',
        'from_date',
        'to_date',
        'bonus_paid_to',
        'fee_item_id',
        'fee_rule_basis',
        'fee_item_currency_code',
        'fee_item_currency_symbol',
        'prorated_volume',
        'total_volume',
        'fee_product',
        'invoice_gross_amount',
        'invoice_net_amount',
        'invoice_vat_amount',
        'is_fee_cancelled',
        'fee_item_tier_prorated_volume',
        'fee_item_tier_total_volume',
        'tier_minimum',
        'tier_rate',
    ]

    _nullables = [
        'payer_id',
        'payer_number',
        'payer_short_name',
        'payer_full_name',
        'account_id',
        'account_number',
        'account_short_name',
        'account_full_name',
        'invoice_account_id',
        'invoice_account_number',
        'invoice_account_short_name',
        'invoice_account_full_name',
        'fee_rule_id',
        'fee_rule_description',
        'from_date',
        'to_date',
        'bonus_paid_to',
        'fee_item_id',
        'fee_rule_basis',
        'fee_item_currency_code',
        'fee_item_currency_symbol',
        'prorated_volume',
        'total_volume',
        'fee_product',
        'invoice_gross_amount',
        'invoice_net_amount',
        'invoice_vat_amount',
        'is_fee_cancelled',
        'fee_item_tier_prorated_volume',
        'fee_item_tier_total_volume',
        'tier_minimum',
        'tier_rate',
    ]

    def __init__(self,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 payer_short_name=APIHelper.SKIP,
                 payer_full_name=APIHelper.SKIP,
                 account_id=APIHelper.SKIP,
                 account_number=APIHelper.SKIP,
                 account_short_name=APIHelper.SKIP,
                 account_full_name=APIHelper.SKIP,
                 invoice_account_id=APIHelper.SKIP,
                 invoice_account_number=APIHelper.SKIP,
                 invoice_account_short_name=APIHelper.SKIP,
                 invoice_account_full_name=APIHelper.SKIP,
                 fee_rule_id=APIHelper.SKIP,
                 fee_rule_description=APIHelper.SKIP,
                 from_date=APIHelper.SKIP,
                 to_date=APIHelper.SKIP,
                 bonus_paid_to=APIHelper.SKIP,
                 fee_item_id=APIHelper.SKIP,
                 fee_rule_basis=APIHelper.SKIP,
                 fee_item_currency_code=APIHelper.SKIP,
                 fee_item_currency_symbol=APIHelper.SKIP,
                 prorated_volume=APIHelper.SKIP,
                 total_volume=APIHelper.SKIP,
                 fee_product=APIHelper.SKIP,
                 invoice_gross_amount=APIHelper.SKIP,
                 invoice_net_amount=APIHelper.SKIP,
                 invoice_vat_amount=APIHelper.SKIP,
                 is_fee_cancelled=APIHelper.SKIP,
                 fee_item_tier_prorated_volume=APIHelper.SKIP,
                 fee_item_tier_total_volume=APIHelper.SKIP,
                 tier_minimum=APIHelper.SKIP,
                 tier_rate=APIHelper.SKIP):
        """Constructor for the BonusHistory class"""

        # Initialize members of the class
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 
        if payer_short_name is not APIHelper.SKIP:
            self.payer_short_name = payer_short_name 
        if payer_full_name is not APIHelper.SKIP:
            self.payer_full_name = payer_full_name 
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if account_short_name is not APIHelper.SKIP:
            self.account_short_name = account_short_name 
        if account_full_name is not APIHelper.SKIP:
            self.account_full_name = account_full_name 
        if invoice_account_id is not APIHelper.SKIP:
            self.invoice_account_id = invoice_account_id 
        if invoice_account_number is not APIHelper.SKIP:
            self.invoice_account_number = invoice_account_number 
        if invoice_account_short_name is not APIHelper.SKIP:
            self.invoice_account_short_name = invoice_account_short_name 
        if invoice_account_full_name is not APIHelper.SKIP:
            self.invoice_account_full_name = invoice_account_full_name 
        if fee_rule_id is not APIHelper.SKIP:
            self.fee_rule_id = fee_rule_id 
        if fee_rule_description is not APIHelper.SKIP:
            self.fee_rule_description = fee_rule_description 
        if from_date is not APIHelper.SKIP:
            self.from_date = from_date 
        if to_date is not APIHelper.SKIP:
            self.to_date = to_date 
        if bonus_paid_to is not APIHelper.SKIP:
            self.bonus_paid_to = bonus_paid_to 
        if fee_item_id is not APIHelper.SKIP:
            self.fee_item_id = fee_item_id 
        if fee_rule_basis is not APIHelper.SKIP:
            self.fee_rule_basis = fee_rule_basis 
        if fee_item_currency_code is not APIHelper.SKIP:
            self.fee_item_currency_code = fee_item_currency_code 
        if fee_item_currency_symbol is not APIHelper.SKIP:
            self.fee_item_currency_symbol = fee_item_currency_symbol 
        if prorated_volume is not APIHelper.SKIP:
            self.prorated_volume = prorated_volume 
        if total_volume is not APIHelper.SKIP:
            self.total_volume = total_volume 
        if fee_product is not APIHelper.SKIP:
            self.fee_product = fee_product 
        if invoice_gross_amount is not APIHelper.SKIP:
            self.invoice_gross_amount = invoice_gross_amount 
        if invoice_net_amount is not APIHelper.SKIP:
            self.invoice_net_amount = invoice_net_amount 
        if invoice_vat_amount is not APIHelper.SKIP:
            self.invoice_vat_amount = invoice_vat_amount 
        if is_fee_cancelled is not APIHelper.SKIP:
            self.is_fee_cancelled = is_fee_cancelled 
        if fee_item_tier_prorated_volume is not APIHelper.SKIP:
            self.fee_item_tier_prorated_volume = fee_item_tier_prorated_volume 
        if fee_item_tier_total_volume is not APIHelper.SKIP:
            self.fee_item_tier_total_volume = fee_item_tier_total_volume 
        if tier_minimum is not APIHelper.SKIP:
            self.tier_minimum = tier_minimum 
        if tier_rate is not APIHelper.SKIP:
            self.tier_rate = tier_rate 

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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        payer_id = dictionary.get("PayerId") if "PayerId" in dictionary.keys() else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if "PayerNumber" in dictionary.keys() else APIHelper.SKIP
        payer_short_name = dictionary.get("PayerShortName") if "PayerShortName" in dictionary.keys() else APIHelper.SKIP
        payer_full_name = dictionary.get("PayerFullName") if "PayerFullName" in dictionary.keys() else APIHelper.SKIP
        account_id = dictionary.get("AccountId") if "AccountId" in dictionary.keys() else APIHelper.SKIP
        account_number = dictionary.get("AccountNumber") if "AccountNumber" in dictionary.keys() else APIHelper.SKIP
        account_short_name = dictionary.get("AccountShortName") if "AccountShortName" in dictionary.keys() else APIHelper.SKIP
        account_full_name = dictionary.get("AccountFullName") if "AccountFullName" in dictionary.keys() else APIHelper.SKIP
        invoice_account_id = dictionary.get("InvoiceAccountId") if "InvoiceAccountId" in dictionary.keys() else APIHelper.SKIP
        invoice_account_number = dictionary.get("InvoiceAccountNumber") if "InvoiceAccountNumber" in dictionary.keys() else APIHelper.SKIP
        invoice_account_short_name = dictionary.get("InvoiceAccountShortName") if "InvoiceAccountShortName" in dictionary.keys() else APIHelper.SKIP
        invoice_account_full_name = dictionary.get("InvoiceAccountFullName") if "InvoiceAccountFullName" in dictionary.keys() else APIHelper.SKIP
        fee_rule_id = dictionary.get("FeeRuleId") if "FeeRuleId" in dictionary.keys() else APIHelper.SKIP
        fee_rule_description = dictionary.get("FeeRuleDescription") if "FeeRuleDescription" in dictionary.keys() else APIHelper.SKIP
        from_date = dictionary.get("FromDate") if "FromDate" in dictionary.keys() else APIHelper.SKIP
        to_date = dictionary.get("ToDate") if "ToDate" in dictionary.keys() else APIHelper.SKIP
        bonus_paid_to = dictionary.get("BonusPaidTo") if "BonusPaidTo" in dictionary.keys() else APIHelper.SKIP
        fee_item_id = dictionary.get("FeeItemId") if "FeeItemId" in dictionary.keys() else APIHelper.SKIP
        fee_rule_basis = dictionary.get("FeeRuleBasis") if "FeeRuleBasis" in dictionary.keys() else APIHelper.SKIP
        fee_item_currency_code = dictionary.get("FeeItemCurrencyCode") if "FeeItemCurrencyCode" in dictionary.keys() else APIHelper.SKIP
        fee_item_currency_symbol = dictionary.get("FeeItemCurrencySymbol") if "FeeItemCurrencySymbol" in dictionary.keys() else APIHelper.SKIP
        prorated_volume = dictionary.get("ProratedVolume") if "ProratedVolume" in dictionary.keys() else APIHelper.SKIP
        total_volume = dictionary.get("TotalVolume") if "TotalVolume" in dictionary.keys() else APIHelper.SKIP
        fee_product = dictionary.get("FeeProduct") if "FeeProduct" in dictionary.keys() else APIHelper.SKIP
        invoice_gross_amount = dictionary.get("InvoiceGrossAmount") if "InvoiceGrossAmount" in dictionary.keys() else APIHelper.SKIP
        invoice_net_amount = dictionary.get("InvoiceNetAmount") if "InvoiceNetAmount" in dictionary.keys() else APIHelper.SKIP
        invoice_vat_amount = dictionary.get("InvoiceVATAmount") if "InvoiceVATAmount" in dictionary.keys() else APIHelper.SKIP
        is_fee_cancelled = dictionary.get("IsFeeCancelled") if "IsFeeCancelled" in dictionary.keys() else APIHelper.SKIP
        fee_item_tier_prorated_volume = dictionary.get("FeeItemTierProratedVolume") if "FeeItemTierProratedVolume" in dictionary.keys() else APIHelper.SKIP
        fee_item_tier_total_volume = dictionary.get("FeeItemTierTotalVolume") if "FeeItemTierTotalVolume" in dictionary.keys() else APIHelper.SKIP
        tier_minimum = dictionary.get("TierMinimum") if "TierMinimum" in dictionary.keys() else APIHelper.SKIP
        tier_rate = dictionary.get("TierRate") if "TierRate" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(payer_id,
                   payer_number,
                   payer_short_name,
                   payer_full_name,
                   account_id,
                   account_number,
                   account_short_name,
                   account_full_name,
                   invoice_account_id,
                   invoice_account_number,
                   invoice_account_short_name,
                   invoice_account_full_name,
                   fee_rule_id,
                   fee_rule_description,
                   from_date,
                   to_date,
                   bonus_paid_to,
                   fee_item_id,
                   fee_rule_basis,
                   fee_item_currency_code,
                   fee_item_currency_symbol,
                   prorated_volume,
                   total_volume,
                   fee_product,
                   invoice_gross_amount,
                   invoice_net_amount,
                   invoice_vat_amount,
                   is_fee_cancelled,
                   fee_item_tier_prorated_volume,
                   fee_item_tier_total_volume,
                   tier_minimum,
                   tier_rate)
