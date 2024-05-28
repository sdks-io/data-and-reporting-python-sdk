# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper


class InvoicesSummaries(object):

    """Implementation of the 'InvoicesSummaries' model.

    TODO: type model description here.

    Attributes:
        amount_due (float): Amount due from last summary document date.
        amount_not_overdue (float): Amount that are due from past summary
            documents.
        amount_overdue (float): Amount that are overdue from past summary
            documents.
        amount_paid (float): Total amount paid in billing currency.
        billing_currency_code (str): Billing currency ISO code.
        billing_currency_symbol (str): Billing currency symbol.  Example: €
        outstanding_balance (float): Current outstanding balance amount
        payment_due_date (str): Payment due date.  Format: YYYYMMDD
        summary_document_date (str): Summary document date.  Format: YYYYMMDD
        total_billing_documents (int): Total number of invoices generated on
            this date.
        total_gross_amount_billing_currency (float): Total gross amount in
            billing currency.
        total_net_amount_billing_currency (float): Total net amount in billing
            currency.
        total_summary_documents (int): Total number of summary documents
            generated on this date.
        total_vat_amount_billing_currency (float): Total VAT amount in billing
            currency.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount_due": 'AmountDue',
        "amount_not_overdue": 'AmountNotOverdue',
        "amount_overdue": 'AmountOverdue',
        "amount_paid": 'AmountPaid',
        "billing_currency_code": 'BillingCurrencyCode',
        "billing_currency_symbol": 'BillingCurrencySymbol',
        "outstanding_balance": 'OutstandingBalance',
        "payment_due_date": 'PaymentDueDate',
        "summary_document_date": 'SummaryDocumentDate',
        "total_billing_documents": 'TotalBillingDocuments',
        "total_gross_amount_billing_currency": 'TotalGrossAmountBillingCurrency',
        "total_net_amount_billing_currency": 'TotalNetAmountBillingCurrency',
        "total_summary_documents": 'TotalSummaryDocuments',
        "total_vat_amount_billing_currency": 'TotalVATAmountBillingCurrency'
    }

    _optionals = [
        'amount_due',
        'amount_not_overdue',
        'amount_overdue',
        'amount_paid',
        'billing_currency_code',
        'billing_currency_symbol',
        'outstanding_balance',
        'payment_due_date',
        'summary_document_date',
        'total_billing_documents',
        'total_gross_amount_billing_currency',
        'total_net_amount_billing_currency',
        'total_summary_documents',
        'total_vat_amount_billing_currency',
    ]

    _nullables = [
        'amount_due',
        'amount_not_overdue',
        'amount_overdue',
        'amount_paid',
        'billing_currency_code',
        'billing_currency_symbol',
        'outstanding_balance',
        'payment_due_date',
        'summary_document_date',
        'total_billing_documents',
        'total_gross_amount_billing_currency',
        'total_net_amount_billing_currency',
        'total_summary_documents',
        'total_vat_amount_billing_currency',
    ]

    def __init__(self,
                 amount_due=APIHelper.SKIP,
                 amount_not_overdue=APIHelper.SKIP,
                 amount_overdue=APIHelper.SKIP,
                 amount_paid=APIHelper.SKIP,
                 billing_currency_code=APIHelper.SKIP,
                 billing_currency_symbol=APIHelper.SKIP,
                 outstanding_balance=APIHelper.SKIP,
                 payment_due_date=APIHelper.SKIP,
                 summary_document_date=APIHelper.SKIP,
                 total_billing_documents=APIHelper.SKIP,
                 total_gross_amount_billing_currency=APIHelper.SKIP,
                 total_net_amount_billing_currency=APIHelper.SKIP,
                 total_summary_documents=APIHelper.SKIP,
                 total_vat_amount_billing_currency=APIHelper.SKIP):
        """Constructor for the InvoicesSummaries class"""

        # Initialize members of the class
        if amount_due is not APIHelper.SKIP:
            self.amount_due = amount_due 
        if amount_not_overdue is not APIHelper.SKIP:
            self.amount_not_overdue = amount_not_overdue 
        if amount_overdue is not APIHelper.SKIP:
            self.amount_overdue = amount_overdue 
        if amount_paid is not APIHelper.SKIP:
            self.amount_paid = amount_paid 
        if billing_currency_code is not APIHelper.SKIP:
            self.billing_currency_code = billing_currency_code 
        if billing_currency_symbol is not APIHelper.SKIP:
            self.billing_currency_symbol = billing_currency_symbol 
        if outstanding_balance is not APIHelper.SKIP:
            self.outstanding_balance = outstanding_balance 
        if payment_due_date is not APIHelper.SKIP:
            self.payment_due_date = payment_due_date 
        if summary_document_date is not APIHelper.SKIP:
            self.summary_document_date = summary_document_date 
        if total_billing_documents is not APIHelper.SKIP:
            self.total_billing_documents = total_billing_documents 
        if total_gross_amount_billing_currency is not APIHelper.SKIP:
            self.total_gross_amount_billing_currency = total_gross_amount_billing_currency 
        if total_net_amount_billing_currency is not APIHelper.SKIP:
            self.total_net_amount_billing_currency = total_net_amount_billing_currency 
        if total_summary_documents is not APIHelper.SKIP:
            self.total_summary_documents = total_summary_documents 
        if total_vat_amount_billing_currency is not APIHelper.SKIP:
            self.total_vat_amount_billing_currency = total_vat_amount_billing_currency 

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
        amount_due = dictionary.get("AmountDue") if "AmountDue" in dictionary.keys() else APIHelper.SKIP
        amount_not_overdue = dictionary.get("AmountNotOverdue") if "AmountNotOverdue" in dictionary.keys() else APIHelper.SKIP
        amount_overdue = dictionary.get("AmountOverdue") if "AmountOverdue" in dictionary.keys() else APIHelper.SKIP
        amount_paid = dictionary.get("AmountPaid") if "AmountPaid" in dictionary.keys() else APIHelper.SKIP
        billing_currency_code = dictionary.get("BillingCurrencyCode") if "BillingCurrencyCode" in dictionary.keys() else APIHelper.SKIP
        billing_currency_symbol = dictionary.get("BillingCurrencySymbol") if "BillingCurrencySymbol" in dictionary.keys() else APIHelper.SKIP
        outstanding_balance = dictionary.get("OutstandingBalance") if "OutstandingBalance" in dictionary.keys() else APIHelper.SKIP
        payment_due_date = dictionary.get("PaymentDueDate") if "PaymentDueDate" in dictionary.keys() else APIHelper.SKIP
        summary_document_date = dictionary.get("SummaryDocumentDate") if "SummaryDocumentDate" in dictionary.keys() else APIHelper.SKIP
        total_billing_documents = dictionary.get("TotalBillingDocuments") if "TotalBillingDocuments" in dictionary.keys() else APIHelper.SKIP
        total_gross_amount_billing_currency = dictionary.get("TotalGrossAmountBillingCurrency") if "TotalGrossAmountBillingCurrency" in dictionary.keys() else APIHelper.SKIP
        total_net_amount_billing_currency = dictionary.get("TotalNetAmountBillingCurrency") if "TotalNetAmountBillingCurrency" in dictionary.keys() else APIHelper.SKIP
        total_summary_documents = dictionary.get("TotalSummaryDocuments") if "TotalSummaryDocuments" in dictionary.keys() else APIHelper.SKIP
        total_vat_amount_billing_currency = dictionary.get("TotalVATAmountBillingCurrency") if "TotalVATAmountBillingCurrency" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(amount_due,
                   amount_not_overdue,
                   amount_overdue,
                   amount_paid,
                   billing_currency_code,
                   billing_currency_symbol,
                   outstanding_balance,
                   payment_due_date,
                   summary_document_date,
                   total_billing_documents,
                   total_gross_amount_billing_currency,
                   total_net_amount_billing_currency,
                   total_summary_documents,
                   total_vat_amount_billing_currency)
