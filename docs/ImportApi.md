# cons3rt.ImportApi

All URIs are relative to *https://api.dev.cons3rt.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_file**](ImportApi.md#upload_file) | **POST** /api/import | Import a New Asset


# **upload_file**
> int upload_file(file=file, filename=filename)

Import a New Asset

Imports an Asset in the form of a zip file.<br> <br> File must be submitted as multipart-form data, with a file element named \"file\" and a filename field containing a name that ends in \".zip\" <br> <br> A \"Connection: Keep-Alive\" configuration may be needed for larger sized files, due to the time it takes to copy to the server.

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
api_instance = cons3rt.ImportApi(cons3rt.ApiClient(configuration))
file = 'file_example' # list[str] |  (optional)
filename = 'filename_example' # str |  (optional)

try:
    # Import a New Asset
    api_response = api_instance.upload_file(file=file, filename=filename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->upload_file: %s\n" % e)
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
api_instance = cons3rt.ImportApi(cons3rt.ApiClient(configuration))
file = 'file_example' # list[str] |  (optional)
filename = 'filename_example' # str |  (optional)

try:
    # Import a New Asset
    api_response = api_instance.upload_file(file=file, filename=filename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | [**list[str]**](str.md)|  | [optional] 
 **filename** | **str**|  | [optional] 

### Return type

**int**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**202** | Accepted |  -  |
**400** | Invalid file data supplied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

