# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper


class InvoiceDatesData(object):

    """Implementation of the 'InvoiceDatesData' model.

    TODO: type model description here.

    Attributes:
        invoice_numbers (List[str]): List of Invoice numbers.
        invoice_dates (List[str]): List of Invoicing dates. Format: yyyyMMdd

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "invoice_numbers": 'InvoiceNumbers',
        "invoice_dates": 'InvoiceDates'
    }

    _optionals = [
        'invoice_numbers',
        'invoice_dates',
    ]

    def __init__(self,
                 invoice_numbers=APIHelper.SKIP,
                 invoice_dates=APIHelper.SKIP):
        """Constructor for the InvoiceDatesData class"""

        # Initialize members of the class
        if invoice_numbers is not APIHelper.SKIP:
            self.invoice_numbers = invoice_numbers 
        if invoice_dates is not APIHelper.SKIP:
            self.invoice_dates = invoice_dates 

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
        invoice_numbers = dictionary.get("InvoiceNumbers") if dictionary.get("InvoiceNumbers") else APIHelper.SKIP
        invoice_dates = dictionary.get("InvoiceDates") if dictionary.get("InvoiceDates") else APIHelper.SKIP
        # Return an object of this model
        return cls(invoice_numbers,
                   invoice_dates)
