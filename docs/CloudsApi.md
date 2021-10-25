# cons3rt.CloudsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_project**](CloudsApi.md#add_project) | **PUT** /api/virtualizationrealms/{id}/projects | Assign Project
[**allocate_virtualization_realm**](CloudsApi.md#allocate_virtualization_realm) | **POST** /api/clouds/{id}/virtualizationrealms/allocate | Allocate Virtualization Realm
[**assign_managing_team**](CloudsApi.md#assign_managing_team) | **PUT** /api/clouds/{id}/virtualizationrealms/{virtualizationRealmId}/team | Assign Virtualization Realm-managing Team
[**deallocate_virt_realm**](CloudsApi.md#deallocate_virt_realm) | **DELETE** /api/clouds/{id}/virtualizationrealms/allocate | De-allocate Virtualization Realm
[**delete_cloud**](CloudsApi.md#delete_cloud) | **DELETE** /api/clouds/{id} | Delete Cloud
[**enable_maintence_mode**](CloudsApi.md#enable_maintence_mode) | **PUT** /api/clouds/{id}/maintenance | Update Maintenance Mode
[**get_cloud**](CloudsApi.md#get_cloud) | **GET** /api/clouds/{id} | Retrieve Cloud
[**get_cloud_resources**](CloudsApi.md#get_cloud_resources) | **GET** /api/clouds/{id}/resources | Retrieve Cloud Resources
[**get_clouds**](CloudsApi.md#get_clouds) | **GET** /api/clouds | List Clouds
[**get_default_network**](CloudsApi.md#get_default_network) | **GET** /api/clouds/defaultnetwork | Retrieve Default Network
[**get_edge_gateway_i_ps**](CloudsApi.md#get_edge_gateway_i_ps) | **GET** /api/clouds/{id}/edgegateways | List Edge Gateways
[**list_virt_realms_in_cloud**](CloudsApi.md#list_virt_realms_in_cloud) | **GET** /api/clouds/{id}/virtualizationrealms | List Virtualization Realms
[**register_cloud**](CloudsApi.md#register_cloud) | **POST** /api/clouds | Create Cloud
[**register_virtualization_realm**](CloudsApi.md#register_virtualization_realm) | **POST** /api/clouds/{id}/virtualizationrealms | Register Virtualization Realm
[**remove_virt_realm**](CloudsApi.md#remove_virt_realm) | **DELETE** /api/clouds/{id}/virtualizationrealms | Unregister Virtualization Realm
[**unassign_managing_team**](CloudsApi.md#unassign_managing_team) | **DELETE** /api/clouds/{id}/virtualizationrealms/{virtualizationRealmId}/team | Unassign Manager from Team
[**update_cloud**](CloudsApi.md#update_cloud) | **PUT** /api/clouds/{id} | Update Cloud Content
[**update_virt_realm**](CloudsApi.md#update_virt_realm) | **PUT** /api/clouds/{id}/virtualizationrealms | Update Virtualization Realm
[**update_virtualization_realm**](CloudsApi.md#update_virtualization_realm) | **PUT** /api/virtualizationrealms/{id} | Update Virtualization Realm
[**update_virtualization_realm_maximum_impact_level**](CloudsApi.md#update_virtualization_realm_maximum_impact_level) | **PUT** /api/clouds/{id}/impactlevel | Update Impact Level


# **add_project**
> int add_project(id, project_id)

Assign Project

Provides members of the Project with access to the specified Virtualization Realm

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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
project_id = 'project_id_example' # str | ID of project to assign

    try:
        # Assign Project
        api_response = api_instance.add_project(id, project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->add_project: %s\n" % e)
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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
project_id = 'project_id_example' # str | ID of project to assign

    try:
        # Assign Project
        api_response = api_instance.add_project(id, project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->add_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of virtualization realm | 
 **project_id** | **str**| ID of project to assign | 

### Return type

**int**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid virtualization realm ID or project ID supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **allocate_virtualization_realm**
> MinimalVirtualizationRealm allocate_virtualization_realm(id, abstract_cloud_space_request)

Allocate Virtualization Realm

Adds a Virtualization Realm as part of the specified Cloud.<br> <br> Since this call results in the construction of a new Virtualization Realm, it has financial implications and should not be used if the user is not prepared to incur the expense of construction and existence of the newly created Virtualization Realm.

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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud
abstract_cloud_space_request = cons3rt.AbstractCloudSpaceRequest() # AbstractCloudSpaceRequest | The virtualization realm allocation information

    try:
        # Allocate Virtualization Realm
        api_response = api_instance.allocate_virtualization_realm(id, abstract_cloud_space_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->allocate_virtualization_realm: %s\n" % e)
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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud
abstract_cloud_space_request = cons3rt.AbstractCloudSpaceRequest() # AbstractCloudSpaceRequest | The virtualization realm allocation information

    try:
        # Allocate Virtualization Realm
        api_response = api_instance.allocate_virtualization_realm(id, abstract_cloud_space_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->allocate_virtualization_realm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of cloud | 
 **abstract_cloud_space_request** | [**AbstractCloudSpaceRequest**](AbstractCloudSpaceRequest.md)| The virtualization realm allocation information | 

### Return type

[**MinimalVirtualizationRealm**](MinimalVirtualizationRealm.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid cloud ID or data supplied |  -  |
**404** | Cloud not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_managing_team**
> bool assign_managing_team(id, virtualization_realm_id, team_id)

Assign Virtualization Realm-managing Team

Assigns the provided Team as a Manager of the Virtualization Realm belonging to the specified Cloud.

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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud
virtualization_realm_id = 'virtualization_realm_id_example' # str | ID of virtualization realm
team_id = 56 # int | ID of team to assign

    try:
        # Assign Virtualization Realm-managing Team
        api_response = api_instance.assign_managing_team(id, virtualization_realm_id, team_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->assign_managing_team: %s\n" % e)
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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud
virtualization_realm_id = 'virtualization_realm_id_example' # str | ID of virtualization realm
team_id = 56 # int | ID of team to assign

    try:
        # Assign Virtualization Realm-managing Team
        api_response = api_instance.assign_managing_team(id, virtualization_realm_id, team_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->assign_managing_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of cloud | 
 **virtualization_realm_id** | **str**| ID of virtualization realm | 
 **team_id** | **int**| ID of team to assign | 

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
**400** | Invalid cloud ID, virtualization realm ID, or team ID supplied |  -  |
**404** | Cloud not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deallocate_virt_realm**
> bool deallocate_virt_realm(id, virt_realm_id)

De-allocate Virtualization Realm

Removes an existing Virtualization Realm from the specified Cloud and destroys the resources in the back-end.

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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud
virt_realm_id = 'virt_realm_id_example' # str | ID of virtualization realm

    try:
        # De-allocate Virtualization Realm
        api_response = api_instance.deallocate_virt_realm(id, virt_realm_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->deallocate_virt_realm: %s\n" % e)
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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud
virt_realm_id = 'virt_realm_id_example' # str | ID of virtualization realm

    try:
        # De-allocate Virtualization Realm
        api_response = api_instance.deallocate_virt_realm(id, virt_realm_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->deallocate_virt_realm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of cloud | 
 **virt_realm_id** | **str**| ID of virtualization realm | 

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
**400** | Invalid cloud ID or virtualization realm ID supplied |  -  |
**404** | Cloud not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud**
> bool delete_cloud(id)

Delete Cloud

Deletes the content of a single Cloud with the given ID.

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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud

    try:
        # Delete Cloud
        api_response = api_instance.delete_cloud(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->delete_cloud: %s\n" % e)
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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud

    try:
        # Delete Cloud
        api_response = api_instance.delete_cloud(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->delete_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of cloud | 

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
**400** | Invalid ID or data supplied |  -  |
**404** | Cloud not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_maintence_mode**
> bool enable_maintence_mode(id, enable=enable, maintenance_mode_request=maintenance_mode_request)

Update Maintenance Mode

Updates the Maintenance status for a single Cloud by the given ID.

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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud
enable = True # bool | Enable or disable maintenance mode (optional)
maintenance_mode_request = cons3rt.MaintenanceModeRequest() # MaintenanceModeRequest | The maintenance mode request, when enabling maintenance mode (optional)

    try:
        # Update Maintenance Mode
        api_response = api_instance.enable_maintence_mode(id, enable=enable, maintenance_mode_request=maintenance_mode_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->enable_maintence_mode: %s\n" % e)
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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud
enable = True # bool | Enable or disable maintenance mode (optional)
maintenance_mode_request = cons3rt.MaintenanceModeRequest() # MaintenanceModeRequest | The maintenance mode request, when enabling maintenance mode (optional)

    try:
        # Update Maintenance Mode
        api_response = api_instance.enable_maintence_mode(id, enable=enable, maintenance_mode_request=maintenance_mode_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->enable_maintence_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of cloud | 
 **enable** | **bool**| Enable or disable maintenance mode | [optional] 
 **maintenance_mode_request** | [**MaintenanceModeRequest**](MaintenanceModeRequest.md)| The maintenance mode request, when enabling maintenance mode | [optional] 

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
**400** | Invalid cloud ID or data supplied |  -  |
**404** | Cloud not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud**
> FullCloud get_cloud(id)

Retrieve Cloud

Returns a single Cloud by the given ID.

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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud

    try:
        # Retrieve Cloud
        api_response = api_instance.get_cloud(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->get_cloud: %s\n" % e)
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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud

    try:
        # Retrieve Cloud
        api_response = api_instance.get_cloud(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->get_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of cloud | 

### Return type

[**FullCloud**](FullCloud.md)

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
**404** | Cloud not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_resources**
> AbstractCloudResources get_cloud_resources(id)

Retrieve Cloud Resources

Returns the back-end resources for a single Cloud by the given ID.

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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud

    try:
        # Retrieve Cloud Resources
        api_response = api_instance.get_cloud_resources(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->get_cloud_resources: %s\n" % e)
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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud

    try:
        # Retrieve Cloud Resources
        api_response = api_instance.get_cloud_resources(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->get_cloud_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of cloud | 

### Return type

[**AbstractCloudResources**](AbstractCloudResources.md)

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
**404** | Cloud not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clouds**
> list[MinimalCloud] get_clouds(maxresults=maxresults, page=page)

List Clouds

Returns a collection of the Clouds you manage.

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
    api_instance = cons3rt.CloudsApi(api_client)
    maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

    try:
        # List Clouds
        api_response = api_instance.get_clouds(maxresults=maxresults, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->get_clouds: %s\n" % e)
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
    api_instance = cons3rt.CloudsApi(api_client)
    maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

    try:
        # List Clouds
        api_response = api_instance.get_clouds(maxresults=maxresults, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->get_clouds: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_network**
> Network get_default_network()

Retrieve Default Network

Returns the default CONS3RT Network definition used by all Clouds.

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
    api_instance = cons3rt.CloudsApi(api_client)
    
    try:
        # Retrieve Default Network
        api_response = api_instance.get_default_network()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->get_default_network: %s\n" % e)
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
    api_instance = cons3rt.CloudsApi(api_client)
    
    try:
        # Retrieve Default Network
        api_response = api_instance.get_default_network()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->get_default_network: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Network**](Network.md)

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

# **get_edge_gateway_i_ps**
> list[str] get_edge_gateway_i_ps(id)

List Edge Gateways

Returns a collection of the Edge Gateway IP addresses belonging to the specified Cloud.

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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud

    try:
        # List Edge Gateways
        api_response = api_instance.get_edge_gateway_i_ps(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->get_edge_gateway_i_ps: %s\n" % e)
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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud

    try:
        # List Edge Gateways
        api_response = api_instance.get_edge_gateway_i_ps(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->get_edge_gateway_i_ps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of cloud | 

### Return type

**list[str]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid cloud ID supplied |  -  |
**404** | Cloud not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virt_realms_in_cloud**
> list[MinimalVirtualizationRealm] list_virt_realms_in_cloud(id, maxresults=maxresults, page=page)

List Virtualization Realms

Returns a collection of the Virtualization Realms belonging to the specified Cloud.

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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

    try:
        # List Virtualization Realms
        api_response = api_instance.list_virt_realms_in_cloud(id, maxresults=maxresults, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->list_virt_realms_in_cloud: %s\n" % e)
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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

    try:
        # List Virtualization Realms
        api_response = api_instance.list_virt_realms_in_cloud(id, maxresults=maxresults, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->list_virt_realms_in_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of cloud | 
 **maxresults** | **int**| Maximum number of results to return | [optional] [default to 40]
 **page** | **int**| Requested page number | [optional] [default to 0]

### Return type

[**list[MinimalVirtualizationRealm]**](MinimalVirtualizationRealm.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid cloud ID supplied |  -  |
**404** | Cloud not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_cloud**
> str register_cloud(cloud_ato_consent=cloud_ato_consent, input_cloud=input_cloud)

Create Cloud

Creates a single Cloud.<br> <br> <strong>Cloud Authority To Operate (ATO) Consent.</strong> <br> <p>Teams are allowed to register their own Clouds and to use the site capabilities to allocate Cloudspaces, configure security, and deploy Systems & Services and/or access them remotely.  However, without a Memorandum of Understanding (MOU) or Memorandum of Agreement (MOA) with the site owner, customer-owned Clouds and Cloudspaces are not covered by the site Authority To Operate (ATO). Customers are responsible for compliance with all DoD security requirements for protecting and maintaining their systems.</p> <p>By setting <code>cloudATOConsent</code> to true, the user acknowledges that - as a Team Manager - they a) are authorized to represent their organization, and b) they understand that their organization is responsible for all security and authorization to operate requirements for Systems deployed in their Cloudspaces.</p>

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
    api_instance = cons3rt.CloudsApi(api_client)
    cloud_ato_consent = False # bool | Cloud ATO consent (optional) (default to False)
input_cloud = cons3rt.InputCloud() # InputCloud | The Cloud to create (optional)

    try:
        # Create Cloud
        api_response = api_instance.register_cloud(cloud_ato_consent=cloud_ato_consent, input_cloud=input_cloud)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->register_cloud: %s\n" % e)
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
    api_instance = cons3rt.CloudsApi(api_client)
    cloud_ato_consent = False # bool | Cloud ATO consent (optional) (default to False)
input_cloud = cons3rt.InputCloud() # InputCloud | The Cloud to create (optional)

    try:
        # Create Cloud
        api_response = api_instance.register_cloud(cloud_ato_consent=cloud_ato_consent, input_cloud=input_cloud)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->register_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_ato_consent** | **bool**| Cloud ATO consent | [optional] [default to False]
 **input_cloud** | [**InputCloud**](InputCloud.md)| The Cloud to create | [optional] 

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
**400** | Invalid data supplied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_virtualization_realm**
> int register_virtualization_realm(id, abstract_register_cloud_space_request)

Register Virtualization Realm

Adds an existing Virtualization Realm as part of the specified Cloud

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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud
abstract_register_cloud_space_request = cons3rt.AbstractRegisterCloudSpaceRequest() # AbstractRegisterCloudSpaceRequest | The virtualization realm registration information

    try:
        # Register Virtualization Realm
        api_response = api_instance.register_virtualization_realm(id, abstract_register_cloud_space_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->register_virtualization_realm: %s\n" % e)
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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud
abstract_register_cloud_space_request = cons3rt.AbstractRegisterCloudSpaceRequest() # AbstractRegisterCloudSpaceRequest | The virtualization realm registration information

    try:
        # Register Virtualization Realm
        api_response = api_instance.register_virtualization_realm(id, abstract_register_cloud_space_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->register_virtualization_realm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of cloud | 
 **abstract_register_cloud_space_request** | [**AbstractRegisterCloudSpaceRequest**](AbstractRegisterCloudSpaceRequest.md)| The virtualization realm registration information | 

### Return type

**int**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid cloud ID or data supplied |  -  |
**404** | Cloud not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_virt_realm**
> bool remove_virt_realm(id, virt_realm_id)

Unregister Virtualization Realm

Removes an existing Virtualization Realm from the specified Cloud.

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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud
virt_realm_id = 'virt_realm_id_example' # str | ID of virtualization realm

    try:
        # Unregister Virtualization Realm
        api_response = api_instance.remove_virt_realm(id, virt_realm_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->remove_virt_realm: %s\n" % e)
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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud
virt_realm_id = 'virt_realm_id_example' # str | ID of virtualization realm

    try:
        # Unregister Virtualization Realm
        api_response = api_instance.remove_virt_realm(id, virt_realm_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->remove_virt_realm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of cloud | 
 **virt_realm_id** | **str**| ID of virtualization realm | 

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
**400** | Invalid cloud ID or virtualization realm ID supplied |  -  |
**404** | Cloud not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_managing_team**
> bool unassign_managing_team(id, virtualization_realm_id, team_id)

Unassign Manager from Team

Removes the provided Team as a Manager of the Virtualization Realm belonging to the specified Cloud.

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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud
virtualization_realm_id = 'virtualization_realm_id_example' # str | ID of virtualization realm
team_id = 56 # int | ID of team to unassign

    try:
        # Unassign Manager from Team
        api_response = api_instance.unassign_managing_team(id, virtualization_realm_id, team_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->unassign_managing_team: %s\n" % e)
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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud
virtualization_realm_id = 'virtualization_realm_id_example' # str | ID of virtualization realm
team_id = 56 # int | ID of team to unassign

    try:
        # Unassign Manager from Team
        api_response = api_instance.unassign_managing_team(id, virtualization_realm_id, team_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->unassign_managing_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of cloud | 
 **virtualization_realm_id** | **str**| ID of virtualization realm | 
 **team_id** | **int**| ID of team to unassign | 

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
**400** | Invalid cloud ID, virtualization realm ID, or team ID supplied |  -  |
**404** | Cloud not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud**
> bool update_cloud(id, input_cloud=input_cloud)

Update Cloud Content

Updates the content of a single Cloud with the given ID.

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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud
input_cloud = cons3rt.InputCloud() # InputCloud | The modified Cloud data (optional)

    try:
        # Update Cloud Content
        api_response = api_instance.update_cloud(id, input_cloud=input_cloud)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->update_cloud: %s\n" % e)
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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud
input_cloud = cons3rt.InputCloud() # InputCloud | The modified Cloud data (optional)

    try:
        # Update Cloud Content
        api_response = api_instance.update_cloud(id, input_cloud=input_cloud)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->update_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of cloud | 
 **input_cloud** | [**InputCloud**](InputCloud.md)| The modified Cloud data | [optional] 

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
**400** | Invalid ID or data supplied |  -  |
**404** | Cloud not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_virt_realm**
> bool update_virt_realm(id, virt_realm_id, input_virtualization_realm)

Update Virtualization Realm

Updates the content of a single Virtualization Realm within the specified Cloud.

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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud
virt_realm_id = 'virt_realm_id_example' # str | ID of virtualization realm
input_virtualization_realm = cons3rt.InputVirtualizationRealm() # InputVirtualizationRealm | The modified virtualization realm information

    try:
        # Update Virtualization Realm
        api_response = api_instance.update_virt_realm(id, virt_realm_id, input_virtualization_realm)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->update_virt_realm: %s\n" % e)
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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud
virt_realm_id = 'virt_realm_id_example' # str | ID of virtualization realm
input_virtualization_realm = cons3rt.InputVirtualizationRealm() # InputVirtualizationRealm | The modified virtualization realm information

    try:
        # Update Virtualization Realm
        api_response = api_instance.update_virt_realm(id, virt_realm_id, input_virtualization_realm)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->update_virt_realm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of cloud | 
 **virt_realm_id** | **str**| ID of virtualization realm | 
 **input_virtualization_realm** | [**InputVirtualizationRealm**](InputVirtualizationRealm.md)| The modified virtualization realm information | 

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
**400** | Invalid cloud ID, virtualization realm ID, or data supplied |  -  |
**404** | Cloud not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_virtualization_realm**
> bool update_virtualization_realm(id, input_vr_admin_virtualization_realm=input_vr_admin_virtualization_realm)

Update Virtualization Realm

Updates the content of a single Virtualization Realm with the given ID.

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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
input_vr_admin_virtualization_realm = cons3rt.InputVRAdminVirtualizationRealm() # InputVRAdminVirtualizationRealm | The updated Virtualization Realm data (optional)

    try:
        # Update Virtualization Realm
        api_response = api_instance.update_virtualization_realm(id, input_vr_admin_virtualization_realm=input_vr_admin_virtualization_realm)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->update_virtualization_realm: %s\n" % e)
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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
input_vr_admin_virtualization_realm = cons3rt.InputVRAdminVirtualizationRealm() # InputVRAdminVirtualizationRealm | The updated Virtualization Realm data (optional)

    try:
        # Update Virtualization Realm
        api_response = api_instance.update_virtualization_realm(id, input_vr_admin_virtualization_realm=input_vr_admin_virtualization_realm)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->update_virtualization_realm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of virtualization realm | 
 **input_vr_admin_virtualization_realm** | [**InputVRAdminVirtualizationRealm**](InputVRAdminVirtualizationRealm.md)| The updated Virtualization Realm data | [optional] 

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
**400** | Invalid ID or data supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_virtualization_realm_maximum_impact_level**
> bool update_virtualization_realm_maximum_impact_level(id, maximumimpactlevel)

Update Impact Level

Updates the maximum Impact Level of the Cloud with the given ID.<br> <br> If specified, this value will prevent Deployments containing Assets whose declared Impact Level is greater than the maximum allowed Impact Level from being run in this Virtualization Realm.<br> <br> Maximum Impact Level can only be set to DOD_LEVEL_6 if allowed in the environment.

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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud
maximumimpactlevel = 'maximumimpactlevel_example' # str | The maximum impact level type.

    try:
        # Update Impact Level
        api_response = api_instance.update_virtualization_realm_maximum_impact_level(id, maximumimpactlevel)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->update_virtualization_realm_maximum_impact_level: %s\n" % e)
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
    api_instance = cons3rt.CloudsApi(api_client)
    id = 'id_example' # str | ID of cloud
maximumimpactlevel = 'maximumimpactlevel_example' # str | The maximum impact level type.

    try:
        # Update Impact Level
        api_response = api_instance.update_virtualization_realm_maximum_impact_level(id, maximumimpactlevel)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudsApi->update_virtualization_realm_maximum_impact_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of cloud | 
 **maximumimpactlevel** | **str**| The maximum impact level type. | 

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
**400** | Invalid ID or impact level supplied |  -  |
**404** | Cloud not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

