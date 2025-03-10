# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper


class CardExceptions(object):

    """Implementation of the 'CardExceptions' model.

    Attributes:
        account_id (int): Account Id
        account_number (str): Account Number
        account_short_name (str): Account Short Name
        card_id (int): Unique Card Id
        currency_code (str): ISO currency code
        currency_symbol (str): Currency symbol of the Invoice Currency Code
        day (int): Summary Day: Populated when the Period is passed as ‘Day’.
        driver_name (str): Driver name
        month (int): Summary Month: Populated when the Value of Period is
            Passed as ‘Month’.
        pan (str): Card PAN
        payer_id (int): Payment customer id of the customer
        payer_number (str): Payment customer number
        payer_short_name (str): Payer Short Name
        total_amount (float): Total Amount (In Customer Currency) of
            Transactions met with the given exceptions criteria.
        total_quantity (int): Total Quantity of Transactions met with the
            given exceptions criteria.
        total_sales_items (int): Total number of Sales Items met with the
            given exception criteria.
        total_transactions (int): Total number of Transactions met with the
            given exception criteria.
        vrn (str): Vehicle Registration Number
        week (int): Summary Week Number with in the given date range.
            Populated when the Value of Period is Passed as ‘Week’.
        year (int): Summary Year: Populated when the Value of Period is Passed
            as ‘Month’.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_id": 'AccountId',
        "account_number": 'AccountNumber',
        "account_short_name": 'AccountShortName',
        "card_id": 'CardId',
        "currency_code": 'CurrencyCode',
        "currency_symbol": 'CurrencySymbol',
        "day": 'Day',
        "driver_name": 'DriverName',
        "month": 'Month',
        "pan": 'PAN',
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber',
        "payer_short_name": 'PayerShortName',
        "total_amount": 'TotalAmount',
        "total_quantity": 'TotalQuantity',
        "total_sales_items": 'TotalSalesItems',
        "total_transactions": 'TotalTransactions',
        "vrn": 'VRN',
        "week": 'Week',
        "year": 'Year'
    }

    _optionals = [
        'account_id',
        'account_number',
        'account_short_name',
        'card_id',
        'currency_code',
        'currency_symbol',
        'day',
        'driver_name',
        'month',
        'pan',
        'payer_id',
        'payer_number',
        'payer_short_name',
        'total_amount',
        'total_quantity',
        'total_sales_items',
        'total_transactions',
        'vrn',
        'week',
        'year',
    ]

    _nullables = [
        'account_id',
        'account_number',
        'account_short_name',
        'card_id',
        'currency_code',
        'currency_symbol',
        'day',
        'driver_name',
        'month',
        'pan',
        'payer_id',
        'payer_number',
        'payer_short_name',
        'total_amount',
        'total_quantity',
        'total_sales_items',
        'total_transactions',
        'vrn',
        'week',
        'year',
    ]

    def __init__(self,
                 account_id=APIHelper.SKIP,
                 account_number=APIHelper.SKIP,
                 account_short_name=APIHelper.SKIP,
                 card_id=APIHelper.SKIP,
                 currency_code=APIHelper.SKIP,
                 currency_symbol=APIHelper.SKIP,
                 day=APIHelper.SKIP,
                 driver_name=APIHelper.SKIP,
                 month=APIHelper.SKIP,
                 pan=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 payer_short_name=APIHelper.SKIP,
                 total_amount=APIHelper.SKIP,
                 total_quantity=APIHelper.SKIP,
                 total_sales_items=APIHelper.SKIP,
                 total_transactions=APIHelper.SKIP,
                 vrn=APIHelper.SKIP,
                 week=APIHelper.SKIP,
                 year=APIHelper.SKIP):
        """Constructor for the CardExceptions class"""

        # Initialize members of the class
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if account_short_name is not APIHelper.SKIP:
            self.account_short_name = account_short_name 
        if card_id is not APIHelper.SKIP:
            self.card_id = card_id 
        if currency_code is not APIHelper.SKIP:
            self.currency_code = currency_code 
        if currency_symbol is not APIHelper.SKIP:
            self.currency_symbol = currency_symbol 
        if day is not APIHelper.SKIP:
            self.day = day 
        if driver_name is not APIHelper.SKIP:
            self.driver_name = driver_name 
        if month is not APIHelper.SKIP:
            self.month = month 
        if pan is not APIHelper.SKIP:
            self.pan = pan 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 
        if payer_short_name is not APIHelper.SKIP:
            self.payer_short_name = payer_short_name 
        if total_amount is not APIHelper.SKIP:
            self.total_amount = total_amount 
        if total_quantity is not APIHelper.SKIP:
            self.total_quantity = total_quantity 
        if total_sales_items is not APIHelper.SKIP:
            self.total_sales_items = total_sales_items 
        if total_transactions is not APIHelper.SKIP:
            self.total_transactions = total_transactions 
        if vrn is not APIHelper.SKIP:
            self.vrn = vrn 
        if week is not APIHelper.SKIP:
            self.week = week 
        if year is not APIHelper.SKIP:
            self.year = year 

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
        account_id = dictionary.get("AccountId") if "AccountId" in dictionary.keys() else APIHelper.SKIP
        account_number = dictionary.get("AccountNumber") if "AccountNumber" in dictionary.keys() else APIHelper.SKIP
        account_short_name = dictionary.get("AccountShortName") if "AccountShortName" in dictionary.keys() else APIHelper.SKIP
        card_id = dictionary.get("CardId") if "CardId" in dictionary.keys() else APIHelper.SKIP
        currency_code = dictionary.get("CurrencyCode") if "CurrencyCode" in dictionary.keys() else APIHelper.SKIP
        currency_symbol = dictionary.get("CurrencySymbol") if "CurrencySymbol" in dictionary.keys() else APIHelper.SKIP
        day = dictionary.get("Day") if "Day" in dictionary.keys() else APIHelper.SKIP
        driver_name = dictionary.get("DriverName") if "DriverName" in dictionary.keys() else APIHelper.SKIP
        month = dictionary.get("Month") if "Month" in dictionary.keys() else APIHelper.SKIP
        pan = dictionary.get("PAN") if "PAN" in dictionary.keys() else APIHelper.SKIP
        payer_id = dictionary.get("PayerId") if "PayerId" in dictionary.keys() else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if "PayerNumber" in dictionary.keys() else APIHelper.SKIP
        payer_short_name = dictionary.get("PayerShortName") if "PayerShortName" in dictionary.keys() else APIHelper.SKIP
        total_amount = dictionary.get("TotalAmount") if "TotalAmount" in dictionary.keys() else APIHelper.SKIP
        total_quantity = dictionary.get("TotalQuantity") if "TotalQuantity" in dictionary.keys() else APIHelper.SKIP
        total_sales_items = dictionary.get("TotalSalesItems") if "TotalSalesItems" in dictionary.keys() else APIHelper.SKIP
        total_transactions = dictionary.get("TotalTransactions") if "TotalTransactions" in dictionary.keys() else APIHelper.SKIP
        vrn = dictionary.get("VRN") if "VRN" in dictionary.keys() else APIHelper.SKIP
        week = dictionary.get("Week") if "Week" in dictionary.keys() else APIHelper.SKIP
        year = dictionary.get("Year") if "Year" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(account_id,
                   account_number,
                   account_short_name,
                   card_id,
                   currency_code,
                   currency_symbol,
                   day,
                   driver_name,
                   month,
                   pan,
                   payer_id,
                   payer_number,
                   payer_short_name,
                   total_amount,
                   total_quantity,
                   total_sales_items,
                   total_transactions,
                   vrn,
                   week,
                   year)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!r}, '
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!r}, '
                f'account_short_name={(self.account_short_name if hasattr(self, "account_short_name") else None)!r}, '
                f'card_id={(self.card_id if hasattr(self, "card_id") else None)!r}, '
                f'currency_code={(self.currency_code if hasattr(self, "currency_code") else None)!r}, '
                f'currency_symbol={(self.currency_symbol if hasattr(self, "currency_symbol") else None)!r}, '
                f'day={(self.day if hasattr(self, "day") else None)!r}, '
                f'driver_name={(self.driver_name if hasattr(self, "driver_name") else None)!r}, '
                f'month={(self.month if hasattr(self, "month") else None)!r}, '
                f'pan={(self.pan if hasattr(self, "pan") else None)!r}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!r}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!r}, '
                f'payer_short_name={(self.payer_short_name if hasattr(self, "payer_short_name") else None)!r}, '
                f'total_amount={(self.total_amount if hasattr(self, "total_amount") else None)!r}, '
                f'total_quantity={(self.total_quantity if hasattr(self, "total_quantity") else None)!r}, '
                f'total_sales_items={(self.total_sales_items if hasattr(self, "total_sales_items") else None)!r}, '
                f'total_transactions={(self.total_transactions if hasattr(self, "total_transactions") else None)!r}, '
                f'vrn={(self.vrn if hasattr(self, "vrn") else None)!r}, '
                f'week={(self.week if hasattr(self, "week") else None)!r}, '
                f'year={(self.year if hasattr(self, "year") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!s}, '
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!s}, '
                f'account_short_name={(self.account_short_name if hasattr(self, "account_short_name") else None)!s}, '
                f'card_id={(self.card_id if hasattr(self, "card_id") else None)!s}, '
                f'currency_code={(self.currency_code if hasattr(self, "currency_code") else None)!s}, '
                f'currency_symbol={(self.currency_symbol if hasattr(self, "currency_symbol") else None)!s}, '
                f'day={(self.day if hasattr(self, "day") else None)!s}, '
                f'driver_name={(self.driver_name if hasattr(self, "driver_name") else None)!s}, '
                f'month={(self.month if hasattr(self, "month") else None)!s}, '
                f'pan={(self.pan if hasattr(self, "pan") else None)!s}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!s}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!s}, '
                f'payer_short_name={(self.payer_short_name if hasattr(self, "payer_short_name") else None)!s}, '
                f'total_amount={(self.total_amount if hasattr(self, "total_amount") else None)!s}, '
                f'total_quantity={(self.total_quantity if hasattr(self, "total_quantity") else None)!s}, '
                f'total_sales_items={(self.total_sales_items if hasattr(self, "total_sales_items") else None)!s}, '
                f'total_transactions={(self.total_transactions if hasattr(self, "total_transactions") else None)!s}, '
                f'vrn={(self.vrn if hasattr(self, "vrn") else None)!s}, '
                f'week={(self.week if hasattr(self, "week") else None)!s}, '
                f'year={(self.year if hasattr(self, "year") else None)!s})')
