# cons3rt.TemplatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_virtualization_realm_templates**](TemplatesApi.md#list_virtualization_realm_templates) | **GET** /api/templates | List all Templates


# **list_virtualization_realm_templates**
> list[MinimalCons3rtTemplateData] list_virtualization_realm_templates(virtualization_realm_id, include_registrations=include_registrations, include_subscriptions=include_subscriptions)

List all Templates

Returns a collection of the user's available Templates matching a specified query.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from __future__ import print_function
import time
import cons3rt
from cons3rt.rest import ApiException
from pprint import pprint
# Configure API key authorization: APIKeyHeader
configuration.api_key['token'] = 'YOUR_VALUE'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Configure API key authorization: Username
configuration.api_key['username'] = 'YOUR_VALUE'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['username'] = 'Bearer'

# Using a client certificate for authentication is required in some cases.
# To use a "soft-token" such as an ECA, provide the path the PEM encoded
# version of the certificate
configuration.cert_file='/path/to/your/client_cert.pem'

# If the key to the provided certificate is stored in a separate file,
# provide the path to the keyfile and, optionally, the key password if
# the key is encrypted
configuration.key_file='/path/to/your/client_cert.key'
configuration.key_password='keyfile_password' # optional

# Enter a context with an instance of the API client
with cons3rt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cons3rt.TemplatesApi(api_client)
    virtualization_realm_id = 56 # int | Virtualization Realm ID to filter by
include_registrations = True # bool | Include templates registered to this virtualization realm (optional) (default to True)
include_subscriptions = False # bool | Include templates this virtualization realm is subscribed to (optional) (default to False)

    try:
        # List all Templates
        api_response = api_instance.list_virtualization_realm_templates(virtualization_realm_id, include_registrations=include_registrations, include_subscriptions=include_subscriptions)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TemplatesApi->list_virtualization_realm_templates: %s\n" % e)
```

* Api Key Authentication (Username):
```python
from __future__ import print_function
import time
import cons3rt
from cons3rt.rest import ApiException
from pprint import pprint
# Configure API key authorization: APIKeyHeader
configuration.api_key['token'] = 'YOUR_VALUE'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
# Configure API key authorization: Username
configuration.api_key['username'] = 'YOUR_VALUE'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['username'] = 'Bearer'

# Using a client certificate for authentication is required in some cases.
# To use a "soft-token" such as an ECA, provide the path the PEM encoded
# version of the certificate
configuration.cert_file='/path/to/your/client_cert.pem'

# If the key to the provided certificate is stored in a separate file,
# provide the path to the keyfile and, optionally, the key password if
# the key is encrypted
configuration.key_file='/path/to/your/client_cert.key'
configuration.key_password='keyfile_password' # optional

# Enter a context with an instance of the API client
with cons3rt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cons3rt.TemplatesApi(api_client)
    virtualization_realm_id = 56 # int | Virtualization Realm ID to filter by
include_registrations = True # bool | Include templates registered to this virtualization realm (optional) (default to True)
include_subscriptions = False # bool | Include templates this virtualization realm is subscribed to (optional) (default to False)

    try:
        # List all Templates
        api_response = api_instance.list_virtualization_realm_templates(virtualization_realm_id, include_registrations=include_registrations, include_subscriptions=include_subscriptions)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TemplatesApi->list_virtualization_realm_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtualization_realm_id** | **int**| Virtualization Realm ID to filter by | 
 **include_registrations** | **bool**| Include templates registered to this virtualization realm | [optional] [default to True]
 **include_subscriptions** | **bool**| Include templates this virtualization realm is subscribed to | [optional] [default to False]

### Return type

[**list[MinimalCons3rtTemplateData]**](MinimalCons3rtTemplateData.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid query parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

