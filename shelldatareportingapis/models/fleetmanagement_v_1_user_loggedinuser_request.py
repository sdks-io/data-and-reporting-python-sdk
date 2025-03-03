# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper


class FleetmanagementV1UserLoggedinuserRequest(object):

    """Implementation of the 'Fleetmanagement V1 User Loggedinuser Request' model.

    Attributes:
        include_payer_group (bool): True/False. The output will include the
            payer group information only when true is passed.
        include_eid_details (bool): True/False. The output will include the
            EID (Electronic Invoice data) information only when true is
            passed..
        requested_api_name (str): Name of the API on which user access needs
            to be validated Optional.
        payer_id (int): Payer id of the customer.</br> Optional.</br> This
            input is a search criterion.</br> Note: If PayerId or PayerNumber
            is provided in the input, the given payer will be available in the
            output if the user has access to the given payer.
        payer_number (str): PayerNumber of the customer.</br> Optional</br>
            This input is a search criterion.</br> Note: If Payerid or
            PayerNumber is provided in the input, the given payer will be
            available in the output if the user has access to the given payer.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "include_payer_group": 'IncludePayerGroup',
        "include_eid_details": 'IncludeEIDDetails',
        "requested_api_name": 'RequestedAPIName',
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber'
    }

    _optionals = [
        'include_payer_group',
        'include_eid_details',
        'requested_api_name',
        'payer_id',
        'payer_number',
    ]

    _nullables = [
        'requested_api_name',
        'payer_id',
        'payer_number',
    ]

    def __init__(self,
                 include_payer_group=False,
                 include_eid_details=False,
                 requested_api_name=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP):
        """Constructor for the FleetmanagementV1UserLoggedinuserRequest class"""

        # Initialize members of the class
        self.include_payer_group = include_payer_group 
        self.include_eid_details = include_eid_details 
        if requested_api_name is not APIHelper.SKIP:
            self.requested_api_name = requested_api_name 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 

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
        include_payer_group = dictionary.get("IncludePayerGroup") if dictionary.get("IncludePayerGroup") else False
        include_eid_details = dictionary.get("IncludeEIDDetails") if dictionary.get("IncludeEIDDetails") else False
        requested_api_name = dictionary.get("RequestedAPIName") if "RequestedAPIName" in dictionary.keys() else APIHelper.SKIP
        payer_id = dictionary.get("PayerId") if "PayerId" in dictionary.keys() else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if "PayerNumber" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(include_payer_group,
                   include_eid_details,
                   requested_api_name,
                   payer_id,
                   payer_number)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'include_payer_group={(self.include_payer_group if hasattr(self, "include_payer_group") else None)!r}, '
                f'include_eid_details={(self.include_eid_details if hasattr(self, "include_eid_details") else None)!r}, '
                f'requested_api_name={(self.requested_api_name if hasattr(self, "requested_api_name") else None)!r}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!r}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'include_payer_group={(self.include_payer_group if hasattr(self, "include_payer_group") else None)!s}, '
                f'include_eid_details={(self.include_eid_details if hasattr(self, "include_eid_details") else None)!s}, '
                f'requested_api_name={(self.requested_api_name if hasattr(self, "requested_api_name") else None)!s}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!s}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!s})')
