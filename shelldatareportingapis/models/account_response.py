# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper
from shelldatareportingapis.models.account_response_accounts_items import AccountResponseAccountsItems
from shelldatareportingapis.models.error_status import ErrorStatus


class AccountResponse(object):

    """Implementation of the 'AccountResponse' model.

    Attributes:
        accounts (List[AccountResponseAccountsItems]): The model property of
            type List[AccountResponseAccountsItems].
        current_page (int): current page
        row_count (int): Total row count matched for the given input criteria
        total_pages (int): Calculated page count based on page size from the
            incoming API request and total number of rows matched for the
            given input criteria.
        error (ErrorStatus): The model property of type ErrorStatus.
        request_id (str): API Request ID

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "accounts": 'Accounts',
        "current_page": 'CurrentPage',
        "row_count": 'RowCount',
        "total_pages": 'TotalPages',
        "error": 'Error',
        "request_id": 'RequestId'
    }

    _optionals = [
        'accounts',
        'current_page',
        'row_count',
        'total_pages',
        'error',
        'request_id',
    ]

    def __init__(self,
                 accounts=APIHelper.SKIP,
                 current_page=APIHelper.SKIP,
                 row_count=APIHelper.SKIP,
                 total_pages=APIHelper.SKIP,
                 error=APIHelper.SKIP,
                 request_id=APIHelper.SKIP):
        """Constructor for the AccountResponse class"""

        # Initialize members of the class
        if accounts is not APIHelper.SKIP:
            self.accounts = accounts 
        if current_page is not APIHelper.SKIP:
            self.current_page = current_page 
        if row_count is not APIHelper.SKIP:
            self.row_count = row_count 
        if total_pages is not APIHelper.SKIP:
            self.total_pages = total_pages 
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
        accounts = None
        if dictionary.get('Accounts') is not None:
            accounts = [AccountResponseAccountsItems.from_dictionary(x) for x in dictionary.get('Accounts')]
        else:
            accounts = APIHelper.SKIP
        current_page = dictionary.get("CurrentPage") if dictionary.get("CurrentPage") else APIHelper.SKIP
        row_count = dictionary.get("RowCount") if dictionary.get("RowCount") else APIHelper.SKIP
        total_pages = dictionary.get("TotalPages") if dictionary.get("TotalPages") else APIHelper.SKIP
        error = ErrorStatus.from_dictionary(dictionary.get('Error')) if 'Error' in dictionary.keys() else APIHelper.SKIP
        request_id = dictionary.get("RequestId") if dictionary.get("RequestId") else APIHelper.SKIP
        # Return an object of this model
        return cls(accounts,
                   current_page,
                   row_count,
                   total_pages,
                   error,
                   request_id)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'accounts={(self.accounts if hasattr(self, "accounts") else None)!r}, '
                f'current_page={(self.current_page if hasattr(self, "current_page") else None)!r}, '
                f'row_count={(self.row_count if hasattr(self, "row_count") else None)!r}, '
                f'total_pages={(self.total_pages if hasattr(self, "total_pages") else None)!r}, '
                f'error={(self.error if hasattr(self, "error") else None)!r}, '
                f'request_id={(self.request_id if hasattr(self, "request_id") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'accounts={(self.accounts if hasattr(self, "accounts") else None)!s}, '
                f'current_page={(self.current_page if hasattr(self, "current_page") else None)!s}, '
                f'row_count={(self.row_count if hasattr(self, "row_count") else None)!s}, '
                f'total_pages={(self.total_pages if hasattr(self, "total_pages") else None)!s}, '
                f'error={(self.error if hasattr(self, "error") else None)!s}, '
                f'request_id={(self.request_id if hasattr(self, "request_id") else None)!s})')
