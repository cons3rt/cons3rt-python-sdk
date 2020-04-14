# cons3rt.VirtualizationRealmsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_network**](VirtualizationRealmsApi.md#add_network) | **POST** /api/virtualizationrealms/{id}/networks | Allocate Network
[**add_project**](VirtualizationRealmsApi.md#add_project) | **PUT** /api/virtualizationrealms/{id}/projects | Assign Project
[**create_template_subsciption**](VirtualizationRealmsApi.md#create_template_subsciption) | **POST** /api/virtualizationrealms/{id}/templates/subscriptions | Create Template Subscription
[**delete_network**](VirtualizationRealmsApi.md#delete_network) | **DELETE** /api/virtualizationrealms/{id}/networks/{networkId} | Delete Network
[**delete_template_subscription**](VirtualizationRealmsApi.md#delete_template_subscription) | **DELETE** /api/virtualizationrealms/{id}/templates/subscriptions/{subscription_id} | Delete Template Subscription
[**disable_virt_realm_remote_access**](VirtualizationRealmsApi.md#disable_virt_realm_remote_access) | **DELETE** /api/virtualizationrealms/{id}/remoteaccess | Disable Remote Access
[**enable_maintence_mode1**](VirtualizationRealmsApi.md#enable_maintence_mode1) | **PUT** /api/virtualizationrealms/{id}/maintenance | Update Maintenance Mode
[**enable_virt_realm_remote_access**](VirtualizationRealmsApi.md#enable_virt_realm_remote_access) | **POST** /api/virtualizationrealms/{id}/remoteaccess | Enable Remote Access
[**get_deployment_runs_in_virtualization_realm**](VirtualizationRealmsApi.md#get_deployment_runs_in_virtualization_realm) | **GET** /api/virtualizationrealms/{id}/deploymentruns | List Deployment Runs
[**get_host_configuration_metrics1**](VirtualizationRealmsApi.md#get_host_configuration_metrics1) | **GET** /api/virtualizationrealms/{id}/metrics/hostconfiguration | Retrieve Metrics
[**get_network**](VirtualizationRealmsApi.md#get_network) | **GET** /api/virtualizationrealms/{id}/networks/{networkId} | Retrieve Network
[**get_networks**](VirtualizationRealmsApi.md#get_networks) | **GET** /api/virtualizationrealms/{id}/networks | List Networks
[**get_template_subscription**](VirtualizationRealmsApi.md#get_template_subscription) | **GET** /api/virtualizationrealms/{id}/templates/subscriptions/{subscription_id} | Retrieve Template Subscription
[**get_templates_in_virtualization_realm**](VirtualizationRealmsApi.md#get_templates_in_virtualization_realm) | **GET** /api/virtualizationrealms/{id}/templates | List Templates
[**get_unregistered_networks**](VirtualizationRealmsApi.md#get_unregistered_networks) | **GET** /api/virtualizationrealms/{id}/networks/unregistered | List Unregistered Networks
[**get_virtual_machine_count_metrics1**](VirtualizationRealmsApi.md#get_virtual_machine_count_metrics1) | **GET** /api/virtualizationrealms/{id}/metrics/virtualmachinecount | Retrieve Virtual Machine Metrics
[**get_virtualization_realm**](VirtualizationRealmsApi.md#get_virtualization_realm) | **GET** /api/virtualizationrealms/{id} | Retrieve Virtualization Realm
[**get_virtualization_realm_resources**](VirtualizationRealmsApi.md#get_virtualization_realm_resources) | **GET** /api/virtualizationrealms/{id}/resources | Retrieve Virtualization Realm Resources
[**get_virtualization_realms**](VirtualizationRealmsApi.md#get_virtualization_realms) | **GET** /api/virtualizationrealms | List Virtualization Realms
[**invalidate_template_cache_in_virtualization_realm**](VirtualizationRealmsApi.md#invalidate_template_cache_in_virtualization_realm) | **PUT** /api/virtualizationrealms/{id}/templates/registrations | Refresh Template Cache
[**list_pending_template_subscriptions**](VirtualizationRealmsApi.md#list_pending_template_subscriptions) | **GET** /api/virtualizationrealms/{id}/templates/subscriptions/pending | List Pending Subscriptions
[**list_projects**](VirtualizationRealmsApi.md#list_projects) | **GET** /api/virtualizationrealms/{id}/projects | List Projects
[**list_template_registrations**](VirtualizationRealmsApi.md#list_template_registrations) | **GET** /api/virtualizationrealms/{id}/templates/registrations | List Template Registrations
[**list_template_subscriptions**](VirtualizationRealmsApi.md#list_template_subscriptions) | **GET** /api/virtualizationrealms/{id}/templates/subscriptions | List Template Subscriptions
[**list_unregistered_templates**](VirtualizationRealmsApi.md#list_unregistered_templates) | **GET** /api/virtualizationrealms/{id}/templates/registrations/pending | List Unregistered Templates
[**redeploy_edges**](VirtualizationRealmsApi.md#redeploy_edges) | **PUT** /api/virtualizationrealms/{id}/networks/redeployedges | Re-deploy Network Edge Devices
[**register_network**](VirtualizationRealmsApi.md#register_network) | **PUT** /api/virtualizationrealms/{id}/networks/{networkIdentifier} | Register Network
[**register_template**](VirtualizationRealmsApi.md#register_template) | **POST** /api/virtualizationrealms/{id}/templates/registrations | Register Template
[**remove_project**](VirtualizationRealmsApi.md#remove_project) | **DELETE** /api/virtualizationrealms/{id}/projects | Unassign Project
[**retrieve_template_registration**](VirtualizationRealmsApi.md#retrieve_template_registration) | **GET** /api/virtualizationrealms/{id}/templates/registrations/{registration_id} | Retrieve Template Registration
[**set_virtualization_realm_active**](VirtualizationRealmsApi.md#set_virtualization_realm_active) | **PUT** /api/virtualizationrealms/{id}/activate | Update State
[**share_template_registration**](VirtualizationRealmsApi.md#share_template_registration) | **POST** /api/virtualizationrealms/{id}/templates/registrations/{registration_id}/share | Share Template
[**unregister_template**](VirtualizationRealmsApi.md#unregister_template) | **DELETE** /api/virtualizationrealms/{id}/templates/registrations/{registration_id} | Delete Template Registration
[**unshare_template_registration**](VirtualizationRealmsApi.md#unshare_template_registration) | **DELETE** /api/virtualizationrealms/{id}/templates/registrations/{registration_id}/share | Unshare Template
[**update_template_registration**](VirtualizationRealmsApi.md#update_template_registration) | **PUT** /api/virtualizationrealms/{id}/templates/registrations/{registration_id} | Update Template Registration
[**update_template_subscription**](VirtualizationRealmsApi.md#update_template_subscription) | **PUT** /api/virtualizationrealms/{id}/templates/subscriptions/{subscription_id} | Update Template Subscription
[**update_virt_realm_remote_access_config**](VirtualizationRealmsApi.md#update_virt_realm_remote_access_config) | **PUT** /api/virtualizationrealms/{id}/remoteaccess | Update Remote Access
[**update_virtualization_realm**](VirtualizationRealmsApi.md#update_virtualization_realm) | **PUT** /api/virtualizationrealms/{id} | Update Virtualization Realm
[**update_virtualization_realm_reachability**](VirtualizationRealmsApi.md#update_virtualization_realm_reachability) | **PUT** /api/virtualizationrealms/{id}/updatereachability | 


# **add_network**
> MinimalVirtualizationRealm add_network(id, abstract_add_network_cloud_space_request)

Allocate Network

Adds a Network to the specified Virtualization Realm.<br> <br> Since this call results in the construction of a new, back-end Network it has financial implications and should not be used if the user is not prepared to incur the expense of construction and existence of the newly created Network.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
abstract_add_network_cloud_space_request = cons3rt.AbstractAddNetworkCloudSpaceRequest() # AbstractAddNetworkCloudSpaceRequest | The network allocation information

    try:
        # Allocate Network
        api_response = api_instance.add_network(id, abstract_add_network_cloud_space_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->add_network: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
abstract_add_network_cloud_space_request = cons3rt.AbstractAddNetworkCloudSpaceRequest() # AbstractAddNetworkCloudSpaceRequest | The network allocation information

    try:
        # Allocate Network
        api_response = api_instance.add_network(id, abstract_add_network_cloud_space_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->add_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of virtualization realm | 
 **abstract_add_network_cloud_space_request** | [**AbstractAddNetworkCloudSpaceRequest**](AbstractAddNetworkCloudSpaceRequest.md)| The network allocation information | 

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
**400** | Invalid virtualization realm ID or data supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
project_id = 'project_id_example' # str | ID of project to assign

    try:
        # Assign Project
        api_response = api_instance.add_project(id, project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->add_project: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
project_id = 'project_id_example' # str | ID of project to assign

    try:
        # Assign Project
        api_response = api_instance.add_project(id, project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->add_project: %s\n" % e)
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

# **create_template_subsciption**
> FullTemplateSubscription create_template_subsciption(id, registration_id)

Create Template Subscription

Creates a Template Subscription in the specified Virtualization Realm.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm
registration_id = 56 # int | ID of template registration

    try:
        # Create Template Subscription
        api_response = api_instance.create_template_subsciption(id, registration_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->create_template_subsciption: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm
registration_id = 56 # int | ID of template registration

    try:
        # Create Template Subscription
        api_response = api_instance.create_template_subsciption(id, registration_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->create_template_subsciption: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of virtualization realm | 
 **registration_id** | **int**| ID of template registration | 

### Return type

[**FullTemplateSubscription**](FullTemplateSubscription.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid virtualization realm ID or template registration ID supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network**
> bool delete_network(id, network_id, deallocate=deallocate)

Delete Network

Removes an existing Network from the specified Virtualization Realm.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
network_id = 56 # int | ID of network
deallocate = False # bool | Attempt to delete all back-end resources (optional) (default to False)

    try:
        # Delete Network
        api_response = api_instance.delete_network(id, network_id, deallocate=deallocate)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->delete_network: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
network_id = 56 # int | ID of network
deallocate = False # bool | Attempt to delete all back-end resources (optional) (default to False)

    try:
        # Delete Network
        api_response = api_instance.delete_network(id, network_id, deallocate=deallocate)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->delete_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of virtualization realm | 
 **network_id** | **int**| ID of network | 
 **deallocate** | **bool**| Attempt to delete all back-end resources | [optional] [default to False]

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
**400** | Invalid virtualization realm ID or network ID supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_subscription**
> bool delete_template_subscription(id, subscription_id)

Delete Template Subscription

Removes an existing Template Subscription from the specified Virtualization Realm.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm
subscription_id = 56 # int | ID of template subscription

    try:
        # Delete Template Subscription
        api_response = api_instance.delete_template_subscription(id, subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->delete_template_subscription: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm
subscription_id = 56 # int | ID of template subscription

    try:
        # Delete Template Subscription
        api_response = api_instance.delete_template_subscription(id, subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->delete_template_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of virtualization realm | 
 **subscription_id** | **int**| ID of template subscription | 

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
**400** | Invalid virtualization realm ID or template subscription ID supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_virt_realm_remote_access**
> bool disable_virt_realm_remote_access(id)

Disable Remote Access

Disables Remote Access for a single Virtualization Realm by the given ID.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm

    try:
        # Disable Remote Access
        api_response = api_instance.disable_virt_realm_remote_access(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->disable_virt_realm_remote_access: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm

    try:
        # Disable Remote Access
        api_response = api_instance.disable_virt_realm_remote_access(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->disable_virt_realm_remote_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of virtualization realm | 

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
**400** | Invalid virtualization realm ID or data supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_maintence_mode1**
> bool enable_maintence_mode1(id, enable=enable, maintenance_mode_request=maintenance_mode_request)

Update Maintenance Mode

Updates the maintenance status for a single Virtualization Realm by the given ID.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
enable = True # bool | Enable or disable maintenance mode (optional)
maintenance_mode_request = cons3rt.MaintenanceModeRequest() # MaintenanceModeRequest | The maintenance mode request, when enabling maintenance mode (optional)

    try:
        # Update Maintenance Mode
        api_response = api_instance.enable_maintence_mode1(id, enable=enable, maintenance_mode_request=maintenance_mode_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->enable_maintence_mode1: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
enable = True # bool | Enable or disable maintenance mode (optional)
maintenance_mode_request = cons3rt.MaintenanceModeRequest() # MaintenanceModeRequest | The maintenance mode request, when enabling maintenance mode (optional)

    try:
        # Update Maintenance Mode
        api_response = api_instance.enable_maintence_mode1(id, enable=enable, maintenance_mode_request=maintenance_mode_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->enable_maintence_mode1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of virtualization realm | 
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
**400** | Invalid virtualization realm ID or data supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_virt_realm_remote_access**
> bool enable_virt_realm_remote_access(id, instance_type=instance_type)

Enable Remote Access

Enables Remote Access for a single Virtualization Realm by the given ID.<br> <br> To do so, Remote Access must be configured for the Virtualization Realm.<br> <br> If no instanceType is provided, the Instance Type will first attempt to use the value from the Virtualization Realm's Remote Access config.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
instance_type = 'instance_type_example' # str | Remote access server instance type (optional)

    try:
        # Enable Remote Access
        api_response = api_instance.enable_virt_realm_remote_access(id, instance_type=instance_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->enable_virt_realm_remote_access: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
instance_type = 'instance_type_example' # str | Remote access server instance type (optional)

    try:
        # Enable Remote Access
        api_response = api_instance.enable_virt_realm_remote_access(id, instance_type=instance_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->enable_virt_realm_remote_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of virtualization realm | 
 **instance_type** | **str**| Remote access server instance type | [optional] 

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
**400** | Invalid virtualization realm ID or data supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_runs_in_virtualization_realm**
> list[MinimalDeploymentRun] get_deployment_runs_in_virtualization_realm(id, search_type, maxresults=maxresults, page=page)

List Deployment Runs

Returns a collection of the Deployment Runs launched into the specified Virtualization Realm.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
search_type = 'SEARCH_ALL' # str | Deployment run status type (default to 'SEARCH_ALL')
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

    try:
        # List Deployment Runs
        api_response = api_instance.get_deployment_runs_in_virtualization_realm(id, search_type, maxresults=maxresults, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->get_deployment_runs_in_virtualization_realm: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
search_type = 'SEARCH_ALL' # str | Deployment run status type (default to 'SEARCH_ALL')
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

    try:
        # List Deployment Runs
        api_response = api_instance.get_deployment_runs_in_virtualization_realm(id, search_type, maxresults=maxresults, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->get_deployment_runs_in_virtualization_realm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of virtualization realm | 
 **search_type** | **str**| Deployment run status type | [default to &#39;SEARCH_ALL&#39;]
 **maxresults** | **int**| Maximum number of results to return | [optional] [default to 40]
 **page** | **int**| Requested page number | [optional] [default to 0]

### Return type

[**list[MinimalDeploymentRun]**](MinimalDeploymentRun.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid virtualization realm ID or query parameter supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_host_configuration_metrics1**
> str get_host_configuration_metrics1(id, start, end, interval=interval, interval_unit=interval_unit)

Retrieve Metrics

Returns metric data for Deployment Runs launched into the specified Virtualization Realm.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
start = 56 # int | Interval start time, specified in seconds since epoch
end = 56 # int | Interval end time, specified in seconds since epoch
interval = 1 # int | Number of intervals (optional) (default to 1)
interval_unit = 'HOURS' # str | Interval unit (optional) (default to 'HOURS')

    try:
        # Retrieve Metrics
        api_response = api_instance.get_host_configuration_metrics1(id, start, end, interval=interval, interval_unit=interval_unit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->get_host_configuration_metrics1: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
start = 56 # int | Interval start time, specified in seconds since epoch
end = 56 # int | Interval end time, specified in seconds since epoch
interval = 1 # int | Number of intervals (optional) (default to 1)
interval_unit = 'HOURS' # str | Interval unit (optional) (default to 'HOURS')

    try:
        # Retrieve Metrics
        api_response = api_instance.get_host_configuration_metrics1(id, start, end, interval=interval, interval_unit=interval_unit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->get_host_configuration_metrics1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of virtualization realm | 
 **start** | **int**| Interval start time, specified in seconds since epoch | 
 **end** | **int**| Interval end time, specified in seconds since epoch | 
 **interval** | **int**| Number of intervals | [optional] [default to 1]
 **interval_unit** | **str**| Interval unit | [optional] [default to &#39;HOURS&#39;]

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
**400** | Invalid ID or query parameters supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network**
> Network get_network(id, network_id)

Retrieve Network

Returns a single Network in the specified Virtualization Realm.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
network_id = 56 # int | ID of network

    try:
        # Retrieve Network
        api_response = api_instance.get_network(id, network_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->get_network: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
network_id = 56 # int | ID of network

    try:
        # Retrieve Network
        api_response = api_instance.get_network(id, network_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->get_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of virtualization realm | 
 **network_id** | **int**| ID of network | 

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
**400** | Invalid virtualization realm ID or network ID supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_networks**
> list[MinimalNetwork] get_networks(id)

List Networks

Returns a collection of the Networks in the specified Virtualization Realm.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm

    try:
        # List Networks
        api_response = api_instance.get_networks(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->get_networks: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm

    try:
        # List Networks
        api_response = api_instance.get_networks(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->get_networks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of virtualization realm | 

### Return type

[**list[MinimalNetwork]**](MinimalNetwork.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid virtualization realm ID supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_subscription**
> FullTemplateSubscription get_template_subscription(id, subscription_id)

Retrieve Template Subscription

Returns a single Template Subscription in the specified Virtualization Realm.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm
subscription_id = 56 # int | ID of template subscription

    try:
        # Retrieve Template Subscription
        api_response = api_instance.get_template_subscription(id, subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->get_template_subscription: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm
subscription_id = 56 # int | ID of template subscription

    try:
        # Retrieve Template Subscription
        api_response = api_instance.get_template_subscription(id, subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->get_template_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of virtualization realm | 
 **subscription_id** | **int**| ID of template subscription | 

### Return type

[**FullTemplateSubscription**](FullTemplateSubscription.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid virtualization realm ID or template subscription ID supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_templates_in_virtualization_realm**
> list[MinimalCons3rtTemplateData] get_templates_in_virtualization_realm(id, include_registrations=include_registrations, include_subscriptions=include_subscriptions)

List Templates

Returns a collection of the Templates in the specified Virtualization Realm.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm
include_registrations = True # bool | Include templates registered to the virtualization realm (optional) (default to True)
include_subscriptions = False # bool | Include templates subscribed to by the virtualization realm (optional) (default to False)

    try:
        # List Templates
        api_response = api_instance.get_templates_in_virtualization_realm(id, include_registrations=include_registrations, include_subscriptions=include_subscriptions)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->get_templates_in_virtualization_realm: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm
include_registrations = True # bool | Include templates registered to the virtualization realm (optional) (default to True)
include_subscriptions = False # bool | Include templates subscribed to by the virtualization realm (optional) (default to False)

    try:
        # List Templates
        api_response = api_instance.get_templates_in_virtualization_realm(id, include_registrations=include_registrations, include_subscriptions=include_subscriptions)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->get_templates_in_virtualization_realm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of virtualization realm | 
 **include_registrations** | **bool**| Include templates registered to the virtualization realm | [optional] [default to True]
 **include_subscriptions** | **bool**| Include templates subscribed to by the virtualization realm | [optional] [default to False]

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
**400** | Invalid virtualization realm ID or query parameter supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unregistered_networks**
> list[Subnet] get_unregistered_networks(id)

List Unregistered Networks

Returns a collection of the unregistered, back-end Networks in the specified Virtualization Realm.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm

    try:
        # List Unregistered Networks
        api_response = api_instance.get_unregistered_networks(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->get_unregistered_networks: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm

    try:
        # List Unregistered Networks
        api_response = api_instance.get_unregistered_networks(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->get_unregistered_networks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of virtualization realm | 

### Return type

[**list[Subnet]**](Subnet.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid virtualization realm ID supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_machine_count_metrics1**
> str get_virtual_machine_count_metrics1(id, start, end, interval=interval, interval_unit=interval_unit)

Retrieve Virtual Machine Metrics

Returns metric data for Virtual Machines launched into the specified Virtualization Realm.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
start = 56 # int | Interval start time, specified in seconds since epoch
end = 56 # int | Interval end time, specified in seconds since epoch
interval = 1 # int | Number of intervals (optional) (default to 1)
interval_unit = 'HOURS' # str | Interval unit (optional) (default to 'HOURS')

    try:
        # Retrieve Virtual Machine Metrics
        api_response = api_instance.get_virtual_machine_count_metrics1(id, start, end, interval=interval, interval_unit=interval_unit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->get_virtual_machine_count_metrics1: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
start = 56 # int | Interval start time, specified in seconds since epoch
end = 56 # int | Interval end time, specified in seconds since epoch
interval = 1 # int | Number of intervals (optional) (default to 1)
interval_unit = 'HOURS' # str | Interval unit (optional) (default to 'HOURS')

    try:
        # Retrieve Virtual Machine Metrics
        api_response = api_instance.get_virtual_machine_count_metrics1(id, start, end, interval=interval, interval_unit=interval_unit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->get_virtual_machine_count_metrics1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of virtualization realm | 
 **start** | **int**| Interval start time, specified in seconds since epoch | 
 **end** | **int**| Interval end time, specified in seconds since epoch | 
 **interval** | **int**| Number of intervals | [optional] [default to 1]
 **interval_unit** | **str**| Interval unit | [optional] [default to &#39;HOURS&#39;]

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
**400** | Invalid ID or query parameters supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtualization_realm**
> FullVirtualizationRealm get_virtualization_realm(id)

Retrieve Virtualization Realm

Returns a single Virtualization Realm by the given ID.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm

    try:
        # Retrieve Virtualization Realm
        api_response = api_instance.get_virtualization_realm(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->get_virtualization_realm: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm

    try:
        # Retrieve Virtualization Realm
        api_response = api_instance.get_virtualization_realm(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->get_virtualization_realm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of virtualization realm | 

### Return type

[**FullVirtualizationRealm**](FullVirtualizationRealm.md)

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
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtualization_realm_resources**
> AbstractCloudResources get_virtualization_realm_resources(id)

Retrieve Virtualization Realm Resources

Returns the back-end resources for a single Virtualization Realm by the given ID.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm

    try:
        # Retrieve Virtualization Realm Resources
        api_response = api_instance.get_virtualization_realm_resources(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->get_virtualization_realm_resources: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm

    try:
        # Retrieve Virtualization Realm Resources
        api_response = api_instance.get_virtualization_realm_resources(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->get_virtualization_realm_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of virtualization realm | 

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
**404** | Virtualization Realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtualization_realms**
> list[MinimalVirtualizationRealm] get_virtualization_realms(maxresults=maxresults, page=page)

List Virtualization Realms

Returns a collection of the Virtualization Realms that the user manages.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

    try:
        # List Virtualization Realms
        api_response = api_instance.get_virtualization_realms(maxresults=maxresults, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->get_virtualization_realms: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

    try:
        # List Virtualization Realms
        api_response = api_instance.get_virtualization_realms(maxresults=maxresults, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->get_virtualization_realms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invalidate_template_cache_in_virtualization_realm**
> bool invalidate_template_cache_in_virtualization_realm(id)

Refresh Template Cache

Forces the back-end Template data to be re-read in the specified Virtualization Realm.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm

    try:
        # Refresh Template Cache
        api_response = api_instance.invalidate_template_cache_in_virtualization_realm(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->invalidate_template_cache_in_virtualization_realm: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm

    try:
        # Refresh Template Cache
        api_response = api_instance.invalidate_template_cache_in_virtualization_realm(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->invalidate_template_cache_in_virtualization_realm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of virtualization realm | 

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
**400** | Invalid virtualization realm ID supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pending_template_subscriptions**
> list[FullTemplateRegistrationForSubscription] list_pending_template_subscriptions(id)

List Pending Subscriptions

Returns a collection of the pending Template Subscriptions in the specified Virtualization Realm.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm

    try:
        # List Pending Subscriptions
        api_response = api_instance.list_pending_template_subscriptions(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->list_pending_template_subscriptions: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm

    try:
        # List Pending Subscriptions
        api_response = api_instance.list_pending_template_subscriptions(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->list_pending_template_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of virtualization realm | 

### Return type

[**list[FullTemplateRegistrationForSubscription]**](FullTemplateRegistrationForSubscription.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid virtualization realm ID supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> list[MinimalProject] list_projects(id, maxresults=maxresults, page=page)

List Projects

Returns a collection of the Projects allowed to access to the specified Virtualization Realm.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

    try:
        # List Projects
        api_response = api_instance.list_projects(id, maxresults=maxresults, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->list_projects: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

    try:
        # List Projects
        api_response = api_instance.list_projects(id, maxresults=maxresults, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->list_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of virtualization realm | 
 **maxresults** | **int**| Maximum number of results to return | [optional] [default to 40]
 **page** | **int**| Requested page number | [optional] [default to 0]

### Return type

[**list[MinimalProject]**](MinimalProject.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid virtualization realm ID supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_template_registrations**
> list[MinimalTemplateRegistration] list_template_registrations(id)

List Template Registrations

Returns a collection of the Template Registrations in the specified Virtualization Realm.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm

    try:
        # List Template Registrations
        api_response = api_instance.list_template_registrations(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->list_template_registrations: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm

    try:
        # List Template Registrations
        api_response = api_instance.list_template_registrations(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->list_template_registrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of virtualization realm | 

### Return type

[**list[MinimalTemplateRegistration]**](MinimalTemplateRegistration.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid virtualization realm ID supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_template_subscriptions**
> list[MinimalTemplateSubscription] list_template_subscriptions(id)

List Template Subscriptions

Returns a collection of the Template Subscriptions in the specified Virtualization Realm.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm

    try:
        # List Template Subscriptions
        api_response = api_instance.list_template_subscriptions(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->list_template_subscriptions: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm

    try:
        # List Template Subscriptions
        api_response = api_instance.list_template_subscriptions(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->list_template_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of virtualization realm | 

### Return type

[**list[MinimalTemplateSubscription]**](MinimalTemplateSubscription.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid virtualization realm ID supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_unregistered_templates**
> list[Cons3rtTemplateTagData] list_unregistered_templates(id)

List Unregistered Templates

Returns a collection of the unregistered, back-end Templates in the specified Virtualization Realm.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm

    try:
        # List Unregistered Templates
        api_response = api_instance.list_unregistered_templates(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->list_unregistered_templates: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm

    try:
        # List Unregistered Templates
        api_response = api_instance.list_unregistered_templates(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->list_unregistered_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of virtualization realm | 

### Return type

[**list[Cons3rtTemplateTagData]**](Cons3rtTemplateTagData.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid virtualization realm ID supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeploy_edges**
> bool redeploy_edges(id)

Re-deploy Network Edge Devices

Re-deploys the Network Edge Device(s) in the specified Virtualization Realm.<br> <br> Note: This option is only available in VCloud Virtualization Realms.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm

    try:
        # Re-deploy Network Edge Devices
        api_response = api_instance.redeploy_edges(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->redeploy_edges: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm

    try:
        # Re-deploy Network Edge Devices
        api_response = api_instance.redeploy_edges(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->redeploy_edges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of virtualization realm | 

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
**400** | Invalid virtualization realm ID supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_network**
> bool register_network(id, network_identifier)

Register Network

Adds an existing, back-end Network the specified Virtualization Realm.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
network_identifier = 'network_identifier_example' # str | Back-end network identifier

    try:
        # Register Network
        api_response = api_instance.register_network(id, network_identifier)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->register_network: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
network_identifier = 'network_identifier_example' # str | Back-end network identifier

    try:
        # Register Network
        api_response = api_instance.register_network(id, network_identifier)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->register_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of virtualization realm | 
 **network_identifier** | **str**| Back-end network identifier | 

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
**400** | Invalid virtualization realm ID or network identifier supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_template**
> FullTemplateRegistration register_template(id, input_register_template_object=input_register_template_object)

Register Template

Adds an existing back-end Template to the specified Virtualization Realm.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm
input_register_template_object = cons3rt.InputRegisterTemplateObject() # InputRegisterTemplateObject | The template registration data (optional)

    try:
        # Register Template
        api_response = api_instance.register_template(id, input_register_template_object=input_register_template_object)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->register_template: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm
input_register_template_object = cons3rt.InputRegisterTemplateObject() # InputRegisterTemplateObject | The template registration data (optional)

    try:
        # Register Template
        api_response = api_instance.register_template(id, input_register_template_object=input_register_template_object)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->register_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of virtualization realm | 
 **input_register_template_object** | [**InputRegisterTemplateObject**](InputRegisterTemplateObject.md)| The template registration data | [optional] 

### Return type

[**FullTemplateRegistration**](FullTemplateRegistration.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid virtualization realm ID or data supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_project**
> bool remove_project(id, project_id)

Unassign Project

Revokes Project member access to the specified Virtualization Realm.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
project_id = 'project_id_example' # str | ID of project to unassign

    try:
        # Unassign Project
        api_response = api_instance.remove_project(id, project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->remove_project: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
project_id = 'project_id_example' # str | ID of project to unassign

    try:
        # Unassign Project
        api_response = api_instance.remove_project(id, project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->remove_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of virtualization realm | 
 **project_id** | **str**| ID of project to unassign | 

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
**400** | Invalid virtualization realm ID or project ID supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_template_registration**
> FullTemplateRegistration retrieve_template_registration(id, registration_id)

Retrieve Template Registration

Returns a single Template Registration in the specified Virtualization Realm.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm
registration_id = 56 # int | ID of template registration

    try:
        # Retrieve Template Registration
        api_response = api_instance.retrieve_template_registration(id, registration_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->retrieve_template_registration: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm
registration_id = 56 # int | ID of template registration

    try:
        # Retrieve Template Registration
        api_response = api_instance.retrieve_template_registration(id, registration_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->retrieve_template_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of virtualization realm | 
 **registration_id** | **int**| ID of template registration | 

### Return type

[**FullTemplateRegistration**](FullTemplateRegistration.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid virtualization realm ID or template registration ID supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_virtualization_realm_active**
> bool set_virtualization_realm_active(id, activate)

Update State

Updates the active State for a single Virtualization Realm by the given ID.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
activate = True # bool | Activate or deactivate virtualization realm

    try:
        # Update State
        api_response = api_instance.set_virtualization_realm_active(id, activate)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->set_virtualization_realm_active: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
activate = True # bool | Activate or deactivate virtualization realm

    try:
        # Update State
        api_response = api_instance.set_virtualization_realm_active(id, activate)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->set_virtualization_realm_active: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of virtualization realm | 
 **activate** | **bool**| Activate or deactivate virtualization realm | 

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
**400** | Invalid virtualization realm ID or data supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_template_registration**
> bool share_template_registration(id, registration_id, target_realm_ids)

Share Template

Shares an existing Template Registration in the specified Virtualization Realm to the provided external Virtualization Realm(s).

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm
registration_id = 56 # int | ID of template registration
target_realm_ids = [56] # list[int] | ID(s) of external virtualization realms to share template registration with

    try:
        # Share Template
        api_response = api_instance.share_template_registration(id, registration_id, target_realm_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->share_template_registration: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm
registration_id = 56 # int | ID of template registration
target_realm_ids = [56] # list[int] | ID(s) of external virtualization realms to share template registration with

    try:
        # Share Template
        api_response = api_instance.share_template_registration(id, registration_id, target_realm_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->share_template_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of virtualization realm | 
 **registration_id** | **int**| ID of template registration | 
 **target_realm_ids** | [**list[int]**](int.md)| ID(s) of external virtualization realms to share template registration with | 

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
**400** | Invalid virtualization realm ID, template registration ID, or data supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister_template**
> bool unregister_template(id, registration_id, input_unregister_template_object)

Delete Template Registration

Removes an existing Template Registration from the specified Virtualization Realm.<br> <br> Note: Unregistering a Template will remove all subscriptions to the Template from other Virtualization Realms.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm
registration_id = 56 # int | ID of template registration
input_unregister_template_object = cons3rt.InputUnregisterTemplateObject() # InputUnregisterTemplateObject | The deletion settings

    try:
        # Delete Template Registration
        api_response = api_instance.unregister_template(id, registration_id, input_unregister_template_object)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->unregister_template: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm
registration_id = 56 # int | ID of template registration
input_unregister_template_object = cons3rt.InputUnregisterTemplateObject() # InputUnregisterTemplateObject | The deletion settings

    try:
        # Delete Template Registration
        api_response = api_instance.unregister_template(id, registration_id, input_unregister_template_object)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->unregister_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of virtualization realm | 
 **registration_id** | **int**| ID of template registration | 
 **input_unregister_template_object** | [**InputUnregisterTemplateObject**](InputUnregisterTemplateObject.md)| The deletion settings | 

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
**400** | Invalid virtualization realm ID or template registration ID supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unshare_template_registration**
> bool unshare_template_registration(id, registration_id, target_realm_id)

Unshare Template

Revokes access to a Template Registration in the specified Virtualization Realm by the provided external Virtualization Realm.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm
registration_id = 56 # int | ID of template registration
target_realm_id = 56 # int | ID of external virtualization realm to revoke template registration access for

    try:
        # Unshare Template
        api_response = api_instance.unshare_template_registration(id, registration_id, target_realm_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->unshare_template_registration: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm
registration_id = 56 # int | ID of template registration
target_realm_id = 56 # int | ID of external virtualization realm to revoke template registration access for

    try:
        # Unshare Template
        api_response = api_instance.unshare_template_registration(id, registration_id, target_realm_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->unshare_template_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of virtualization realm | 
 **registration_id** | **int**| ID of template registration | 
 **target_realm_id** | **int**| ID of external virtualization realm to revoke template registration access for | 

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
**400** | Invalid virtualization realm ID, template registration ID, or external virtualization realm ID supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_registration**
> bool update_template_registration(id, registration_id, input_cons3rt_template_data, offline=offline)

Update Template Registration

Updates the Template Registration for a single Virtualization Realm by the given ID.<br> <br> Note: The state of a Template Registration can only be set to OFFLINE or PUBLISHED.<br> <br> Note: All fields in Template data are honored on update, therefore any configuration that is desired in the updated Registration should be provided.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm
registration_id = 56 # int | ID of template registration
input_cons3rt_template_data = cons3rt.InputCons3rtTemplateData() # InputCons3rtTemplateData | The modified template registration data
offline = False # bool | The desired template registration state (optional) (default to False)

    try:
        # Update Template Registration
        api_response = api_instance.update_template_registration(id, registration_id, input_cons3rt_template_data, offline=offline)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->update_template_registration: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm
registration_id = 56 # int | ID of template registration
input_cons3rt_template_data = cons3rt.InputCons3rtTemplateData() # InputCons3rtTemplateData | The modified template registration data
offline = False # bool | The desired template registration state (optional) (default to False)

    try:
        # Update Template Registration
        api_response = api_instance.update_template_registration(id, registration_id, input_cons3rt_template_data, offline=offline)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->update_template_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of virtualization realm | 
 **registration_id** | **int**| ID of template registration | 
 **input_cons3rt_template_data** | [**InputCons3rtTemplateData**](InputCons3rtTemplateData.md)| The modified template registration data | 
 **offline** | **bool**| The desired template registration state | [optional] [default to False]

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
**400** | Invalid virtualization realm ID, template registration ID, or data supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_subscription**
> bool update_template_subscription(id, subscription_id, input_template_subscription, offline=offline)

Update Template Subscription

Updates the Template Subscription for a single Virtualization Realm by the given ID.<br> <br> Note: The state of a Template Subscription can only be set to OFFLINE or PUBLISHED.<br> <br> Note: The limits of a Template subscription (CPU, RAM, etc.) cannot exceed the value included in the Registration.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm
subscription_id = 56 # int | ID of template subscription
input_template_subscription = cons3rt.InputTemplateSubscription() # InputTemplateSubscription | The modified template subscription data
offline = False # bool | The desired template subscription state (optional) (default to False)

    try:
        # Update Template Subscription
        api_response = api_instance.update_template_subscription(id, subscription_id, input_template_subscription, offline=offline)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->update_template_subscription: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 56 # int | ID of virtualization realm
subscription_id = 56 # int | ID of template subscription
input_template_subscription = cons3rt.InputTemplateSubscription() # InputTemplateSubscription | The modified template subscription data
offline = False # bool | The desired template subscription state (optional) (default to False)

    try:
        # Update Template Subscription
        api_response = api_instance.update_template_subscription(id, subscription_id, input_template_subscription, offline=offline)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->update_template_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of virtualization realm | 
 **subscription_id** | **int**| ID of template subscription | 
 **input_template_subscription** | [**InputTemplateSubscription**](InputTemplateSubscription.md)| The modified template subscription data | 
 **offline** | **bool**| The desired template subscription state | [optional] [default to False]

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
**400** | Invalid virtualization realm ID, template subscription ID, or data supplied |  -  |
**404** | Virtualization realm not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_virt_realm_remote_access_config**
> bool update_virt_realm_remote_access_config(id, remote_access_config)

Update Remote Access

Updates the Remote Access configuration for a single Virtualization Realm by the given ID.<br> <br> Note: remoteAccessIpAddress cannot be updated if the Virtualization Realm's Remote Access is currently enabled.

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
remote_access_config = cons3rt.RemoteAccessConfig() # RemoteAccessConfig | The updated remote access configuration

    try:
        # Update Remote Access
        api_response = api_instance.update_virt_realm_remote_access_config(id, remote_access_config)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->update_virt_realm_remote_access_config: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
remote_access_config = cons3rt.RemoteAccessConfig() # RemoteAccessConfig | The updated remote access configuration

    try:
        # Update Remote Access
        api_response = api_instance.update_virt_realm_remote_access_config(id, remote_access_config)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->update_virt_realm_remote_access_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of virtualization realm | 
 **remote_access_config** | [**RemoteAccessConfig**](RemoteAccessConfig.md)| The updated remote access configuration | 

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
**400** | Invalid virtualization realm ID or data supplied |  -  |
**404** | Virtualization realm not found |  -  |

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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
input_vr_admin_virtualization_realm = cons3rt.InputVRAdminVirtualizationRealm() # InputVRAdminVirtualizationRealm | The updated Virtualization Realm data (optional)

    try:
        # Update Virtualization Realm
        api_response = api_instance.update_virtualization_realm(id, input_vr_admin_virtualization_realm=input_vr_admin_virtualization_realm)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->update_virtualization_realm: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm
input_vr_admin_virtualization_realm = cons3rt.InputVRAdminVirtualizationRealm() # InputVRAdminVirtualizationRealm | The updated Virtualization Realm data (optional)

    try:
        # Update Virtualization Realm
        api_response = api_instance.update_virtualization_realm(id, input_vr_admin_virtualization_realm=input_vr_admin_virtualization_realm)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->update_virtualization_realm: %s\n" % e)
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

# **update_virtualization_realm_reachability**
> bool update_virtualization_realm_reachability(id)



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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm

    try:
        api_response = api_instance.update_virtualization_realm_reachability(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->update_virtualization_realm_reachability: %s\n" % e)
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
    api_instance = cons3rt.VirtualizationRealmsApi(api_client)
    id = 'id_example' # str | ID of virtualization realm

    try:
        api_response = api_instance.update_virtualization_realm_reachability(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VirtualizationRealmsApi->update_virtualization_realm_reachability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of virtualization realm | 

### Return type

**bool**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

