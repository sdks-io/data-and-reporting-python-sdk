# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper
from shelldatareportingapis.models.recent_transactions import RecentTransactions


class RecentTransactionsResponse(object):

    """Implementation of the 'RecentTransactionsResponse' model.

    Attributes:
        request_id (str): RequestID is unique identifier value that is
            attached to requests and messages that allow reference to a
            particular transaction or event chain.
        status (str): status of the API call
        page (int): CurrentPage
        row_count (int): RowCount
        total_pages (int): TotalPages
        data (List[RecentTransactions]): API Response

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request_id": 'RequestId',
        "status": 'Status',
        "page": 'Page',
        "row_count": 'RowCount',
        "total_pages": 'TotalPages',
        "data": 'Data'
    }

    _optionals = [
        'request_id',
        'status',
        'page',
        'row_count',
        'total_pages',
        'data',
    ]

    def __init__(self,
                 request_id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 page=APIHelper.SKIP,
                 row_count=APIHelper.SKIP,
                 total_pages=APIHelper.SKIP,
                 data=APIHelper.SKIP):
        """Constructor for the RecentTransactionsResponse class"""

        # Initialize members of the class
        if request_id is not APIHelper.SKIP:
            self.request_id = request_id 
        if status is not APIHelper.SKIP:
            self.status = status 
        if page is not APIHelper.SKIP:
            self.page = page 
        if row_count is not APIHelper.SKIP:
            self.row_count = row_count 
        if total_pages is not APIHelper.SKIP:
            self.total_pages = total_pages 
        if data is not APIHelper.SKIP:
            self.data = data 

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
        request_id = dictionary.get("RequestId") if dictionary.get("RequestId") else APIHelper.SKIP
        status = dictionary.get("Status") if dictionary.get("Status") else APIHelper.SKIP
        page = dictionary.get("Page") if dictionary.get("Page") else APIHelper.SKIP
        row_count = dictionary.get("RowCount") if dictionary.get("RowCount") else APIHelper.SKIP
        total_pages = dictionary.get("TotalPages") if dictionary.get("TotalPages") else APIHelper.SKIP
        data = None
        if dictionary.get('Data') is not None:
            data = [RecentTransactions.from_dictionary(x) for x in dictionary.get('Data')]
        else:
            data = APIHelper.SKIP
        # Return an object of this model
        return cls(request_id,
                   status,
                   page,
                   row_count,
                   total_pages,
                   data)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'request_id={(self.request_id if hasattr(self, "request_id") else None)!r}, '
                f'status={(self.status if hasattr(self, "status") else None)!r}, '
                f'page={(self.page if hasattr(self, "page") else None)!r}, '
                f'row_count={(self.row_count if hasattr(self, "row_count") else None)!r}, '
                f'total_pages={(self.total_pages if hasattr(self, "total_pages") else None)!r}, '
                f'data={(self.data if hasattr(self, "data") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'request_id={(self.request_id if hasattr(self, "request_id") else None)!s}, '
                f'status={(self.status if hasattr(self, "status") else None)!s}, '
                f'page={(self.page if hasattr(self, "page") else None)!s}, '
                f'row_count={(self.row_count if hasattr(self, "row_count") else None)!s}, '
                f'total_pages={(self.total_pages if hasattr(self, "total_pages") else None)!s}, '
                f'data={(self.data if hasattr(self, "data") else None)!s})')
