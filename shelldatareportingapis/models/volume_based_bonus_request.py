# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper


class VolumeBasedBonusRequest(object):

    """Implementation of the 'VolumeBasedBonusRequest' model.

    Attributes:
        col_co_id (int): Collecting Company Id of the selected payer.  
            Optional if ColCoCode is passed else Mandatory.  Example:  1 for
            Philippines  5 for UK
        col_co_code (int): Collecting Company Code of the selected payer.  
            Mandatory for serviced OUs such as Romania, Latvia, Lithuania,
            Estonia, Ukraine etc. It is optional for other countries if
            ColCoID is provided.  Example:  86 for Philippines  5 for UK
        payer_id (int): Payer Id of the selected payer. Optional if
            PayerNumber is passed else Mandatory
        payer_number (str): Payer Number of the selected payer. Optional if
            PayerId is passed else Mandatory
        include_history (bool): The API will return the details of the
            previously calculated/paid bonus and fuel consumption (Volume) in
            the response when this flag is ‘True’.
        include_current_period_volume (bool): The API will return the details
            of the monthly breakup of current period fuel consumption (Volume)
            in the response when this flag is ‘True’.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "col_co_id": 'ColCoId',
        "col_co_code": 'ColCoCode',
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber',
        "include_history": 'IncludeHistory',
        "include_current_period_volume": 'IncludeCurrentPeriodVolume'
    }

    _optionals = [
        'col_co_id',
        'col_co_code',
        'payer_id',
        'payer_number',
        'include_history',
        'include_current_period_volume',
    ]

    def __init__(self,
                 col_co_id=APIHelper.SKIP,
                 col_co_code=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 include_history=APIHelper.SKIP,
                 include_current_period_volume=APIHelper.SKIP):
        """Constructor for the VolumeBasedBonusRequest class"""

        # Initialize members of the class
        if col_co_id is not APIHelper.SKIP:
            self.col_co_id = col_co_id 
        if col_co_code is not APIHelper.SKIP:
            self.col_co_code = col_co_code 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 
        if include_history is not APIHelper.SKIP:
            self.include_history = include_history 
        if include_current_period_volume is not APIHelper.SKIP:
            self.include_current_period_volume = include_current_period_volume 

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
        col_co_id = dictionary.get("ColCoId") if dictionary.get("ColCoId") else APIHelper.SKIP
        col_co_code = dictionary.get("ColCoCode") if dictionary.get("ColCoCode") else APIHelper.SKIP
        payer_id = dictionary.get("PayerId") if dictionary.get("PayerId") else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if dictionary.get("PayerNumber") else APIHelper.SKIP
        include_history = dictionary.get("IncludeHistory") if "IncludeHistory" in dictionary.keys() else APIHelper.SKIP
        include_current_period_volume = dictionary.get("IncludeCurrentPeriodVolume") if "IncludeCurrentPeriodVolume" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(col_co_id,
                   col_co_code,
                   payer_id,
                   payer_number,
                   include_history,
                   include_current_period_volume)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_id={(self.col_co_id if hasattr(self, "col_co_id") else None)!r}, '
                f'col_co_code={(self.col_co_code if hasattr(self, "col_co_code") else None)!r}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!r}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!r}, '
                f'include_history={(self.include_history if hasattr(self, "include_history") else None)!r}, '
                f'include_current_period_volume={(self.include_current_period_volume if hasattr(self, "include_current_period_volume") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_id={(self.col_co_id if hasattr(self, "col_co_id") else None)!s}, '
                f'col_co_code={(self.col_co_code if hasattr(self, "col_co_code") else None)!s}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!s}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!s}, '
                f'include_history={(self.include_history if hasattr(self, "include_history") else None)!s}, '
                f'include_current_period_volume={(self.include_current_period_volume if hasattr(self, "include_current_period_volume") else None)!s})')
