# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper


class FeeRuleTier(object):

    """Implementation of the 'FeeRuleTier' model.

    TODO: type model description here.

    Attributes:
        tier_minimum (int): Minimum consumption configured in the tier.
        value (float): Bonus value for the tier.
        tier_maximum (int): Maximum consumption configured in the tier.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tier_minimum": 'TierMinimum',
        "value": 'Value',
        "tier_maximum": 'TierMaximum'
    }

    _optionals = [
        'tier_minimum',
        'value',
        'tier_maximum',
    ]

    _nullables = [
        'tier_minimum',
        'value',
        'tier_maximum',
    ]

    def __init__(self,
                 tier_minimum=APIHelper.SKIP,
                 value=APIHelper.SKIP,
                 tier_maximum=APIHelper.SKIP):
        """Constructor for the FeeRuleTier class"""

        # Initialize members of the class
        if tier_minimum is not APIHelper.SKIP:
            self.tier_minimum = tier_minimum 
        if value is not APIHelper.SKIP:
            self.value = value 
        if tier_maximum is not APIHelper.SKIP:
            self.tier_maximum = tier_maximum 

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
        tier_minimum = dictionary.get("TierMinimum") if "TierMinimum" in dictionary.keys() else APIHelper.SKIP
        value = dictionary.get("Value") if "Value" in dictionary.keys() else APIHelper.SKIP
        tier_maximum = dictionary.get("TierMaximum") if "TierMaximum" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(tier_minimum,
                   value,
                   tier_maximum)
