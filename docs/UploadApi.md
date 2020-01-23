# cons3rt.UploadApi

All URIs are relative to *https://api.dev.cons3rt.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_file_content**](UploadApi.md#get_file_content) | **GET** /api/upload/content | Get File Content
[**get_file_object**](UploadApi.md#get_file_object) | **GET** /api/upload | Download File
[**upload_file1**](UploadApi.md#upload_file1) | **POST** /api/upload | Upload File


# **get_file_content**
> str get_file_content(uuid)

Get File Content

Retrieves content of uploaded temporary file.

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
api_instance = cons3rt.UploadApi(cons3rt.ApiClient(configuration))
uuid = 'uuid_example' # str | UUID of the temporary file

try:
    # Get File Content
    api_response = api_instance.get_file_content(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadApi->get_file_content: %s\n" % e)
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
api_instance = cons3rt.UploadApi(cons3rt.ApiClient(configuration))
uuid = 'uuid_example' # str | UUID of the temporary file

try:
    # Get File Content
    api_response = api_instance.get_file_content(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadApi->get_file_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the temporary file | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid file data supplied |  -  |
**404** | File not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_object**
> get_file_object(uuid)

Download File

Downloads an uploaded temporary file for UUID handle.

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
api_instance = cons3rt.UploadApi(cons3rt.ApiClient(configuration))
uuid = 'uuid_example' # str | UUID of the temporary file

try:
    # Download File
    api_instance.get_file_object(uuid)
except ApiException as e:
    print("Exception when calling UploadApi->get_file_object: %s\n" % e)
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
api_instance = cons3rt.UploadApi(cons3rt.ApiClient(configuration))
uuid = 'uuid_example' # str | UUID of the temporary file

try:
    # Download File
    api_instance.get_file_object(uuid)
except ApiException as e:
    print("Exception when calling UploadApi->get_file_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the temporary file | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid file data supplied |  -  |
**404** | File not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file1**
> str upload_file1(file=file, filename=filename)

Upload File

Uploads a temporary file for later use within the API.<br> <br> By default, this file will only be available for 30 minutes.

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
api_instance = cons3rt.UploadApi(cons3rt.ApiClient(configuration))
file = 'file_example' # list[str] |  (optional)
filename = 'filename_example' # str |  (optional)

try:
    # Upload File
    api_response = api_instance.upload_file1(file=file, filename=filename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadApi->upload_file1: %s\n" % e)
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
api_instance = cons3rt.UploadApi(cons3rt.ApiClient(configuration))
file = 'file_example' # list[str] |  (optional)
filename = 'filename_example' # str |  (optional)

try:
    # Upload File
    api_response = api_instance.upload_file1(file=file, filename=filename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadApi->upload_file1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | [**list[str]**](str.md)|  | [optional] 
 **filename** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid file data supplied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

