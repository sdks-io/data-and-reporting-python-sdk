# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper
from shelldatareportingapis.models.card_type_response_customer_card_types_items import CardTypeResponseCustomerCardTypesItems
from shelldatareportingapis.models.card_type_response_error import CardTypeResponseError


class CardTypeResponse(object):

    """Implementation of the 'CardTypeResponse' model.

    Attributes:
        customer_card_types (List[CardTypeResponseCustomerCardTypesItems]):
            The model property of type
            List[CardTypeResponseCustomerCardTypesItems].
        error (CardTypeResponseError): The model property of type
            CardTypeResponseError.
        request_id (str): API Request Id

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "customer_card_types": 'CustomerCardTypes',
        "error": 'Error',
        "request_id": 'RequestId'
    }

    _optionals = [
        'customer_card_types',
        'error',
        'request_id',
    ]

    def __init__(self,
                 customer_card_types=APIHelper.SKIP,
                 error=APIHelper.SKIP,
                 request_id=APIHelper.SKIP):
        """Constructor for the CardTypeResponse class"""

        # Initialize members of the class
        if customer_card_types is not APIHelper.SKIP:
            self.customer_card_types = customer_card_types 
        if error is not APIHelper.SKIP:
            self.error = error 
        if request_id is not APIHelper.SKIP:
            self.request_id = request_id 

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
        customer_card_types = None
        if dictionary.get('CustomerCardTypes') is not None:
            customer_card_types = [CardTypeResponseCustomerCardTypesItems.from_dictionary(x) for x in dictionary.get('CustomerCardTypes')]
        else:
            customer_card_types = APIHelper.SKIP
        error = CardTypeResponseError.from_dictionary(dictionary.get('Error')) if 'Error' in dictionary.keys() else APIHelper.SKIP
        request_id = dictionary.get("RequestId") if dictionary.get("RequestId") else APIHelper.SKIP
        # Return an object of this model
        return cls(customer_card_types,
                   error,
                   request_id)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'customer_card_types={(self.customer_card_types if hasattr(self, "customer_card_types") else None)!r}, '
                f'error={(self.error if hasattr(self, "error") else None)!r}, '
                f'request_id={(self.request_id if hasattr(self, "request_id") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'customer_card_types={(self.customer_card_types if hasattr(self, "customer_card_types") else None)!s}, '
                f'error={(self.error if hasattr(self, "error") else None)!s}, '
                f'request_id={(self.request_id if hasattr(self, "request_id") else None)!s})')
