# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper


class FuelConsumptionCard(object):

    """Implementation of the 'FuelConsumptionCard' model.

    Attributes:
        card_id (int): Card Id   Optional, when PAN is provided else mandatory.
        pan (str): Full Card PAN Optional, when CardId is provided else
            mandatory.
        expiry_date (str): Card Expiry Date Format: yyyyMMdd

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "card_id": 'CardId',
        "pan": 'PAN',
        "expiry_date": 'ExpiryDate'
    }

    _optionals = [
        'card_id',
        'pan',
        'expiry_date',
    ]

    def __init__(self,
                 card_id=APIHelper.SKIP,
                 pan=APIHelper.SKIP,
                 expiry_date=APIHelper.SKIP):
        """Constructor for the FuelConsumptionCard class"""

        # Initialize members of the class
        if card_id is not APIHelper.SKIP:
            self.card_id = card_id 
        if pan is not APIHelper.SKIP:
            self.pan = pan 
        if expiry_date is not APIHelper.SKIP:
            self.expiry_date = expiry_date 

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
        card_id = dictionary.get("CardId") if dictionary.get("CardId") else APIHelper.SKIP
        pan = dictionary.get("PAN") if dictionary.get("PAN") else APIHelper.SKIP
        expiry_date = dictionary.get("ExpiryDate") if dictionary.get("ExpiryDate") else APIHelper.SKIP
        # Return an object of this model
        return cls(card_id,
                   pan,
                   expiry_date)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'card_id={(self.card_id if hasattr(self, "card_id") else None)!r}, '
                f'pan={(self.pan if hasattr(self, "pan") else None)!r}, '
                f'expiry_date={(self.expiry_date if hasattr(self, "expiry_date") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'card_id={(self.card_id if hasattr(self, "card_id") else None)!s}, '
                f'pan={(self.pan if hasattr(self, "pan") else None)!s}, '
                f'expiry_date={(self.expiry_date if hasattr(self, "expiry_date") else None)!s})')
