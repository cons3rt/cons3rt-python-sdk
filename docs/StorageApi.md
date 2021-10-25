# cons3rt.StorageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bucket**](StorageApi.md#create_bucket) | **POST** /api/buckets | Create Storage Bucket
[**delete_bucket**](StorageApi.md#delete_bucket) | **DELETE** /api/buckets/{id} | Delete Storage Buckets
[**download_file_from_bucket**](StorageApi.md#download_file_from_bucket) | **GET** /api/buckets/{id}/download | Download File From Bucket
[**get_bucket**](StorageApi.md#get_bucket) | **GET** /api/buckets/{id} | Retrieve Storage Buckets
[**get_bucket_listing**](StorageApi.md#get_bucket_listing) | **GET** /api/buckets/{id}/listing | List Bucket Contents
[**list_available_clouds_for_buckets**](StorageApi.md#list_available_clouds_for_buckets) | **GET** /api/buckets/clouds | List Clouds Available For Bucket Creation
[**list_buckets**](StorageApi.md#list_buckets) | **GET** /api/buckets | List Storage Buckets
[**submit_bucket_resource_to_submission_service**](StorageApi.md#submit_bucket_resource_to_submission_service) | **POST** /api/buckets/{id}/submit/{submission_service_id} | Submit Bucket Resource to the Project&#39;s Submission Service
[**update_bucket**](StorageApi.md#update_bucket) | **PUT** /api/buckets/{id} | Update Storage Buckets
[**upload_file_to_bucket**](StorageApi.md#upload_file_to_bucket) | **POST** /api/buckets/{id} | Upload File to Bucket


# **create_bucket**
> str create_bucket(bucket)

Create Storage Bucket

Creates a storage bucket as defined by the user

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
    api_instance = cons3rt.StorageApi(api_client)
    bucket = cons3rt.Bucket() # Bucket | The bucket creation information

    try:
        # Create Storage Bucket
        api_response = api_instance.create_bucket(bucket)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->create_bucket: %s\n" % e)
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
    api_instance = cons3rt.StorageApi(api_client)
    bucket = cons3rt.Bucket() # Bucket | The bucket creation information

    try:
        # Create Storage Bucket
        api_response = api_instance.create_bucket(bucket)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->create_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | [**Bucket**](Bucket.md)| The bucket creation information | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid bucket configuration requested |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bucket**
> bool delete_bucket(id)

Delete Storage Buckets

Deletes an existing storage bucket by identifier

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
    api_instance = cons3rt.StorageApi(api_client)
    id = 'id_example' # str | ID of bucket

    try:
        # Delete Storage Buckets
        api_response = api_instance.delete_bucket(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->delete_bucket: %s\n" % e)
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
    api_instance = cons3rt.StorageApi(api_client)
    id = 'id_example' # str | ID of bucket

    try:
        # Delete Storage Buckets
        api_response = api_instance.delete_bucket(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->delete_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of bucket | 

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
**400** | Invalid ID supplied |  -  |
**404** | Storage bucket not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    api_instance = cons3rt.StorageApi(api_client)
    id = 'id_example' # str | ID of bucket
file_name = 'file_name_example' # str | The filename within the bucket to download
background = False # bool | Force the download to happen in the background (optional) (default to False)

    try:
        # Download File From Bucket
        api_response = api_instance.download_file_from_bucket(id, file_name, background=background)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->download_file_from_bucket: %s\n" % e)
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
    api_instance = cons3rt.StorageApi(api_client)
    id = 'id_example' # str | ID of bucket
file_name = 'file_name_example' # str | The filename within the bucket to download
background = False # bool | Force the download to happen in the background (optional) (default to False)

    try:
        # Download File From Bucket
        api_response = api_instance.download_file_from_bucket(id, file_name, background=background)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->download_file_from_bucket: %s\n" % e)
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

# **get_bucket**
> Bucket get_bucket(id)

Retrieve Storage Buckets

returns a storage bucket

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
    api_instance = cons3rt.StorageApi(api_client)
    id = 'id_example' # str | ID of bucket

    try:
        # Retrieve Storage Buckets
        api_response = api_instance.get_bucket(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_bucket: %s\n" % e)
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
    api_instance = cons3rt.StorageApi(api_client)
    id = 'id_example' # str | ID of bucket

    try:
        # Retrieve Storage Buckets
        api_response = api_instance.get_bucket(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of bucket | 

### Return type

[**Bucket**](Bucket.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid ID |  -  |
**404** | Storage bucket not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bucket_listing**
> str get_bucket_listing(id)

List Bucket Contents

lists all files contents for an existing bucket

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
    api_instance = cons3rt.StorageApi(api_client)
    id = 'id_example' # str | ID of bucket

    try:
        # List Bucket Contents
        api_response = api_instance.get_bucket_listing(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_bucket_listing: %s\n" % e)
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
    api_instance = cons3rt.StorageApi(api_client)
    id = 'id_example' # str | ID of bucket

    try:
        # List Bucket Contents
        api_response = api_instance.get_bucket_listing(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->get_bucket_listing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of bucket | 

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
**400** | Invalid ID supplied |  -  |
**404** | Storage bucket not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_clouds_for_buckets**
> list[MinimalCloud] list_available_clouds_for_buckets(maxresults=maxresults, page=page)

List Clouds Available For Bucket Creation

returns a collection of clouds accessible to the user

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
    api_instance = cons3rt.StorageApi(api_client)
    maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

    try:
        # List Clouds Available For Bucket Creation
        api_response = api_instance.list_available_clouds_for_buckets(maxresults=maxresults, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->list_available_clouds_for_buckets: %s\n" % e)
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
    api_instance = cons3rt.StorageApi(api_client)
    maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

    try:
        # List Clouds Available For Bucket Creation
        api_response = api_instance.list_available_clouds_for_buckets(maxresults=maxresults, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->list_available_clouds_for_buckets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maxresults** | **int**| Maximum number of results to return | [optional] [default to 40]
 **page** | **int**| Requested page number | [optional] [default to 0]

### Return type

[**list[MinimalCloud]**](MinimalCloud.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid query parameter supplied |  -  |
**404** | Clouds not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_buckets**
> list[Bucket] list_buckets(cloud=cloud, project=project, maxresults=maxresults, page=page)

List Storage Buckets

returns a collection of storage buckets

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
    api_instance = cons3rt.StorageApi(api_client)
    cloud = 'cloud_example' # str | ID of the cloud (optional)
project = False # bool | Include project buckets (optional) (default to False)
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

    try:
        # List Storage Buckets
        api_response = api_instance.list_buckets(cloud=cloud, project=project, maxresults=maxresults, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->list_buckets: %s\n" % e)
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
    api_instance = cons3rt.StorageApi(api_client)
    cloud = 'cloud_example' # str | ID of the cloud (optional)
project = False # bool | Include project buckets (optional) (default to False)
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

    try:
        # List Storage Buckets
        api_response = api_instance.list_buckets(cloud=cloud, project=project, maxresults=maxresults, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->list_buckets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud** | **str**| ID of the cloud | [optional] 
 **project** | **bool**| Include project buckets | [optional] [default to False]
 **maxresults** | **int**| Maximum number of results to return | [optional] [default to 40]
 **page** | **int**| Requested page number | [optional] [default to 0]

### Return type

[**list[Bucket]**](Bucket.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid ID or query parameter supplied |  -  |
**404** | Storage buckets not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_bucket_resource_to_submission_service**
> bool submit_bucket_resource_to_submission_service(id, submission_service_id, file_name, input_submission_service_for_asset_submission=input_submission_service_for_asset_submission)

Submit Bucket Resource to the Project's Submission Service

Publishes a resource in the specified bucket to the requested Submission Service.<br> <br> The requested Project Submission Service will act as a template. Credentials provided when submitting to the Service will override the Project Submission Service's credentials. However, neither the Host nor Port of the Service can be overridden.<br> <br> If the Service's endpoint is an SFTP Host, the Submission will only be able to override the remote path (i.e. if one has not already been defined in this default Submission Service).<br>

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
    api_instance = cons3rt.StorageApi(api_client)
    id = 'id_example' # str | ID of the bucket to publish a resource from
submission_service_id = 'submission_service_id_example' # str | ID of project submission service
file_name = 'file_name_example' # str | The filename within the bucket to download
input_submission_service_for_asset_submission = cons3rt.InputSubmissionServiceForAssetSubmission() # InputSubmissionServiceForAssetSubmission | Submission service override values (optional)

    try:
        # Submit Bucket Resource to the Project's Submission Service
        api_response = api_instance.submit_bucket_resource_to_submission_service(id, submission_service_id, file_name, input_submission_service_for_asset_submission=input_submission_service_for_asset_submission)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->submit_bucket_resource_to_submission_service: %s\n" % e)
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
    api_instance = cons3rt.StorageApi(api_client)
    id = 'id_example' # str | ID of the bucket to publish a resource from
submission_service_id = 'submission_service_id_example' # str | ID of project submission service
file_name = 'file_name_example' # str | The filename within the bucket to download
input_submission_service_for_asset_submission = cons3rt.InputSubmissionServiceForAssetSubmission() # InputSubmissionServiceForAssetSubmission | Submission service override values (optional)

    try:
        # Submit Bucket Resource to the Project's Submission Service
        api_response = api_instance.submit_bucket_resource_to_submission_service(id, submission_service_id, file_name, input_submission_service_for_asset_submission=input_submission_service_for_asset_submission)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->submit_bucket_resource_to_submission_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the bucket to publish a resource from | 
 **submission_service_id** | **str**| ID of project submission service | 
 **file_name** | **str**| The filename within the bucket to download | 
 **input_submission_service_for_asset_submission** | [**InputSubmissionServiceForAssetSubmission**](InputSubmissionServiceForAssetSubmission.md)| Submission service override values | [optional] 

### Return type

**bool**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid bucket ID or submission service ID supplied |  -  |
**404** | Bucket or Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bucket**
> Bucket update_bucket(id, bucket)

Update Storage Buckets

updates the configuration information for an existing bucket

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
    api_instance = cons3rt.StorageApi(api_client)
    id = 'id_example' # str | ID of bucket
bucket = cons3rt.Bucket() # Bucket | The bucket creation information

    try:
        # Update Storage Buckets
        api_response = api_instance.update_bucket(id, bucket)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->update_bucket: %s\n" % e)
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
    api_instance = cons3rt.StorageApi(api_client)
    id = 'id_example' # str | ID of bucket
bucket = cons3rt.Bucket() # Bucket | The bucket creation information

    try:
        # Update Storage Buckets
        api_response = api_instance.update_bucket(id, bucket)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->update_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of bucket | 
 **bucket** | [**Bucket**](Bucket.md)| The bucket creation information | 

### Return type

[**Bucket**](Bucket.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid ID or configuration request supplied |  -  |
**404** | Storage bucket not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file_to_bucket**
> int upload_file_to_bucket(id, file=file, filename=filename)

Upload File to Bucket

Uploads a file to a bucket.<br> <br> File must be submitted as multipart-form data, with a file element named \"file\" and a filename field <br> <br> A \"Connection: Keep-Alive\" configuration may be needed for larger sized files, due to the time it takes to copy to the server.

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
    api_instance = cons3rt.StorageApi(api_client)
    id = 'id_example' # str | ID of bucket
file = '/path/to/file' # list[file] |  (optional)
filename = 'filename_example' # str |  (optional)

    try:
        # Upload File to Bucket
        api_response = api_instance.upload_file_to_bucket(id, file=file, filename=filename)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->upload_file_to_bucket: %s\n" % e)
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
    api_instance = cons3rt.StorageApi(api_client)
    id = 'id_example' # str | ID of bucket
file = '/path/to/file' # list[file] |  (optional)
filename = 'filename_example' # str |  (optional)

    try:
        # Upload File to Bucket
        api_response = api_instance.upload_file_to_bucket(id, file=file, filename=filename)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageApi->upload_file_to_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of bucket | 
 **file** | **list[file]**|  | [optional] 
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

