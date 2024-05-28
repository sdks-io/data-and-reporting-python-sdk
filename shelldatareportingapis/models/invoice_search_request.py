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

    TODO: type model description here.

    Attributes:
        filters (InvoiceSearchRequestFilters): TODO: type description here.
        page_size (int): TODO: type description here.
        page (int): TODO: type description here.
        sort_by (List[int]): Sort option –  1. InvoiceDate ASC  2. InvoiceDate
            DESC  3. NetAmountCustomerCurrency ASC  4.
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

        if dictionary is None:
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
