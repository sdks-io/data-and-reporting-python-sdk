# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper


class AccountAccess(object):

    """Implementation of the 'AccountAccess' model.

    Attributes:
        colco_id (int): Collecting company id.
        colco_code (int): Collecting company code.
        payer_id (int): Payer Id to which the user has access
        payer_number (str): Payer Number to which the user has access
        payer_name (str): Name of the Payer to which the user has access
        account_id (int): Account Id to which the user has access
        account_number (str): Account Number to which the user has access
        account_name (str): Name of the Account to which the user has access

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "colco_id": 'ColcoId',
        "colco_code": 'ColcoCode',
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber',
        "payer_name": 'PayerName',
        "account_id": 'AccountId',
        "account_number": 'AccountNumber',
        "account_name": 'AccountName'
    }

    _optionals = [
        'colco_id',
        'colco_code',
        'payer_id',
        'payer_number',
        'payer_name',
        'account_id',
        'account_number',
        'account_name',
    ]

    _nullables = [
        'colco_id',
        'colco_code',
        'payer_id',
        'payer_number',
        'payer_name',
        'account_id',
        'account_name',
    ]

    def __init__(self,
                 colco_id=APIHelper.SKIP,
                 colco_code=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 payer_name=APIHelper.SKIP,
                 account_id=APIHelper.SKIP,
                 account_number=APIHelper.SKIP,
                 account_name=APIHelper.SKIP):
        """Constructor for the AccountAccess class"""

        # Initialize members of the class
        if colco_id is not APIHelper.SKIP:
            self.colco_id = colco_id 
        if colco_code is not APIHelper.SKIP:
            self.colco_code = colco_code 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 
        if payer_name is not APIHelper.SKIP:
            self.payer_name = payer_name 
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 

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
        colco_id = dictionary.get("ColcoId") if "ColcoId" in dictionary.keys() else APIHelper.SKIP
        colco_code = dictionary.get("ColcoCode") if "ColcoCode" in dictionary.keys() else APIHelper.SKIP
        payer_id = dictionary.get("PayerId") if "PayerId" in dictionary.keys() else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if "PayerNumber" in dictionary.keys() else APIHelper.SKIP
        payer_name = dictionary.get("PayerName") if "PayerName" in dictionary.keys() else APIHelper.SKIP
        account_id = dictionary.get("AccountId") if "AccountId" in dictionary.keys() else APIHelper.SKIP
        account_number = dictionary.get("AccountNumber") if dictionary.get("AccountNumber") else APIHelper.SKIP
        account_name = dictionary.get("AccountName") if "AccountName" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(colco_id,
                   colco_code,
                   payer_id,
                   payer_number,
                   payer_name,
                   account_id,
                   account_number,
                   account_name)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'colco_id={(self.colco_id if hasattr(self, "colco_id") else None)!r}, '
                f'colco_code={(self.colco_code if hasattr(self, "colco_code") else None)!r}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!r}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!r}, '
                f'payer_name={(self.payer_name if hasattr(self, "payer_name") else None)!r}, '
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!r}, '
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!r}, '
                f'account_name={(self.account_name if hasattr(self, "account_name") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'colco_id={(self.colco_id if hasattr(self, "colco_id") else None)!s}, '
                f'colco_code={(self.colco_code if hasattr(self, "colco_code") else None)!s}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!s}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!s}, '
                f'payer_name={(self.payer_name if hasattr(self, "payer_name") else None)!s}, '
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!s}, '
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!s}, '
                f'account_name={(self.account_name if hasattr(self, "account_name") else None)!s})')
