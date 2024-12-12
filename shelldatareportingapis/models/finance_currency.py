# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper


class FinanceCurrency(object):

    """Implementation of the 'FinanceCurrency' model.

    This entity will not be present in the response if the
    ‘IncludeFinanceCurrency’ flag in the request is ‘false’

    Attributes:
        currency_code (str): Currency ISO Code used for the Finance Widget.
        currency_symbol (str): Currency Symbol
        invoice_exchange_rate (float): Factor to be used for converting the
            amounts in invoice currency to finance widget currency. (If
            finance currency is same as invoice currency, then the value of
            this field will be “1” so that the value does not change)
        credit_limit_exchange_rate (float): Factor to be used for converting
            the amounts in credit limit currency to finance widget currency.
            (If finance currency is same as credit limit currency, then the
            value of this field will be “1” so that the value does not change)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "currency_code": 'CurrencyCode',
        "currency_symbol": 'CurrencySymbol',
        "invoice_exchange_rate": 'Invoice_ExchangeRate',
        "credit_limit_exchange_rate": 'CreditLimit_ExchangeRate'
    }

    _optionals = [
        'currency_code',
        'currency_symbol',
        'invoice_exchange_rate',
        'credit_limit_exchange_rate',
    ]

    _nullables = [
        'currency_code',
        'currency_symbol',
        'invoice_exchange_rate',
        'credit_limit_exchange_rate',
    ]

    def __init__(self,
                 currency_code=APIHelper.SKIP,
                 currency_symbol=APIHelper.SKIP,
                 invoice_exchange_rate=APIHelper.SKIP,
                 credit_limit_exchange_rate=APIHelper.SKIP):
        """Constructor for the FinanceCurrency class"""

        # Initialize members of the class
        if currency_code is not APIHelper.SKIP:
            self.currency_code = currency_code 
        if currency_symbol is not APIHelper.SKIP:
            self.currency_symbol = currency_symbol 
        if invoice_exchange_rate is not APIHelper.SKIP:
            self.invoice_exchange_rate = invoice_exchange_rate 
        if credit_limit_exchange_rate is not APIHelper.SKIP:
            self.credit_limit_exchange_rate = credit_limit_exchange_rate 

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
        currency_code = dictionary.get("CurrencyCode") if "CurrencyCode" in dictionary.keys() else APIHelper.SKIP
        currency_symbol = dictionary.get("CurrencySymbol") if "CurrencySymbol" in dictionary.keys() else APIHelper.SKIP
        invoice_exchange_rate = dictionary.get("Invoice_ExchangeRate") if "Invoice_ExchangeRate" in dictionary.keys() else APIHelper.SKIP
        credit_limit_exchange_rate = dictionary.get("CreditLimit_ExchangeRate") if "CreditLimit_ExchangeRate" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(currency_code,
                   currency_symbol,
                   invoice_exchange_rate,
                   credit_limit_exchange_rate)
