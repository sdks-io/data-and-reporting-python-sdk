# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper
from shelldatareportingapis.models.audit_response_audits_items import AuditResponseAuditsItems
from shelldatareportingapis.models.error_status import ErrorStatus


class AuditResponse(object):

    """Implementation of the 'AuditResponse' model.

    TODO: type model description here.

    Attributes:
        audits (List[AuditResponseAuditsItems]): TODO: type description here.
        current_page (int): Current Page
        row_count (int): Total row count matched for the given input criteria
        total_pages (int): Calculated page count based on page size from the
            incoming API request and total number of rows matched for the
            given input criteria
        error (ErrorStatus): TODO: type description here.
        request_id (str): API RequestId

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "audits": 'Audits',
        "current_page": 'CurrentPage',
        "row_count": 'RowCount',
        "total_pages": 'TotalPages',
        "error": 'Error',
        "request_id": 'RequestId'
    }

    _optionals = [
        'audits',
        'current_page',
        'row_count',
        'total_pages',
        'error',
        'request_id',
    ]

    def __init__(self,
                 audits=APIHelper.SKIP,
                 current_page=APIHelper.SKIP,
                 row_count=APIHelper.SKIP,
                 total_pages=APIHelper.SKIP,
                 error=APIHelper.SKIP,
                 request_id=APIHelper.SKIP):
        """Constructor for the AuditResponse class"""

        # Initialize members of the class
        if audits is not APIHelper.SKIP:
            self.audits = audits 
        if current_page is not APIHelper.SKIP:
            self.current_page = current_page 
        if row_count is not APIHelper.SKIP:
            self.row_count = row_count 
        if total_pages is not APIHelper.SKIP:
            self.total_pages = total_pages 
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
        audits = None
        if dictionary.get('Audits') is not None:
            audits = [AuditResponseAuditsItems.from_dictionary(x) for x in dictionary.get('Audits')]
        else:
            audits = APIHelper.SKIP
        current_page = dictionary.get("CurrentPage") if dictionary.get("CurrentPage") else APIHelper.SKIP
        row_count = dictionary.get("RowCount") if dictionary.get("RowCount") else APIHelper.SKIP
        total_pages = dictionary.get("TotalPages") if dictionary.get("TotalPages") else APIHelper.SKIP
        error = ErrorStatus.from_dictionary(dictionary.get('Error')) if 'Error' in dictionary.keys() else APIHelper.SKIP
        request_id = dictionary.get("RequestId") if dictionary.get("RequestId") else APIHelper.SKIP
        # Return an object of this model
        return cls(audits,
                   current_page,
                   row_count,
                   total_pages,
                   error,
                   request_id)
