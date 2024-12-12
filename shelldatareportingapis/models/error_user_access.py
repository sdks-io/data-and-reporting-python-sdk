# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper
from shelldatareportingapis.models.error_user_access_error import ErrorUserAccessError


class ErrorUserAccess(object):

    """Implementation of the 'ErrorUserAccess' model.

    TODO: type model description here.

    Attributes:
        error (ErrorUserAccessError): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error": 'Error'
    }

    _optionals = [
        'error',
    ]

    def __init__(self,
                 error=APIHelper.SKIP):
        """Constructor for the ErrorUserAccess class"""

        # Initialize members of the class
        if error is not APIHelper.SKIP:
            self.error = error 

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
        error = ErrorUserAccessError.from_dictionary(dictionary.get('Error')) if 'Error' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(error)
