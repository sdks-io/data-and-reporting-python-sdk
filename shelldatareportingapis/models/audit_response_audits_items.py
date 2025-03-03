# -*- coding: utf-8 -*-

"""
shelldatareportingapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shelldatareportingapis.api_helper import APIHelper


class AuditResponseAuditsItems(object):

    """Implementation of the 'AuditResponseAuditsItems' model.

    Attributes:
        account_id (int): Account id of the customer. It will be the source
            account id in case of “Fund Transfer
        account_number (str): Account number of the customer. It will be the
            source account number in case of “Fund Transfer”
        additional_information_1 (str): Additional information in the request.
        additional_information_2 (str): Additional information in the request.
        additional_information_3 (str): Additional information in the request.
        additional_information_4 (str): Additional information in the request.
        additional_information_5 (str): Additional information in the request.
        additional_information_6 (str): Additional information in the request.
        additional_information_7 (str): Additional information in the request.
        additional_information_8 (str): Additional information in the request.
        additional_information_9 (str): Additional information in the request.
        card_group_id (int): Additional information in the request.
        card_group_name (str): Card group name in the request.
        card_id (int): Card Id in the request
        col_co_code (int): Collecting company code of the customer
        col_co_id (int): Collecting company id of the customer.
        error_code (str): Error code of the request
        error_string (str): Error description of the request
        global_request_id (str): Global unique request reference provided by
            client application.
        pan (str): PAN in the request. If Mask PAN is enabled at Microservices
            configuration then all digits of the PAN, except the last 6
            digits, will be masked.
        payer_id (int): Payer id of the customer.
        payer_number (str): Payer number of the customer.
        processed_on (str): Request processed date.   Format: yyyyMMdd HH:mm:
            ss
        requested_by (str): vUUID of the user who submitted this request. It
            will be the UUID of the Driver in the case of
            “MobilePaymentRegistration”
        requested_operation (str): User requested operation.   Possible
            values:  •    OrderCard  •    CreateCardGroup  •    PINReminder  •
            MoveCard  •    UpdateCardStatus  •    UpdateCardGroup  •   
            AutoRenew  •    BulkCardOrder  •    BulkCardBlock  •   
            BulkCardOrderMultiAccount  •    MobilePaymentRegistration  •   
            UpdateCompanyInfo  •    BCOSummary  •    BCOMultiAccountSummary  •
            BCBSummary  •    FundTransfer  •    DeliveryAddressUpdate
        request_reference (int): Reference number for the requested operation.
        request_type (str): Request type initiated under the requested
            operation.   Possible values:  •    OrderCard  •   
            CreateCardGroup  •    PINReminder  •    MoveCard  •   
            UpdateCardStatus  •    UpdateCardGroup  •    AutoRenew  •   
            BulkCardOrder  •    BulkCardBlock  •    BulkCardOrderMultiAccount 
            •    MobilePaymentRegistration  •    UpdateCompanyInfo  •   
            BCOSummary  •    BCOMultiAccountSummary  •    BCBSummary  •   
            FundTransfer  •    DeliveryAddressUpdate
        status (str): Status of the request. Possible values: •    Success •  
            Failed •    InProgress •    Submitted •    Rejected •   
            PendingApproval •    MailedToCSC
        submitted_on (str): Request submitted date.   Format: yyyyMMdd HH:mm:
            ss
        sub_request_reference (int): Reference number for the individual
            request type.
        user_display_name (str): Display name of the user who submitted this
            request. It will be the Display Name of the Driver in the case of
            “MobilePaymentRegistration” in the below format:

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_id": 'AccountId',
        "account_number": 'AccountNumber',
        "additional_information_1": 'AdditionalInformation1',
        "additional_information_2": 'AdditionalInformation2',
        "additional_information_3": 'AdditionalInformation3',
        "additional_information_4": 'AdditionalInformation4',
        "additional_information_5": 'AdditionalInformation5',
        "additional_information_6": 'AdditionalInformation6',
        "additional_information_7": 'AdditionalInformation7',
        "additional_information_8": 'AdditionalInformation8',
        "additional_information_9": 'AdditionalInformation9',
        "card_group_id": 'CardGroupId',
        "card_group_name": 'CardGroupName',
        "card_id": 'CardId',
        "col_co_code": 'ColCoCode',
        "col_co_id": 'ColCoId',
        "error_code": 'ErrorCode',
        "error_string": 'ErrorString',
        "global_request_id": 'GlobalRequestID',
        "pan": 'PAN',
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber',
        "processed_on": 'ProcessedOn',
        "requested_by": 'RequestedBy',
        "requested_operation": 'RequestedOperation',
        "request_reference": 'RequestReference',
        "request_type": 'RequestType',
        "status": 'Status',
        "submitted_on": 'SubmittedOn',
        "sub_request_reference": 'SubRequestReference',
        "user_display_name": 'UserDisplayName'
    }

    _optionals = [
        'account_id',
        'account_number',
        'additional_information_1',
        'additional_information_2',
        'additional_information_3',
        'additional_information_4',
        'additional_information_5',
        'additional_information_6',
        'additional_information_7',
        'additional_information_8',
        'additional_information_9',
        'card_group_id',
        'card_group_name',
        'card_id',
        'col_co_code',
        'col_co_id',
        'error_code',
        'error_string',
        'global_request_id',
        'pan',
        'payer_id',
        'payer_number',
        'processed_on',
        'requested_by',
        'requested_operation',
        'request_reference',
        'request_type',
        'status',
        'submitted_on',
        'sub_request_reference',
        'user_display_name',
    ]

    _nullables = [
        'account_id',
        'account_number',
        'additional_information_1',
        'additional_information_2',
        'additional_information_3',
        'additional_information_4',
        'additional_information_5',
        'additional_information_6',
        'additional_information_7',
        'additional_information_8',
        'additional_information_9',
        'card_group_id',
        'card_group_name',
        'card_id',
        'col_co_code',
        'col_co_id',
        'error_string',
        'global_request_id',
        'pan',
        'payer_id',
        'payer_number',
        'processed_on',
        'requested_by',
        'requested_operation',
        'request_reference',
        'request_type',
        'status',
        'submitted_on',
        'sub_request_reference',
        'user_display_name',
    ]

    def __init__(self,
                 account_id=APIHelper.SKIP,
                 account_number=APIHelper.SKIP,
                 additional_information_1=APIHelper.SKIP,
                 additional_information_2=APIHelper.SKIP,
                 additional_information_3=APIHelper.SKIP,
                 additional_information_4=APIHelper.SKIP,
                 additional_information_5=APIHelper.SKIP,
                 additional_information_6=APIHelper.SKIP,
                 additional_information_7=APIHelper.SKIP,
                 additional_information_8=APIHelper.SKIP,
                 additional_information_9=APIHelper.SKIP,
                 card_group_id=APIHelper.SKIP,
                 card_group_name=APIHelper.SKIP,
                 card_id=APIHelper.SKIP,
                 col_co_code=APIHelper.SKIP,
                 col_co_id=APIHelper.SKIP,
                 error_code=APIHelper.SKIP,
                 error_string=APIHelper.SKIP,
                 global_request_id=APIHelper.SKIP,
                 pan=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 processed_on=APIHelper.SKIP,
                 requested_by=APIHelper.SKIP,
                 requested_operation=APIHelper.SKIP,
                 request_reference=APIHelper.SKIP,
                 request_type=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 submitted_on=APIHelper.SKIP,
                 sub_request_reference=APIHelper.SKIP,
                 user_display_name=APIHelper.SKIP):
        """Constructor for the AuditResponseAuditsItems class"""

        # Initialize members of the class
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if additional_information_1 is not APIHelper.SKIP:
            self.additional_information_1 = additional_information_1 
        if additional_information_2 is not APIHelper.SKIP:
            self.additional_information_2 = additional_information_2 
        if additional_information_3 is not APIHelper.SKIP:
            self.additional_information_3 = additional_information_3 
        if additional_information_4 is not APIHelper.SKIP:
            self.additional_information_4 = additional_information_4 
        if additional_information_5 is not APIHelper.SKIP:
            self.additional_information_5 = additional_information_5 
        if additional_information_6 is not APIHelper.SKIP:
            self.additional_information_6 = additional_information_6 
        if additional_information_7 is not APIHelper.SKIP:
            self.additional_information_7 = additional_information_7 
        if additional_information_8 is not APIHelper.SKIP:
            self.additional_information_8 = additional_information_8 
        if additional_information_9 is not APIHelper.SKIP:
            self.additional_information_9 = additional_information_9 
        if card_group_id is not APIHelper.SKIP:
            self.card_group_id = card_group_id 
        if card_group_name is not APIHelper.SKIP:
            self.card_group_name = card_group_name 
        if card_id is not APIHelper.SKIP:
            self.card_id = card_id 
        if col_co_code is not APIHelper.SKIP:
            self.col_co_code = col_co_code 
        if col_co_id is not APIHelper.SKIP:
            self.col_co_id = col_co_id 
        if error_code is not APIHelper.SKIP:
            self.error_code = error_code 
        if error_string is not APIHelper.SKIP:
            self.error_string = error_string 
        if global_request_id is not APIHelper.SKIP:
            self.global_request_id = global_request_id 
        if pan is not APIHelper.SKIP:
            self.pan = pan 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 
        if processed_on is not APIHelper.SKIP:
            self.processed_on = processed_on 
        if requested_by is not APIHelper.SKIP:
            self.requested_by = requested_by 
        if requested_operation is not APIHelper.SKIP:
            self.requested_operation = requested_operation 
        if request_reference is not APIHelper.SKIP:
            self.request_reference = request_reference 
        if request_type is not APIHelper.SKIP:
            self.request_type = request_type 
        if status is not APIHelper.SKIP:
            self.status = status 
        if submitted_on is not APIHelper.SKIP:
            self.submitted_on = submitted_on 
        if sub_request_reference is not APIHelper.SKIP:
            self.sub_request_reference = sub_request_reference 
        if user_display_name is not APIHelper.SKIP:
            self.user_display_name = user_display_name 

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
        account_id = dictionary.get("AccountId") if "AccountId" in dictionary.keys() else APIHelper.SKIP
        account_number = dictionary.get("AccountNumber") if "AccountNumber" in dictionary.keys() else APIHelper.SKIP
        additional_information_1 = dictionary.get("AdditionalInformation1") if "AdditionalInformation1" in dictionary.keys() else APIHelper.SKIP
        additional_information_2 = dictionary.get("AdditionalInformation2") if "AdditionalInformation2" in dictionary.keys() else APIHelper.SKIP
        additional_information_3 = dictionary.get("AdditionalInformation3") if "AdditionalInformation3" in dictionary.keys() else APIHelper.SKIP
        additional_information_4 = dictionary.get("AdditionalInformation4") if "AdditionalInformation4" in dictionary.keys() else APIHelper.SKIP
        additional_information_5 = dictionary.get("AdditionalInformation5") if "AdditionalInformation5" in dictionary.keys() else APIHelper.SKIP
        additional_information_6 = dictionary.get("AdditionalInformation6") if "AdditionalInformation6" in dictionary.keys() else APIHelper.SKIP
        additional_information_7 = dictionary.get("AdditionalInformation7") if "AdditionalInformation7" in dictionary.keys() else APIHelper.SKIP
        additional_information_8 = dictionary.get("AdditionalInformation8") if "AdditionalInformation8" in dictionary.keys() else APIHelper.SKIP
        additional_information_9 = dictionary.get("AdditionalInformation9") if "AdditionalInformation9" in dictionary.keys() else APIHelper.SKIP
        card_group_id = dictionary.get("CardGroupId") if "CardGroupId" in dictionary.keys() else APIHelper.SKIP
        card_group_name = dictionary.get("CardGroupName") if "CardGroupName" in dictionary.keys() else APIHelper.SKIP
        card_id = dictionary.get("CardId") if "CardId" in dictionary.keys() else APIHelper.SKIP
        col_co_code = dictionary.get("ColCoCode") if "ColCoCode" in dictionary.keys() else APIHelper.SKIP
        col_co_id = dictionary.get("ColCoId") if "ColCoId" in dictionary.keys() else APIHelper.SKIP
        error_code = dictionary.get("ErrorCode") if dictionary.get("ErrorCode") else APIHelper.SKIP
        error_string = dictionary.get("ErrorString") if "ErrorString" in dictionary.keys() else APIHelper.SKIP
        global_request_id = dictionary.get("GlobalRequestID") if "GlobalRequestID" in dictionary.keys() else APIHelper.SKIP
        pan = dictionary.get("PAN") if "PAN" in dictionary.keys() else APIHelper.SKIP
        payer_id = dictionary.get("PayerId") if "PayerId" in dictionary.keys() else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if "PayerNumber" in dictionary.keys() else APIHelper.SKIP
        processed_on = dictionary.get("ProcessedOn") if "ProcessedOn" in dictionary.keys() else APIHelper.SKIP
        requested_by = dictionary.get("RequestedBy") if "RequestedBy" in dictionary.keys() else APIHelper.SKIP
        requested_operation = dictionary.get("RequestedOperation") if "RequestedOperation" in dictionary.keys() else APIHelper.SKIP
        request_reference = dictionary.get("RequestReference") if "RequestReference" in dictionary.keys() else APIHelper.SKIP
        request_type = dictionary.get("RequestType") if "RequestType" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("Status") if "Status" in dictionary.keys() else APIHelper.SKIP
        submitted_on = dictionary.get("SubmittedOn") if "SubmittedOn" in dictionary.keys() else APIHelper.SKIP
        sub_request_reference = dictionary.get("SubRequestReference") if "SubRequestReference" in dictionary.keys() else APIHelper.SKIP
        user_display_name = dictionary.get("UserDisplayName") if "UserDisplayName" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(account_id,
                   account_number,
                   additional_information_1,
                   additional_information_2,
                   additional_information_3,
                   additional_information_4,
                   additional_information_5,
                   additional_information_6,
                   additional_information_7,
                   additional_information_8,
                   additional_information_9,
                   card_group_id,
                   card_group_name,
                   card_id,
                   col_co_code,
                   col_co_id,
                   error_code,
                   error_string,
                   global_request_id,
                   pan,
                   payer_id,
                   payer_number,
                   processed_on,
                   requested_by,
                   requested_operation,
                   request_reference,
                   request_type,
                   status,
                   submitted_on,
                   sub_request_reference,
                   user_display_name)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!r}, '
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!r}, '
                f'additional_information_1={(self.additional_information_1 if hasattr(self, "additional_information_1") else None)!r}, '
                f'additional_information_2={(self.additional_information_2 if hasattr(self, "additional_information_2") else None)!r}, '
                f'additional_information_3={(self.additional_information_3 if hasattr(self, "additional_information_3") else None)!r}, '
                f'additional_information_4={(self.additional_information_4 if hasattr(self, "additional_information_4") else None)!r}, '
                f'additional_information_5={(self.additional_information_5 if hasattr(self, "additional_information_5") else None)!r}, '
                f'additional_information_6={(self.additional_information_6 if hasattr(self, "additional_information_6") else None)!r}, '
                f'additional_information_7={(self.additional_information_7 if hasattr(self, "additional_information_7") else None)!r}, '
                f'additional_information_8={(self.additional_information_8 if hasattr(self, "additional_information_8") else None)!r}, '
                f'additional_information_9={(self.additional_information_9 if hasattr(self, "additional_information_9") else None)!r}, '
                f'card_group_id={(self.card_group_id if hasattr(self, "card_group_id") else None)!r}, '
                f'card_group_name={(self.card_group_name if hasattr(self, "card_group_name") else None)!r}, '
                f'card_id={(self.card_id if hasattr(self, "card_id") else None)!r}, '
                f'col_co_code={(self.col_co_code if hasattr(self, "col_co_code") else None)!r}, '
                f'col_co_id={(self.col_co_id if hasattr(self, "col_co_id") else None)!r}, '
                f'error_code={(self.error_code if hasattr(self, "error_code") else None)!r}, '
                f'error_string={(self.error_string if hasattr(self, "error_string") else None)!r}, '
                f'global_request_id={(self.global_request_id if hasattr(self, "global_request_id") else None)!r}, '
                f'pan={(self.pan if hasattr(self, "pan") else None)!r}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!r}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!r}, '
                f'processed_on={(self.processed_on if hasattr(self, "processed_on") else None)!r}, '
                f'requested_by={(self.requested_by if hasattr(self, "requested_by") else None)!r}, '
                f'requested_operation={(self.requested_operation if hasattr(self, "requested_operation") else None)!r}, '
                f'request_reference={(self.request_reference if hasattr(self, "request_reference") else None)!r}, '
                f'request_type={(self.request_type if hasattr(self, "request_type") else None)!r}, '
                f'status={(self.status if hasattr(self, "status") else None)!r}, '
                f'submitted_on={(self.submitted_on if hasattr(self, "submitted_on") else None)!r}, '
                f'sub_request_reference={(self.sub_request_reference if hasattr(self, "sub_request_reference") else None)!r}, '
                f'user_display_name={(self.user_display_name if hasattr(self, "user_display_name") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!s}, '
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!s}, '
                f'additional_information_1={(self.additional_information_1 if hasattr(self, "additional_information_1") else None)!s}, '
                f'additional_information_2={(self.additional_information_2 if hasattr(self, "additional_information_2") else None)!s}, '
                f'additional_information_3={(self.additional_information_3 if hasattr(self, "additional_information_3") else None)!s}, '
                f'additional_information_4={(self.additional_information_4 if hasattr(self, "additional_information_4") else None)!s}, '
                f'additional_information_5={(self.additional_information_5 if hasattr(self, "additional_information_5") else None)!s}, '
                f'additional_information_6={(self.additional_information_6 if hasattr(self, "additional_information_6") else None)!s}, '
                f'additional_information_7={(self.additional_information_7 if hasattr(self, "additional_information_7") else None)!s}, '
                f'additional_information_8={(self.additional_information_8 if hasattr(self, "additional_information_8") else None)!s}, '
                f'additional_information_9={(self.additional_information_9 if hasattr(self, "additional_information_9") else None)!s}, '
                f'card_group_id={(self.card_group_id if hasattr(self, "card_group_id") else None)!s}, '
                f'card_group_name={(self.card_group_name if hasattr(self, "card_group_name") else None)!s}, '
                f'card_id={(self.card_id if hasattr(self, "card_id") else None)!s}, '
                f'col_co_code={(self.col_co_code if hasattr(self, "col_co_code") else None)!s}, '
                f'col_co_id={(self.col_co_id if hasattr(self, "col_co_id") else None)!s}, '
                f'error_code={(self.error_code if hasattr(self, "error_code") else None)!s}, '
                f'error_string={(self.error_string if hasattr(self, "error_string") else None)!s}, '
                f'global_request_id={(self.global_request_id if hasattr(self, "global_request_id") else None)!s}, '
                f'pan={(self.pan if hasattr(self, "pan") else None)!s}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!s}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!s}, '
                f'processed_on={(self.processed_on if hasattr(self, "processed_on") else None)!s}, '
                f'requested_by={(self.requested_by if hasattr(self, "requested_by") else None)!s}, '
                f'requested_operation={(self.requested_operation if hasattr(self, "requested_operation") else None)!s}, '
                f'request_reference={(self.request_reference if hasattr(self, "request_reference") else None)!s}, '
                f'request_type={(self.request_type if hasattr(self, "request_type") else None)!s}, '
                f'status={(self.status if hasattr(self, "status") else None)!s}, '
                f'submitted_on={(self.submitted_on if hasattr(self, "submitted_on") else None)!s}, '
                f'sub_request_reference={(self.sub_request_reference if hasattr(self, "sub_request_reference") else None)!s}, '
                f'user_display_name={(self.user_display_name if hasattr(self, "user_display_name") else None)!s})')
