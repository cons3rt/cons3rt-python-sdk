# cons3rt.SoftwareBundlesApi

All URIs are relative to *https://api.dev.cons3rt.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_software_asset_bundle_from_system_module**](SoftwareBundlesApi.md#create_software_asset_bundle_from_system_module) | **POST** /api/software/bundles | Create Software Bundle
[**delete_software_asset_bundle**](SoftwareBundlesApi.md#delete_software_asset_bundle) | **DELETE** /api/software/bundles/{id} | Delete Software Bundle
[**get_software_asset_bundle_expanded**](SoftwareBundlesApi.md#get_software_asset_bundle_expanded) | **GET** /api/software/bundles/expanded | List all Software Bundles, including Project Assets
[**get_software_bundle**](SoftwareBundlesApi.md#get_software_bundle) | **GET** /api/software/bundles/{id} | Retrieve Software Bundle
[**get_software_bundles**](SoftwareBundlesApi.md#get_software_bundles) | **GET** /api/software/bundles | List Software Bundles


# **create_software_asset_bundle_from_system_module**
> str create_software_asset_bundle_from_system_module(system_id, name, body=body)

Create Software Bundle

Create a single Software Bundle from the Software Components of the specified System Module.

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
api_instance = cons3rt.SoftwareBundlesApi(cons3rt.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of system module
name = 'name_example' # str | Name of the new software bundle
body = 'body_example' # str | Description of the new software bundle (optional)

try:
    # Create Software Bundle
    api_response = api_instance.create_software_asset_bundle_from_system_module(system_id, name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareBundlesApi->create_software_asset_bundle_from_system_module: %s\n" % e)
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
api_instance = cons3rt.SoftwareBundlesApi(cons3rt.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of system module
name = 'name_example' # str | Name of the new software bundle
body = 'body_example' # str | Description of the new software bundle (optional)

try:
    # Create Software Bundle
    api_response = api_instance.create_software_asset_bundle_from_system_module(system_id, name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareBundlesApi->create_software_asset_bundle_from_system_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of system module | 
 **name** | **str**| Name of the new software bundle | 
 **body** | **str**| Description of the new software bundle | [optional] 

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
**400** | Invalid system module ID or data supplied |  -  |
**404** | System module not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_software_asset_bundle**
> bool delete_software_asset_bundle(id)

Delete Software Bundle

Delete a single Software Bundle with the given ID.

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
api_instance = cons3rt.SoftwareBundlesApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of software bundle

try:
    # Delete Software Bundle
    api_response = api_instance.delete_software_asset_bundle(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareBundlesApi->delete_software_asset_bundle: %s\n" % e)
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
api_instance = cons3rt.SoftwareBundlesApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of software bundle

try:
    # Delete Software Bundle
    api_response = api_instance.delete_software_asset_bundle(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareBundlesApi->delete_software_asset_bundle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of software bundle | 

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
**404** | Software Bundle not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_software_asset_bundle_expanded**
> list[BasicSoftwareAssetBundle] get_software_asset_bundle_expanded(community=community, categoryids=categoryids, maxresults=maxresults, page=page)

List all Software Bundles, including Project Assets

Returns a collection of all relevant Software Bundles matching a specified query, including those from the Project.

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
api_instance = cons3rt.SoftwareBundlesApi(cons3rt.ApiClient(configuration))
community = False # bool | Include community assets (optional) (default to False)
categoryids = [56] # list[int] | Category ID(s) to filter by. Multiple categories can be provided with comma-separated strings. (optional)
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

try:
    # List all Software Bundles, including Project Assets
    api_response = api_instance.get_software_asset_bundle_expanded(community=community, categoryids=categoryids, maxresults=maxresults, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareBundlesApi->get_software_asset_bundle_expanded: %s\n" % e)
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
api_instance = cons3rt.SoftwareBundlesApi(cons3rt.ApiClient(configuration))
community = False # bool | Include community assets (optional) (default to False)
categoryids = [56] # list[int] | Category ID(s) to filter by. Multiple categories can be provided with comma-separated strings. (optional)
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

try:
    # List all Software Bundles, including Project Assets
    api_response = api_instance.get_software_asset_bundle_expanded(community=community, categoryids=categoryids, maxresults=maxresults, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareBundlesApi->get_software_asset_bundle_expanded: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **community** | **bool**| Include community assets | [optional] [default to False]
 **categoryids** | [**list[int]**](int.md)| Category ID(s) to filter by. Multiple categories can be provided with comma-separated strings. | [optional] 
 **maxresults** | **int**| Maximum number of results to return | [optional] [default to 40]
 **page** | **int**| Requested page number | [optional] [default to 0]

### Return type

[**list[BasicSoftwareAssetBundle]**](BasicSoftwareAssetBundle.md)

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

# **get_software_bundle**
> FullSoftwareAssetBundle get_software_bundle(id)

Retrieve Software Bundle

Returns a single Software Bundle by the given ID.

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
api_instance = cons3rt.SoftwareBundlesApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of software bundle

try:
    # Retrieve Software Bundle
    api_response = api_instance.get_software_bundle(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareBundlesApi->get_software_bundle: %s\n" % e)
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
api_instance = cons3rt.SoftwareBundlesApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of software bundle

try:
    # Retrieve Software Bundle
    api_response = api_instance.get_software_bundle(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareBundlesApi->get_software_bundle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of software bundle | 

### Return type

[**FullSoftwareAssetBundle**](FullSoftwareAssetBundle.md)

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
**404** | Software Bundle not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_software_bundles**
> list[MinimalSoftwareAssetBundle] get_software_bundles(categoryids=categoryids, maxresults=maxresults, page=page)

List Software Bundles

Returns a collection of the user's relevant Software Bundles matching a specified query.

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
api_instance = cons3rt.SoftwareBundlesApi(cons3rt.ApiClient(configuration))
categoryids = [56] # list[int] | Category ID(s) to filter by. Multiple categories can be provided with comma-separated strings. (optional)
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

try:
    # List Software Bundles
    api_response = api_instance.get_software_bundles(categoryids=categoryids, maxresults=maxresults, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareBundlesApi->get_software_bundles: %s\n" % e)
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
api_instance = cons3rt.SoftwareBundlesApi(cons3rt.ApiClient(configuration))
categoryids = [56] # list[int] | Category ID(s) to filter by. Multiple categories can be provided with comma-separated strings. (optional)
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

try:
    # List Software Bundles
    api_response = api_instance.get_software_bundles(categoryids=categoryids, maxresults=maxresults, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareBundlesApi->get_software_bundles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categoryids** | [**list[int]**](int.md)| Category ID(s) to filter by. Multiple categories can be provided with comma-separated strings. | [optional] 
 **maxresults** | **int**| Maximum number of results to return | [optional] [default to 40]
 **page** | **int**| Requested page number | [optional] [default to 0]

### Return type

[**list[MinimalSoftwareAssetBundle]**](MinimalSoftwareAssetBundle.md)

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

