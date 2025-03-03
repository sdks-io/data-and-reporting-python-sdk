# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper


class RecentTransactionReq(object):

    """Implementation of the 'RecentTransactionReq' model.

    Attributes:
        col_co_code (int): Three character Collecting Company Code (Shell
            Code) of the selected payer
        payer_number (str): Unique Identifier for the customer at payment
            point.
        account_number (str): Customer account number.
        product_code (str): Global product code
        purchased_in_country (str): Delco country
        card_pan (str): Card identifier number masked
        from_date_time (str): Start date and time of transactions
        to_date_time (str): End date and time of transactions. Mandatory if
            FromDateTime is provided.
        transaction_status (str): Status of transaction. DO NOT pass the value
            if includeDeclines is passed
        fuel_only (str): When passed as ‘true’ Only returned records with Fuel
            transactions.(All Fuels).When passed as ‘false’ the above
            condition will not be checked. (Both All Fuels and Non-Fuel)
        product_group_name (str): Product group name
        vehicle_registration_number (str): Vehicle registration number
            embossed on the card
        include_declines (bool): Flag to enable to get declined records
        card_issuer_name (str): Card issuer name
        column_list (str): Column list to be part of response, it can be 'All'
            to return all possible column. E.g. 'All'  To get specific columns
            pass multiple columns name separated by comma along with
            'PayerNumber'. E.g. "PayerNumber,ProductCode"

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "col_co_code": 'ColCoCode',
        "payer_number": 'PayerNumber',
        "account_number": 'AccountNumber',
        "product_code": 'ProductCode',
        "purchased_in_country": 'PurchasedInCountry',
        "card_pan": 'CardPAN',
        "from_date_time": 'FromDateTime',
        "to_date_time": 'ToDateTime',
        "transaction_status": 'TransactionStatus',
        "fuel_only": 'FuelOnly',
        "product_group_name": 'ProductGroupName',
        "vehicle_registration_number": 'VehicleRegistrationNumber',
        "include_declines": 'IncludeDeclines',
        "card_issuer_name": 'CardIssuerName',
        "column_list": 'ColumnList'
    }

    _optionals = [
        'account_number',
        'product_code',
        'purchased_in_country',
        'card_pan',
        'from_date_time',
        'to_date_time',
        'transaction_status',
        'fuel_only',
        'product_group_name',
        'vehicle_registration_number',
        'include_declines',
        'card_issuer_name',
        'column_list',
    ]

    _nullables = [
        'col_co_code',
        'payer_number',
        'account_number',
        'product_code',
        'purchased_in_country',
        'card_pan',
        'from_date_time',
        'to_date_time',
        'transaction_status',
        'fuel_only',
        'product_group_name',
        'vehicle_registration_number',
        'include_declines',
        'card_issuer_name',
    ]

    def __init__(self,
                 col_co_code=None,
                 payer_number=None,
                 account_number=APIHelper.SKIP,
                 product_code=APIHelper.SKIP,
                 purchased_in_country=APIHelper.SKIP,
                 card_pan=APIHelper.SKIP,
                 from_date_time=APIHelper.SKIP,
                 to_date_time=APIHelper.SKIP,
                 transaction_status=APIHelper.SKIP,
                 fuel_only=APIHelper.SKIP,
                 product_group_name=APIHelper.SKIP,
                 vehicle_registration_number=APIHelper.SKIP,
                 include_declines=APIHelper.SKIP,
                 card_issuer_name=APIHelper.SKIP,
                 column_list=APIHelper.SKIP):
        """Constructor for the RecentTransactionReq class"""

        # Initialize members of the class
        self.col_co_code = col_co_code 
        self.payer_number = payer_number 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if product_code is not APIHelper.SKIP:
            self.product_code = product_code 
        if purchased_in_country is not APIHelper.SKIP:
            self.purchased_in_country = purchased_in_country 
        if card_pan is not APIHelper.SKIP:
            self.card_pan = card_pan 
        if from_date_time is not APIHelper.SKIP:
            self.from_date_time = from_date_time 
        if to_date_time is not APIHelper.SKIP:
            self.to_date_time = to_date_time 
        if transaction_status is not APIHelper.SKIP:
            self.transaction_status = transaction_status 
        if fuel_only is not APIHelper.SKIP:
            self.fuel_only = fuel_only 
        if product_group_name is not APIHelper.SKIP:
            self.product_group_name = product_group_name 
        if vehicle_registration_number is not APIHelper.SKIP:
            self.vehicle_registration_number = vehicle_registration_number 
        if include_declines is not APIHelper.SKIP:
            self.include_declines = include_declines 
        if card_issuer_name is not APIHelper.SKIP:
            self.card_issuer_name = card_issuer_name 
        if column_list is not APIHelper.SKIP:
            self.column_list = column_list 

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
        col_co_code = dictionary.get("ColCoCode") if dictionary.get("ColCoCode") else None
        payer_number = dictionary.get("PayerNumber") if dictionary.get("PayerNumber") else None
        account_number = dictionary.get("AccountNumber") if "AccountNumber" in dictionary.keys() else APIHelper.SKIP
        product_code = dictionary.get("ProductCode") if "ProductCode" in dictionary.keys() else APIHelper.SKIP
        purchased_in_country = dictionary.get("PurchasedInCountry") if "PurchasedInCountry" in dictionary.keys() else APIHelper.SKIP
        card_pan = dictionary.get("CardPAN") if "CardPAN" in dictionary.keys() else APIHelper.SKIP
        from_date_time = dictionary.get("FromDateTime") if "FromDateTime" in dictionary.keys() else APIHelper.SKIP
        to_date_time = dictionary.get("ToDateTime") if "ToDateTime" in dictionary.keys() else APIHelper.SKIP
        transaction_status = dictionary.get("TransactionStatus") if "TransactionStatus" in dictionary.keys() else APIHelper.SKIP
        fuel_only = dictionary.get("FuelOnly") if "FuelOnly" in dictionary.keys() else APIHelper.SKIP
        product_group_name = dictionary.get("ProductGroupName") if "ProductGroupName" in dictionary.keys() else APIHelper.SKIP
        vehicle_registration_number = dictionary.get("VehicleRegistrationNumber") if "VehicleRegistrationNumber" in dictionary.keys() else APIHelper.SKIP
        include_declines = dictionary.get("IncludeDeclines") if "IncludeDeclines" in dictionary.keys() else APIHelper.SKIP
        card_issuer_name = dictionary.get("CardIssuerName") if "CardIssuerName" in dictionary.keys() else APIHelper.SKIP
        column_list = dictionary.get("ColumnList") if dictionary.get("ColumnList") else APIHelper.SKIP
        # Return an object of this model
        return cls(col_co_code,
                   payer_number,
                   account_number,
                   product_code,
                   purchased_in_country,
                   card_pan,
                   from_date_time,
                   to_date_time,
                   transaction_status,
                   fuel_only,
                   product_group_name,
                   vehicle_registration_number,
                   include_declines,
                   card_issuer_name,
                   column_list)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_code={self.col_co_code!r}, '
                f'payer_number={self.payer_number!r}, '
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!r}, '
                f'product_code={(self.product_code if hasattr(self, "product_code") else None)!r}, '
                f'purchased_in_country={(self.purchased_in_country if hasattr(self, "purchased_in_country") else None)!r}, '
                f'card_pan={(self.card_pan if hasattr(self, "card_pan") else None)!r}, '
                f'from_date_time={(self.from_date_time if hasattr(self, "from_date_time") else None)!r}, '
                f'to_date_time={(self.to_date_time if hasattr(self, "to_date_time") else None)!r}, '
                f'transaction_status={(self.transaction_status if hasattr(self, "transaction_status") else None)!r}, '
                f'fuel_only={(self.fuel_only if hasattr(self, "fuel_only") else None)!r}, '
                f'product_group_name={(self.product_group_name if hasattr(self, "product_group_name") else None)!r}, '
                f'vehicle_registration_number={(self.vehicle_registration_number if hasattr(self, "vehicle_registration_number") else None)!r}, '
                f'include_declines={(self.include_declines if hasattr(self, "include_declines") else None)!r}, '
                f'card_issuer_name={(self.card_issuer_name if hasattr(self, "card_issuer_name") else None)!r}, '
                f'column_list={(self.column_list if hasattr(self, "column_list") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_code={self.col_co_code!s}, '
                f'payer_number={self.payer_number!s}, '
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!s}, '
                f'product_code={(self.product_code if hasattr(self, "product_code") else None)!s}, '
                f'purchased_in_country={(self.purchased_in_country if hasattr(self, "purchased_in_country") else None)!s}, '
                f'card_pan={(self.card_pan if hasattr(self, "card_pan") else None)!s}, '
                f'from_date_time={(self.from_date_time if hasattr(self, "from_date_time") else None)!s}, '
                f'to_date_time={(self.to_date_time if hasattr(self, "to_date_time") else None)!s}, '
                f'transaction_status={(self.transaction_status if hasattr(self, "transaction_status") else None)!s}, '
                f'fuel_only={(self.fuel_only if hasattr(self, "fuel_only") else None)!s}, '
                f'product_group_name={(self.product_group_name if hasattr(self, "product_group_name") else None)!s}, '
                f'vehicle_registration_number={(self.vehicle_registration_number if hasattr(self, "vehicle_registration_number") else None)!s}, '
                f'include_declines={(self.include_declines if hasattr(self, "include_declines") else None)!s}, '
                f'card_issuer_name={(self.card_issuer_name if hasattr(self, "card_issuer_name") else None)!s}, '
                f'column_list={(self.column_list if hasattr(self, "column_list") else None)!s})')
