# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper


class EIDAccess(object):

    """Implementation of the 'EIDAccess' model.

    TODO: type model description here.

    Attributes:
        col_co_id (str): Collecting company id.
        col_co_code (int): Collecting company Code
        account_group_id (str): Identifier for the EID account group
            configured for the user.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "col_co_id": 'ColCoId',
        "col_co_code": 'ColCoCode',
        "account_group_id": 'AccountGroupId'
    }

    _optionals = [
        'col_co_id',
        'col_co_code',
        'account_group_id',
    ]

    _nullables = [
        'col_co_id',
        'col_co_code',
        'account_group_id',
    ]

    def __init__(self,
                 col_co_id=APIHelper.SKIP,
                 col_co_code=APIHelper.SKIP,
                 account_group_id=APIHelper.SKIP):
        """Constructor for the EIDAccess class"""

        # Initialize members of the class
        if col_co_id is not APIHelper.SKIP:
            self.col_co_id = col_co_id 
        if col_co_code is not APIHelper.SKIP:
            self.col_co_code = col_co_code 
        if account_group_id is not APIHelper.SKIP:
            self.account_group_id = account_group_id 

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
        col_co_id = dictionary.get("ColCoId") if "ColCoId" in dictionary.keys() else APIHelper.SKIP
        col_co_code = dictionary.get("ColCoCode") if "ColCoCode" in dictionary.keys() else APIHelper.SKIP
        account_group_id = dictionary.get("AccountGroupId") if "AccountGroupId" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(col_co_id,
                   col_co_code,
                   account_group_id)
