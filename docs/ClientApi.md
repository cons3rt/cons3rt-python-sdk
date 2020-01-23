# cons3rt.ClientApi

All URIs are relative to *https://api.dev.cons3rt.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**launch_composition**](ClientApi.md#launch_composition) | **POST** /api/client/{id} | Launch Composition
[**list_composition_status**](ClientApi.md#list_composition_status) | **GET** /api/client | List Composition Statuses


# **launch_composition**
> list[int] launch_composition(id, composition_launch_options=composition_launch_options)

Launch Composition

Launch a pre-existing Composition, declaring the username, password, and (optionally) the time to live.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from __future__ import print_function
import time
import cons3rt
from cons3rt.rest import ApiException
from pprint import pprint
configuration = cons3rt.Configuration()
# Configure API key authorization: APIKeyHeader
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
configuration = cons3rt.Configuration()
# Configure API key authorization: Username
configuration.api_key['username'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['username'] = 'Bearer'

# Defining host is optional and default to https://api.dev.cons3rt.io/rest
configuration.host = "https://api.dev.cons3rt.io/rest"
# Create an instance of the API class
api_instance = cons3rt.ClientApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of composition to launch
composition_launch_options = cons3rt.CompositionLaunchOptions() # CompositionLaunchOptions | The Composition launch options (optional)

try:
    # Launch Composition
    api_response = api_instance.launch_composition(id, composition_launch_options=composition_launch_options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->launch_composition: %s\n" % e)
```

* Api Key Authentication (Username):
```python
from __future__ import print_function
import time
import cons3rt
from cons3rt.rest import ApiException
from pprint import pprint
configuration = cons3rt.Configuration()
# Configure API key authorization: APIKeyHeader
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
configuration = cons3rt.Configuration()
# Configure API key authorization: Username
configuration.api_key['username'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['username'] = 'Bearer'

# Defining host is optional and default to https://api.dev.cons3rt.io/rest
configuration.host = "https://api.dev.cons3rt.io/rest"
# Create an instance of the API class
api_instance = cons3rt.ClientApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of composition to launch
composition_launch_options = cons3rt.CompositionLaunchOptions() # CompositionLaunchOptions | The Composition launch options (optional)

try:
    # Launch Composition
    api_response = api_instance.launch_composition(id, composition_launch_options=composition_launch_options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->launch_composition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of composition to launch | 
 **composition_launch_options** | [**CompositionLaunchOptions**](CompositionLaunchOptions.md)| The Composition launch options | [optional] 

### Return type

**list[int]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid ID supplied |  -  |
**404** | Composition not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_composition_status**
> list[AbstractCompositionStatus] list_composition_status()

List Composition Statuses

Returns a collection of statuses for the user's available Compositions.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from __future__ import print_function
import time
import cons3rt
from cons3rt.rest import ApiException
from pprint import pprint
configuration = cons3rt.Configuration()
# Configure API key authorization: APIKeyHeader
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
configuration = cons3rt.Configuration()
# Configure API key authorization: Username
configuration.api_key['username'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['username'] = 'Bearer'

# Defining host is optional and default to https://api.dev.cons3rt.io/rest
configuration.host = "https://api.dev.cons3rt.io/rest"
# Create an instance of the API class
api_instance = cons3rt.ClientApi(cons3rt.ApiClient(configuration))

try:
    # List Composition Statuses
    api_response = api_instance.list_composition_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->list_composition_status: %s\n" % e)
```

* Api Key Authentication (Username):
```python
from __future__ import print_function
import time
import cons3rt
from cons3rt.rest import ApiException
from pprint import pprint
configuration = cons3rt.Configuration()
# Configure API key authorization: APIKeyHeader
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'
configuration = cons3rt.Configuration()
# Configure API key authorization: Username
configuration.api_key['username'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['username'] = 'Bearer'

# Defining host is optional and default to https://api.dev.cons3rt.io/rest
configuration.host = "https://api.dev.cons3rt.io/rest"
# Create an instance of the API class
api_instance = cons3rt.ClientApi(cons3rt.ApiClient(configuration))

try:
    # List Composition Statuses
    api_response = api_instance.list_composition_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->list_composition_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AbstractCompositionStatus]**](AbstractCompositionStatus.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

