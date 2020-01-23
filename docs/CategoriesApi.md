# cons3rt.CategoriesApi

All URIs are relative to *https://api.dev.cons3rt.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_category_to_asset**](CategoriesApi.md#add_category_to_asset) | **PUT** /api/categories/{id}/asset | Assign Category to Asset
[**create_category**](CategoriesApi.md#create_category) | **POST** /api/categories | Create a Category
[**delete_category**](CategoriesApi.md#delete_category) | **DELETE** /api/categories/{id} | Delete Category
[**get_categories**](CategoriesApi.md#get_categories) | **GET** /api/categories | List all Categories
[**remove_category_from_asset**](CategoriesApi.md#remove_category_from_asset) | **DELETE** /api/categories/{id}/asset | Unassign Category from Asset
[**set_category_parent**](CategoriesApi.md#set_category_parent) | **PUT** /api/categories/{id}/parent | Set Parent Category
[**update_category**](CategoriesApi.md#update_category) | **PUT** /api/categories/{id} | Update Category


# **add_category_to_asset**
> bool add_category_to_asset(id, assetid)

Assign Category to Asset

Assigns the Category as a filter tag to the provided Asset.<br> <br> Altering the Category will affect future Asset filtering.

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
api_instance = cons3rt.CategoriesApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of category
assetid = 'assetid_example' # str | ID of asset to assign

try:
    # Assign Category to Asset
    api_response = api_instance.add_category_to_asset(id, assetid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->add_category_to_asset: %s\n" % e)
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
api_instance = cons3rt.CategoriesApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of category
assetid = 'assetid_example' # str | ID of asset to assign

try:
    # Assign Category to Asset
    api_response = api_instance.add_category_to_asset(id, assetid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->add_category_to_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of category | 
 **assetid** | **str**| ID of asset to assign | 

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
**400** | Invalid category ID or asset ID supplied |  -  |
**404** | Category not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_category**
> FullCategory create_category(input_category=input_category)

Create a Category

Creates a single Category in order to organize Assets.

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
api_instance = cons3rt.CategoriesApi(cons3rt.ApiClient(configuration))
input_category = cons3rt.InputCategory() # InputCategory | The Category to create (optional)

try:
    # Create a Category
    api_response = api_instance.create_category(input_category=input_category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->create_category: %s\n" % e)
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
api_instance = cons3rt.CategoriesApi(cons3rt.ApiClient(configuration))
input_category = cons3rt.InputCategory() # InputCategory | The Category to create (optional)

try:
    # Create a Category
    api_response = api_instance.create_category(input_category=input_category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->create_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_category** | [**InputCategory**](InputCategory.md)| The Category to create | [optional] 

### Return type

[**FullCategory**](FullCategory.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid data supplied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_category**
> bool delete_category(id)

Delete Category

Deletes a single Category with the given ID.

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
api_instance = cons3rt.CategoriesApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of category to delete

try:
    # Delete Category
    api_response = api_instance.delete_category(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->delete_category: %s\n" % e)
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
api_instance = cons3rt.CategoriesApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of category to delete

try:
    # Delete Category
    api_response = api_instance.delete_category(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->delete_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of category to delete | 

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
**400** | Invalid category ID supplied |  -  |
**404** | Category not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories**
> list[MinimalCategory] get_categories()

List all Categories

Returns a collection of the currently available Categories.

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
api_instance = cons3rt.CategoriesApi(cons3rt.ApiClient(configuration))

try:
    # List all Categories
    api_response = api_instance.get_categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_categories: %s\n" % e)
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
api_instance = cons3rt.CategoriesApi(cons3rt.ApiClient(configuration))

try:
    # List all Categories
    api_response = api_instance.get_categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MinimalCategory]**](MinimalCategory.md)

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

# **remove_category_from_asset**
> bool remove_category_from_asset(id, assetid)

Unassign Category from Asset

Removes the Category as a filter tag from the provided Asset.<br> <br> Altering the Category will affect future Asset filtering.

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
api_instance = cons3rt.CategoriesApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of category
assetid = 'assetid_example' # str | ID of asset to unassign

try:
    # Unassign Category from Asset
    api_response = api_instance.remove_category_from_asset(id, assetid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->remove_category_from_asset: %s\n" % e)
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
api_instance = cons3rt.CategoriesApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of category
assetid = 'assetid_example' # str | ID of asset to unassign

try:
    # Unassign Category from Asset
    api_response = api_instance.remove_category_from_asset(id, assetid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->remove_category_from_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of category | 
 **assetid** | **str**| ID of asset to unassign | 

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
**400** | Invalid category ID or asset ID supplied |  -  |
**404** | Category not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_category_parent**
> FullCategory set_category_parent(id, parentid)

Set Parent Category

Sets the Parent for an existing Category

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
api_instance = cons3rt.CategoriesApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of category to modify
parentid = 'parentid_example' # str | ID of desired parent category

try:
    # Set Parent Category
    api_response = api_instance.set_category_parent(id, parentid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->set_category_parent: %s\n" % e)
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
api_instance = cons3rt.CategoriesApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of category to modify
parentid = 'parentid_example' # str | ID of desired parent category

try:
    # Set Parent Category
    api_response = api_instance.set_category_parent(id, parentid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->set_category_parent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of category to modify | 
 **parentid** | **str**| ID of desired parent category | 

### Return type

[**FullCategory**](FullCategory.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid category ID or parent category ID supplied |  -  |
**404** | Category not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_category**
> FullCategory update_category(id, input_category=input_category)

Update Category

Updates the content of a single Category with the given ID.

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
api_instance = cons3rt.CategoriesApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of Category to update
input_category = cons3rt.InputCategory() # InputCategory | The modified Category definition (optional)

try:
    # Update Category
    api_response = api_instance.update_category(id, input_category=input_category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->update_category: %s\n" % e)
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
api_instance = cons3rt.CategoriesApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of Category to update
input_category = cons3rt.InputCategory() # InputCategory | The modified Category definition (optional)

try:
    # Update Category
    api_response = api_instance.update_category(id, input_category=input_category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->update_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Category to update | 
 **input_category** | [**InputCategory**](InputCategory.md)| The modified Category definition | [optional] 

### Return type

[**FullCategory**](FullCategory.md)

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
**404** | Category not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

