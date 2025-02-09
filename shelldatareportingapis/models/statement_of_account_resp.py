# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper
from shelldatareportingapis.models.invoices_summaries import InvoicesSummaries
from shelldatareportingapis.models.last_statement_of_account import LastStatementOfAccount
from shelldatareportingapis.models.monthly_invoice_trend import MonthlyInvoiceTrend
from shelldatareportingapis.models.past_statement_of_accounts import PastStatementOfAccounts
from shelldatareportingapis.models.payments_since_last_soa import PaymentsSinceLastSOA


class StatementOfAccountResp(object):

    """Implementation of the 'StatementOfAccountResp' model.

    TODO: type model description here.

    Attributes:
        last_statement_of_account (LastStatementOfAccount): Latest statement
            of the account generated for the given Payer.
        monthly_invoice_trend (List[MonthlyInvoiceTrend]): TODO: type
            description here.
        past_statement_of_accounts (List[PastStatementOfAccounts]): TODO: type
            description here.
        payments_since_last_soa (List[PaymentsSinceLastSOA]): TODO: type
            description here.
        invoices_summaries (List[InvoicesSummaries]): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "last_statement_of_account": 'LastStatementOfAccount',
        "monthly_invoice_trend": 'MonthlyInvoiceTrend',
        "past_statement_of_accounts": 'PastStatementOfAccounts',
        "payments_since_last_soa": 'PaymentsSinceLastSOA',
        "invoices_summaries": 'InvoicesSummaries'
    }

    _optionals = [
        'last_statement_of_account',
        'monthly_invoice_trend',
        'past_statement_of_accounts',
        'payments_since_last_soa',
        'invoices_summaries',
    ]

    _nullables = [
        'monthly_invoice_trend',
        'payments_since_last_soa',
        'invoices_summaries',
    ]

    def __init__(self,
                 last_statement_of_account=APIHelper.SKIP,
                 monthly_invoice_trend=APIHelper.SKIP,
                 past_statement_of_accounts=APIHelper.SKIP,
                 payments_since_last_soa=APIHelper.SKIP,
                 invoices_summaries=APIHelper.SKIP):
        """Constructor for the StatementOfAccountResp class"""

        # Initialize members of the class
        if last_statement_of_account is not APIHelper.SKIP:
            self.last_statement_of_account = last_statement_of_account 
        if monthly_invoice_trend is not APIHelper.SKIP:
            self.monthly_invoice_trend = monthly_invoice_trend 
        if past_statement_of_accounts is not APIHelper.SKIP:
            self.past_statement_of_accounts = past_statement_of_accounts 
        if payments_since_last_soa is not APIHelper.SKIP:
            self.payments_since_last_soa = payments_since_last_soa 
        if invoices_summaries is not APIHelper.SKIP:
            self.invoices_summaries = invoices_summaries 

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
        last_statement_of_account = LastStatementOfAccount.from_dictionary(dictionary.get('LastStatementOfAccount')) if 'LastStatementOfAccount' in dictionary.keys() else APIHelper.SKIP
        if 'MonthlyInvoiceTrend' in dictionary.keys():
            monthly_invoice_trend = [MonthlyInvoiceTrend.from_dictionary(x) for x in dictionary.get('MonthlyInvoiceTrend')] if dictionary.get('MonthlyInvoiceTrend') else None
        else:
            monthly_invoice_trend = APIHelper.SKIP
        past_statement_of_accounts = None
        if dictionary.get('PastStatementOfAccounts') is not None:
            past_statement_of_accounts = [PastStatementOfAccounts.from_dictionary(x) for x in dictionary.get('PastStatementOfAccounts')]
        else:
            past_statement_of_accounts = APIHelper.SKIP
        if 'PaymentsSinceLastSOA' in dictionary.keys():
            payments_since_last_soa = [PaymentsSinceLastSOA.from_dictionary(x) for x in dictionary.get('PaymentsSinceLastSOA')] if dictionary.get('PaymentsSinceLastSOA') else None
        else:
            payments_since_last_soa = APIHelper.SKIP
        if 'InvoicesSummaries' in dictionary.keys():
            invoices_summaries = [InvoicesSummaries.from_dictionary(x) for x in dictionary.get('InvoicesSummaries')] if dictionary.get('InvoicesSummaries') else None
        else:
            invoices_summaries = APIHelper.SKIP
        # Return an object of this model
        return cls(last_statement_of_account,
                   monthly_invoice_trend,
                   past_statement_of_accounts,
                   payments_since_last_soa,
                   invoices_summaries)
