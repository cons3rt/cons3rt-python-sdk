# cons3rt.DeploymentsApi

All URIs are relative to *https://api.dev.cons3rt.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_recurring_schedule**](DeploymentsApi.md#add_recurring_schedule) | **PUT** /api/deployments/{id}/schedules | Add Recurring Schedule
[**add_trusted_project**](DeploymentsApi.md#add_trusted_project) | **PUT** /api/assets/{id}/addtrustedproject | Assign Trusted Project to Asset
[**clone_deployment**](DeploymentsApi.md#clone_deployment) | **PUT** /api/deployments/{id}/clone | Clone Deployment
[**clone_system**](DeploymentsApi.md#clone_system) | **PUT** /api/systems/{id}/clone | Clone System
[**create_deployment_entire**](DeploymentsApi.md#create_deployment_entire) | **PUT** /api/deployments/createdeployment | Create Deployment
[**delete_asset**](DeploymentsApi.md#delete_asset) | **DELETE** /api/assets/{id} | Delete Asset
[**determine_valid_virtualization_realms**](DeploymentsApi.md#determine_valid_virtualization_realms) | **GET** /api/deployments/{id}/validrealms | List Valid Virtualization Realms
[**get_bindings_for_deployment**](DeploymentsApi.md#get_bindings_for_deployment) | **GET** /api/deployments/{id}/bindings | List Bindings
[**get_deployment**](DeploymentsApi.md#get_deployment) | **GET** /api/deployments/{id} | Retrieve Deployment
[**get_deployment_metric**](DeploymentsApi.md#get_deployment_metric) | **GET** /api/deployments/{id}/metrics | Retrieve Metrics
[**get_deployment_runs**](DeploymentsApi.md#get_deployment_runs) | **GET** /api/deployments/{id}/runs | List Deployment Runs
[**get_deployment_runs1**](DeploymentsApi.md#get_deployment_runs1) | **GET** /api/drs | List Deployment Runs
[**get_deployment_runs_in_virtualization_realm**](DeploymentsApi.md#get_deployment_runs_in_virtualization_realm) | **GET** /api/virtualizationrealms/{id}/deploymentruns | List Deployment Runs
[**get_deployments**](DeploymentsApi.md#get_deployments) | **GET** /api/deployments | List Deployments
[**get_deployments_expanded**](DeploymentsApi.md#get_deployments_expanded) | **GET** /api/deployments/expanded | List all Deployments, including Project Assets
[**get_valid_networks_for_virtualization_realm**](DeploymentsApi.md#get_valid_networks_for_virtualization_realm) | **GET** /api/deployments/{id}/networks/{virtualizationRealmId} | List Virtualization Realm Networks
[**itar_restrict_asset**](DeploymentsApi.md#itar_restrict_asset) | **PUT** /api/assets/{id}/setitar | Set Asset Export Restriction
[**launch_deployment**](DeploymentsApi.md#launch_deployment) | **POST** /api/deployments/{id}/launch | Launch Deployment
[**list_dependent_assets**](DeploymentsApi.md#list_dependent_assets) | **GET** /api/assets/{id}/dependent | List all Dependent Assets
[**list_options**](DeploymentsApi.md#list_options) | **GET** /api/deployments/{id}/options | List Run Options
[**list_properties**](DeploymentsApi.md#list_properties) | **GET** /api/deployments/{id}/properties | List Properties
[**list_schedules**](DeploymentsApi.md#list_schedules) | **GET** /api/deployments/{id}/schedules | List Recurring Schedules
[**remove_recurring_schedule**](DeploymentsApi.md#remove_recurring_schedule) | **DELETE** /api/deployments/{id}/schedules | Remove Recurring Schedule
[**remove_trusted_project**](DeploymentsApi.md#remove_trusted_project) | **PUT** /api/assets/{id}/removetrustedproject | Unassign Trusted Project from Asset
[**update_asset**](DeploymentsApi.md#update_asset) | **PUT** /api/assets/{id}/update | Update Asset
[**update_asset_state**](DeploymentsApi.md#update_asset_state) | **PUT** /api/assets/{id}/updatestate | Update State
[**update_asset_visibility_query**](DeploymentsApi.md#update_asset_visibility_query) | **PUT** /api/assets/{id}/updatevisibility | Update Visibility
[**update_impact_level**](DeploymentsApi.md#update_impact_level) | **PUT** /api/assets/{id}/impactlevel | Update Impact Level
[**update_instance_limit**](DeploymentsApi.md#update_instance_limit) | **PUT** /api/assets/{id}/limit | Update Instance Limit
[**update_offline_status**](DeploymentsApi.md#update_offline_status) | **PUT** /api/assets/{id}/offline | Update Offline Status


# **add_recurring_schedule**
> bool add_recurring_schedule(id, input_recurring_schedule=input_recurring_schedule)

Add Recurring Schedule

Adds the Recurring Schedule to a Deployment, creating a Deployment run with the given parameters at intervals specified by the Schedule.<br> <br> Timezone must be provided as Java Timezone, and thus must take the form of \"GMT + or - (hour)(hour)(min)(min)\" Example: GMT-0700 <br> <br> The Schedule field must be provided in valid cron format: \"(minute 0-59) (hour 0-23) (day of month 1-31) (month 1-12) (day of week 0-6, with 0 representing Sunday)<br> <br> \"*\" is a wildcard that can replace any single entry, representing any or all of the possible entries (e.g. an hour of * means every hour).<br> <br> Individual entries in the Schedule string can also be represented as ranges (e.g. day of month 4-17, would represent the 4th through the 17th of the month).<br> <br> In addition, values can also be specified as comma lists (e.g. hours 1,4,6 would represent occurrences at the first, fourth, and sixth hour respectively).

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment
input_recurring_schedule = cons3rt.InputRecurringSchedule() # InputRecurringSchedule | The Recurring Schedule definition (optional)

try:
    # Add Recurring Schedule
    api_response = api_instance.add_recurring_schedule(id, input_recurring_schedule=input_recurring_schedule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->add_recurring_schedule: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment
input_recurring_schedule = cons3rt.InputRecurringSchedule() # InputRecurringSchedule | The Recurring Schedule definition (optional)

try:
    # Add Recurring Schedule
    api_response = api_instance.add_recurring_schedule(id, input_recurring_schedule=input_recurring_schedule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->add_recurring_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment | 
 **input_recurring_schedule** | [**InputRecurringSchedule**](InputRecurringSchedule.md)| The Recurring Schedule definition | [optional] 

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
**400** | Invalid deployment ID or recurring schedule definition supplied |  -  |
**404** | Deployment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_trusted_project**
> bool add_trusted_project(id, trustedid)

Assign Trusted Project to Asset

Allows members of the provided Project to access the specified Asset.<br> <br> The Asset must have a visibility set to TRUSTED_PROJECT for this to have any effect.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of asset
trustedid = 'trustedid_example' # str | ID of project to trust

try:
    # Assign Trusted Project to Asset
    api_response = api_instance.add_trusted_project(id, trustedid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->add_trusted_project: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of asset
trustedid = 'trustedid_example' # str | ID of project to trust

try:
    # Assign Trusted Project to Asset
    api_response = api_instance.add_trusted_project(id, trustedid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->add_trusted_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of asset | 
 **trustedid** | **str**| ID of project to trust | 

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
**400** | Invalid asset ID or project ID supplied |  -  |
**404** | Asset not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_deployment**
> str clone_deployment(id, name)

Clone Deployment

Clones the specified Deployment to a new Deployment with the provided name.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment
name = 'name_example' # str | Name of the new deployment

try:
    # Clone Deployment
    api_response = api_instance.clone_deployment(id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->clone_deployment: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment
name = 'name_example' # str | Name of the new deployment

try:
    # Clone Deployment
    api_response = api_instance.clone_deployment(id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->clone_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment | 
 **name** | **str**| Name of the new deployment | 

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
**400** | Invalid deployment ID or name supplied |  -  |
**404** | Deployment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_system**
> str clone_system(id, name)

Clone System

Clones the specified System to a new System with the provided name.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of system
name = 'name_example' # str | Name of the new system

try:
    # Clone System
    api_response = api_instance.clone_system(id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->clone_system: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of system
name = 'name_example' # str | Name of the new system

try:
    # Clone System
    api_response = api_instance.clone_system(id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->clone_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of system | 
 **name** | **str**| Name of the new system | 

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
**400** | Invalid system ID or name supplied |  -  |
**404** | System not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_deployment_entire**
> str create_deployment_entire(input_deployment=input_deployment)

Create Deployment

Create a single Deplyoment.<br> <br> All existing Assets used in creation must contain their Asset ID, while to-be-constructed Composite Assets must contain a valid Asset ID for each element contained.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
input_deployment = cons3rt.InputDeployment() # InputDeployment | The Deployment to create (optional)

try:
    # Create Deployment
    api_response = api_instance.create_deployment_entire(input_deployment=input_deployment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->create_deployment_entire: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
input_deployment = cons3rt.InputDeployment() # InputDeployment | The Deployment to create (optional)

try:
    # Create Deployment
    api_response = api_instance.create_deployment_entire(input_deployment=input_deployment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->create_deployment_entire: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_deployment** | [**InputDeployment**](InputDeployment.md)| The Deployment to create | [optional] 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid data supplied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset**
> bool delete_asset(id, force=force)

Delete Asset

Deletes a single Asset with the given ID.<br> <br> Optionally, this call can delete the Asset in question even if that Asset has dependents.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of asset to delete
force = False # bool | Allow delete if there are dependent assets (optional) (default to False)

try:
    # Delete Asset
    api_response = api_instance.delete_asset(id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->delete_asset: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of asset to delete
force = False # bool | Allow delete if there are dependent assets (optional) (default to False)

try:
    # Delete Asset
    api_response = api_instance.delete_asset(id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->delete_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of asset to delete | 
 **force** | **bool**| Allow delete if there are dependent assets | [optional] [default to False]

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
**400** | Invalid asset ID supplied |  -  |
**404** | Asset not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **determine_valid_virtualization_realms**
> list[MinimalVirtualizationRealm] determine_valid_virtualization_realms(id)

List Valid Virtualization Realms

Returns a collection of the available Virtualization Realms for launching the specified Deployment.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment

try:
    # List Valid Virtualization Realms
    api_response = api_instance.determine_valid_virtualization_realms(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->determine_valid_virtualization_realms: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment

try:
    # List Valid Virtualization Realms
    api_response = api_instance.determine_valid_virtualization_realms(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->determine_valid_virtualization_realms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment | 

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
**400** | Invalid deployment ID supplied |  -  |
**404** | Deployment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bindings_for_deployment**
> list[VirtualizationRealmBinding] get_bindings_for_deployment(id, virtualization_realm_id=virtualization_realm_id)

List Bindings

Returns a collection of the possible Virtualization Realm bindings for a single Deployment.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment
virtualization_realm_id = 56 # int | ID of preferred virtualization realm (optional)

try:
    # List Bindings
    api_response = api_instance.get_bindings_for_deployment(id, virtualization_realm_id=virtualization_realm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_bindings_for_deployment: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment
virtualization_realm_id = 56 # int | ID of preferred virtualization realm (optional)

try:
    # List Bindings
    api_response = api_instance.get_bindings_for_deployment(id, virtualization_realm_id=virtualization_realm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_bindings_for_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment | 
 **virtualization_realm_id** | **int**| ID of preferred virtualization realm | [optional] 

### Return type

[**list[VirtualizationRealmBinding]**](VirtualizationRealmBinding.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid deployment ID or virtualization realm ID supplied |  -  |
**404** | Deployment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment**
> FullDeployment get_deployment(id)

Retrieve Deployment

Returns a single Deployment by the given ID.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment

try:
    # Retrieve Deployment
    api_response = api_instance.get_deployment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_deployment: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment

try:
    # Retrieve Deployment
    api_response = api_instance.get_deployment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment | 

### Return type

[**FullDeployment**](FullDeployment.md)

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
**404** | Deployment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_metric**
> DeploymentAssetMetric get_deployment_metric(id)

Retrieve Metrics

Returns historical metric data for a single Deployment.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment

try:
    # Retrieve Metrics
    api_response = api_instance.get_deployment_metric(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_deployment_metric: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment

try:
    # Retrieve Metrics
    api_response = api_instance.get_deployment_metric(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_deployment_metric: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment | 

### Return type

[**DeploymentAssetMetric**](DeploymentAssetMetric.md)

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
**404** | Deployment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_runs**
> list[MinimalDeploymentRun] get_deployment_runs(id)

List Deployment Runs

Returns a collection of the Deployment Runs for a single Deployment.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment

try:
    # List Deployment Runs
    api_response = api_instance.get_deployment_runs(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_deployment_runs: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment

try:
    # List Deployment Runs
    api_response = api_instance.get_deployment_runs(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_deployment_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment | 

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
**400** | Invalid deployment ID supplied |  -  |
**404** | Deployment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_runs1**
> list[MinimalDeploymentRun] get_deployment_runs1(search_type, in_project=in_project, maxresults=maxresults, page=page)

List Deployment Runs

Returns a collection of the user's relevant Deployment Runs matching a specified query.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
search_type = 'search_type_example' # str | Deployment run status
in_project = False # bool | Include project runs (optional) (default to False)
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

try:
    # List Deployment Runs
    api_response = api_instance.get_deployment_runs1(search_type, in_project=in_project, maxresults=maxresults, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_deployment_runs1: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
search_type = 'search_type_example' # str | Deployment run status
in_project = False # bool | Include project runs (optional) (default to False)
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

try:
    # List Deployment Runs
    api_response = api_instance.get_deployment_runs1(search_type, in_project=in_project, maxresults=maxresults, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_deployment_runs1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_type** | **str**| Deployment run status | 
 **in_project** | **bool**| Include project runs | [optional] [default to False]
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
**400** | Invalid query parameter |  -  |

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of virtualization realm
search_type = 'SEARCH_ALL' # str | Deployment run status type (default to 'SEARCH_ALL')
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

try:
    # List Deployment Runs
    api_response = api_instance.get_deployment_runs_in_virtualization_realm(id, search_type, maxresults=maxresults, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_deployment_runs_in_virtualization_realm: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of virtualization realm
search_type = 'SEARCH_ALL' # str | Deployment run status type (default to 'SEARCH_ALL')
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

try:
    # List Deployment Runs
    api_response = api_instance.get_deployment_runs_in_virtualization_realm(id, search_type, maxresults=maxresults, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_deployment_runs_in_virtualization_realm: %s\n" % e)
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

# **get_deployments**
> list[MinimalDeployment] get_deployments(categoryids=categoryids, maxresults=maxresults, page=page)

List Deployments

Returns a collection of the user's relevant Deployments matching a specified query.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
categoryids = [56] # list[int] | Category ID(s) to filter by. Multiple categories can be provided with comma-separated strings. (optional)
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

try:
    # List Deployments
    api_response = api_instance.get_deployments(categoryids=categoryids, maxresults=maxresults, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_deployments: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
categoryids = [56] # list[int] | Category ID(s) to filter by. Multiple categories can be provided with comma-separated strings. (optional)
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

try:
    # List Deployments
    api_response = api_instance.get_deployments(categoryids=categoryids, maxresults=maxresults, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_deployments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categoryids** | [**list[int]**](int.md)| Category ID(s) to filter by. Multiple categories can be provided with comma-separated strings. | [optional] 
 **maxresults** | **int**| Maximum number of results to return | [optional] [default to 40]
 **page** | **int**| Requested page number | [optional] [default to 0]

### Return type

[**list[MinimalDeployment]**](MinimalDeployment.md)

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

# **get_deployments_expanded**
> list[BasicDeployment] get_deployments_expanded(community=community, categoryids=categoryids, maxresults=maxresults, page=page)

List all Deployments, including Project Assets

Returns a collection of all relevant Deployments matching a specified query, including those from the Project.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
community = False # bool | Include community assets (optional) (default to False)
categoryids = [56] # list[int] | Category ID(s) to filter by. Multiple categories can be provided with comma-separated strings. (optional)
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

try:
    # List all Deployments, including Project Assets
    api_response = api_instance.get_deployments_expanded(community=community, categoryids=categoryids, maxresults=maxresults, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_deployments_expanded: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
community = False # bool | Include community assets (optional) (default to False)
categoryids = [56] # list[int] | Category ID(s) to filter by. Multiple categories can be provided with comma-separated strings. (optional)
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

try:
    # List all Deployments, including Project Assets
    api_response = api_instance.get_deployments_expanded(community=community, categoryids=categoryids, maxresults=maxresults, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_deployments_expanded: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **community** | **bool**| Include community assets | [optional] [default to False]
 **categoryids** | [**list[int]**](int.md)| Category ID(s) to filter by. Multiple categories can be provided with comma-separated strings. | [optional] 
 **maxresults** | **int**| Maximum number of results to return | [optional] [default to 40]
 **page** | **int**| Requested page number | [optional] [default to 0]

### Return type

[**list[BasicDeployment]**](BasicDeployment.md)

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

# **get_valid_networks_for_virtualization_realm**
> list[MinimalNetwork] get_valid_networks_for_virtualization_realm(id, virtualization_realm_id)

List Virtualization Realm Networks

Returns a collection of the Networks that will be created for a single Deployment that has launched into the specified Virtualization Realm.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment
virtualization_realm_id = 'virtualization_realm_id_example' # str | ID of virtualization realm

try:
    # List Virtualization Realm Networks
    api_response = api_instance.get_valid_networks_for_virtualization_realm(id, virtualization_realm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_valid_networks_for_virtualization_realm: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment
virtualization_realm_id = 'virtualization_realm_id_example' # str | ID of virtualization realm

try:
    # List Virtualization Realm Networks
    api_response = api_instance.get_valid_networks_for_virtualization_realm(id, virtualization_realm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->get_valid_networks_for_virtualization_realm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment | 
 **virtualization_realm_id** | **str**| ID of virtualization realm | 

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
**400** | Invalid deployment ID or virtualization realm ID supplied |  -  |
**404** | Deployment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **itar_restrict_asset**
> bool itar_restrict_asset(id)

Set Asset Export Restriction

Sets the Export Restriction of a single Asset with the given ID.<br> <br> Export Restriction can only be set if the owning Project is an ITAR-restricted Project.<br> <br> Setting an Export Restriction cannot be undone.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of asset

try:
    # Set Asset Export Restriction
    api_response = api_instance.itar_restrict_asset(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->itar_restrict_asset: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of asset

try:
    # Set Asset Export Restriction
    api_response = api_instance.itar_restrict_asset(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->itar_restrict_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of asset | 

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
**400** | Invalid ID or asset impact level supplied |  -  |
**404** | Asset not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launch_deployment**
> SubmitDeploymentRunRequestReturnType launch_deployment(id, input_deployment_run_options=input_deployment_run_options)

Launch Deployment

Launches a Deployment with Run Options.<br> <br> Either provide a virtualizationRealmId or a virtualizationRealmBinding object to determine the Virtualization Realm to deploy into, and the template bindings to use (if specified).<br> <br> Network interface objects must be provided for each desired network connection.<br> <br> A root password can be set within the provided Deployment Run Options, which will override the password for all Hosts.<br> <br> The override of Host passwords may fail due to template password complexity rules and should not be done without consideration.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment
input_deployment_run_options = cons3rt.InputDeploymentRunOptions() # InputDeploymentRunOptions | The deployment run options to use when launching the deployment (optional)

try:
    # Launch Deployment
    api_response = api_instance.launch_deployment(id, input_deployment_run_options=input_deployment_run_options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->launch_deployment: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment
input_deployment_run_options = cons3rt.InputDeploymentRunOptions() # InputDeploymentRunOptions | The deployment run options to use when launching the deployment (optional)

try:
    # Launch Deployment
    api_response = api_instance.launch_deployment(id, input_deployment_run_options=input_deployment_run_options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->launch_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment | 
 **input_deployment_run_options** | [**InputDeploymentRunOptions**](InputDeploymentRunOptions.md)| The deployment run options to use when launching the deployment | [optional] 

### Return type

[**SubmitDeploymentRunRequestReturnType**](SubmitDeploymentRunRequestReturnType.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid deployment ID or run options supplied |  -  |
**404** | Deployment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dependent_assets**
> list[BasicAsset] list_dependent_assets(id)

List all Dependent Assets

Returns a collection of the Composite Assets that include the specified Asset.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of asset

try:
    # List all Dependent Assets
    api_response = api_instance.list_dependent_assets(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->list_dependent_assets: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of asset

try:
    # List all Dependent Assets
    api_response = api_instance.list_dependent_assets(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->list_dependent_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of asset | 

### Return type

[**list[BasicAsset]**](BasicAsset.md)

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
**404** | Asset not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_options**
> list[MinimalDeploymentRunOptions] list_options(id)

List Run Options

Returns a collection of the previously used Run Options for a single Deployment.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment

try:
    # List Run Options
    api_response = api_instance.list_options(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->list_options: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment

try:
    # List Run Options
    api_response = api_instance.list_options(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->list_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment | 

### Return type

[**list[MinimalDeploymentRunOptions]**](MinimalDeploymentRunOptions.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid deployment ID supplied |  -  |
**404** | Deployment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_properties**
> list[ModelProperty] list_properties(id)

List Properties

Returns a collection of the Properties for a single Deployment.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment

try:
    # List Properties
    api_response = api_instance.list_properties(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->list_properties: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment

try:
    # List Properties
    api_response = api_instance.list_properties(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->list_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment | 

### Return type

[**list[ModelProperty]**](ModelProperty.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid deployment ID supplied |  -  |
**404** | Deployment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_schedules**
> list[MinimalRecurringSchedule] list_schedules(id)

List Recurring Schedules

Returns a collection of the active Recurring Schedules for a single Deployment.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment

try:
    # List Recurring Schedules
    api_response = api_instance.list_schedules(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->list_schedules: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment

try:
    # List Recurring Schedules
    api_response = api_instance.list_schedules(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->list_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment | 

### Return type

[**list[MinimalRecurringSchedule]**](MinimalRecurringSchedule.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid deployment ID supplied |  -  |
**404** | Deployment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_recurring_schedule**
> bool remove_recurring_schedule(id)

Remove Recurring Schedule

Removes the provided Recurring Schedule from the Deployment.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment

try:
    # Remove Recurring Schedule
    api_response = api_instance.remove_recurring_schedule(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->remove_recurring_schedule: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of deployment

try:
    # Remove Recurring Schedule
    api_response = api_instance.remove_recurring_schedule(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->remove_recurring_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment | 

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
**400** | Invalid deployment ID supplied |  -  |
**404** | Deployment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_trusted_project**
> bool remove_trusted_project(id, trustedid)

Unassign Trusted Project from Asset

Removes the provided Project from the Asset's list of Trusted Projects.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of asset
trustedid = 'trustedid_example' # str | ID of project to untrust

try:
    # Unassign Trusted Project from Asset
    api_response = api_instance.remove_trusted_project(id, trustedid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->remove_trusted_project: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of asset
trustedid = 'trustedid_example' # str | ID of project to untrust

try:
    # Unassign Trusted Project from Asset
    api_response = api_instance.remove_trusted_project(id, trustedid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->remove_trusted_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of asset | 
 **trustedid** | **str**| ID of project to untrust | 

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
**400** | Invalid asset ID or project ID supplied |  -  |
**404** | Asset not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset**
> bool update_asset(id, input_asset_for_update=input_asset_for_update)

Update Asset

Updates the metadata of a single Asset with the given ID.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of asset
input_asset_for_update = cons3rt.InputAssetForUpdate() # InputAssetForUpdate | The modified Asset metadata (optional)

try:
    # Update Asset
    api_response = api_instance.update_asset(id, input_asset_for_update=input_asset_for_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->update_asset: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of asset
input_asset_for_update = cons3rt.InputAssetForUpdate() # InputAssetForUpdate | The modified Asset metadata (optional)

try:
    # Update Asset
    api_response = api_instance.update_asset(id, input_asset_for_update=input_asset_for_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->update_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of asset | 
 **input_asset_for_update** | [**InputAssetForUpdate**](InputAssetForUpdate.md)| The modified Asset metadata | [optional] 

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
**400** | Invalid ID supplied |  -  |
**404** | Asset not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_state**
> bool update_asset_state(id, state)

Update State

Updates the state of a single Asset with the given ID.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of asset to delete
state = 'state_example' # str | The new asset state type

try:
    # Update State
    api_response = api_instance.update_asset_state(id, state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->update_asset_state: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of asset to delete
state = 'state_example' # str | The new asset state type

try:
    # Update State
    api_response = api_instance.update_asset_state(id, state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->update_asset_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of asset to delete | 
 **state** | **str**| The new asset state type | 

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
**400** | Invalid ID or asset state supplied |  -  |
**404** | Asset not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_visibility_query**
> bool update_asset_visibility_query(id, visibility)

Update Visibility

Updates the visibility of a single Asset with the given ID.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of asset to update
visibility = 'visibility_example' # str | The new asset visibility type

try:
    # Update Visibility
    api_response = api_instance.update_asset_visibility_query(id, visibility)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->update_asset_visibility_query: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of asset to update
visibility = 'visibility_example' # str | The new asset visibility type

try:
    # Update Visibility
    api_response = api_instance.update_asset_visibility_query(id, visibility)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->update_asset_visibility_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of asset to update | 
 **visibility** | **str**| The new asset visibility type | 

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
**400** | Invalid ID or asset visibility supplied |  -  |
**404** | Asset not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_impact_level**
> bool update_impact_level(id, impactlevel)

Update Impact Level

Updates the Impact Level of a single Asset with the given ID.<br> <br >Maximum Impact Level can only be set to DOD_LEVEL_6 if allowed in the Environment.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of asset
impactlevel = 'impactlevel_example' # str | The new asset impact level type.

try:
    # Update Impact Level
    api_response = api_instance.update_impact_level(id, impactlevel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->update_impact_level: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of asset
impactlevel = 'impactlevel_example' # str | The new asset impact level type.

try:
    # Update Impact Level
    api_response = api_instance.update_impact_level(id, impactlevel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->update_impact_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of asset | 
 **impactlevel** | **str**| The new asset impact level type. | 

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
**400** | Invalid ID or asset impact level supplied |  -  |
**404** | Asset not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_instance_limit**
> bool update_instance_limit(id, limit)

Update Instance Limit

Updates the instance limit of a single Asset with the given ID.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of asset
limit = 56 # int | The new asset instance limit

try:
    # Update Instance Limit
    api_response = api_instance.update_instance_limit(id, limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->update_instance_limit: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of asset
limit = 56 # int | The new asset instance limit

try:
    # Update Instance Limit
    api_response = api_instance.update_instance_limit(id, limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->update_instance_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of asset | 
 **limit** | **int**| The new asset instance limit | 

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
**400** | Invalid ID or asset impact level supplied |  -  |
**404** | Asset not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_offline_status**
> bool update_offline_status(id, offline=offline)

Update Offline Status

Updates the Offline Status of a single Asset with the given ID.

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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of asset to update
offline = True # bool | Set the asset status to offline (optional) (default to True)

try:
    # Update Offline Status
    api_response = api_instance.update_offline_status(id, offline=offline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->update_offline_status: %s\n" % e)
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
api_instance = cons3rt.DeploymentsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of asset to update
offline = True # bool | Set the asset status to offline (optional) (default to True)

try:
    # Update Offline Status
    api_response = api_instance.update_offline_status(id, offline=offline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentsApi->update_offline_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of asset to update | 
 **offline** | **bool**| Set the asset status to offline | [optional] [default to True]

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
**400** | Invalid ID or asset offline status supplied |  -  |
**404** | Asset not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

