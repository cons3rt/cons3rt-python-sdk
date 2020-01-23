# cons3rt.SystemAssetsApi

All URIs are relative to *https://api.dev.cons3rt.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_system_asset**](SystemAssetsApi.md#create_system_asset) | **POST** /api/systemassets | Create System Asset
[**delete_system_asset**](SystemAssetsApi.md#delete_system_asset) | **DELETE** /api/systemassets/{id} | Delete System Asset
[**import_system_asset**](SystemAssetsApi.md#import_system_asset) | **POST** /api/systemassets/{id}/import | Import System Asset
[**list_system_assets**](SystemAssetsApi.md#list_system_assets) | **GET** /api/systemassets | List System Assets
[**retrieve_system_asset**](SystemAssetsApi.md#retrieve_system_asset) | **GET** /api/systemassets/{id} | Retrieve System Asset
[**update_system_asset**](SystemAssetsApi.md#update_system_asset) | **PUT** /api/systemassets/{id} | Update System Asset


# **create_system_asset**
> list[FullSystemAsset] create_system_asset(input_system_asset=input_system_asset)

Create System Asset

Create a new System Asset registration.

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
api_instance = cons3rt.SystemAssetsApi(cons3rt.ApiClient(configuration))
input_system_asset = cons3rt.InputSystemAsset() # InputSystemAsset | The System Asset definition (optional)

try:
    # Create System Asset
    api_response = api_instance.create_system_asset(input_system_asset=input_system_asset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAssetsApi->create_system_asset: %s\n" % e)
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
api_instance = cons3rt.SystemAssetsApi(cons3rt.ApiClient(configuration))
input_system_asset = cons3rt.InputSystemAsset() # InputSystemAsset | The System Asset definition (optional)

try:
    # Create System Asset
    api_response = api_instance.create_system_asset(input_system_asset=input_system_asset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAssetsApi->create_system_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_system_asset** | [**InputSystemAsset**](InputSystemAsset.md)| The System Asset definition | [optional] 

### Return type

[**list[FullSystemAsset]**](FullSystemAsset.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_system_asset**
> bool delete_system_asset(id)

Delete System Asset

Delete a single System Asset with the given ID.

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
api_instance = cons3rt.SystemAssetsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of system asset to delete

try:
    # Delete System Asset
    api_response = api_instance.delete_system_asset(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAssetsApi->delete_system_asset: %s\n" % e)
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
api_instance = cons3rt.SystemAssetsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of system asset to delete

try:
    # Delete System Asset
    api_response = api_instance.delete_system_asset(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAssetsApi->delete_system_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of system asset to delete | 

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
**400** | Invalid System Asset ID supplied |  -  |
**404** | System Asset not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_system_asset**
> bool import_system_asset(id)

Import System Asset

Import a System Asset from an existing System Asset registration, based on ID.

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
api_instance = cons3rt.SystemAssetsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of system asset to import

try:
    # Import System Asset
    api_response = api_instance.import_system_asset(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAssetsApi->import_system_asset: %s\n" % e)
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
api_instance = cons3rt.SystemAssetsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of system asset to import

try:
    # Import System Asset
    api_response = api_instance.import_system_asset(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAssetsApi->import_system_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of system asset to import | 

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
**400** | Invalid System Asset ID supplied |  -  |
**404** | System Asset not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_system_assets**
> list[MinimalSystemAsset] list_system_assets()

List System Assets

Returns a collection of currently registered System Assets.

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
api_instance = cons3rt.SystemAssetsApi(cons3rt.ApiClient(configuration))

try:
    # List System Assets
    api_response = api_instance.list_system_assets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAssetsApi->list_system_assets: %s\n" % e)
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
api_instance = cons3rt.SystemAssetsApi(cons3rt.ApiClient(configuration))

try:
    # List System Assets
    api_response = api_instance.list_system_assets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAssetsApi->list_system_assets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MinimalSystemAsset]**](MinimalSystemAsset.md)

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

# **retrieve_system_asset**
> list[FullSystemAsset] retrieve_system_asset(id)

Retrieve System Asset

Retrieves an existing System Asset registration based on ID.

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
api_instance = cons3rt.SystemAssetsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of System Asset

try:
    # Retrieve System Asset
    api_response = api_instance.retrieve_system_asset(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAssetsApi->retrieve_system_asset: %s\n" % e)
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
api_instance = cons3rt.SystemAssetsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of System Asset

try:
    # Retrieve System Asset
    api_response = api_instance.retrieve_system_asset(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAssetsApi->retrieve_system_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of System Asset | 

### Return type

[**list[FullSystemAsset]**](FullSystemAsset.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid system asset ID supplied |  -  |
**404** | System Asset not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_system_asset**
> FullSystemAsset update_system_asset(id, input_system_asset=input_system_asset)

Update System Asset

Update the content of a single System Asset with the given ID and new registration information.

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
api_instance = cons3rt.SystemAssetsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of System Asset to update
input_system_asset = cons3rt.InputSystemAsset() # InputSystemAsset | The modified System Asset definition (optional)

try:
    # Update System Asset
    api_response = api_instance.update_system_asset(id, input_system_asset=input_system_asset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAssetsApi->update_system_asset: %s\n" % e)
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
api_instance = cons3rt.SystemAssetsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of System Asset to update
input_system_asset = cons3rt.InputSystemAsset() # InputSystemAsset | The modified System Asset definition (optional)

try:
    # Update System Asset
    api_response = api_instance.update_system_asset(id, input_system_asset=input_system_asset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAssetsApi->update_system_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of System Asset to update | 
 **input_system_asset** | [**InputSystemAsset**](InputSystemAsset.md)| The modified System Asset definition | [optional] 

### Return type

[**FullSystemAsset**](FullSystemAsset.md)

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
**404** | System Asset not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

