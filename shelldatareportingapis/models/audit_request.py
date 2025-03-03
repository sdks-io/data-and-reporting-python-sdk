# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper
from shelldatareportingapis.models.accounts import Accounts


class AuditRequest(object):

    """Implementation of the 'AuditRequest' model.

    Attributes:
        status (str): Status of requests to be fetched. •    Success •   
            Failed •    InProgress •    Submitted •    Rejected •   
            PendingApproval •    All •    MailedToCSC Optional If not passed
            “All” will be considered as the default value.
        payer_number (str): Payer Number of the selected payer. Optional if
            PayerId is passed else Mandatory
        payer_id (int): Payer Id  of the selected payer. Optional if
            PayerNumber is passed else Mandatory Example: 123456
        account_number (str): The model property of type str.
        col_co_code (int): Collecting Company Code (Shell Code) of the
            selected payer.   Mandatory for serviced OUs such as Romania,
            Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other
            countries if ColCoID is provided.  Example:  86 for Philippines  5
            for UK
        col_co_id (int): Collecting Company Id  of the selected payer.  
            Optional if ColCoCode is passed else Mandatory.  Example:  1 for
            Philippines  5 for UK
        accounts (Accounts): The model property of type Accounts.
        page_size (int): Page Size – Number of records to show on a page
            Optional Default value 50
        requested_operation (List[str]): To search for requests submitted
            until this date.  Optional   Format: yyyyMMdd   Example: 20200130 
            If ToDate is not provided and FromDate is provided, then ToDate
            will be considered as current date or 30 days from FromDate,
            whichever is earlier. However, when both FromDate and ToDate is
            not provided then last 30 days will be considered for filtering.
        sort_order (str): Allowed Sorting Options:  1.   
            SubmittedDateDescending  2.    SubmittedDateAscending   3.   
            AccountNumberAscending  4.    AccountNumberDescending  Optional:
            Default value is 1  Example value to be passed: 1,3
        search_text (str): Search text used as criteria to filter the
            requests. Optional Minimum length is 4 characters (configurable).
            Else, an error (0007) will be returned. When valid text is
            provided, MS will return all the records that contains the Search
            Text within any of the look up fields
        current_page (int): Page Number (as shown to the users) Optional
            Default value 1
        from_date (str): To search for requests submitted from this date.
            Optional Maximum of X days duration allowed per search. The X
            value is configurable and initially set to 180 days. Format:
            yyyyMMdd Example: 20200101 If FromDate is not provided and ToDate
            is provided, then FromDate will be considered as 30 days less than
            ToDate. However, when both FromDate and ToDate is not provided
            then last 30 days will be considered for filtering.
        to_date (str): To search for requests submitted until this date. 
            Optional   Format: yyyyMMdd   Example: 20200130  If ToDate is not
            provided and FromDate is provided, then ToDate will be considered
            as current date or 30 days from FromDate, whichever is earlier.
            However, when both FromDate and ToDate is not provided then last
            30 days will be considered for filtering.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status": 'Status',
        "payer_number": 'PayerNumber',
        "payer_id": 'PayerId',
        "account_number": 'AccountNumber',
        "col_co_code": 'ColCoCode',
        "col_co_id": 'ColCoId',
        "accounts": 'Accounts',
        "page_size": 'PageSize',
        "requested_operation": 'RequestedOperation',
        "sort_order": 'SortOrder',
        "search_text": 'SearchText',
        "current_page": 'CurrentPage',
        "from_date": 'FromDate',
        "to_date": 'ToDate'
    }

    _optionals = [
        'status',
        'payer_number',
        'payer_id',
        'account_number',
        'col_co_code',
        'col_co_id',
        'accounts',
        'page_size',
        'requested_operation',
        'sort_order',
        'search_text',
        'current_page',
        'from_date',
        'to_date',
    ]

    _nullables = [
        'payer_number',
        'payer_id',
        'account_number',
        'col_co_code',
        'col_co_id',
        'sort_order',
        'search_text',
        'current_page',
        'from_date',
        'to_date',
    ]

    def __init__(self,
                 status=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 account_number=APIHelper.SKIP,
                 col_co_code=APIHelper.SKIP,
                 col_co_id=APIHelper.SKIP,
                 accounts=APIHelper.SKIP,
                 page_size=APIHelper.SKIP,
                 requested_operation=APIHelper.SKIP,
                 sort_order=APIHelper.SKIP,
                 search_text=APIHelper.SKIP,
                 current_page=APIHelper.SKIP,
                 from_date=APIHelper.SKIP,
                 to_date=APIHelper.SKIP):
        """Constructor for the AuditRequest class"""

        # Initialize members of the class
        if status is not APIHelper.SKIP:
            self.status = status 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if col_co_code is not APIHelper.SKIP:
            self.col_co_code = col_co_code 
        if col_co_id is not APIHelper.SKIP:
            self.col_co_id = col_co_id 
        if accounts is not APIHelper.SKIP:
            self.accounts = accounts 
        if page_size is not APIHelper.SKIP:
            self.page_size = page_size 
        if requested_operation is not APIHelper.SKIP:
            self.requested_operation = requested_operation 
        if sort_order is not APIHelper.SKIP:
            self.sort_order = sort_order 
        if search_text is not APIHelper.SKIP:
            self.search_text = search_text 
        if current_page is not APIHelper.SKIP:
            self.current_page = current_page 
        if from_date is not APIHelper.SKIP:
            self.from_date = from_date 
        if to_date is not APIHelper.SKIP:
            self.to_date = to_date 

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
        status = dictionary.get("Status") if dictionary.get("Status") else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if "PayerNumber" in dictionary.keys() else APIHelper.SKIP
        payer_id = dictionary.get("PayerId") if "PayerId" in dictionary.keys() else APIHelper.SKIP
        account_number = dictionary.get("AccountNumber") if "AccountNumber" in dictionary.keys() else APIHelper.SKIP
        col_co_code = dictionary.get("ColCoCode") if "ColCoCode" in dictionary.keys() else APIHelper.SKIP
        col_co_id = dictionary.get("ColCoId") if "ColCoId" in dictionary.keys() else APIHelper.SKIP
        accounts = Accounts.from_dictionary(dictionary.get('Accounts')) if 'Accounts' in dictionary.keys() else APIHelper.SKIP
        page_size = dictionary.get("PageSize") if dictionary.get("PageSize") else APIHelper.SKIP
        requested_operation = dictionary.get("RequestedOperation") if dictionary.get("RequestedOperation") else APIHelper.SKIP
        sort_order = dictionary.get("SortOrder") if "SortOrder" in dictionary.keys() else APIHelper.SKIP
        search_text = dictionary.get("SearchText") if "SearchText" in dictionary.keys() else APIHelper.SKIP
        current_page = dictionary.get("CurrentPage") if "CurrentPage" in dictionary.keys() else APIHelper.SKIP
        from_date = dictionary.get("FromDate") if "FromDate" in dictionary.keys() else APIHelper.SKIP
        to_date = dictionary.get("ToDate") if "ToDate" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(status,
                   payer_number,
                   payer_id,
                   account_number,
                   col_co_code,
                   col_co_id,
                   accounts,
                   page_size,
                   requested_operation,
                   sort_order,
                   search_text,
                   current_page,
                   from_date,
                   to_date)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'status={(self.status if hasattr(self, "status") else None)!r}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!r}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!r}, '
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!r}, '
                f'col_co_code={(self.col_co_code if hasattr(self, "col_co_code") else None)!r}, '
                f'col_co_id={(self.col_co_id if hasattr(self, "col_co_id") else None)!r}, '
                f'accounts={(self.accounts if hasattr(self, "accounts") else None)!r}, '
                f'page_size={(self.page_size if hasattr(self, "page_size") else None)!r}, '
                f'requested_operation={(self.requested_operation if hasattr(self, "requested_operation") else None)!r}, '
                f'sort_order={(self.sort_order if hasattr(self, "sort_order") else None)!r}, '
                f'search_text={(self.search_text if hasattr(self, "search_text") else None)!r}, '
                f'current_page={(self.current_page if hasattr(self, "current_page") else None)!r}, '
                f'from_date={(self.from_date if hasattr(self, "from_date") else None)!r}, '
                f'to_date={(self.to_date if hasattr(self, "to_date") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'status={(self.status if hasattr(self, "status") else None)!s}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!s}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!s}, '
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!s}, '
                f'col_co_code={(self.col_co_code if hasattr(self, "col_co_code") else None)!s}, '
                f'col_co_id={(self.col_co_id if hasattr(self, "col_co_id") else None)!s}, '
                f'accounts={(self.accounts if hasattr(self, "accounts") else None)!s}, '
                f'page_size={(self.page_size if hasattr(self, "page_size") else None)!s}, '
                f'requested_operation={(self.requested_operation if hasattr(self, "requested_operation") else None)!s}, '
                f'sort_order={(self.sort_order if hasattr(self, "sort_order") else None)!s}, '
                f'search_text={(self.search_text if hasattr(self, "search_text") else None)!s}, '
                f'current_page={(self.current_page if hasattr(self, "current_page") else None)!s}, '
                f'from_date={(self.from_date if hasattr(self, "from_date") else None)!s}, '
                f'to_date={(self.to_date if hasattr(self, "to_date") else None)!s})')
