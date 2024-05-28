# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper


class EIDDocument(object):

    """Implementation of the 'EIDDocument' model.

    TODO: type model description here.

    Attributes:
        document_id (int): Technical identifier for the EID file. Should not
            be stored in database as it is not guaranteed to stay unchanged
            over time.
        account_group_id (str): Account Group Id
        account_group_name (str): Account group name
        document_type (str): Document type.  Possible values:  • NAT
            (National)  • INT (International)
        document_format (str): Document format (CHORUS, DIFI etc.)
        document_date (str): Document date.  Example: 20170101
        number_of_invoices (int): Number of invoices
        file_size (int): Document size
        document_status (str): Document status.  Possible values:  • NEW  •
            VIEWED  • DOWNLOADED  • RESTORED
        document_name (str): Document file name.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "document_id": 'DocumentId',
        "account_group_id": 'AccountGroupId',
        "account_group_name": 'AccountGroupName',
        "document_type": 'DocumentType',
        "document_format": 'DocumentFormat',
        "document_date": 'DocumentDate',
        "number_of_invoices": 'NumberOfInvoices',
        "file_size": 'FileSize',
        "document_status": 'DocumentStatus',
        "document_name": 'DocumentName'
    }

    _optionals = [
        'document_id',
        'account_group_id',
        'account_group_name',
        'document_type',
        'document_format',
        'document_date',
        'number_of_invoices',
        'file_size',
        'document_status',
        'document_name',
    ]

    _nullables = [
        'document_id',
        'account_group_id',
        'account_group_name',
        'document_type',
        'document_format',
        'document_date',
        'number_of_invoices',
        'file_size',
        'document_status',
        'document_name',
    ]

    def __init__(self,
                 document_id=APIHelper.SKIP,
                 account_group_id=APIHelper.SKIP,
                 account_group_name=APIHelper.SKIP,
                 document_type=APIHelper.SKIP,
                 document_format=APIHelper.SKIP,
                 document_date=APIHelper.SKIP,
                 number_of_invoices=APIHelper.SKIP,
                 file_size=APIHelper.SKIP,
                 document_status=APIHelper.SKIP,
                 document_name=APIHelper.SKIP):
        """Constructor for the EIDDocument class"""

        # Initialize members of the class
        if document_id is not APIHelper.SKIP:
            self.document_id = document_id 
        if account_group_id is not APIHelper.SKIP:
            self.account_group_id = account_group_id 
        if account_group_name is not APIHelper.SKIP:
            self.account_group_name = account_group_name 
        if document_type is not APIHelper.SKIP:
            self.document_type = document_type 
        if document_format is not APIHelper.SKIP:
            self.document_format = document_format 
        if document_date is not APIHelper.SKIP:
            self.document_date = document_date 
        if number_of_invoices is not APIHelper.SKIP:
            self.number_of_invoices = number_of_invoices 
        if file_size is not APIHelper.SKIP:
            self.file_size = file_size 
        if document_status is not APIHelper.SKIP:
            self.document_status = document_status 
        if document_name is not APIHelper.SKIP:
            self.document_name = document_name 

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
        document_id = dictionary.get("DocumentId") if "DocumentId" in dictionary.keys() else APIHelper.SKIP
        account_group_id = dictionary.get("AccountGroupId") if "AccountGroupId" in dictionary.keys() else APIHelper.SKIP
        account_group_name = dictionary.get("AccountGroupName") if "AccountGroupName" in dictionary.keys() else APIHelper.SKIP
        document_type = dictionary.get("DocumentType") if "DocumentType" in dictionary.keys() else APIHelper.SKIP
        document_format = dictionary.get("DocumentFormat") if "DocumentFormat" in dictionary.keys() else APIHelper.SKIP
        document_date = dictionary.get("DocumentDate") if "DocumentDate" in dictionary.keys() else APIHelper.SKIP
        number_of_invoices = dictionary.get("NumberOfInvoices") if "NumberOfInvoices" in dictionary.keys() else APIHelper.SKIP
        file_size = dictionary.get("FileSize") if "FileSize" in dictionary.keys() else APIHelper.SKIP
        document_status = dictionary.get("DocumentStatus") if "DocumentStatus" in dictionary.keys() else APIHelper.SKIP
        document_name = dictionary.get("DocumentName") if "DocumentName" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(document_id,
                   account_group_id,
                   account_group_name,
                   document_type,
                   document_format,
                   document_date,
                   number_of_invoices,
                   file_size,
                   document_status,
                   document_name)
