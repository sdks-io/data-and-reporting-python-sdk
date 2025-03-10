# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper


class InvoiceSummaryDetails(object):

    """Implementation of the 'InvoiceSummaryDetails' model.

    Attributes:
        total_invoices (int): Total number of invoices matching with the given
            search criteria.
        total_gross_amount_customer_currency (float): Total gross amount in
            customer currency combined from all the invoices matching with the
            given search criteria.
        total_net_amount_customer_currency (float): Total net amount in
            customer currency combined from all the invoices matching with the
            given search criteria.
        total_vat_amount_customer_currency (float): Total VAT amount in
            customer currency combined from all the invoices matching with the
            given search criteria.
        customer_currency_code (str): Customer currency ISO code. Example: EUR
        customer_currency_symbol (str): Customer currency code. Example: €

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "total_invoices": 'TotalInvoices',
        "total_gross_amount_customer_currency": 'TotalGrossAmountCustomerCurrency',
        "total_net_amount_customer_currency": 'TotalNetAmountCustomerCurrency',
        "total_vat_amount_customer_currency": 'TotalVATAmountCustomerCurrency',
        "customer_currency_code": 'CustomerCurrencyCode',
        "customer_currency_symbol": 'CustomerCurrencySymbol'
    }

    _optionals = [
        'total_invoices',
        'total_gross_amount_customer_currency',
        'total_net_amount_customer_currency',
        'total_vat_amount_customer_currency',
        'customer_currency_code',
        'customer_currency_symbol',
    ]

    _nullables = [
        'total_invoices',
        'total_gross_amount_customer_currency',
        'total_net_amount_customer_currency',
        'total_vat_amount_customer_currency',
        'customer_currency_code',
        'customer_currency_symbol',
    ]

    def __init__(self,
                 total_invoices=APIHelper.SKIP,
                 total_gross_amount_customer_currency=APIHelper.SKIP,
                 total_net_amount_customer_currency=APIHelper.SKIP,
                 total_vat_amount_customer_currency=APIHelper.SKIP,
                 customer_currency_code=APIHelper.SKIP,
                 customer_currency_symbol=APIHelper.SKIP):
        """Constructor for the InvoiceSummaryDetails class"""

        # Initialize members of the class
        if total_invoices is not APIHelper.SKIP:
            self.total_invoices = total_invoices 
        if total_gross_amount_customer_currency is not APIHelper.SKIP:
            self.total_gross_amount_customer_currency = total_gross_amount_customer_currency 
        if total_net_amount_customer_currency is not APIHelper.SKIP:
            self.total_net_amount_customer_currency = total_net_amount_customer_currency 
        if total_vat_amount_customer_currency is not APIHelper.SKIP:
            self.total_vat_amount_customer_currency = total_vat_amount_customer_currency 
        if customer_currency_code is not APIHelper.SKIP:
            self.customer_currency_code = customer_currency_code 
        if customer_currency_symbol is not APIHelper.SKIP:
            self.customer_currency_symbol = customer_currency_symbol 

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
        total_invoices = dictionary.get("TotalInvoices") if "TotalInvoices" in dictionary.keys() else APIHelper.SKIP
        total_gross_amount_customer_currency = dictionary.get("TotalGrossAmountCustomerCurrency") if "TotalGrossAmountCustomerCurrency" in dictionary.keys() else APIHelper.SKIP
        total_net_amount_customer_currency = dictionary.get("TotalNetAmountCustomerCurrency") if "TotalNetAmountCustomerCurrency" in dictionary.keys() else APIHelper.SKIP
        total_vat_amount_customer_currency = dictionary.get("TotalVATAmountCustomerCurrency") if "TotalVATAmountCustomerCurrency" in dictionary.keys() else APIHelper.SKIP
        customer_currency_code = dictionary.get("CustomerCurrencyCode") if "CustomerCurrencyCode" in dictionary.keys() else APIHelper.SKIP
        customer_currency_symbol = dictionary.get("CustomerCurrencySymbol") if "CustomerCurrencySymbol" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(total_invoices,
                   total_gross_amount_customer_currency,
                   total_net_amount_customer_currency,
                   total_vat_amount_customer_currency,
                   customer_currency_code,
                   customer_currency_symbol)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'total_invoices={(self.total_invoices if hasattr(self, "total_invoices") else None)!r}, '
                f'total_gross_amount_customer_currency={(self.total_gross_amount_customer_currency if hasattr(self, "total_gross_amount_customer_currency") else None)!r}, '
                f'total_net_amount_customer_currency={(self.total_net_amount_customer_currency if hasattr(self, "total_net_amount_customer_currency") else None)!r}, '
                f'total_vat_amount_customer_currency={(self.total_vat_amount_customer_currency if hasattr(self, "total_vat_amount_customer_currency") else None)!r}, '
                f'customer_currency_code={(self.customer_currency_code if hasattr(self, "customer_currency_code") else None)!r}, '
                f'customer_currency_symbol={(self.customer_currency_symbol if hasattr(self, "customer_currency_symbol") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'total_invoices={(self.total_invoices if hasattr(self, "total_invoices") else None)!s}, '
                f'total_gross_amount_customer_currency={(self.total_gross_amount_customer_currency if hasattr(self, "total_gross_amount_customer_currency") else None)!s}, '
                f'total_net_amount_customer_currency={(self.total_net_amount_customer_currency if hasattr(self, "total_net_amount_customer_currency") else None)!s}, '
                f'total_vat_amount_customer_currency={(self.total_vat_amount_customer_currency if hasattr(self, "total_vat_amount_customer_currency") else None)!s}, '
                f'customer_currency_code={(self.customer_currency_code if hasattr(self, "customer_currency_code") else None)!s}, '
                f'customer_currency_symbol={(self.customer_currency_symbol if hasattr(self, "customer_currency_symbol") else None)!s})')
