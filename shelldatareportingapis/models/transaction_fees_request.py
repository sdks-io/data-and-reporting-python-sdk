# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper
from shelldatareportingapis.models.accounts import Accounts


class TransactionFeesRequest(object):

    """Implementation of the 'TransactionFeesRequest' model.

    Attributes:
        col_co_id (int): Collecting Company Id  of the selected payer.  
            Optional if ColCoCode is passed else Mandatory.  Example:  1 for
            Philippines  5 for UK
        col_co_code (int): Collecting Company Code (Shell Code) of the
            selected payer.   Mandatory for serviced OUs such as Romania,
            Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other
            countries if ColCoID is provided.  Example:  86 for Philippines  5
            for UK
        payer_id (int): Payer Id of the selected payer. Optional if
            PayerNumber is passed else Mandatory Example: 123456
        payer_number (str): Payer Number (Ex: GB000000123) of the selected
            payer. Optional if PayerId is passed else Mandatory
        accounts (List[Accounts]): The model property of type List[Accounts].
        card_id (int): Card Id   Optional  When both Card Id and Card PAN are
            not present on request, the response will have all the fee items
            under the selected payer or account.  Example: 275549
        card_pan (str): Full Card PAN Optional When both Card Id and Card PAN
            are not present on request, the response will have all the fee
            items under the selected payer or account or card group.
        invoice_status (str): Invoice status of the fee items Mandatory
            Possible options: I - Invoiced U – Un-Invoiced A – All
        fee_type_group (str): Fee type group in under which the Fee item is
            generated. Optional. Allowed values: - Account Charges - Card
            Charges - Others Charges
        fee_type_id (int): Fee Type Id.  Optional.  Example:   1. Simple Fee 
            2. Card Event Fee  3. Customer Event Fee
        from_date (str): Fee Item FromDate/Time   Should be with in last 24
            months   Optional  Maximum of 210 days duration allowed per
            search, its configurable.  Format: yyyyMMdd
        to_date (str): Fee Item To Date/Time  Optional  When blank and
            FromDate is provided on the input, all fee items took place after
            the given from date/time should be returned. Note that the search
            is allowed for the maximum of 60 days. Hence if the FromDate is
            older than 60 days from current date then the fee items for 60
            days from FromDate will be returned.   Format: yyyyMMdd
        period (int): Fee items Period. This is ignored when FromDate/Todate
            is supplied on the request.   1.    Last 7 Days  2.    Last 30
            Days  3.    Last 90 Days  4.    Last 180 Days  Example : Pass 1
            for Last 7 days fee items
        include_cancelled_items (bool): True or False. When True, cancelled
            fee items are included on API response
        product_id (int): Product Id Optional Example: Sample list of product
            ids and description. 100    Service fee 102    Invoice production
            fee 103    Account fee 104    Transaction fee 105    Card
            membership fee
        product_code (str): Product Code   Optional  Example:   1. Service fee
            2. Invoice production fee  3. Account fee  4. Transaction fee  5.
            Card membership fee
        line_item_description (str): Line item description. Optional Minimum
            of 4 characters should be provided else not considered Those fee
            items that have the entered value at any part of the line item
            description will be returned.
        sort_order (str): Allowed Sorting Options: •    FeeDateAscending •   
            FeeDateDescending •    NetAmountAscending •    NetAmountDescending
            Optional. Default: 1
        current_page (int): Page Number
        page_size (int): Page Size – Number of records to show on a page

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "col_co_id": 'ColCoId',
        "col_co_code": 'ColCoCode',
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber',
        "accounts": 'Accounts',
        "card_id": 'CardId',
        "card_pan": 'CardPAN',
        "invoice_status": 'InvoiceStatus',
        "fee_type_group": 'FeeTypeGroup',
        "fee_type_id": 'FeeTypeId',
        "from_date": 'FromDate',
        "to_date": 'ToDate',
        "period": 'Period',
        "include_cancelled_items": 'IncludeCancelledItems',
        "product_id": 'ProductId',
        "product_code": 'ProductCode',
        "line_item_description": 'LineItemDescription',
        "sort_order": 'SortOrder',
        "current_page": 'CurrentPage',
        "page_size": 'PageSize'
    }

    _optionals = [
        'col_co_id',
        'col_co_code',
        'payer_id',
        'payer_number',
        'accounts',
        'card_id',
        'card_pan',
        'invoice_status',
        'fee_type_group',
        'fee_type_id',
        'from_date',
        'to_date',
        'period',
        'include_cancelled_items',
        'product_id',
        'product_code',
        'line_item_description',
        'sort_order',
        'current_page',
        'page_size',
    ]

    _nullables = [
        'col_co_id',
        'col_co_code',
        'payer_id',
        'payer_number',
        'card_id',
        'card_pan',
        'invoice_status',
        'fee_type_group',
        'fee_type_id',
        'from_date',
        'to_date',
        'period',
        'include_cancelled_items',
        'product_id',
        'product_code',
        'line_item_description',
        'sort_order',
        'current_page',
        'page_size',
    ]

    def __init__(self,
                 col_co_id=APIHelper.SKIP,
                 col_co_code=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 accounts=APIHelper.SKIP,
                 card_id=APIHelper.SKIP,
                 card_pan=APIHelper.SKIP,
                 invoice_status=APIHelper.SKIP,
                 fee_type_group=APIHelper.SKIP,
                 fee_type_id=APIHelper.SKIP,
                 from_date=APIHelper.SKIP,
                 to_date=APIHelper.SKIP,
                 period=APIHelper.SKIP,
                 include_cancelled_items=APIHelper.SKIP,
                 product_id=APIHelper.SKIP,
                 product_code=APIHelper.SKIP,
                 line_item_description=APIHelper.SKIP,
                 sort_order=APIHelper.SKIP,
                 current_page=APIHelper.SKIP,
                 page_size=APIHelper.SKIP):
        """Constructor for the TransactionFeesRequest class"""

        # Initialize members of the class
        if col_co_id is not APIHelper.SKIP:
            self.col_co_id = col_co_id 
        if col_co_code is not APIHelper.SKIP:
            self.col_co_code = col_co_code 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 
        if accounts is not APIHelper.SKIP:
            self.accounts = accounts 
        if card_id is not APIHelper.SKIP:
            self.card_id = card_id 
        if card_pan is not APIHelper.SKIP:
            self.card_pan = card_pan 
        if invoice_status is not APIHelper.SKIP:
            self.invoice_status = invoice_status 
        if fee_type_group is not APIHelper.SKIP:
            self.fee_type_group = fee_type_group 
        if fee_type_id is not APIHelper.SKIP:
            self.fee_type_id = fee_type_id 
        if from_date is not APIHelper.SKIP:
            self.from_date = from_date 
        if to_date is not APIHelper.SKIP:
            self.to_date = to_date 
        if period is not APIHelper.SKIP:
            self.period = period 
        if include_cancelled_items is not APIHelper.SKIP:
            self.include_cancelled_items = include_cancelled_items 
        if product_id is not APIHelper.SKIP:
            self.product_id = product_id 
        if product_code is not APIHelper.SKIP:
            self.product_code = product_code 
        if line_item_description is not APIHelper.SKIP:
            self.line_item_description = line_item_description 
        if sort_order is not APIHelper.SKIP:
            self.sort_order = sort_order 
        if current_page is not APIHelper.SKIP:
            self.current_page = current_page 
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
        col_co_id = dictionary.get("ColCoId") if "ColCoId" in dictionary.keys() else APIHelper.SKIP
        col_co_code = dictionary.get("ColCoCode") if "ColCoCode" in dictionary.keys() else APIHelper.SKIP
        payer_id = dictionary.get("PayerId") if "PayerId" in dictionary.keys() else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if "PayerNumber" in dictionary.keys() else APIHelper.SKIP
        accounts = None
        if dictionary.get('Accounts') is not None:
            accounts = [Accounts.from_dictionary(x) for x in dictionary.get('Accounts')]
        else:
            accounts = APIHelper.SKIP
        card_id = dictionary.get("CardId") if "CardId" in dictionary.keys() else APIHelper.SKIP
        card_pan = dictionary.get("CardPAN") if "CardPAN" in dictionary.keys() else APIHelper.SKIP
        invoice_status = dictionary.get("InvoiceStatus") if "InvoiceStatus" in dictionary.keys() else APIHelper.SKIP
        fee_type_group = dictionary.get("FeeTypeGroup") if "FeeTypeGroup" in dictionary.keys() else APIHelper.SKIP
        fee_type_id = dictionary.get("FeeTypeId") if "FeeTypeId" in dictionary.keys() else APIHelper.SKIP
        from_date = dictionary.get("FromDate") if "FromDate" in dictionary.keys() else APIHelper.SKIP
        to_date = dictionary.get("ToDate") if "ToDate" in dictionary.keys() else APIHelper.SKIP
        period = dictionary.get("Period") if "Period" in dictionary.keys() else APIHelper.SKIP
        include_cancelled_items = dictionary.get("IncludeCancelledItems") if "IncludeCancelledItems" in dictionary.keys() else APIHelper.SKIP
        product_id = dictionary.get("ProductId") if "ProductId" in dictionary.keys() else APIHelper.SKIP
        product_code = dictionary.get("ProductCode") if "ProductCode" in dictionary.keys() else APIHelper.SKIP
        line_item_description = dictionary.get("LineItemDescription") if "LineItemDescription" in dictionary.keys() else APIHelper.SKIP
        sort_order = dictionary.get("SortOrder") if "SortOrder" in dictionary.keys() else APIHelper.SKIP
        current_page = dictionary.get("CurrentPage") if "CurrentPage" in dictionary.keys() else APIHelper.SKIP
        page_size = dictionary.get("PageSize") if "PageSize" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(col_co_id,
                   col_co_code,
                   payer_id,
                   payer_number,
                   accounts,
                   card_id,
                   card_pan,
                   invoice_status,
                   fee_type_group,
                   fee_type_id,
                   from_date,
                   to_date,
                   period,
                   include_cancelled_items,
                   product_id,
                   product_code,
                   line_item_description,
                   sort_order,
                   current_page,
                   page_size)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_id={(self.col_co_id if hasattr(self, "col_co_id") else None)!r}, '
                f'col_co_code={(self.col_co_code if hasattr(self, "col_co_code") else None)!r}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!r}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!r}, '
                f'accounts={(self.accounts if hasattr(self, "accounts") else None)!r}, '
                f'card_id={(self.card_id if hasattr(self, "card_id") else None)!r}, '
                f'card_pan={(self.card_pan if hasattr(self, "card_pan") else None)!r}, '
                f'invoice_status={(self.invoice_status if hasattr(self, "invoice_status") else None)!r}, '
                f'fee_type_group={(self.fee_type_group if hasattr(self, "fee_type_group") else None)!r}, '
                f'fee_type_id={(self.fee_type_id if hasattr(self, "fee_type_id") else None)!r}, '
                f'from_date={(self.from_date if hasattr(self, "from_date") else None)!r}, '
                f'to_date={(self.to_date if hasattr(self, "to_date") else None)!r}, '
                f'period={(self.period if hasattr(self, "period") else None)!r}, '
                f'include_cancelled_items={(self.include_cancelled_items if hasattr(self, "include_cancelled_items") else None)!r}, '
                f'product_id={(self.product_id if hasattr(self, "product_id") else None)!r}, '
                f'product_code={(self.product_code if hasattr(self, "product_code") else None)!r}, '
                f'line_item_description={(self.line_item_description if hasattr(self, "line_item_description") else None)!r}, '
                f'sort_order={(self.sort_order if hasattr(self, "sort_order") else None)!r}, '
                f'current_page={(self.current_page if hasattr(self, "current_page") else None)!r}, '
                f'page_size={(self.page_size if hasattr(self, "page_size") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_id={(self.col_co_id if hasattr(self, "col_co_id") else None)!s}, '
                f'col_co_code={(self.col_co_code if hasattr(self, "col_co_code") else None)!s}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!s}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!s}, '
                f'accounts={(self.accounts if hasattr(self, "accounts") else None)!s}, '
                f'card_id={(self.card_id if hasattr(self, "card_id") else None)!s}, '
                f'card_pan={(self.card_pan if hasattr(self, "card_pan") else None)!s}, '
                f'invoice_status={(self.invoice_status if hasattr(self, "invoice_status") else None)!s}, '
                f'fee_type_group={(self.fee_type_group if hasattr(self, "fee_type_group") else None)!s}, '
                f'fee_type_id={(self.fee_type_id if hasattr(self, "fee_type_id") else None)!s}, '
                f'from_date={(self.from_date if hasattr(self, "from_date") else None)!s}, '
                f'to_date={(self.to_date if hasattr(self, "to_date") else None)!s}, '
                f'period={(self.period if hasattr(self, "period") else None)!s}, '
                f'include_cancelled_items={(self.include_cancelled_items if hasattr(self, "include_cancelled_items") else None)!s}, '
                f'product_id={(self.product_id if hasattr(self, "product_id") else None)!s}, '
                f'product_code={(self.product_code if hasattr(self, "product_code") else None)!s}, '
                f'line_item_description={(self.line_item_description if hasattr(self, "line_item_description") else None)!s}, '
                f'sort_order={(self.sort_order if hasattr(self, "sort_order") else None)!s}, '
                f'current_page={(self.current_page if hasattr(self, "current_page") else None)!s}, '
                f'page_size={(self.page_size if hasattr(self, "page_size") else None)!s})')
