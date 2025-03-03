# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper


class SearchDocumentsInvoice(object):

    """Implementation of the 'SearchDocumentsInvoice' model.

    Attributes:
        document_reference (int): Unique Invoice Reference id of the invoice
            for downloading the zip file containing PDF and proofing elements.
            Example: 123456
        invoice_number (str): Payment customer number. Example: GB000000123
        payer_name (str): Customer payer name
        account_number (str): Account Number Example: GB99215176
        account_name (str): Invoice account name
        document_type (str): Document type String containing one of the
            following values: •    NAT (National) •    INT (International) •  
            SOA (Statement of Account)
        gross_amount (float): Included tax amount in the invoice
        net_amount (float): The model property of type float.
        tax_amount (float): The model property of type float.
        currency_code (str): The model property of type str.
        invoice_status (str): The model property of type str.
        invoice_date (str): The model property of type str.
        due_date (str): The model property of type str.
        vat_country_iso_code (str): The model property of type str.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "document_reference": 'DocumentReference',
        "invoice_number": 'InvoiceNumber',
        "payer_name": 'PayerName',
        "account_number": 'AccountNumber',
        "account_name": 'AccountName',
        "document_type": 'DocumentType',
        "gross_amount": 'GrossAmount',
        "net_amount": 'NetAmount',
        "tax_amount": 'TaxAmount',
        "currency_code": 'CurrencyCode',
        "invoice_status": 'InvoiceStatus',
        "invoice_date": 'InvoiceDate',
        "due_date": 'DueDate',
        "vat_country_iso_code": 'VATCountryISOCode'
    }

    _optionals = [
        'document_reference',
        'invoice_number',
        'payer_name',
        'account_number',
        'account_name',
        'document_type',
        'gross_amount',
        'net_amount',
        'tax_amount',
        'currency_code',
        'invoice_status',
        'invoice_date',
        'due_date',
        'vat_country_iso_code',
    ]

    _nullables = [
        'invoice_number',
        'payer_name',
        'account_number',
        'account_name',
        'document_type',
        'gross_amount',
        'net_amount',
        'tax_amount',
        'currency_code',
        'invoice_status',
        'invoice_date',
        'due_date',
        'vat_country_iso_code',
    ]

    def __init__(self,
                 document_reference=APIHelper.SKIP,
                 invoice_number=APIHelper.SKIP,
                 payer_name=APIHelper.SKIP,
                 account_number=APIHelper.SKIP,
                 account_name=APIHelper.SKIP,
                 document_type=APIHelper.SKIP,
                 gross_amount=APIHelper.SKIP,
                 net_amount=APIHelper.SKIP,
                 tax_amount=APIHelper.SKIP,
                 currency_code=APIHelper.SKIP,
                 invoice_status=APIHelper.SKIP,
                 invoice_date=APIHelper.SKIP,
                 due_date=APIHelper.SKIP,
                 vat_country_iso_code=APIHelper.SKIP):
        """Constructor for the SearchDocumentsInvoice class"""

        # Initialize members of the class
        if document_reference is not APIHelper.SKIP:
            self.document_reference = document_reference 
        if invoice_number is not APIHelper.SKIP:
            self.invoice_number = invoice_number 
        if payer_name is not APIHelper.SKIP:
            self.payer_name = payer_name 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if document_type is not APIHelper.SKIP:
            self.document_type = document_type 
        if gross_amount is not APIHelper.SKIP:
            self.gross_amount = gross_amount 
        if net_amount is not APIHelper.SKIP:
            self.net_amount = net_amount 
        if tax_amount is not APIHelper.SKIP:
            self.tax_amount = tax_amount 
        if currency_code is not APIHelper.SKIP:
            self.currency_code = currency_code 
        if invoice_status is not APIHelper.SKIP:
            self.invoice_status = invoice_status 
        if invoice_date is not APIHelper.SKIP:
            self.invoice_date = invoice_date 
        if due_date is not APIHelper.SKIP:
            self.due_date = due_date 
        if vat_country_iso_code is not APIHelper.SKIP:
            self.vat_country_iso_code = vat_country_iso_code 

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
        document_reference = dictionary.get("DocumentReference") if dictionary.get("DocumentReference") else APIHelper.SKIP
        invoice_number = dictionary.get("InvoiceNumber") if "InvoiceNumber" in dictionary.keys() else APIHelper.SKIP
        payer_name = dictionary.get("PayerName") if "PayerName" in dictionary.keys() else APIHelper.SKIP
        account_number = dictionary.get("AccountNumber") if "AccountNumber" in dictionary.keys() else APIHelper.SKIP
        account_name = dictionary.get("AccountName") if "AccountName" in dictionary.keys() else APIHelper.SKIP
        document_type = dictionary.get("DocumentType") if "DocumentType" in dictionary.keys() else APIHelper.SKIP
        gross_amount = dictionary.get("GrossAmount") if "GrossAmount" in dictionary.keys() else APIHelper.SKIP
        net_amount = dictionary.get("NetAmount") if "NetAmount" in dictionary.keys() else APIHelper.SKIP
        tax_amount = dictionary.get("TaxAmount") if "TaxAmount" in dictionary.keys() else APIHelper.SKIP
        currency_code = dictionary.get("CurrencyCode") if "CurrencyCode" in dictionary.keys() else APIHelper.SKIP
        invoice_status = dictionary.get("InvoiceStatus") if "InvoiceStatus" in dictionary.keys() else APIHelper.SKIP
        invoice_date = dictionary.get("InvoiceDate") if "InvoiceDate" in dictionary.keys() else APIHelper.SKIP
        due_date = dictionary.get("DueDate") if "DueDate" in dictionary.keys() else APIHelper.SKIP
        vat_country_iso_code = dictionary.get("VATCountryISOCode") if "VATCountryISOCode" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(document_reference,
                   invoice_number,
                   payer_name,
                   account_number,
                   account_name,
                   document_type,
                   gross_amount,
                   net_amount,
                   tax_amount,
                   currency_code,
                   invoice_status,
                   invoice_date,
                   due_date,
                   vat_country_iso_code)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'document_reference={(self.document_reference if hasattr(self, "document_reference") else None)!r}, '
                f'invoice_number={(self.invoice_number if hasattr(self, "invoice_number") else None)!r}, '
                f'payer_name={(self.payer_name if hasattr(self, "payer_name") else None)!r}, '
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!r}, '
                f'account_name={(self.account_name if hasattr(self, "account_name") else None)!r}, '
                f'document_type={(self.document_type if hasattr(self, "document_type") else None)!r}, '
                f'gross_amount={(self.gross_amount if hasattr(self, "gross_amount") else None)!r}, '
                f'net_amount={(self.net_amount if hasattr(self, "net_amount") else None)!r}, '
                f'tax_amount={(self.tax_amount if hasattr(self, "tax_amount") else None)!r}, '
                f'currency_code={(self.currency_code if hasattr(self, "currency_code") else None)!r}, '
                f'invoice_status={(self.invoice_status if hasattr(self, "invoice_status") else None)!r}, '
                f'invoice_date={(self.invoice_date if hasattr(self, "invoice_date") else None)!r}, '
                f'due_date={(self.due_date if hasattr(self, "due_date") else None)!r}, '
                f'vat_country_iso_code={(self.vat_country_iso_code if hasattr(self, "vat_country_iso_code") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'document_reference={(self.document_reference if hasattr(self, "document_reference") else None)!s}, '
                f'invoice_number={(self.invoice_number if hasattr(self, "invoice_number") else None)!s}, '
                f'payer_name={(self.payer_name if hasattr(self, "payer_name") else None)!s}, '
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!s}, '
                f'account_name={(self.account_name if hasattr(self, "account_name") else None)!s}, '
                f'document_type={(self.document_type if hasattr(self, "document_type") else None)!s}, '
                f'gross_amount={(self.gross_amount if hasattr(self, "gross_amount") else None)!s}, '
                f'net_amount={(self.net_amount if hasattr(self, "net_amount") else None)!s}, '
                f'tax_amount={(self.tax_amount if hasattr(self, "tax_amount") else None)!s}, '
                f'currency_code={(self.currency_code if hasattr(self, "currency_code") else None)!s}, '
                f'invoice_status={(self.invoice_status if hasattr(self, "invoice_status") else None)!s}, '
                f'invoice_date={(self.invoice_date if hasattr(self, "invoice_date") else None)!s}, '
                f'due_date={(self.due_date if hasattr(self, "due_date") else None)!s}, '
                f'vat_country_iso_code={(self.vat_country_iso_code if hasattr(self, "vat_country_iso_code") else None)!s})')
