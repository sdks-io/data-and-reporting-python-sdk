# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper


class PricedTransactionItemsLocationItems(object):

    """Implementation of the 'PricedTransactionItemsLocationItems' model.

    TODO: type model description here.

    Attributes:
        latitude (str): Latitude for the Site Geographic Location  Example:
            37.4224764  Note: - The value could be null/blank for fees item.
        longitude (str): Longitude for the Site Geographic Location  Example:
            122.0842499  Note: - The value could be null/blank for fees item.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "latitude": 'Latitude',
        "longitude": 'Longitude'
    }

    _optionals = [
        'latitude',
        'longitude',
    ]

    _nullables = [
        'latitude',
        'longitude',
    ]

    def __init__(self,
                 latitude=APIHelper.SKIP,
                 longitude=APIHelper.SKIP):
        """Constructor for the PricedTransactionItemsLocationItems class"""

        # Initialize members of the class
        if latitude is not APIHelper.SKIP:
            self.latitude = latitude 
        if longitude is not APIHelper.SKIP:
            self.longitude = longitude 

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
        latitude = dictionary.get("Latitude") if "Latitude" in dictionary.keys() else APIHelper.SKIP
        longitude = dictionary.get("Longitude") if "Longitude" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(latitude,
                   longitude)
