# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper
from shelldatareportingapis.models.bonus_configuration import BonusConfiguration
from shelldatareportingapis.models.bonus_history import BonusHistory
from shelldatareportingapis.models.current_volume import CurrentVolume
from shelldatareportingapis.models.error_status import ErrorStatus


class VolumeBasedBonusResponse(object):

    """Implementation of the 'VolumeBasedBonusResponse' model.

    TODO: type model description here.

    Attributes:
        configuration (List[BonusConfiguration]): TODO: type description here.
        current_period_consumption (List[CurrentVolume]): TODO: type
            description here.
        historical_bonus_paid (List[BonusHistory]): TODO: type description
            here.
        error (ErrorStatus): TODO: type description here.
        request_id (str): API Request Id

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "configuration": 'Configuration',
        "current_period_consumption": 'CurrentPeriodConsumption',
        "historical_bonus_paid": 'HistoricalBonusPaid',
        "error": 'Error',
        "request_id": 'RequestId'
    }

    _optionals = [
        'configuration',
        'current_period_consumption',
        'historical_bonus_paid',
        'error',
        'request_id',
    ]

    def __init__(self,
                 configuration=APIHelper.SKIP,
                 current_period_consumption=APIHelper.SKIP,
                 historical_bonus_paid=APIHelper.SKIP,
                 error=APIHelper.SKIP,
                 request_id=APIHelper.SKIP):
        """Constructor for the VolumeBasedBonusResponse class"""

        # Initialize members of the class
        if configuration is not APIHelper.SKIP:
            self.configuration = configuration 
        if current_period_consumption is not APIHelper.SKIP:
            self.current_period_consumption = current_period_consumption 
        if historical_bonus_paid is not APIHelper.SKIP:
            self.historical_bonus_paid = historical_bonus_paid 
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
        configuration = None
        if dictionary.get('Configuration') is not None:
            configuration = [BonusConfiguration.from_dictionary(x) for x in dictionary.get('Configuration')]
        else:
            configuration = APIHelper.SKIP
        current_period_consumption = None
        if dictionary.get('CurrentPeriodConsumption') is not None:
            current_period_consumption = [CurrentVolume.from_dictionary(x) for x in dictionary.get('CurrentPeriodConsumption')]
        else:
            current_period_consumption = APIHelper.SKIP
        historical_bonus_paid = None
        if dictionary.get('HistoricalBonusPaid') is not None:
            historical_bonus_paid = [BonusHistory.from_dictionary(x) for x in dictionary.get('HistoricalBonusPaid')]
        else:
            historical_bonus_paid = APIHelper.SKIP
        error = ErrorStatus.from_dictionary(dictionary.get('Error')) if 'Error' in dictionary.keys() else APIHelper.SKIP
        request_id = dictionary.get("RequestId") if dictionary.get("RequestId") else APIHelper.SKIP
        # Return an object of this model
        return cls(configuration,
                   current_period_consumption,
                   historical_bonus_paid,
                   error,
                   request_id)
