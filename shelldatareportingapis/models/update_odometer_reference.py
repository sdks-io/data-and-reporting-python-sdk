# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper


class UpdateOdometerReference(object):

    """Implementation of the 'UpdateOdometerReference' model.

    TODO: type model description here.

    Attributes:
        sales_item_id (int): SalesItemId of input parameter
        update_odometer_reference_id (int): Reference number for each
            individual update odometer reference.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "sales_item_id": 'SalesItemId',
        "update_odometer_reference_id": 'UpdateOdometerReferenceId'
    }

    _optionals = [
        'sales_item_id',
        'update_odometer_reference_id',
    ]

    _nullables = [
        'sales_item_id',
        'update_odometer_reference_id',
    ]

    def __init__(self,
                 sales_item_id=APIHelper.SKIP,
                 update_odometer_reference_id=APIHelper.SKIP):
        """Constructor for the UpdateOdometerReference class"""

        # Initialize members of the class
        if sales_item_id is not APIHelper.SKIP:
            self.sales_item_id = sales_item_id 
        if update_odometer_reference_id is not APIHelper.SKIP:
            self.update_odometer_reference_id = update_odometer_reference_id 

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
        sales_item_id = dictionary.get("SalesItemId") if "SalesItemId" in dictionary.keys() else APIHelper.SKIP
        update_odometer_reference_id = dictionary.get("UpdateOdometerReferenceId") if "UpdateOdometerReferenceId" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(sales_item_id,
                   update_odometer_reference_id)
