# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper


class FeesFeeRuleTiers(object):

    """Implementation of the 'FeesFeeRuleTiers' model.

    Attributes:
        tier_min (int): The model property of type int.
        tier_max (int): The model property of type int.
        date_effective (str): The model property of type str.
        date_terminated (str): The model property of type str.
        tier_value (float): The model property of type float.
        fee_rule_basis_id (int): The model property of type int.
        fee_rule_basis_description (str): The model property of type str.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tier_min": 'TierMin',
        "tier_max": 'TierMax',
        "date_effective": 'DateEffective',
        "date_terminated": 'DateTerminated',
        "tier_value": 'TierValue',
        "fee_rule_basis_id": 'FeeRuleBasisID',
        "fee_rule_basis_description": 'FeeRuleBasisDescription'
    }

    _optionals = [
        'tier_min',
        'tier_max',
        'date_effective',
        'date_terminated',
        'tier_value',
        'fee_rule_basis_id',
        'fee_rule_basis_description',
    ]

    _nullables = [
        'tier_min',
        'tier_max',
        'date_effective',
        'date_terminated',
        'tier_value',
        'fee_rule_basis_id',
        'fee_rule_basis_description',
    ]

    def __init__(self,
                 tier_min=APIHelper.SKIP,
                 tier_max=APIHelper.SKIP,
                 date_effective=APIHelper.SKIP,
                 date_terminated=APIHelper.SKIP,
                 tier_value=APIHelper.SKIP,
                 fee_rule_basis_id=APIHelper.SKIP,
                 fee_rule_basis_description=APIHelper.SKIP):
        """Constructor for the FeesFeeRuleTiers class"""

        # Initialize members of the class
        if tier_min is not APIHelper.SKIP:
            self.tier_min = tier_min 
        if tier_max is not APIHelper.SKIP:
            self.tier_max = tier_max 
        if date_effective is not APIHelper.SKIP:
            self.date_effective = date_effective 
        if date_terminated is not APIHelper.SKIP:
            self.date_terminated = date_terminated 
        if tier_value is not APIHelper.SKIP:
            self.tier_value = tier_value 
        if fee_rule_basis_id is not APIHelper.SKIP:
            self.fee_rule_basis_id = fee_rule_basis_id 
        if fee_rule_basis_description is not APIHelper.SKIP:
            self.fee_rule_basis_description = fee_rule_basis_description 

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
        tier_min = dictionary.get("TierMin") if "TierMin" in dictionary.keys() else APIHelper.SKIP
        tier_max = dictionary.get("TierMax") if "TierMax" in dictionary.keys() else APIHelper.SKIP
        date_effective = dictionary.get("DateEffective") if "DateEffective" in dictionary.keys() else APIHelper.SKIP
        date_terminated = dictionary.get("DateTerminated") if "DateTerminated" in dictionary.keys() else APIHelper.SKIP
        tier_value = dictionary.get("TierValue") if "TierValue" in dictionary.keys() else APIHelper.SKIP
        fee_rule_basis_id = dictionary.get("FeeRuleBasisID") if "FeeRuleBasisID" in dictionary.keys() else APIHelper.SKIP
        fee_rule_basis_description = dictionary.get("FeeRuleBasisDescription") if "FeeRuleBasisDescription" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(tier_min,
                   tier_max,
                   date_effective,
                   date_terminated,
                   tier_value,
                   fee_rule_basis_id,
                   fee_rule_basis_description)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'tier_min={(self.tier_min if hasattr(self, "tier_min") else None)!r}, '
                f'tier_max={(self.tier_max if hasattr(self, "tier_max") else None)!r}, '
                f'date_effective={(self.date_effective if hasattr(self, "date_effective") else None)!r}, '
                f'date_terminated={(self.date_terminated if hasattr(self, "date_terminated") else None)!r}, '
                f'tier_value={(self.tier_value if hasattr(self, "tier_value") else None)!r}, '
                f'fee_rule_basis_id={(self.fee_rule_basis_id if hasattr(self, "fee_rule_basis_id") else None)!r}, '
                f'fee_rule_basis_description={(self.fee_rule_basis_description if hasattr(self, "fee_rule_basis_description") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'tier_min={(self.tier_min if hasattr(self, "tier_min") else None)!s}, '
                f'tier_max={(self.tier_max if hasattr(self, "tier_max") else None)!s}, '
                f'date_effective={(self.date_effective if hasattr(self, "date_effective") else None)!s}, '
                f'date_terminated={(self.date_terminated if hasattr(self, "date_terminated") else None)!s}, '
                f'tier_value={(self.tier_value if hasattr(self, "tier_value") else None)!s}, '
                f'fee_rule_basis_id={(self.fee_rule_basis_id if hasattr(self, "fee_rule_basis_id") else None)!s}, '
                f'fee_rule_basis_description={(self.fee_rule_basis_description if hasattr(self, "fee_rule_basis_description") else None)!s})')
