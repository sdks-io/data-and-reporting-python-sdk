# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper


class ColCoAccess(object):

    """Implementation of the 'ColCoAccess' model.

    Attributes:
        col_co_id (str): Collecting company ID.
        col_co_code (str): Collecting company code.
        col_co_country_name (str): Collecting company’s Country name. ex:
            United Kingdom
        issuing_country_number (str): Issuing Country Number.   ex: 032 -
            Czech Republic

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "col_co_id": 'ColCoId',
        "col_co_code": 'ColCoCode',
        "col_co_country_name": 'ColCoCountryName',
        "issuing_country_number": 'IssuingCountryNumber'
    }

    _optionals = [
        'col_co_id',
        'col_co_code',
        'col_co_country_name',
        'issuing_country_number',
    ]

    _nullables = [
        'col_co_id',
        'col_co_code',
        'col_co_country_name',
        'issuing_country_number',
    ]

    def __init__(self,
                 col_co_id=APIHelper.SKIP,
                 col_co_code=APIHelper.SKIP,
                 col_co_country_name=APIHelper.SKIP,
                 issuing_country_number=APIHelper.SKIP):
        """Constructor for the ColCoAccess class"""

        # Initialize members of the class
        if col_co_id is not APIHelper.SKIP:
            self.col_co_id = col_co_id 
        if col_co_code is not APIHelper.SKIP:
            self.col_co_code = col_co_code 
        if col_co_country_name is not APIHelper.SKIP:
            self.col_co_country_name = col_co_country_name 
        if issuing_country_number is not APIHelper.SKIP:
            self.issuing_country_number = issuing_country_number 

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
        col_co_id = dictionary.get("ColCoId") if "ColCoId" in dictionary.keys() else APIHelper.SKIP
        col_co_code = dictionary.get("ColCoCode") if "ColCoCode" in dictionary.keys() else APIHelper.SKIP
        col_co_country_name = dictionary.get("ColCoCountryName") if "ColCoCountryName" in dictionary.keys() else APIHelper.SKIP
        issuing_country_number = dictionary.get("IssuingCountryNumber") if "IssuingCountryNumber" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(col_co_id,
                   col_co_code,
                   col_co_country_name,
                   issuing_country_number)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_id={(self.col_co_id if hasattr(self, "col_co_id") else None)!r}, '
                f'col_co_code={(self.col_co_code if hasattr(self, "col_co_code") else None)!r}, '
                f'col_co_country_name={(self.col_co_country_name if hasattr(self, "col_co_country_name") else None)!r}, '
                f'issuing_country_number={(self.issuing_country_number if hasattr(self, "issuing_country_number") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_id={(self.col_co_id if hasattr(self, "col_co_id") else None)!s}, '
                f'col_co_code={(self.col_co_code if hasattr(self, "col_co_code") else None)!s}, '
                f'col_co_country_name={(self.col_co_country_name if hasattr(self, "col_co_country_name") else None)!s}, '
                f'issuing_country_number={(self.issuing_country_number if hasattr(self, "issuing_country_number") else None)!s})')
