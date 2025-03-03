# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper
from shelldatareportingapis.models.accounts import Accounts
from shelldatareportingapis.models.fuel_consumption_card import FuelConsumptionCard


class FuelConsumptionRequest(object):

    """Implementation of the 'FuelConsumptionRequest' model.

    Attributes:
        col_co_id (int): Collecting Company Id  of the selected payer.  
            Optional if ColCoCode is passed else Mandatory.  Example:  1 for
            Philippines  5 for UK
        col_co_code (int): Collecting Company Code  of the selected payer.  
            Mandatory for serviced OUs such as Romania, Latvia, Lithuania,
            Estonia, Ukraine etc. It is optional for other countries if
            ColCoID is provided.  Example:  86 for Philippines  5 for UK
        payer_id (int): Payer Id  of the selected payer. Optional if
            PayerNumber is passed else Mandatory
        payer_number (str): Payer Number of the selected payer. Optional if
            PayerId is passed else Mandatory
        accounts (List[Accounts]): The model property of type List[Accounts].
        card_group_id (int): Card Group Id in GFN Optional Example: 200
        card_group_name (str): Card Group Name Optional This input is a search
            criterion, if given.
        cards (List[FuelConsumptionCard]): The model property of type
            List[FuelConsumptionCard].
        from_date (str): Transactions from Date Optional – ‘Period’ will be
            considered when this field is not provided.
        to_date (str): Transactions to Date Optional Format: yyyyMMdd
        period (int): Transactions Period. This is ignored when FromDate is
            supplied on the request   Allowed values :  1.    Last 7 Days  2. 
            Last 30 Days  3.    Last 90 Days  Optional - When FromDate/ToDate
            and Period are not provided, ‘Last 7 Days’ value is considered as
            default Period.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "col_co_id": 'ColCoId',
        "col_co_code": 'ColCoCode',
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber',
        "accounts": 'Accounts',
        "card_group_id": 'CardGroupId',
        "card_group_name": 'CardGroupName',
        "cards": 'Cards',
        "from_date": 'FromDate',
        "to_date": 'ToDate',
        "period": 'Period'
    }

    _optionals = [
        'col_co_id',
        'col_co_code',
        'payer_id',
        'payer_number',
        'accounts',
        'card_group_id',
        'card_group_name',
        'cards',
        'from_date',
        'to_date',
        'period',
    ]

    def __init__(self,
                 col_co_id=APIHelper.SKIP,
                 col_co_code=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 accounts=APIHelper.SKIP,
                 card_group_id=APIHelper.SKIP,
                 card_group_name=APIHelper.SKIP,
                 cards=APIHelper.SKIP,
                 from_date=APIHelper.SKIP,
                 to_date=APIHelper.SKIP,
                 period=APIHelper.SKIP):
        """Constructor for the FuelConsumptionRequest class"""

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
        if card_group_id is not APIHelper.SKIP:
            self.card_group_id = card_group_id 
        if card_group_name is not APIHelper.SKIP:
            self.card_group_name = card_group_name 
        if cards is not APIHelper.SKIP:
            self.cards = cards 
        if from_date is not APIHelper.SKIP:
            self.from_date = from_date 
        if to_date is not APIHelper.SKIP:
            self.to_date = to_date 
        if period is not APIHelper.SKIP:
            self.period = period 

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
        col_co_id = dictionary.get("ColCoId") if dictionary.get("ColCoId") else APIHelper.SKIP
        col_co_code = dictionary.get("ColCoCode") if dictionary.get("ColCoCode") else APIHelper.SKIP
        payer_id = dictionary.get("PayerId") if dictionary.get("PayerId") else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if dictionary.get("PayerNumber") else APIHelper.SKIP
        accounts = None
        if dictionary.get('Accounts') is not None:
            accounts = [Accounts.from_dictionary(x) for x in dictionary.get('Accounts')]
        else:
            accounts = APIHelper.SKIP
        card_group_id = dictionary.get("CardGroupId") if dictionary.get("CardGroupId") else APIHelper.SKIP
        card_group_name = dictionary.get("CardGroupName") if dictionary.get("CardGroupName") else APIHelper.SKIP
        cards = None
        if dictionary.get('Cards') is not None:
            cards = [FuelConsumptionCard.from_dictionary(x) for x in dictionary.get('Cards')]
        else:
            cards = APIHelper.SKIP
        from_date = dictionary.get("FromDate") if dictionary.get("FromDate") else APIHelper.SKIP
        to_date = dictionary.get("ToDate") if dictionary.get("ToDate") else APIHelper.SKIP
        period = dictionary.get("Period") if dictionary.get("Period") else APIHelper.SKIP
        # Return an object of this model
        return cls(col_co_id,
                   col_co_code,
                   payer_id,
                   payer_number,
                   accounts,
                   card_group_id,
                   card_group_name,
                   cards,
                   from_date,
                   to_date,
                   period)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_id={(self.col_co_id if hasattr(self, "col_co_id") else None)!r}, '
                f'col_co_code={(self.col_co_code if hasattr(self, "col_co_code") else None)!r}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!r}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!r}, '
                f'accounts={(self.accounts if hasattr(self, "accounts") else None)!r}, '
                f'card_group_id={(self.card_group_id if hasattr(self, "card_group_id") else None)!r}, '
                f'card_group_name={(self.card_group_name if hasattr(self, "card_group_name") else None)!r}, '
                f'cards={(self.cards if hasattr(self, "cards") else None)!r}, '
                f'from_date={(self.from_date if hasattr(self, "from_date") else None)!r}, '
                f'to_date={(self.to_date if hasattr(self, "to_date") else None)!r}, '
                f'period={(self.period if hasattr(self, "period") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_id={(self.col_co_id if hasattr(self, "col_co_id") else None)!s}, '
                f'col_co_code={(self.col_co_code if hasattr(self, "col_co_code") else None)!s}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!s}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!s}, '
                f'accounts={(self.accounts if hasattr(self, "accounts") else None)!s}, '
                f'card_group_id={(self.card_group_id if hasattr(self, "card_group_id") else None)!s}, '
                f'card_group_name={(self.card_group_name if hasattr(self, "card_group_name") else None)!s}, '
                f'cards={(self.cards if hasattr(self, "cards") else None)!s}, '
                f'from_date={(self.from_date if hasattr(self, "from_date") else None)!s}, '
                f'to_date={(self.to_date if hasattr(self, "to_date") else None)!s}, '
                f'period={(self.period if hasattr(self, "period") else None)!s})')
