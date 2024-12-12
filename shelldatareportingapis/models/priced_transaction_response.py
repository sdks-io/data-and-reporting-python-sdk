# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper
from shelldatareportingapis.models.priced_transaction_response_transactions_items import PricedTransactionResponseTransactionsItems


class PricedTransactionResponse(object):

    """Implementation of the 'PricedTransactionResponse' model.

    TODO: type model description here.

    Attributes:
        transactions (List[PricedTransactionResponseTransactionsItems]): TODO:
            type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "transactions": 'Transactions'
    }

    _optionals = [
        'transactions',
    ]

    def __init__(self,
                 transactions=APIHelper.SKIP):
        """Constructor for the PricedTransactionResponse class"""

        # Initialize members of the class
        if transactions is not APIHelper.SKIP:
            self.transactions = transactions 

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
        transactions = None
        if dictionary.get('Transactions') is not None:
            transactions = [PricedTransactionResponseTransactionsItems.from_dictionary(x) for x in dictionary.get('Transactions')]
        else:
            transactions = APIHelper.SKIP
        # Return an object of this model
        return cls(transactions)
