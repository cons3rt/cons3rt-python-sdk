# cons3rt.DownloadApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_file_from_bucket**](DownloadApi.md#download_file_from_bucket) | **GET** /api/buckets/{id}/download | Download File From Bucket


# **download_file_from_bucket**
> bool download_file_from_bucket(id, file_name, background=background)

Download File From Bucket

Downloads the Asset in the form of a zip file. Download is only available for importable Asset types (i.e. Software, Test, and Container).<br> <br> Based on the background flag, the download will be done in the foreground (false), background (true), or in a location as determined by Asset size (default).<br> <br> If the background flag is set to true (or if no value for the background flag is provided), and the Asset is larger than the site threshold, the Asset will be prepared for download in the background.In that case, an email with a link to retrieve the Asset will be sent.If the Asset is larger than download threshold, it will be prepared for download in the background, and an email with a download link will be sent.

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
    api_instance = cons3rt.DownloadApi(api_client)
    id = 'id_example' # str | ID of bucket
file_name = 'file_name_example' # str | The filename within the bucket to download
background = False # bool | Force the download to happen in the background (optional) (default to False)

    try:
        # Download File From Bucket
        api_response = api_instance.download_file_from_bucket(id, file_name, background=background)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DownloadApi->download_file_from_bucket: %s\n" % e)
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
    api_instance = cons3rt.DownloadApi(api_client)
    id = 'id_example' # str | ID of bucket
file_name = 'file_name_example' # str | The filename within the bucket to download
background = False # bool | Force the download to happen in the background (optional) (default to False)

    try:
        # Download File From Bucket
        api_response = api_instance.download_file_from_bucket(id, file_name, background=background)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DownloadApi->download_file_from_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of bucket | 
 **file_name** | **str**| The filename within the bucket to download | 
 **background** | **bool**| Force the download to happen in the background | [optional] [default to False]

### Return type

**bool**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**202** | Accepted |  -  |
**400** | Invalid ID supplied or asset is not the correct type |  -  |
**404** | Asset not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

