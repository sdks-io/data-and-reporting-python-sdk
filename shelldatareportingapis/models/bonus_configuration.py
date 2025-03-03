# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper
from shelldatareportingapis.models.associated_account import AssociatedAccount
from shelldatareportingapis.models.fee_rule_location import FeeRuleLocation
from shelldatareportingapis.models.fee_rule_product import FeeRuleProduct
from shelldatareportingapis.models.fee_rule_tier import FeeRuleTier


class BonusConfiguration(object):

    """Implementation of the 'BonusConfiguration' model.

    Attributes:
        pricing_account_id (int): Account identifier of the Pricing Account
            associated with the Payer.
        pricing_account_number (str): Account number of the Pricing Account
            associated with the Payer.
        pricing_account_short_name (str): Short name of the Pricing Account
            associated with the Payer.
        pricing_account_full_name (str): Full name of the Pricing Account
            associated with the Payer.
        fee_rule_id (int): Bonus or association bonus configuration identifier
            that is associated to the payer.
        fee_rule_description (str): Bonus or association bonus configuration
            description that is associated to the payer.
        fee_rule_date_effective (str): The bonus or association bonus
            configuration becomes effective on the payer from this date.
            Format: YYYYMMDD
        fee_rule_date_terminated (str): The bonus or association bonus
            configuration is terminated for the payer on this date. Format:
            YYYYMMDD
        bonus_paid_to (str): Configuration to specify how the bonus is paid. 
            Format: ID-Description  Example:   1-Pay to Payer  2-Pay to
            invoice levels before the payer  3-Pay to specific customer  4-Pay
            to Association Customer  5-Pay to Associated Customers
        bonus_paid_to_account_id (int): Account identifier of the specific
            account to which the bonus is paid back
        bonus_paid_to_account_number (str): Account number of the specific
            account to which the bonus is paid back
        bonus_paid_to_account_short_name (str): Short name of the specific
            account to which the bonus is paid back
        bonus_paid_to_account_full_name (str): Full name of the specific
            account to which the bonus is paid back
        frequency (str): Frequency of the configuration. Format:
            ID-Description Examples: 1-Daily (all days) 2-Daily (only working
            days) 3-Weekly – Monday
        next_calculation_date (str): The next bonus is calculated for the
            payer on this date. Format: YYYYMMDD
        previous_calculated_date (str): The previous bonus was calculated for
            the payer on this date. Format: YYYYMMDD
        fee_rule_basis (str): Fee Rule Basis configured. Format:
            ID-Description Example: 1-Currency Per Unit 2-Percentage of Uplift
            3-Lump Sum
        fee_rule_currency_code (str): ISO currency code of the currency
            configured in the Bonus Configuration, if any.
        fee_rule_currency_symbol (str): Currency symbol of the currency
            configured in the Bonus Configuration, if any.
        fee_rule_available_from (str): This bonus or association bonus is
            available from this date. Format: YYYYMMDD
        fee_rule_available_to (str): This bonus or association bonus
            configuration will not be available from this date. Format:
            YYYYMMDD
        fee_rule_locations (List[FeeRuleLocation]): The model property of type
            List[FeeRuleLocation].
        fee_rule_tiers (List[FeeRuleTier]): The model property of type
            List[FeeRuleTier].
        associated_accounts (List[AssociatedAccount]): The model property of
            type List[AssociatedAccount].
        fee_rule_products (List[FeeRuleProduct]): The model property of type
            List[FeeRuleProduct].

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pricing_account_id": 'PricingAccountId',
        "pricing_account_number": 'PricingAccountNumber',
        "pricing_account_short_name": 'PricingAccountShortName',
        "pricing_account_full_name": 'PricingAccountFullName',
        "fee_rule_id": 'FeeRuleId',
        "fee_rule_description": 'FeeRuleDescription',
        "fee_rule_date_effective": 'FeeRuleDateEffective',
        "fee_rule_date_terminated": 'FeeRuleDateTerminated',
        "bonus_paid_to": 'BonusPaidTo',
        "bonus_paid_to_account_id": 'BonusPaidToAccountId',
        "bonus_paid_to_account_number": 'BonusPaidToAccountNumber',
        "bonus_paid_to_account_short_name": 'BonusPaidToAccountShortName',
        "bonus_paid_to_account_full_name": 'BonusPaidToAccountFullName',
        "frequency": 'Frequency',
        "next_calculation_date": 'NextCalculationDate',
        "previous_calculated_date": 'PreviousCalculatedDate',
        "fee_rule_basis": 'FeeRuleBasis',
        "fee_rule_currency_code": 'FeeRuleCurrencyCode',
        "fee_rule_currency_symbol": 'FeeRuleCurrencySymbol',
        "fee_rule_available_from": 'FeeRuleAvailableFrom',
        "fee_rule_available_to": 'FeeRuleAvailableTo',
        "fee_rule_locations": 'FeeRuleLocations',
        "fee_rule_tiers": 'FeeRuleTiers',
        "associated_accounts": 'AssociatedAccounts',
        "fee_rule_products": 'FeeRuleProducts'
    }

    _optionals = [
        'pricing_account_id',
        'pricing_account_number',
        'pricing_account_short_name',
        'pricing_account_full_name',
        'fee_rule_id',
        'fee_rule_description',
        'fee_rule_date_effective',
        'fee_rule_date_terminated',
        'bonus_paid_to',
        'bonus_paid_to_account_id',
        'bonus_paid_to_account_number',
        'bonus_paid_to_account_short_name',
        'bonus_paid_to_account_full_name',
        'frequency',
        'next_calculation_date',
        'previous_calculated_date',
        'fee_rule_basis',
        'fee_rule_currency_code',
        'fee_rule_currency_symbol',
        'fee_rule_available_from',
        'fee_rule_available_to',
        'fee_rule_locations',
        'fee_rule_tiers',
        'associated_accounts',
        'fee_rule_products',
    ]

    _nullables = [
        'pricing_account_id',
        'pricing_account_number',
        'pricing_account_short_name',
        'pricing_account_full_name',
        'fee_rule_id',
        'fee_rule_description',
        'fee_rule_date_effective',
        'fee_rule_date_terminated',
        'bonus_paid_to',
        'bonus_paid_to_account_id',
        'bonus_paid_to_account_number',
        'bonus_paid_to_account_short_name',
        'bonus_paid_to_account_full_name',
        'frequency',
        'next_calculation_date',
        'previous_calculated_date',
        'fee_rule_basis',
        'fee_rule_currency_code',
        'fee_rule_currency_symbol',
        'fee_rule_available_from',
        'fee_rule_available_to',
    ]

    def __init__(self,
                 pricing_account_id=APIHelper.SKIP,
                 pricing_account_number=APIHelper.SKIP,
                 pricing_account_short_name=APIHelper.SKIP,
                 pricing_account_full_name=APIHelper.SKIP,
                 fee_rule_id=APIHelper.SKIP,
                 fee_rule_description=APIHelper.SKIP,
                 fee_rule_date_effective=APIHelper.SKIP,
                 fee_rule_date_terminated=APIHelper.SKIP,
                 bonus_paid_to=APIHelper.SKIP,
                 bonus_paid_to_account_id=APIHelper.SKIP,
                 bonus_paid_to_account_number=APIHelper.SKIP,
                 bonus_paid_to_account_short_name=APIHelper.SKIP,
                 bonus_paid_to_account_full_name=APIHelper.SKIP,
                 frequency=APIHelper.SKIP,
                 next_calculation_date=APIHelper.SKIP,
                 previous_calculated_date=APIHelper.SKIP,
                 fee_rule_basis=APIHelper.SKIP,
                 fee_rule_currency_code=APIHelper.SKIP,
                 fee_rule_currency_symbol=APIHelper.SKIP,
                 fee_rule_available_from=APIHelper.SKIP,
                 fee_rule_available_to=APIHelper.SKIP,
                 fee_rule_locations=APIHelper.SKIP,
                 fee_rule_tiers=APIHelper.SKIP,
                 associated_accounts=APIHelper.SKIP,
                 fee_rule_products=APIHelper.SKIP):
        """Constructor for the BonusConfiguration class"""

        # Initialize members of the class
        if pricing_account_id is not APIHelper.SKIP:
            self.pricing_account_id = pricing_account_id 
        if pricing_account_number is not APIHelper.SKIP:
            self.pricing_account_number = pricing_account_number 
        if pricing_account_short_name is not APIHelper.SKIP:
            self.pricing_account_short_name = pricing_account_short_name 
        if pricing_account_full_name is not APIHelper.SKIP:
            self.pricing_account_full_name = pricing_account_full_name 
        if fee_rule_id is not APIHelper.SKIP:
            self.fee_rule_id = fee_rule_id 
        if fee_rule_description is not APIHelper.SKIP:
            self.fee_rule_description = fee_rule_description 
        if fee_rule_date_effective is not APIHelper.SKIP:
            self.fee_rule_date_effective = fee_rule_date_effective 
        if fee_rule_date_terminated is not APIHelper.SKIP:
            self.fee_rule_date_terminated = fee_rule_date_terminated 
        if bonus_paid_to is not APIHelper.SKIP:
            self.bonus_paid_to = bonus_paid_to 
        if bonus_paid_to_account_id is not APIHelper.SKIP:
            self.bonus_paid_to_account_id = bonus_paid_to_account_id 
        if bonus_paid_to_account_number is not APIHelper.SKIP:
            self.bonus_paid_to_account_number = bonus_paid_to_account_number 
        if bonus_paid_to_account_short_name is not APIHelper.SKIP:
            self.bonus_paid_to_account_short_name = bonus_paid_to_account_short_name 
        if bonus_paid_to_account_full_name is not APIHelper.SKIP:
            self.bonus_paid_to_account_full_name = bonus_paid_to_account_full_name 
        if frequency is not APIHelper.SKIP:
            self.frequency = frequency 
        if next_calculation_date is not APIHelper.SKIP:
            self.next_calculation_date = next_calculation_date 
        if previous_calculated_date is not APIHelper.SKIP:
            self.previous_calculated_date = previous_calculated_date 
        if fee_rule_basis is not APIHelper.SKIP:
            self.fee_rule_basis = fee_rule_basis 
        if fee_rule_currency_code is not APIHelper.SKIP:
            self.fee_rule_currency_code = fee_rule_currency_code 
        if fee_rule_currency_symbol is not APIHelper.SKIP:
            self.fee_rule_currency_symbol = fee_rule_currency_symbol 
        if fee_rule_available_from is not APIHelper.SKIP:
            self.fee_rule_available_from = fee_rule_available_from 
        if fee_rule_available_to is not APIHelper.SKIP:
            self.fee_rule_available_to = fee_rule_available_to 
        if fee_rule_locations is not APIHelper.SKIP:
            self.fee_rule_locations = fee_rule_locations 
        if fee_rule_tiers is not APIHelper.SKIP:
            self.fee_rule_tiers = fee_rule_tiers 
        if associated_accounts is not APIHelper.SKIP:
            self.associated_accounts = associated_accounts 
        if fee_rule_products is not APIHelper.SKIP:
            self.fee_rule_products = fee_rule_products 

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
        pricing_account_id = dictionary.get("PricingAccountId") if "PricingAccountId" in dictionary.keys() else APIHelper.SKIP
        pricing_account_number = dictionary.get("PricingAccountNumber") if "PricingAccountNumber" in dictionary.keys() else APIHelper.SKIP
        pricing_account_short_name = dictionary.get("PricingAccountShortName") if "PricingAccountShortName" in dictionary.keys() else APIHelper.SKIP
        pricing_account_full_name = dictionary.get("PricingAccountFullName") if "PricingAccountFullName" in dictionary.keys() else APIHelper.SKIP
        fee_rule_id = dictionary.get("FeeRuleId") if "FeeRuleId" in dictionary.keys() else APIHelper.SKIP
        fee_rule_description = dictionary.get("FeeRuleDescription") if "FeeRuleDescription" in dictionary.keys() else APIHelper.SKIP
        fee_rule_date_effective = dictionary.get("FeeRuleDateEffective") if "FeeRuleDateEffective" in dictionary.keys() else APIHelper.SKIP
        fee_rule_date_terminated = dictionary.get("FeeRuleDateTerminated") if "FeeRuleDateTerminated" in dictionary.keys() else APIHelper.SKIP
        bonus_paid_to = dictionary.get("BonusPaidTo") if "BonusPaidTo" in dictionary.keys() else APIHelper.SKIP
        bonus_paid_to_account_id = dictionary.get("BonusPaidToAccountId") if "BonusPaidToAccountId" in dictionary.keys() else APIHelper.SKIP
        bonus_paid_to_account_number = dictionary.get("BonusPaidToAccountNumber") if "BonusPaidToAccountNumber" in dictionary.keys() else APIHelper.SKIP
        bonus_paid_to_account_short_name = dictionary.get("BonusPaidToAccountShortName") if "BonusPaidToAccountShortName" in dictionary.keys() else APIHelper.SKIP
        bonus_paid_to_account_full_name = dictionary.get("BonusPaidToAccountFullName") if "BonusPaidToAccountFullName" in dictionary.keys() else APIHelper.SKIP
        frequency = dictionary.get("Frequency") if "Frequency" in dictionary.keys() else APIHelper.SKIP
        next_calculation_date = dictionary.get("NextCalculationDate") if "NextCalculationDate" in dictionary.keys() else APIHelper.SKIP
        previous_calculated_date = dictionary.get("PreviousCalculatedDate") if "PreviousCalculatedDate" in dictionary.keys() else APIHelper.SKIP
        fee_rule_basis = dictionary.get("FeeRuleBasis") if "FeeRuleBasis" in dictionary.keys() else APIHelper.SKIP
        fee_rule_currency_code = dictionary.get("FeeRuleCurrencyCode") if "FeeRuleCurrencyCode" in dictionary.keys() else APIHelper.SKIP
        fee_rule_currency_symbol = dictionary.get("FeeRuleCurrencySymbol") if "FeeRuleCurrencySymbol" in dictionary.keys() else APIHelper.SKIP
        fee_rule_available_from = dictionary.get("FeeRuleAvailableFrom") if "FeeRuleAvailableFrom" in dictionary.keys() else APIHelper.SKIP
        fee_rule_available_to = dictionary.get("FeeRuleAvailableTo") if "FeeRuleAvailableTo" in dictionary.keys() else APIHelper.SKIP
        fee_rule_locations = None
        if dictionary.get('FeeRuleLocations') is not None:
            fee_rule_locations = [FeeRuleLocation.from_dictionary(x) for x in dictionary.get('FeeRuleLocations')]
        else:
            fee_rule_locations = APIHelper.SKIP
        fee_rule_tiers = None
        if dictionary.get('FeeRuleTiers') is not None:
            fee_rule_tiers = [FeeRuleTier.from_dictionary(x) for x in dictionary.get('FeeRuleTiers')]
        else:
            fee_rule_tiers = APIHelper.SKIP
        associated_accounts = None
        if dictionary.get('AssociatedAccounts') is not None:
            associated_accounts = [AssociatedAccount.from_dictionary(x) for x in dictionary.get('AssociatedAccounts')]
        else:
            associated_accounts = APIHelper.SKIP
        fee_rule_products = None
        if dictionary.get('FeeRuleProducts') is not None:
            fee_rule_products = [FeeRuleProduct.from_dictionary(x) for x in dictionary.get('FeeRuleProducts')]
        else:
            fee_rule_products = APIHelper.SKIP
        # Return an object of this model
        return cls(pricing_account_id,
                   pricing_account_number,
                   pricing_account_short_name,
                   pricing_account_full_name,
                   fee_rule_id,
                   fee_rule_description,
                   fee_rule_date_effective,
                   fee_rule_date_terminated,
                   bonus_paid_to,
                   bonus_paid_to_account_id,
                   bonus_paid_to_account_number,
                   bonus_paid_to_account_short_name,
                   bonus_paid_to_account_full_name,
                   frequency,
                   next_calculation_date,
                   previous_calculated_date,
                   fee_rule_basis,
                   fee_rule_currency_code,
                   fee_rule_currency_symbol,
                   fee_rule_available_from,
                   fee_rule_available_to,
                   fee_rule_locations,
                   fee_rule_tiers,
                   associated_accounts,
                   fee_rule_products)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'pricing_account_id={(self.pricing_account_id if hasattr(self, "pricing_account_id") else None)!r}, '
                f'pricing_account_number={(self.pricing_account_number if hasattr(self, "pricing_account_number") else None)!r}, '
                f'pricing_account_short_name={(self.pricing_account_short_name if hasattr(self, "pricing_account_short_name") else None)!r}, '
                f'pricing_account_full_name={(self.pricing_account_full_name if hasattr(self, "pricing_account_full_name") else None)!r}, '
                f'fee_rule_id={(self.fee_rule_id if hasattr(self, "fee_rule_id") else None)!r}, '
                f'fee_rule_description={(self.fee_rule_description if hasattr(self, "fee_rule_description") else None)!r}, '
                f'fee_rule_date_effective={(self.fee_rule_date_effective if hasattr(self, "fee_rule_date_effective") else None)!r}, '
                f'fee_rule_date_terminated={(self.fee_rule_date_terminated if hasattr(self, "fee_rule_date_terminated") else None)!r}, '
                f'bonus_paid_to={(self.bonus_paid_to if hasattr(self, "bonus_paid_to") else None)!r}, '
                f'bonus_paid_to_account_id={(self.bonus_paid_to_account_id if hasattr(self, "bonus_paid_to_account_id") else None)!r}, '
                f'bonus_paid_to_account_number={(self.bonus_paid_to_account_number if hasattr(self, "bonus_paid_to_account_number") else None)!r}, '
                f'bonus_paid_to_account_short_name={(self.bonus_paid_to_account_short_name if hasattr(self, "bonus_paid_to_account_short_name") else None)!r}, '
                f'bonus_paid_to_account_full_name={(self.bonus_paid_to_account_full_name if hasattr(self, "bonus_paid_to_account_full_name") else None)!r}, '
                f'frequency={(self.frequency if hasattr(self, "frequency") else None)!r}, '
                f'next_calculation_date={(self.next_calculation_date if hasattr(self, "next_calculation_date") else None)!r}, '
                f'previous_calculated_date={(self.previous_calculated_date if hasattr(self, "previous_calculated_date") else None)!r}, '
                f'fee_rule_basis={(self.fee_rule_basis if hasattr(self, "fee_rule_basis") else None)!r}, '
                f'fee_rule_currency_code={(self.fee_rule_currency_code if hasattr(self, "fee_rule_currency_code") else None)!r}, '
                f'fee_rule_currency_symbol={(self.fee_rule_currency_symbol if hasattr(self, "fee_rule_currency_symbol") else None)!r}, '
                f'fee_rule_available_from={(self.fee_rule_available_from if hasattr(self, "fee_rule_available_from") else None)!r}, '
                f'fee_rule_available_to={(self.fee_rule_available_to if hasattr(self, "fee_rule_available_to") else None)!r}, '
                f'fee_rule_locations={(self.fee_rule_locations if hasattr(self, "fee_rule_locations") else None)!r}, '
                f'fee_rule_tiers={(self.fee_rule_tiers if hasattr(self, "fee_rule_tiers") else None)!r}, '
                f'associated_accounts={(self.associated_accounts if hasattr(self, "associated_accounts") else None)!r}, '
                f'fee_rule_products={(self.fee_rule_products if hasattr(self, "fee_rule_products") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'pricing_account_id={(self.pricing_account_id if hasattr(self, "pricing_account_id") else None)!s}, '
                f'pricing_account_number={(self.pricing_account_number if hasattr(self, "pricing_account_number") else None)!s}, '
                f'pricing_account_short_name={(self.pricing_account_short_name if hasattr(self, "pricing_account_short_name") else None)!s}, '
                f'pricing_account_full_name={(self.pricing_account_full_name if hasattr(self, "pricing_account_full_name") else None)!s}, '
                f'fee_rule_id={(self.fee_rule_id if hasattr(self, "fee_rule_id") else None)!s}, '
                f'fee_rule_description={(self.fee_rule_description if hasattr(self, "fee_rule_description") else None)!s}, '
                f'fee_rule_date_effective={(self.fee_rule_date_effective if hasattr(self, "fee_rule_date_effective") else None)!s}, '
                f'fee_rule_date_terminated={(self.fee_rule_date_terminated if hasattr(self, "fee_rule_date_terminated") else None)!s}, '
                f'bonus_paid_to={(self.bonus_paid_to if hasattr(self, "bonus_paid_to") else None)!s}, '
                f'bonus_paid_to_account_id={(self.bonus_paid_to_account_id if hasattr(self, "bonus_paid_to_account_id") else None)!s}, '
                f'bonus_paid_to_account_number={(self.bonus_paid_to_account_number if hasattr(self, "bonus_paid_to_account_number") else None)!s}, '
                f'bonus_paid_to_account_short_name={(self.bonus_paid_to_account_short_name if hasattr(self, "bonus_paid_to_account_short_name") else None)!s}, '
                f'bonus_paid_to_account_full_name={(self.bonus_paid_to_account_full_name if hasattr(self, "bonus_paid_to_account_full_name") else None)!s}, '
                f'frequency={(self.frequency if hasattr(self, "frequency") else None)!s}, '
                f'next_calculation_date={(self.next_calculation_date if hasattr(self, "next_calculation_date") else None)!s}, '
                f'previous_calculated_date={(self.previous_calculated_date if hasattr(self, "previous_calculated_date") else None)!s}, '
                f'fee_rule_basis={(self.fee_rule_basis if hasattr(self, "fee_rule_basis") else None)!s}, '
                f'fee_rule_currency_code={(self.fee_rule_currency_code if hasattr(self, "fee_rule_currency_code") else None)!s}, '
                f'fee_rule_currency_symbol={(self.fee_rule_currency_symbol if hasattr(self, "fee_rule_currency_symbol") else None)!s}, '
                f'fee_rule_available_from={(self.fee_rule_available_from if hasattr(self, "fee_rule_available_from") else None)!s}, '
                f'fee_rule_available_to={(self.fee_rule_available_to if hasattr(self, "fee_rule_available_to") else None)!s}, '
                f'fee_rule_locations={(self.fee_rule_locations if hasattr(self, "fee_rule_locations") else None)!s}, '
                f'fee_rule_tiers={(self.fee_rule_tiers if hasattr(self, "fee_rule_tiers") else None)!s}, '
                f'associated_accounts={(self.associated_accounts if hasattr(self, "associated_accounts") else None)!s}, '
                f'fee_rule_products={(self.fee_rule_products if hasattr(self, "fee_rule_products") else None)!s})')
