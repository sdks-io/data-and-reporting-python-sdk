# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper
from shelldatareportingapis.models.customer_contract import CustomerContract
from shelldatareportingapis.models.invoice_distribution_method import InvoiceDistributionMethod


class AccountResponseAccountsItems(object):

    """Implementation of the 'AccountResponseAccountsItems' model.

    TODO: type model description here.

    Attributes:
        account_full_name (str): Account Full Name
        account_id (int): Account Id
        account_number (str): Account Number
        account_short_name (str): Account Short Name
        best_of_indicator (bool): Best of Indicator of the Pricing
            customer/account configured.
        billing_frequency_type (str): Billing/Invoice frequency. The frequency
            in which the transactions will be considered for invoicing in a
            bulling run  E.g.:   1    Daily (all days)  2    Daily (only
            working days)  3    Weekly - Monday  4    Weekly – Tuesday  Etc.
        billing_frequency_type_id (int): Billing/Invoice frequency Identifier.
            Indicates the frequency in which the transactions will be
            considered for invoicing in a bulling run
        billing_run_frequency (str): Frequency at which the billing process is
            triggered. E.g.:   1    Daily (all days)  2    Daily (only working
            days)  3    Weekly - Monday  4    Weekly – Tuesday  Etc.
        billing_run_frequency_type_id (int): Frequency at which the billing
            process is triggered. E.g.: 1, 2, 3, etc.
        col_co_country_code (str): The 2-character ISO Code for the customer
            and card owning country.
        currency_code (str): ISO code of customer currency.
        currency_symbol (str): €
        day_1_run (int): The first day in a month when the billing should run
            in case of multiple billing runs configured with in a single month
        day_2_run (int): The second day in a month when the billing should run
            in case of multiple billing runs configured with in a single month
        day_3_run (int): The third day in a month when the billing should run
            in case of multiple billing runs configured with in a single month
        day_4_run (int): The fourth day in a month when the billing should run
            in case of multiple billing runs configured with in a single month
        frequency_type (str): Frequency type unit id & description E.g.: 1 -
            Daily 2 - Weekly 3 - Monthly 4 - Invoicing 6 - Calendar quarter
        gross_amount (float): Gross amount in customer currency.
        international_pos_language_code (str): POS international language code
        international_pos_language_id (int): POS international language ID
        invoice_account_id (int): The Account ID of the account on which the
            invoice is generated.
        invoice_account_number (str): The Account Number of the account on
            which the invoice is generated.
        invoice_account_short_name (str): The Account Short Name of the
            account on which the invoice is generated.
        invoice_distribution_methods (List[InvoiceDistributionMethod]): TODO:
            type description here.
        is_international (bool): Whether the account is international.
        is_invoice_point (bool): Whether the account is an invoice point.
        last_modified_date (str): Account last modified date and time
        local_currency_code (str): ISO code of customer currency.
        local_currency_symbol (str): Customer currency symbol.
        local_pos_language_code (str): POS local language code
        local_pos_language_id (int): POS local language ID
        net_amount (float): Net amount in customer currency.
        outstanding_balance (float): Outstanding balance in customer currency.
        paid_amount (float): Amount paid in customer currency.
        status (str): Account Status
        status_reason (str): Account status change reason id-description for
            the Status Reason, if any
        total_active_card_groups (int): Total number of active card groups
            under the account
        total_active_cards (int): Total number of active cards under the
            account.
        total_blocked_cards (int): Total number of cards under the account
            that are permanently blocked
        total_cancelled_cards (int): Total number of cards under the account
            that are cancelled
        total_cards (int): Total number of cards under the account.
        total_expired_cards (int): Total number of expired cards under the
            account.
        total_fraud_cards (int): Total number of cards in Fraud status.
        total_new_cards (int): Total number of cards in “New” status.
        total_renewal_pending_cards (int): Total number of Renewal Pending
            account under the payer
        total_replaced_cards (int): Total number of cards under the account
            with status as “Replaced”
        total_temporary_block_cards_by_customer (int): Total number of cards
            under the account that are temporarily blocked by customer.
        total_temporary_block_cards_by_shell (int): Total number of cards
            under the account that are temporarily blocked by Shell.
        vat_amount (float): VAT amount in customer currency.
        is_partner_card (int): The account / sub-account is partner card
            account or not. Possible values (1= Non-PC account, 2= PC account,
            3= PC Payer with Card Types, 4= PC Payer) Note: A partner card
            account is assumed to have only partner card card-types associated
        tolls_customer_id (str): Customer id in e-TM system
        tolls_colco_country_type_id (str): Colco country type id in e-TM system
        contracts (List[CustomerContract]): TODO: type description here.
        is_consortium_member (str): true

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_full_name": 'AccountFullName',
        "account_id": 'AccountId',
        "account_number": 'AccountNumber',
        "account_short_name": 'AccountShortName',
        "best_of_indicator": 'BestOfIndicator',
        "billing_frequency_type": 'BillingFrequencyType',
        "billing_frequency_type_id": 'BillingFrequencyTypeId',
        "billing_run_frequency": 'BillingRunFrequency',
        "billing_run_frequency_type_id": 'BillingRunFrequencyTypeId',
        "col_co_country_code": 'ColCoCountryCode',
        "currency_code": 'CurrencyCode',
        "currency_symbol": 'CurrencySymbol',
        "day_1_run": 'Day1Run',
        "day_2_run": 'Day2Run',
        "day_3_run": 'Day3Run',
        "day_4_run": 'Day4Run',
        "frequency_type": 'FrequencyType',
        "gross_amount": 'GrossAmount',
        "international_pos_language_code": 'InternationalPOSLanguageCode',
        "international_pos_language_id": 'InternationalPOSLanguageID',
        "invoice_account_id": 'InvoiceAccountID',
        "invoice_account_number": 'InvoiceAccountNumber',
        "invoice_account_short_name": 'InvoiceAccountShortName',
        "invoice_distribution_methods": 'InvoiceDistributionMethods',
        "is_international": 'IsInternational',
        "is_invoice_point": 'IsInvoicePoint',
        "last_modified_date": 'LastModifiedDate',
        "local_currency_code": 'LocalCurrencyCode',
        "local_currency_symbol": 'LocalCurrencySymbol',
        "local_pos_language_code": 'LocalPOSLanguageCode',
        "local_pos_language_id": 'LocalPOSLanguageID',
        "net_amount": 'NetAmount',
        "outstanding_balance": 'OutstandingBalance',
        "paid_amount": 'PaidAmount',
        "status": 'Status',
        "status_reason": 'StatusReason',
        "total_active_card_groups": 'TotalActiveCardGroups',
        "total_active_cards": 'TotalActiveCards',
        "total_blocked_cards": 'TotalBlockedCards',
        "total_cancelled_cards": 'TotalCancelledCards',
        "total_cards": 'TotalCards',
        "total_expired_cards": 'TotalExpiredCards',
        "total_fraud_cards": 'TotalFraudCards',
        "total_new_cards": 'TotalNewCards',
        "total_renewal_pending_cards": 'TotalRenewalPendingCards',
        "total_replaced_cards": 'TotalReplacedCards',
        "total_temporary_block_cards_by_customer": 'TotalTemporaryBlockCardsByCustomer',
        "total_temporary_block_cards_by_shell": 'TotalTemporaryBlockCardsByShell',
        "vat_amount": 'VATAmount',
        "is_partner_card": 'IsPartnerCard',
        "tolls_customer_id": 'TollsCustomerId',
        "tolls_colco_country_type_id": 'TollsColcoCountryTypeId',
        "contracts": 'Contracts',
        "is_consortium_member": 'IsConsortiumMember'
    }

    _optionals = [
        'account_full_name',
        'account_id',
        'account_number',
        'account_short_name',
        'best_of_indicator',
        'billing_frequency_type',
        'billing_frequency_type_id',
        'billing_run_frequency',
        'billing_run_frequency_type_id',
        'col_co_country_code',
        'currency_code',
        'currency_symbol',
        'day_1_run',
        'day_2_run',
        'day_3_run',
        'day_4_run',
        'frequency_type',
        'gross_amount',
        'international_pos_language_code',
        'international_pos_language_id',
        'invoice_account_id',
        'invoice_account_number',
        'invoice_account_short_name',
        'invoice_distribution_methods',
        'is_international',
        'is_invoice_point',
        'last_modified_date',
        'local_currency_code',
        'local_currency_symbol',
        'local_pos_language_code',
        'local_pos_language_id',
        'net_amount',
        'outstanding_balance',
        'paid_amount',
        'status',
        'status_reason',
        'total_active_card_groups',
        'total_active_cards',
        'total_blocked_cards',
        'total_cancelled_cards',
        'total_cards',
        'total_expired_cards',
        'total_fraud_cards',
        'total_new_cards',
        'total_renewal_pending_cards',
        'total_replaced_cards',
        'total_temporary_block_cards_by_customer',
        'total_temporary_block_cards_by_shell',
        'vat_amount',
        'is_partner_card',
        'tolls_customer_id',
        'tolls_colco_country_type_id',
        'contracts',
        'is_consortium_member',
    ]

    _nullables = [
        'account_full_name',
        'account_id',
        'account_number',
        'account_short_name',
        'billing_frequency_type',
        'billing_frequency_type_id',
        'billing_run_frequency',
        'billing_run_frequency_type_id',
        'col_co_country_code',
        'currency_code',
        'currency_symbol',
        'day_1_run',
        'day_2_run',
        'day_3_run',
        'day_4_run',
        'frequency_type',
        'gross_amount',
        'international_pos_language_code',
        'international_pos_language_id',
        'invoice_account_id',
        'invoice_account_number',
        'invoice_account_short_name',
        'is_international',
        'is_invoice_point',
        'last_modified_date',
        'local_currency_code',
        'local_currency_symbol',
        'local_pos_language_code',
        'local_pos_language_id',
        'net_amount',
        'outstanding_balance',
        'paid_amount',
        'status',
        'status_reason',
        'total_active_card_groups',
        'total_active_cards',
        'total_blocked_cards',
        'total_cancelled_cards',
        'total_cards',
        'total_expired_cards',
        'total_fraud_cards',
        'total_new_cards',
        'total_renewal_pending_cards',
        'total_replaced_cards',
        'total_temporary_block_cards_by_customer',
        'total_temporary_block_cards_by_shell',
        'vat_amount',
        'is_partner_card',
        'tolls_customer_id',
        'tolls_colco_country_type_id',
        'is_consortium_member',
    ]

    def __init__(self,
                 account_full_name=APIHelper.SKIP,
                 account_id=APIHelper.SKIP,
                 account_number=APIHelper.SKIP,
                 account_short_name=APIHelper.SKIP,
                 best_of_indicator=APIHelper.SKIP,
                 billing_frequency_type=APIHelper.SKIP,
                 billing_frequency_type_id=APIHelper.SKIP,
                 billing_run_frequency=APIHelper.SKIP,
                 billing_run_frequency_type_id=APIHelper.SKIP,
                 col_co_country_code=APIHelper.SKIP,
                 currency_code=APIHelper.SKIP,
                 currency_symbol=APIHelper.SKIP,
                 day_1_run=APIHelper.SKIP,
                 day_2_run=APIHelper.SKIP,
                 day_3_run=APIHelper.SKIP,
                 day_4_run=APIHelper.SKIP,
                 frequency_type=APIHelper.SKIP,
                 gross_amount=APIHelper.SKIP,
                 international_pos_language_code=APIHelper.SKIP,
                 international_pos_language_id=APIHelper.SKIP,
                 invoice_account_id=APIHelper.SKIP,
                 invoice_account_number=APIHelper.SKIP,
                 invoice_account_short_name=APIHelper.SKIP,
                 invoice_distribution_methods=APIHelper.SKIP,
                 is_international=APIHelper.SKIP,
                 is_invoice_point=APIHelper.SKIP,
                 last_modified_date=APIHelper.SKIP,
                 local_currency_code=APIHelper.SKIP,
                 local_currency_symbol=APIHelper.SKIP,
                 local_pos_language_code=APIHelper.SKIP,
                 local_pos_language_id=APIHelper.SKIP,
                 net_amount=APIHelper.SKIP,
                 outstanding_balance=APIHelper.SKIP,
                 paid_amount=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 status_reason=APIHelper.SKIP,
                 total_active_card_groups=APIHelper.SKIP,
                 total_active_cards=APIHelper.SKIP,
                 total_blocked_cards=APIHelper.SKIP,
                 total_cancelled_cards=APIHelper.SKIP,
                 total_cards=APIHelper.SKIP,
                 total_expired_cards=APIHelper.SKIP,
                 total_fraud_cards=APIHelper.SKIP,
                 total_new_cards=APIHelper.SKIP,
                 total_renewal_pending_cards=APIHelper.SKIP,
                 total_replaced_cards=APIHelper.SKIP,
                 total_temporary_block_cards_by_customer=APIHelper.SKIP,
                 total_temporary_block_cards_by_shell=APIHelper.SKIP,
                 vat_amount=APIHelper.SKIP,
                 is_partner_card=APIHelper.SKIP,
                 tolls_customer_id=APIHelper.SKIP,
                 tolls_colco_country_type_id=APIHelper.SKIP,
                 contracts=APIHelper.SKIP,
                 is_consortium_member=APIHelper.SKIP):
        """Constructor for the AccountResponseAccountsItems class"""

        # Initialize members of the class
        if account_full_name is not APIHelper.SKIP:
            self.account_full_name = account_full_name 
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if account_short_name is not APIHelper.SKIP:
            self.account_short_name = account_short_name 
        if best_of_indicator is not APIHelper.SKIP:
            self.best_of_indicator = best_of_indicator 
        if billing_frequency_type is not APIHelper.SKIP:
            self.billing_frequency_type = billing_frequency_type 
        if billing_frequency_type_id is not APIHelper.SKIP:
            self.billing_frequency_type_id = billing_frequency_type_id 
        if billing_run_frequency is not APIHelper.SKIP:
            self.billing_run_frequency = billing_run_frequency 
        if billing_run_frequency_type_id is not APIHelper.SKIP:
            self.billing_run_frequency_type_id = billing_run_frequency_type_id 
        if col_co_country_code is not APIHelper.SKIP:
            self.col_co_country_code = col_co_country_code 
        if currency_code is not APIHelper.SKIP:
            self.currency_code = currency_code 
        if currency_symbol is not APIHelper.SKIP:
            self.currency_symbol = currency_symbol 
        if day_1_run is not APIHelper.SKIP:
            self.day_1_run = day_1_run 
        if day_2_run is not APIHelper.SKIP:
            self.day_2_run = day_2_run 
        if day_3_run is not APIHelper.SKIP:
            self.day_3_run = day_3_run 
        if day_4_run is not APIHelper.SKIP:
            self.day_4_run = day_4_run 
        if frequency_type is not APIHelper.SKIP:
            self.frequency_type = frequency_type 
        if gross_amount is not APIHelper.SKIP:
            self.gross_amount = gross_amount 
        if international_pos_language_code is not APIHelper.SKIP:
            self.international_pos_language_code = international_pos_language_code 
        if international_pos_language_id is not APIHelper.SKIP:
            self.international_pos_language_id = international_pos_language_id 
        if invoice_account_id is not APIHelper.SKIP:
            self.invoice_account_id = invoice_account_id 
        if invoice_account_number is not APIHelper.SKIP:
            self.invoice_account_number = invoice_account_number 
        if invoice_account_short_name is not APIHelper.SKIP:
            self.invoice_account_short_name = invoice_account_short_name 
        if invoice_distribution_methods is not APIHelper.SKIP:
            self.invoice_distribution_methods = invoice_distribution_methods 
        if is_international is not APIHelper.SKIP:
            self.is_international = is_international 
        if is_invoice_point is not APIHelper.SKIP:
            self.is_invoice_point = is_invoice_point 
        if last_modified_date is not APIHelper.SKIP:
            self.last_modified_date = last_modified_date 
        if local_currency_code is not APIHelper.SKIP:
            self.local_currency_code = local_currency_code 
        if local_currency_symbol is not APIHelper.SKIP:
            self.local_currency_symbol = local_currency_symbol 
        if local_pos_language_code is not APIHelper.SKIP:
            self.local_pos_language_code = local_pos_language_code 
        if local_pos_language_id is not APIHelper.SKIP:
            self.local_pos_language_id = local_pos_language_id 
        if net_amount is not APIHelper.SKIP:
            self.net_amount = net_amount 
        if outstanding_balance is not APIHelper.SKIP:
            self.outstanding_balance = outstanding_balance 
        if paid_amount is not APIHelper.SKIP:
            self.paid_amount = paid_amount 
        if status is not APIHelper.SKIP:
            self.status = status 
        if status_reason is not APIHelper.SKIP:
            self.status_reason = status_reason 
        if total_active_card_groups is not APIHelper.SKIP:
            self.total_active_card_groups = total_active_card_groups 
        if total_active_cards is not APIHelper.SKIP:
            self.total_active_cards = total_active_cards 
        if total_blocked_cards is not APIHelper.SKIP:
            self.total_blocked_cards = total_blocked_cards 
        if total_cancelled_cards is not APIHelper.SKIP:
            self.total_cancelled_cards = total_cancelled_cards 
        if total_cards is not APIHelper.SKIP:
            self.total_cards = total_cards 
        if total_expired_cards is not APIHelper.SKIP:
            self.total_expired_cards = total_expired_cards 
        if total_fraud_cards is not APIHelper.SKIP:
            self.total_fraud_cards = total_fraud_cards 
        if total_new_cards is not APIHelper.SKIP:
            self.total_new_cards = total_new_cards 
        if total_renewal_pending_cards is not APIHelper.SKIP:
            self.total_renewal_pending_cards = total_renewal_pending_cards 
        if total_replaced_cards is not APIHelper.SKIP:
            self.total_replaced_cards = total_replaced_cards 
        if total_temporary_block_cards_by_customer is not APIHelper.SKIP:
            self.total_temporary_block_cards_by_customer = total_temporary_block_cards_by_customer 
        if total_temporary_block_cards_by_shell is not APIHelper.SKIP:
            self.total_temporary_block_cards_by_shell = total_temporary_block_cards_by_shell 
        if vat_amount is not APIHelper.SKIP:
            self.vat_amount = vat_amount 
        if is_partner_card is not APIHelper.SKIP:
            self.is_partner_card = is_partner_card 
        if tolls_customer_id is not APIHelper.SKIP:
            self.tolls_customer_id = tolls_customer_id 
        if tolls_colco_country_type_id is not APIHelper.SKIP:
            self.tolls_colco_country_type_id = tolls_colco_country_type_id 
        if contracts is not APIHelper.SKIP:
            self.contracts = contracts 
        if is_consortium_member is not APIHelper.SKIP:
            self.is_consortium_member = is_consortium_member 

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
        account_full_name = dictionary.get("AccountFullName") if "AccountFullName" in dictionary.keys() else APIHelper.SKIP
        account_id = dictionary.get("AccountId") if "AccountId" in dictionary.keys() else APIHelper.SKIP
        account_number = dictionary.get("AccountNumber") if "AccountNumber" in dictionary.keys() else APIHelper.SKIP
        account_short_name = dictionary.get("AccountShortName") if "AccountShortName" in dictionary.keys() else APIHelper.SKIP
        best_of_indicator = dictionary.get("BestOfIndicator") if "BestOfIndicator" in dictionary.keys() else APIHelper.SKIP
        billing_frequency_type = dictionary.get("BillingFrequencyType") if "BillingFrequencyType" in dictionary.keys() else APIHelper.SKIP
        billing_frequency_type_id = dictionary.get("BillingFrequencyTypeId") if "BillingFrequencyTypeId" in dictionary.keys() else APIHelper.SKIP
        billing_run_frequency = dictionary.get("BillingRunFrequency") if "BillingRunFrequency" in dictionary.keys() else APIHelper.SKIP
        billing_run_frequency_type_id = dictionary.get("BillingRunFrequencyTypeId") if "BillingRunFrequencyTypeId" in dictionary.keys() else APIHelper.SKIP
        col_co_country_code = dictionary.get("ColCoCountryCode") if "ColCoCountryCode" in dictionary.keys() else APIHelper.SKIP
        currency_code = dictionary.get("CurrencyCode") if "CurrencyCode" in dictionary.keys() else APIHelper.SKIP
        currency_symbol = dictionary.get("CurrencySymbol") if "CurrencySymbol" in dictionary.keys() else APIHelper.SKIP
        day_1_run = dictionary.get("Day1Run") if "Day1Run" in dictionary.keys() else APIHelper.SKIP
        day_2_run = dictionary.get("Day2Run") if "Day2Run" in dictionary.keys() else APIHelper.SKIP
        day_3_run = dictionary.get("Day3Run") if "Day3Run" in dictionary.keys() else APIHelper.SKIP
        day_4_run = dictionary.get("Day4Run") if "Day4Run" in dictionary.keys() else APIHelper.SKIP
        frequency_type = dictionary.get("FrequencyType") if "FrequencyType" in dictionary.keys() else APIHelper.SKIP
        gross_amount = dictionary.get("GrossAmount") if "GrossAmount" in dictionary.keys() else APIHelper.SKIP
        international_pos_language_code = dictionary.get("InternationalPOSLanguageCode") if "InternationalPOSLanguageCode" in dictionary.keys() else APIHelper.SKIP
        international_pos_language_id = dictionary.get("InternationalPOSLanguageID") if "InternationalPOSLanguageID" in dictionary.keys() else APIHelper.SKIP
        invoice_account_id = dictionary.get("InvoiceAccountID") if "InvoiceAccountID" in dictionary.keys() else APIHelper.SKIP
        invoice_account_number = dictionary.get("InvoiceAccountNumber") if "InvoiceAccountNumber" in dictionary.keys() else APIHelper.SKIP
        invoice_account_short_name = dictionary.get("InvoiceAccountShortName") if "InvoiceAccountShortName" in dictionary.keys() else APIHelper.SKIP
        invoice_distribution_methods = None
        if dictionary.get('InvoiceDistributionMethods') is not None:
            invoice_distribution_methods = [InvoiceDistributionMethod.from_dictionary(x) for x in dictionary.get('InvoiceDistributionMethods')]
        else:
            invoice_distribution_methods = APIHelper.SKIP
        is_international = dictionary.get("IsInternational") if "IsInternational" in dictionary.keys() else APIHelper.SKIP
        is_invoice_point = dictionary.get("IsInvoicePoint") if "IsInvoicePoint" in dictionary.keys() else APIHelper.SKIP
        last_modified_date = dictionary.get("LastModifiedDate") if "LastModifiedDate" in dictionary.keys() else APIHelper.SKIP
        local_currency_code = dictionary.get("LocalCurrencyCode") if "LocalCurrencyCode" in dictionary.keys() else APIHelper.SKIP
        local_currency_symbol = dictionary.get("LocalCurrencySymbol") if "LocalCurrencySymbol" in dictionary.keys() else APIHelper.SKIP
        local_pos_language_code = dictionary.get("LocalPOSLanguageCode") if "LocalPOSLanguageCode" in dictionary.keys() else APIHelper.SKIP
        local_pos_language_id = dictionary.get("LocalPOSLanguageID") if "LocalPOSLanguageID" in dictionary.keys() else APIHelper.SKIP
        net_amount = dictionary.get("NetAmount") if "NetAmount" in dictionary.keys() else APIHelper.SKIP
        outstanding_balance = dictionary.get("OutstandingBalance") if "OutstandingBalance" in dictionary.keys() else APIHelper.SKIP
        paid_amount = dictionary.get("PaidAmount") if "PaidAmount" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("Status") if "Status" in dictionary.keys() else APIHelper.SKIP
        status_reason = dictionary.get("StatusReason") if "StatusReason" in dictionary.keys() else APIHelper.SKIP
        total_active_card_groups = dictionary.get("TotalActiveCardGroups") if "TotalActiveCardGroups" in dictionary.keys() else APIHelper.SKIP
        total_active_cards = dictionary.get("TotalActiveCards") if "TotalActiveCards" in dictionary.keys() else APIHelper.SKIP
        total_blocked_cards = dictionary.get("TotalBlockedCards") if "TotalBlockedCards" in dictionary.keys() else APIHelper.SKIP
        total_cancelled_cards = dictionary.get("TotalCancelledCards") if "TotalCancelledCards" in dictionary.keys() else APIHelper.SKIP
        total_cards = dictionary.get("TotalCards") if "TotalCards" in dictionary.keys() else APIHelper.SKIP
        total_expired_cards = dictionary.get("TotalExpiredCards") if "TotalExpiredCards" in dictionary.keys() else APIHelper.SKIP
        total_fraud_cards = dictionary.get("TotalFraudCards") if "TotalFraudCards" in dictionary.keys() else APIHelper.SKIP
        total_new_cards = dictionary.get("TotalNewCards") if "TotalNewCards" in dictionary.keys() else APIHelper.SKIP
        total_renewal_pending_cards = dictionary.get("TotalRenewalPendingCards") if "TotalRenewalPendingCards" in dictionary.keys() else APIHelper.SKIP
        total_replaced_cards = dictionary.get("TotalReplacedCards") if "TotalReplacedCards" in dictionary.keys() else APIHelper.SKIP
        total_temporary_block_cards_by_customer = dictionary.get("TotalTemporaryBlockCardsByCustomer") if "TotalTemporaryBlockCardsByCustomer" in dictionary.keys() else APIHelper.SKIP
        total_temporary_block_cards_by_shell = dictionary.get("TotalTemporaryBlockCardsByShell") if "TotalTemporaryBlockCardsByShell" in dictionary.keys() else APIHelper.SKIP
        vat_amount = dictionary.get("VATAmount") if "VATAmount" in dictionary.keys() else APIHelper.SKIP
        is_partner_card = dictionary.get("IsPartnerCard") if "IsPartnerCard" in dictionary.keys() else APIHelper.SKIP
        tolls_customer_id = dictionary.get("TollsCustomerId") if "TollsCustomerId" in dictionary.keys() else APIHelper.SKIP
        tolls_colco_country_type_id = dictionary.get("TollsColcoCountryTypeId") if "TollsColcoCountryTypeId" in dictionary.keys() else APIHelper.SKIP
        contracts = None
        if dictionary.get('Contracts') is not None:
            contracts = [CustomerContract.from_dictionary(x) for x in dictionary.get('Contracts')]
        else:
            contracts = APIHelper.SKIP
        is_consortium_member = dictionary.get("IsConsortiumMember") if "IsConsortiumMember" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(account_full_name,
                   account_id,
                   account_number,
                   account_short_name,
                   best_of_indicator,
                   billing_frequency_type,
                   billing_frequency_type_id,
                   billing_run_frequency,
                   billing_run_frequency_type_id,
                   col_co_country_code,
                   currency_code,
                   currency_symbol,
                   day_1_run,
                   day_2_run,
                   day_3_run,
                   day_4_run,
                   frequency_type,
                   gross_amount,
                   international_pos_language_code,
                   international_pos_language_id,
                   invoice_account_id,
                   invoice_account_number,
                   invoice_account_short_name,
                   invoice_distribution_methods,
                   is_international,
                   is_invoice_point,
                   last_modified_date,
                   local_currency_code,
                   local_currency_symbol,
                   local_pos_language_code,
                   local_pos_language_id,
                   net_amount,
                   outstanding_balance,
                   paid_amount,
                   status,
                   status_reason,
                   total_active_card_groups,
                   total_active_cards,
                   total_blocked_cards,
                   total_cancelled_cards,
                   total_cards,
                   total_expired_cards,
                   total_fraud_cards,
                   total_new_cards,
                   total_renewal_pending_cards,
                   total_replaced_cards,
                   total_temporary_block_cards_by_customer,
                   total_temporary_block_cards_by_shell,
                   vat_amount,
                   is_partner_card,
                   tolls_customer_id,
                   tolls_colco_country_type_id,
                   contracts,
                   is_consortium_member)
