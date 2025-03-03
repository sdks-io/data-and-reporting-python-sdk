# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class EIDDownloadReq(object):

    """Implementation of the 'EIDDownloadReq' model.

    Attributes:
        col_co_code (int): Collecting Company Code of the selected payer.  
            Mandatory
        eid_list (List[str]): The model property of type List[str].
        account_group_country (int): ColCo code associated with the Account
            Group IDs of the given EID/EDI files. Mandatory
        account_group_id_list (List[str]): The model property of type
            List[str].

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "col_co_code": 'ColCoCode',
        "eid_list": 'EIDList',
        "account_group_country": 'AccountGroupCountry',
        "account_group_id_list": 'AccountGroupIdList'
    }

    _nullables = [
        'col_co_code',
        'account_group_country',
    ]

    def __init__(self,
                 col_co_code=None,
                 eid_list=None,
                 account_group_country=None,
                 account_group_id_list=None):
        """Constructor for the EIDDownloadReq class"""

        # Initialize members of the class
        self.col_co_code = col_co_code 
        self.eid_list = eid_list 
        self.account_group_country = account_group_country 
        self.account_group_id_list = account_group_id_list 

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
        eid_list = dictionary.get("EIDList") if dictionary.get("EIDList") else None
        account_group_country = dictionary.get("AccountGroupCountry") if dictionary.get("AccountGroupCountry") else None
        account_group_id_list = dictionary.get("AccountGroupIdList") if dictionary.get("AccountGroupIdList") else None
        # Return an object of this model
        return cls(col_co_code,
                   eid_list,
                   account_group_country,
                   account_group_id_list)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_code={self.col_co_code!r}, '
                f'eid_list={self.eid_list!r}, '
                f'account_group_country={self.account_group_country!r}, '
                f'account_group_id_list={self.account_group_id_list!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_code={self.col_co_code!s}, '
                f'eid_list={self.eid_list!s}, '
                f'account_group_country={self.account_group_country!s}, '
                f'account_group_id_list={self.account_group_id_list!s})')
