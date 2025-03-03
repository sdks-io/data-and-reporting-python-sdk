# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper
from shelldatareportingapis.models.accounts import Accounts


class InvoiceDatesRequestFilters(object):

    """Implementation of the 'InvoiceDatesRequestFilters' model.

    Attributes:
        col_co_code (int): Collecting Company Code of the selected payer.  
            Mandatory for serviced OUs such as Romania, Latvia, Lithuania,
            Estonia, Ukraine etc. It is optional for other countries if
            ColCoID is provided.  Example:  86-Philippines  5-UK
        col_co_id (int): Collecting Company Id of the selected payer.  
            Optional if ColCoCode is passed else Mandatory.  Example: 
            1-Philippines  5-UK
        payer_id (int): Payer Id of the selected payer. Optional if
            PayerNumber is passed else Mandatory
        payer_number (str): Payer Number of the selected payer. Optional if
            PayerId is passed else Mandatory
        from_date (str): Invoice date searched from this date. Optional. This
            input is a search criterion, if given. Date format: yyyyMMdd
        to_date (str): Invoice date searched until this date. Optional. This
            input is a search criterion, if given. Date format: yyyyMMdd
        accounts (List[Accounts]): The model property of type List[Accounts].

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "col_co_code": 'ColCoCode',
        "col_co_id": 'ColCoId',
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber',
        "from_date": 'FromDate',
        "to_date": 'ToDate',
        "accounts": 'Accounts'
    }

    _optionals = [
        'col_co_code',
        'col_co_id',
        'payer_id',
        'payer_number',
        'from_date',
        'to_date',
        'accounts',
    ]

    _nullables = [
        'col_co_code',
        'col_co_id',
        'payer_id',
        'payer_number',
        'from_date',
        'to_date',
    ]

    def __init__(self,
                 col_co_code=APIHelper.SKIP,
                 col_co_id=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 from_date=APIHelper.SKIP,
                 to_date=APIHelper.SKIP,
                 accounts=APIHelper.SKIP):
        """Constructor for the InvoiceDatesRequestFilters class"""

        # Initialize members of the class
        if col_co_code is not APIHelper.SKIP:
            self.col_co_code = col_co_code 
        if col_co_id is not APIHelper.SKIP:
            self.col_co_id = col_co_id 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 
        if from_date is not APIHelper.SKIP:
            self.from_date = from_date 
        if to_date is not APIHelper.SKIP:
            self.to_date = to_date 
        if accounts is not APIHelper.SKIP:
            self.accounts = accounts 

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
        col_co_code = dictionary.get("ColCoCode") if "ColCoCode" in dictionary.keys() else APIHelper.SKIP
        col_co_id = dictionary.get("ColCoId") if "ColCoId" in dictionary.keys() else APIHelper.SKIP
        payer_id = dictionary.get("PayerId") if "PayerId" in dictionary.keys() else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if "PayerNumber" in dictionary.keys() else APIHelper.SKIP
        from_date = dictionary.get("FromDate") if "FromDate" in dictionary.keys() else APIHelper.SKIP
        to_date = dictionary.get("ToDate") if "ToDate" in dictionary.keys() else APIHelper.SKIP
        accounts = None
        if dictionary.get('Accounts') is not None:
            accounts = [Accounts.from_dictionary(x) for x in dictionary.get('Accounts')]
        else:
            accounts = APIHelper.SKIP
        # Return an object of this model
        return cls(col_co_code,
                   col_co_id,
                   payer_id,
                   payer_number,
                   from_date,
                   to_date,
                   accounts)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_code={(self.col_co_code if hasattr(self, "col_co_code") else None)!r}, '
                f'col_co_id={(self.col_co_id if hasattr(self, "col_co_id") else None)!r}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!r}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!r}, '
                f'from_date={(self.from_date if hasattr(self, "from_date") else None)!r}, '
                f'to_date={(self.to_date if hasattr(self, "to_date") else None)!r}, '
                f'accounts={(self.accounts if hasattr(self, "accounts") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_code={(self.col_co_code if hasattr(self, "col_co_code") else None)!s}, '
                f'col_co_id={(self.col_co_id if hasattr(self, "col_co_id") else None)!s}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!s}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!s}, '
                f'from_date={(self.from_date if hasattr(self, "from_date") else None)!s}, '
                f'to_date={(self.to_date if hasattr(self, "to_date") else None)!s}, '
                f'accounts={(self.accounts if hasattr(self, "accounts") else None)!s})')
