# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.models.recent_transaction_req import RecentTransactionReq


class RecentTransactionRequest(object):

    """Implementation of the 'RecentTransactionRequest' model.

    Attributes:
        page_size (int): Specify the number of records to returned; Max 1000
        page (int): Specify the page of results to be returned.
        filters (RecentTransactionReq): The model property of type
            RecentTransactionReq.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "page_size": 'PageSize',
        "page": 'Page',
        "filters": 'Filters'
    }

    def __init__(self,
                 page_size=None,
                 page=None,
                 filters=None):
        """Constructor for the RecentTransactionRequest class"""

        # Initialize members of the class
        self.page_size = page_size 
        self.page = page 
        self.filters = filters 

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
        page_size = dictionary.get("PageSize") if dictionary.get("PageSize") else None
        page = dictionary.get("Page") if dictionary.get("Page") else None
        filters = RecentTransactionReq.from_dictionary(dictionary.get('Filters')) if dictionary.get('Filters') else None
        # Return an object of this model
        return cls(page_size,
                   page,
                   filters)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'page_size={self.page_size!r}, '
                f'page={self.page!r}, '
                f'filters={self.filters!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'page_size={self.page_size!s}, '
                f'page={self.page!s}, '
                f'filters={self.filters!s})')
