# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper
from shelldatareportingapis.models.invoice_search_request_filters import InvoiceSearchRequestFilters


class InvoiceSearchRequest(object):

    """Implementation of the 'InvoiceSearchRequest' model.

    Attributes:
        filters (InvoiceSearchRequestFilters): The model property of type
            InvoiceSearchRequestFilters.
        page_size (int): The model property of type int.
        page (int): The model property of type int.
        sort_by (List[int]): Sort option –  1.    InvoiceDate ASC  2.   
            InvoiceDate DESC  3.    NetAmountCustomerCurrency ASC  4.   
            NetAmountCustomerCurrency DESC  Optional  Note:  This option uses
            a column name with a combination of “ASC or DESC” for sorting.  If
            only the column name is provided, it is sorted by ascending. 
            Example values to be passed:   [“InvoiceDate”,
            “NetAmountCustomerCurrency DESC”]

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "filters": 'Filters',
        "page_size": 'PageSize',
        "page": 'Page',
        "sort_by": 'SortBy'
    }

    _optionals = [
        'filters',
        'page_size',
        'page',
        'sort_by',
    ]

    def __init__(self,
                 filters=APIHelper.SKIP,
                 page_size=APIHelper.SKIP,
                 page=APIHelper.SKIP,
                 sort_by=APIHelper.SKIP):
        """Constructor for the InvoiceSearchRequest class"""

        # Initialize members of the class
        if filters is not APIHelper.SKIP:
            self.filters = filters 
        if page_size is not APIHelper.SKIP:
            self.page_size = page_size 
        if page is not APIHelper.SKIP:
            self.page = page 
        if sort_by is not APIHelper.SKIP:
            self.sort_by = sort_by 

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
        filters = InvoiceSearchRequestFilters.from_dictionary(dictionary.get('Filters')) if 'Filters' in dictionary.keys() else APIHelper.SKIP
        page_size = dictionary.get("PageSize") if dictionary.get("PageSize") else APIHelper.SKIP
        page = dictionary.get("Page") if dictionary.get("Page") else APIHelper.SKIP
        sort_by = dictionary.get("SortBy") if dictionary.get("SortBy") else APIHelper.SKIP
        # Return an object of this model
        return cls(filters,
                   page_size,
                   page,
                   sort_by)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'filters={(self.filters if hasattr(self, "filters") else None)!r}, '
                f'page_size={(self.page_size if hasattr(self, "page_size") else None)!r}, '
                f'page={(self.page if hasattr(self, "page") else None)!r}, '
                f'sort_by={(self.sort_by if hasattr(self, "sort_by") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'filters={(self.filters if hasattr(self, "filters") else None)!s}, '
                f'page_size={(self.page_size if hasattr(self, "page_size") else None)!s}, '
                f'page={(self.page if hasattr(self, "page") else None)!s}, '
                f'sort_by={(self.sort_by if hasattr(self, "sort_by") else None)!s})')
