# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper
from shelldatareportingapis.models.error_status import ErrorStatus
from shelldatareportingapis.models.priced_trans_summary_response_transactions_summary_items import PricedTransSummaryResponseTransactionsSummaryItems


class PricedTransSummaryResponse(object):

    """Implementation of the 'PricedTransSummaryResponse' model.

    TODO: type model description here.

    Attributes:
        transactions_summary
            (List[PricedTransSummaryResponseTransactionsSummaryItems]): TODO:
            type description here.
        error (ErrorStatus): TODO: type description here.
        request_id (str): API Request Id

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "transactions_summary": 'TransactionsSummary',
        "error": 'Error',
        "request_id": 'RequestId'
    }

    _optionals = [
        'transactions_summary',
        'error',
        'request_id',
    ]

    def __init__(self,
                 transactions_summary=APIHelper.SKIP,
                 error=APIHelper.SKIP,
                 request_id=APIHelper.SKIP):
        """Constructor for the PricedTransSummaryResponse class"""

        # Initialize members of the class
        if transactions_summary is not APIHelper.SKIP:
            self.transactions_summary = transactions_summary 
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
        transactions_summary = None
        if dictionary.get('TransactionsSummary') is not None:
            transactions_summary = [PricedTransSummaryResponseTransactionsSummaryItems.from_dictionary(x) for x in dictionary.get('TransactionsSummary')]
        else:
            transactions_summary = APIHelper.SKIP
        error = ErrorStatus.from_dictionary(dictionary.get('Error')) if 'Error' in dictionary.keys() else APIHelper.SKIP
        request_id = dictionary.get("RequestId") if dictionary.get("RequestId") else APIHelper.SKIP
        # Return an object of this model
        return cls(transactions_summary,
                   error,
                   request_id)
