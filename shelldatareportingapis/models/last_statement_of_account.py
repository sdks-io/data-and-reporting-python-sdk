# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper


class LastStatementOfAccount(object):

    """Implementation of the 'LastStatementOfAccount' model.

    Latest statement of the account generated for the given Payer.

    Attributes:
        amount_due (float): Invoiced amount and due for payment.
        amount_not_overdue (float): Invoiced amount and not overdue for
            payment.
        amount_overdue (float): Invoiced amount and overdue for payment.
        credit_limit (int): Credit limit.
        credit_limit_currency_code (str): ISO code of the credit limit’s
            currency. Example: EUR
        credit_limit_currency_symbol (str): Symbol of the credit limit’s
            currency. Example: €
        credit_limit_in_customer_currency (float): Credit limit in Customer
            currency. **Note**: For currency details refer the parameters
            CurrencyCode & CurrencySymbol in the StatementOfAccount response.
        currency_code (str): ISO code of SOA currency.   Example: EUR
        currency_symbol (str): Symbol of SOA currency.   Example: €
        last_payment_currency_code (str): ISO code of Last Payment currency.  
            Example: EUR
        last_payment_currency_symbol (str): Symbol of Last Payment currency.  
            Example: €
        last_payment_date (str): Last payment date. Format: yyyyMMdd
        last_payment_value (float): Last payment value.
        outstanding_balance (float): Current outstanding balance amount.
        payer_id (int): Payment customer id of the customer.
        payer_number (str): Payment customer number.
        payment_due_date (str): Due date for payment. Format: yyyyMMdd
        payment_method (str): Payment method description of the Payer.  
            Example: Id & Description  •    Incoming - Direct Debit  •   
            Incoming - Cheque  •    Incoming - Direct Debit A  •    Incoming -
            Bank Transfer  •    Incoming - Cash
        payment_method_id (int): Payment method Id of the Payer.   Example: Id
            & Description  •    Incoming - Direct Debit  •    Incoming -
            Cheque  •    Incoming - Direct Debit A  •    Incoming - Bank
            Transfer  •    Incoming - Cash
        payment_terms (str): Payment terms description of the Payer. Example:
            Id & Description •    14 days after Invoice •    15 days after
            Invoice •    21 days after Invoice •    30 days after Invoice •   
            45 days after Invoice •    0 days after invoice •    days after
            invoice •    days after invoice •    7 days after invoice •   
            10th of the following month
        payment_terms_id (int): Payment terms Id of the Payer. Example: Id &
            Description •    14 days after Invoice •    15 days after Invoice
            •    21 days after Invoice •    30 days after Invoice •    45 days
            after Invoice •    0 days after invoice •    days after invoice • 
            days after invoice •    7 days after invoice •    10th of the
            following month
        so_a_reference_number (str): Statement of account reference number
        statement_date (str): Date on which the SOA was generated. Format:
            yyyyMMdd
        statement_of_account_id (int): Statement of account identifier,
            Example: 1
        total_billing_documents (int): Total number of billing documents for
            this Statement of Account
        total_summary_billing_documents (int): Total number of summary billing
            documents for this Statement of Account
        unallocated_payment (int): Unallocated payment.   When negative,
            indicates overdue amount.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount_due": 'AmountDue',
        "amount_not_overdue": 'AmountNotOverdue',
        "amount_overdue": 'AmountOverdue',
        "credit_limit": 'CreditLimit',
        "credit_limit_currency_code": 'CreditLimitCurrencyCode',
        "credit_limit_currency_symbol": 'CreditLimitCurrencySymbol',
        "credit_limit_in_customer_currency": 'CreditLimitInCustomerCurrency',
        "currency_code": 'CurrencyCode',
        "currency_symbol": 'CurrencySymbol',
        "last_payment_currency_code": 'LastPaymentCurrencyCode',
        "last_payment_currency_symbol": 'LastPaymentCurrencySymbol',
        "last_payment_date": 'LastPaymentDate',
        "last_payment_value": 'LastPaymentValue',
        "outstanding_balance": 'OutstandingBalance',
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber',
        "payment_due_date": 'PaymentDueDate',
        "payment_method": 'PaymentMethod',
        "payment_method_id": 'PaymentMethodId',
        "payment_terms": 'PaymentTerms',
        "payment_terms_id": 'PaymentTermsId',
        "so_a_reference_number": 'SoAReferenceNumber',
        "statement_date": 'StatementDate',
        "statement_of_account_id": 'StatementOfAccountId',
        "total_billing_documents": 'TotalBillingDocuments',
        "total_summary_billing_documents": 'TotalSummaryBillingDocuments',
        "unallocated_payment": 'UnallocatedPayment'
    }

    _optionals = [
        'amount_due',
        'amount_not_overdue',
        'amount_overdue',
        'credit_limit',
        'credit_limit_currency_code',
        'credit_limit_currency_symbol',
        'credit_limit_in_customer_currency',
        'currency_code',
        'currency_symbol',
        'last_payment_currency_code',
        'last_payment_currency_symbol',
        'last_payment_date',
        'last_payment_value',
        'outstanding_balance',
        'payer_id',
        'payer_number',
        'payment_due_date',
        'payment_method',
        'payment_method_id',
        'payment_terms',
        'payment_terms_id',
        'so_a_reference_number',
        'statement_date',
        'statement_of_account_id',
        'total_billing_documents',
        'total_summary_billing_documents',
        'unallocated_payment',
    ]

    _nullables = [
        'amount_due',
        'amount_not_overdue',
        'amount_overdue',
        'credit_limit',
        'credit_limit_currency_code',
        'credit_limit_currency_symbol',
        'credit_limit_in_customer_currency',
        'currency_code',
        'currency_symbol',
        'last_payment_currency_code',
        'last_payment_currency_symbol',
        'last_payment_date',
        'last_payment_value',
        'outstanding_balance',
        'payer_id',
        'payer_number',
        'payment_due_date',
        'payment_method',
        'payment_method_id',
        'payment_terms',
        'payment_terms_id',
        'so_a_reference_number',
        'statement_date',
        'statement_of_account_id',
        'total_billing_documents',
        'total_summary_billing_documents',
        'unallocated_payment',
    ]

    def __init__(self,
                 amount_due=APIHelper.SKIP,
                 amount_not_overdue=APIHelper.SKIP,
                 amount_overdue=APIHelper.SKIP,
                 credit_limit=APIHelper.SKIP,
                 credit_limit_currency_code=APIHelper.SKIP,
                 credit_limit_currency_symbol=APIHelper.SKIP,
                 credit_limit_in_customer_currency=APIHelper.SKIP,
                 currency_code=APIHelper.SKIP,
                 currency_symbol=APIHelper.SKIP,
                 last_payment_currency_code=APIHelper.SKIP,
                 last_payment_currency_symbol=APIHelper.SKIP,
                 last_payment_date=APIHelper.SKIP,
                 last_payment_value=APIHelper.SKIP,
                 outstanding_balance=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 payment_due_date=APIHelper.SKIP,
                 payment_method=APIHelper.SKIP,
                 payment_method_id=APIHelper.SKIP,
                 payment_terms=APIHelper.SKIP,
                 payment_terms_id=APIHelper.SKIP,
                 so_a_reference_number=APIHelper.SKIP,
                 statement_date=APIHelper.SKIP,
                 statement_of_account_id=APIHelper.SKIP,
                 total_billing_documents=APIHelper.SKIP,
                 total_summary_billing_documents=APIHelper.SKIP,
                 unallocated_payment=APIHelper.SKIP):
        """Constructor for the LastStatementOfAccount class"""

        # Initialize members of the class
        if amount_due is not APIHelper.SKIP:
            self.amount_due = amount_due 
        if amount_not_overdue is not APIHelper.SKIP:
            self.amount_not_overdue = amount_not_overdue 
        if amount_overdue is not APIHelper.SKIP:
            self.amount_overdue = amount_overdue 
        if credit_limit is not APIHelper.SKIP:
            self.credit_limit = credit_limit 
        if credit_limit_currency_code is not APIHelper.SKIP:
            self.credit_limit_currency_code = credit_limit_currency_code 
        if credit_limit_currency_symbol is not APIHelper.SKIP:
            self.credit_limit_currency_symbol = credit_limit_currency_symbol 
        if credit_limit_in_customer_currency is not APIHelper.SKIP:
            self.credit_limit_in_customer_currency = credit_limit_in_customer_currency 
        if currency_code is not APIHelper.SKIP:
            self.currency_code = currency_code 
        if currency_symbol is not APIHelper.SKIP:
            self.currency_symbol = currency_symbol 
        if last_payment_currency_code is not APIHelper.SKIP:
            self.last_payment_currency_code = last_payment_currency_code 
        if last_payment_currency_symbol is not APIHelper.SKIP:
            self.last_payment_currency_symbol = last_payment_currency_symbol 
        if last_payment_date is not APIHelper.SKIP:
            self.last_payment_date = last_payment_date 
        if last_payment_value is not APIHelper.SKIP:
            self.last_payment_value = last_payment_value 
        if outstanding_balance is not APIHelper.SKIP:
            self.outstanding_balance = outstanding_balance 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 
        if payment_due_date is not APIHelper.SKIP:
            self.payment_due_date = payment_due_date 
        if payment_method is not APIHelper.SKIP:
            self.payment_method = payment_method 
        if payment_method_id is not APIHelper.SKIP:
            self.payment_method_id = payment_method_id 
        if payment_terms is not APIHelper.SKIP:
            self.payment_terms = payment_terms 
        if payment_terms_id is not APIHelper.SKIP:
            self.payment_terms_id = payment_terms_id 
        if so_a_reference_number is not APIHelper.SKIP:
            self.so_a_reference_number = so_a_reference_number 
        if statement_date is not APIHelper.SKIP:
            self.statement_date = statement_date 
        if statement_of_account_id is not APIHelper.SKIP:
            self.statement_of_account_id = statement_of_account_id 
        if total_billing_documents is not APIHelper.SKIP:
            self.total_billing_documents = total_billing_documents 
        if total_summary_billing_documents is not APIHelper.SKIP:
            self.total_summary_billing_documents = total_summary_billing_documents 
        if unallocated_payment is not APIHelper.SKIP:
            self.unallocated_payment = unallocated_payment 

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
        amount_due = dictionary.get("AmountDue") if "AmountDue" in dictionary.keys() else APIHelper.SKIP
        amount_not_overdue = dictionary.get("AmountNotOverdue") if "AmountNotOverdue" in dictionary.keys() else APIHelper.SKIP
        amount_overdue = dictionary.get("AmountOverdue") if "AmountOverdue" in dictionary.keys() else APIHelper.SKIP
        credit_limit = dictionary.get("CreditLimit") if "CreditLimit" in dictionary.keys() else APIHelper.SKIP
        credit_limit_currency_code = dictionary.get("CreditLimitCurrencyCode") if "CreditLimitCurrencyCode" in dictionary.keys() else APIHelper.SKIP
        credit_limit_currency_symbol = dictionary.get("CreditLimitCurrencySymbol") if "CreditLimitCurrencySymbol" in dictionary.keys() else APIHelper.SKIP
        credit_limit_in_customer_currency = dictionary.get("CreditLimitInCustomerCurrency") if "CreditLimitInCustomerCurrency" in dictionary.keys() else APIHelper.SKIP
        currency_code = dictionary.get("CurrencyCode") if "CurrencyCode" in dictionary.keys() else APIHelper.SKIP
        currency_symbol = dictionary.get("CurrencySymbol") if "CurrencySymbol" in dictionary.keys() else APIHelper.SKIP
        last_payment_currency_code = dictionary.get("LastPaymentCurrencyCode") if "LastPaymentCurrencyCode" in dictionary.keys() else APIHelper.SKIP
        last_payment_currency_symbol = dictionary.get("LastPaymentCurrencySymbol") if "LastPaymentCurrencySymbol" in dictionary.keys() else APIHelper.SKIP
        last_payment_date = dictionary.get("LastPaymentDate") if "LastPaymentDate" in dictionary.keys() else APIHelper.SKIP
        last_payment_value = dictionary.get("LastPaymentValue") if "LastPaymentValue" in dictionary.keys() else APIHelper.SKIP
        outstanding_balance = dictionary.get("OutstandingBalance") if "OutstandingBalance" in dictionary.keys() else APIHelper.SKIP
        payer_id = dictionary.get("PayerId") if "PayerId" in dictionary.keys() else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if "PayerNumber" in dictionary.keys() else APIHelper.SKIP
        payment_due_date = dictionary.get("PaymentDueDate") if "PaymentDueDate" in dictionary.keys() else APIHelper.SKIP
        payment_method = dictionary.get("PaymentMethod") if "PaymentMethod" in dictionary.keys() else APIHelper.SKIP
        payment_method_id = dictionary.get("PaymentMethodId") if "PaymentMethodId" in dictionary.keys() else APIHelper.SKIP
        payment_terms = dictionary.get("PaymentTerms") if "PaymentTerms" in dictionary.keys() else APIHelper.SKIP
        payment_terms_id = dictionary.get("PaymentTermsId") if "PaymentTermsId" in dictionary.keys() else APIHelper.SKIP
        so_a_reference_number = dictionary.get("SoAReferenceNumber") if "SoAReferenceNumber" in dictionary.keys() else APIHelper.SKIP
        statement_date = dictionary.get("StatementDate") if "StatementDate" in dictionary.keys() else APIHelper.SKIP
        statement_of_account_id = dictionary.get("StatementOfAccountId") if "StatementOfAccountId" in dictionary.keys() else APIHelper.SKIP
        total_billing_documents = dictionary.get("TotalBillingDocuments") if "TotalBillingDocuments" in dictionary.keys() else APIHelper.SKIP
        total_summary_billing_documents = dictionary.get("TotalSummaryBillingDocuments") if "TotalSummaryBillingDocuments" in dictionary.keys() else APIHelper.SKIP
        unallocated_payment = dictionary.get("UnallocatedPayment") if "UnallocatedPayment" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(amount_due,
                   amount_not_overdue,
                   amount_overdue,
                   credit_limit,
                   credit_limit_currency_code,
                   credit_limit_currency_symbol,
                   credit_limit_in_customer_currency,
                   currency_code,
                   currency_symbol,
                   last_payment_currency_code,
                   last_payment_currency_symbol,
                   last_payment_date,
                   last_payment_value,
                   outstanding_balance,
                   payer_id,
                   payer_number,
                   payment_due_date,
                   payment_method,
                   payment_method_id,
                   payment_terms,
                   payment_terms_id,
                   so_a_reference_number,
                   statement_date,
                   statement_of_account_id,
                   total_billing_documents,
                   total_summary_billing_documents,
                   unallocated_payment)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'amount_due={(self.amount_due if hasattr(self, "amount_due") else None)!r}, '
                f'amount_not_overdue={(self.amount_not_overdue if hasattr(self, "amount_not_overdue") else None)!r}, '
                f'amount_overdue={(self.amount_overdue if hasattr(self, "amount_overdue") else None)!r}, '
                f'credit_limit={(self.credit_limit if hasattr(self, "credit_limit") else None)!r}, '
                f'credit_limit_currency_code={(self.credit_limit_currency_code if hasattr(self, "credit_limit_currency_code") else None)!r}, '
                f'credit_limit_currency_symbol={(self.credit_limit_currency_symbol if hasattr(self, "credit_limit_currency_symbol") else None)!r}, '
                f'credit_limit_in_customer_currency={(self.credit_limit_in_customer_currency if hasattr(self, "credit_limit_in_customer_currency") else None)!r}, '
                f'currency_code={(self.currency_code if hasattr(self, "currency_code") else None)!r}, '
                f'currency_symbol={(self.currency_symbol if hasattr(self, "currency_symbol") else None)!r}, '
                f'last_payment_currency_code={(self.last_payment_currency_code if hasattr(self, "last_payment_currency_code") else None)!r}, '
                f'last_payment_currency_symbol={(self.last_payment_currency_symbol if hasattr(self, "last_payment_currency_symbol") else None)!r}, '
                f'last_payment_date={(self.last_payment_date if hasattr(self, "last_payment_date") else None)!r}, '
                f'last_payment_value={(self.last_payment_value if hasattr(self, "last_payment_value") else None)!r}, '
                f'outstanding_balance={(self.outstanding_balance if hasattr(self, "outstanding_balance") else None)!r}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!r}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!r}, '
                f'payment_due_date={(self.payment_due_date if hasattr(self, "payment_due_date") else None)!r}, '
                f'payment_method={(self.payment_method if hasattr(self, "payment_method") else None)!r}, '
                f'payment_method_id={(self.payment_method_id if hasattr(self, "payment_method_id") else None)!r}, '
                f'payment_terms={(self.payment_terms if hasattr(self, "payment_terms") else None)!r}, '
                f'payment_terms_id={(self.payment_terms_id if hasattr(self, "payment_terms_id") else None)!r}, '
                f'so_a_reference_number={(self.so_a_reference_number if hasattr(self, "so_a_reference_number") else None)!r}, '
                f'statement_date={(self.statement_date if hasattr(self, "statement_date") else None)!r}, '
                f'statement_of_account_id={(self.statement_of_account_id if hasattr(self, "statement_of_account_id") else None)!r}, '
                f'total_billing_documents={(self.total_billing_documents if hasattr(self, "total_billing_documents") else None)!r}, '
                f'total_summary_billing_documents={(self.total_summary_billing_documents if hasattr(self, "total_summary_billing_documents") else None)!r}, '
                f'unallocated_payment={(self.unallocated_payment if hasattr(self, "unallocated_payment") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'amount_due={(self.amount_due if hasattr(self, "amount_due") else None)!s}, '
                f'amount_not_overdue={(self.amount_not_overdue if hasattr(self, "amount_not_overdue") else None)!s}, '
                f'amount_overdue={(self.amount_overdue if hasattr(self, "amount_overdue") else None)!s}, '
                f'credit_limit={(self.credit_limit if hasattr(self, "credit_limit") else None)!s}, '
                f'credit_limit_currency_code={(self.credit_limit_currency_code if hasattr(self, "credit_limit_currency_code") else None)!s}, '
                f'credit_limit_currency_symbol={(self.credit_limit_currency_symbol if hasattr(self, "credit_limit_currency_symbol") else None)!s}, '
                f'credit_limit_in_customer_currency={(self.credit_limit_in_customer_currency if hasattr(self, "credit_limit_in_customer_currency") else None)!s}, '
                f'currency_code={(self.currency_code if hasattr(self, "currency_code") else None)!s}, '
                f'currency_symbol={(self.currency_symbol if hasattr(self, "currency_symbol") else None)!s}, '
                f'last_payment_currency_code={(self.last_payment_currency_code if hasattr(self, "last_payment_currency_code") else None)!s}, '
                f'last_payment_currency_symbol={(self.last_payment_currency_symbol if hasattr(self, "last_payment_currency_symbol") else None)!s}, '
                f'last_payment_date={(self.last_payment_date if hasattr(self, "last_payment_date") else None)!s}, '
                f'last_payment_value={(self.last_payment_value if hasattr(self, "last_payment_value") else None)!s}, '
                f'outstanding_balance={(self.outstanding_balance if hasattr(self, "outstanding_balance") else None)!s}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!s}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!s}, '
                f'payment_due_date={(self.payment_due_date if hasattr(self, "payment_due_date") else None)!s}, '
                f'payment_method={(self.payment_method if hasattr(self, "payment_method") else None)!s}, '
                f'payment_method_id={(self.payment_method_id if hasattr(self, "payment_method_id") else None)!s}, '
                f'payment_terms={(self.payment_terms if hasattr(self, "payment_terms") else None)!s}, '
                f'payment_terms_id={(self.payment_terms_id if hasattr(self, "payment_terms_id") else None)!s}, '
                f'so_a_reference_number={(self.so_a_reference_number if hasattr(self, "so_a_reference_number") else None)!s}, '
                f'statement_date={(self.statement_date if hasattr(self, "statement_date") else None)!s}, '
                f'statement_of_account_id={(self.statement_of_account_id if hasattr(self, "statement_of_account_id") else None)!s}, '
                f'total_billing_documents={(self.total_billing_documents if hasattr(self, "total_billing_documents") else None)!s}, '
                f'total_summary_billing_documents={(self.total_summary_billing_documents if hasattr(self, "total_summary_billing_documents") else None)!s}, '
                f'unallocated_payment={(self.unallocated_payment if hasattr(self, "unallocated_payment") else None)!s})')
