
# Getting Started with Shell Data & Reporting APIs

## Introduction

The Shell Card Transaction and Invoice API is part of the Data and Reporting product suite, designed to provide secure and flexible access to transaction and invoice data related to Shell Cards.

### Authentication

- OAuth 2.0 Authentication.

### Architecture

- RESTful API design.
- All endpoints use the `POST` HTTP method for all operations including retrieval, creation, update, and deletion of resources.
- Requests and responses are encoded in JSON format.
- Standard HTTP status codes are used for response handling.

### Platform

- All resources are managed within the **Shell Card Platform**, which integrates multiple internal Shell systems for resource management.

### Features

- Flexible search parameters supported in the request body for data retrieval.
- Designed for integration with enterprise systems requiring Shell Card transaction and invoice data.

### Use Cases

- Retrieve detailed transaction history for Shell Cards.
- Access invoice summaries and line-item details.
- Integrate Shell Card financial data into internal reporting tools.

Go to the Shell Developer Portal: [https://developer.shell.com](https://developer.shell.com)

## Install the Package

The package is compatible with Python versions `3.7+`.
Install the package from PyPi using the following pip command:

```bash
pip install data-and-reporting-sdk==2.0.0
```

You can also view the package at:
https://pypi.python.org/pypi/data-and-reporting-sdk/2.0.0

## Test the SDK

You can test the generated SDK and the server with test cases. `unittest` is used as the testing framework and `pytest` is used as the test runner. You can run the tests as follows:

Navigate to the root directory of the SDK and run the following commands


pip install -r test-requirements.txt
pytest


## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/sdks-io/data-and-reporting-python-sdk/tree/2.0.0/doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| environment | `Environment` | The API environment. <br> **Default: `Environment.SIT`** |
| http_client_instance | `HttpClient` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 60** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| client_credentials_auth_credentials | [`ClientCredentialsAuthCredentials`](https://www.github.com/sdks-io/data-and-reporting-python-sdk/tree/2.0.0/doc/auth/oauth-2-client-credentials-grant.md) | The credential object for OAuth 2 Client Credentials Grant |

The API client can be initialized as follows:

```python
from shelldatareportingapis.configuration import Environment
from shelldatareportingapis.http.auth.o_auth_2 import ClientCredentialsAuthCredentials
from shelldatareportingapis.shelldatareportingapis_client import ShelldatareportingapisClient

client = ShelldatareportingapisClient(
    client_credentials_auth_credentials=ClientCredentialsAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret'
    ),
    environment=Environment.SIT
)
```

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| SIT | **Default** |
| Production | - |

## Authorization

This API uses the following authentication schemes.

* [`BearerToken (OAuth 2 Client Credentials Grant)`](https://www.github.com/sdks-io/data-and-reporting-python-sdk/tree/2.0.0/doc/auth/oauth-2-client-credentials-grant.md)

## List of APIs

* [Customer](https://www.github.com/sdks-io/data-and-reporting-python-sdk/tree/2.0.0/doc/controllers/customer.md)
* [Transaction](https://www.github.com/sdks-io/data-and-reporting-python-sdk/tree/2.0.0/doc/controllers/transaction.md)
* [Invoice](https://www.github.com/sdks-io/data-and-reporting-python-sdk/tree/2.0.0/doc/controllers/invoice.md)

## SDK Infrastructure

### HTTP

* [HttpResponse](https://www.github.com/sdks-io/data-and-reporting-python-sdk/tree/2.0.0/doc/http-response.md)
* [HttpRequest](https://www.github.com/sdks-io/data-and-reporting-python-sdk/tree/2.0.0/doc/http-request.md)

### Utilities

* [ApiHelper](https://www.github.com/sdks-io/data-and-reporting-python-sdk/tree/2.0.0/doc/api-helper.md)
* [HttpDateTime](https://www.github.com/sdks-io/data-and-reporting-python-sdk/tree/2.0.0/doc/http-date-time.md)
* [RFC3339DateTime](https://www.github.com/sdks-io/data-and-reporting-python-sdk/tree/2.0.0/doc/rfc3339-date-time.md)
* [UnixDateTime](https://www.github.com/sdks-io/data-and-reporting-python-sdk/tree/2.0.0/doc/unix-date-time.md)

