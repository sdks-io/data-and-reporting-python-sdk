# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper


class ErrorDetails(object):

    """Implementation of the 'ErrorDetails' model.

    Attributes:
        code (str): Error code representing the error encountered
        title (str): Error type description
        detail (str): Detailed inforamtion about the error
        additional_info (Dict[str, str]): Applicable when more details related
            to error to be returned

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": 'Code',
        "title": 'Title',
        "detail": 'Detail',
        "additional_info": 'AdditionalInfo'
    }

    _optionals = [
        'code',
        'title',
        'detail',
        'additional_info',
    ]

    def __init__(self,
                 code=APIHelper.SKIP,
                 title=APIHelper.SKIP,
                 detail=APIHelper.SKIP,
                 additional_info=APIHelper.SKIP):
        """Constructor for the ErrorDetails class"""

        # Initialize members of the class
        if code is not APIHelper.SKIP:
            self.code = code 
        if title is not APIHelper.SKIP:
            self.title = title 
        if detail is not APIHelper.SKIP:
            self.detail = detail 
        if additional_info is not APIHelper.SKIP:
            self.additional_info = additional_info 

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
        code = dictionary.get("Code") if dictionary.get("Code") else APIHelper.SKIP
        title = dictionary.get("Title") if dictionary.get("Title") else APIHelper.SKIP
        detail = dictionary.get("Detail") if dictionary.get("Detail") else APIHelper.SKIP
        additional_info = dictionary.get("AdditionalInfo") if dictionary.get("AdditionalInfo") else APIHelper.SKIP
        # Return an object of this model
        return cls(code,
                   title,
                   detail,
                   additional_info)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'code={(self.code if hasattr(self, "code") else None)!r}, '
                f'title={(self.title if hasattr(self, "title") else None)!r}, '
                f'detail={(self.detail if hasattr(self, "detail") else None)!r}, '
                f'additional_info={(self.additional_info if hasattr(self, "additional_info") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'code={(self.code if hasattr(self, "code") else None)!s}, '
                f'title={(self.title if hasattr(self, "title") else None)!s}, '
                f'detail={(self.detail if hasattr(self, "detail") else None)!s}, '
                f'additional_info={(self.additional_info if hasattr(self, "additional_info") else None)!s})')
