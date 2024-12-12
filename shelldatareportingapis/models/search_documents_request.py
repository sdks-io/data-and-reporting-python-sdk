# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper
from shelldatareportingapis.models.search_doc_req import SearchDocReq


class SearchDocumentsRequest(object):

    """Implementation of the 'SearchDocumentsRequest' model.

    TODO: type model description here.

    Attributes:
        filters (SearchDocReq): TODO: type description here.
        page (str): Specify the page of results to be returned.
        page_size (str): Specify the number of records to returned; Max 1000

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "filters": 'Filters',
        "page": 'Page',
        "page_size": 'PageSize'
    }

    _optionals = [
        'filters',
        'page',
        'page_size',
    ]

    def __init__(self,
                 filters=APIHelper.SKIP,
                 page=APIHelper.SKIP,
                 page_size=APIHelper.SKIP):
        """Constructor for the SearchDocumentsRequest class"""

        # Initialize members of the class
        if filters is not APIHelper.SKIP:
            self.filters = filters 
        if page is not APIHelper.SKIP:
            self.page = page 
        if page_size is not APIHelper.SKIP:
            self.page_size = page_size 

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
        filters = SearchDocReq.from_dictionary(dictionary.get('Filters')) if 'Filters' in dictionary.keys() else APIHelper.SKIP
        page = dictionary.get("Page") if dictionary.get("Page") else APIHelper.SKIP
        page_size = dictionary.get("PageSize") if dictionary.get("PageSize") else APIHelper.SKIP
        # Return an object of this model
        return cls(filters,
                   page,
                   page_size)
