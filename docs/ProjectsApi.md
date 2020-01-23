# cons3rt.ProjectsApi

All URIs are relative to *https://api.dev.cons3rt.io/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_project_member**](ProjectsApi.md#add_project_member) | **PUT** /api/projects/{id}/members | Assign Project Member
[**add_role_to_project_member**](ProjectsApi.md#add_role_to_project_member) | **PUT** /api/projects/{id}/members/roles | Assign Role to Member
[**add_submission_service_to_project**](ProjectsApi.md#add_submission_service_to_project) | **POST** /api/projects/{id}/submission | Add Submission Service
[**add_trusted_project1**](ProjectsApi.md#add_trusted_project1) | **PUT** /api/projects/{id}/addtrustedproject | Assign Trusted Project to Project
[**create_project**](ProjectsApi.md#create_project) | **POST** /api/projects | Create a Project
[**delete_project**](ProjectsApi.md#delete_project) | **DELETE** /api/projects/{id} | Delete Project
[**get_host_configuration_metrics**](ProjectsApi.md#get_host_configuration_metrics) | **GET** /api/projects/{id}/metrics/hostconfiguration | Retrieve Metrics
[**get_project**](ProjectsApi.md#get_project) | **GET** /api/projects/{id} | Retrieve Project
[**get_project_virt_realms**](ProjectsApi.md#get_project_virt_realms) | **GET** /api/projects/{id}/virtualizationrealms | List Virtualization Realms
[**get_projects**](ProjectsApi.md#get_projects) | **GET** /api/projects | List Joined Projects
[**get_projects_expanded**](ProjectsApi.md#get_projects_expanded) | **GET** /api/projects/expanded | List Unjoined Projects
[**get_virtual_machine_count_metrics**](ProjectsApi.md#get_virtual_machine_count_metrics) | **GET** /api/projects/{id}/metrics/virtualmachinecount | Retrieve Virtual Machine Metrics
[**list_members**](ProjectsApi.md#list_members) | **GET** /api/projects/{id}/members | List Members
[**list_submission_serivces_for_project**](ProjectsApi.md#list_submission_serivces_for_project) | **GET** /api/projects/{id}/submission | List Submission Services
[**remove_project_member**](ProjectsApi.md#remove_project_member) | **DELETE** /api/projects/{id}/members | Unassign Member from Project
[**remove_role_from_project_member**](ProjectsApi.md#remove_role_from_project_member) | **DELETE** /api/projects/{id}/members/roles | Unassign Role from Member
[**remove_submission_service_from_project**](ProjectsApi.md#remove_submission_service_from_project) | **DELETE** /api/projects/{id}/submission/{submission_service_id} | Remove Submission Service
[**remove_trusted_project1**](ProjectsApi.md#remove_trusted_project1) | **PUT** /api/projects/{id}/removetrustedproject | Unassign Trusted Project from Project
[**request_project_invitation**](ProjectsApi.md#request_project_invitation) | **POST** /api/projects/{id}/invitation | Create Invitation Code
[**set_project_default_power_schedule**](ProjectsApi.md#set_project_default_power_schedule) | **PUT** /api/projects/{id}/powerschedule | Update Default Power Schedule
[**set_project_default_virtualization_realm**](ProjectsApi.md#set_project_default_virtualization_realm) | **PUT** /api/projects/{id}/virtualizationrealms/default | Update Default Virtualization Realm
[**set_project_itar_information**](ProjectsApi.md#set_project_itar_information) | **PUT** /api/projects/{id}/itar | Set Asset Export Restriction
[**update_project**](ProjectsApi.md#update_project) | **PUT** /api/projects/{id} | Update Project
[**update_submission_service**](ProjectsApi.md#update_submission_service) | **PUT** /api/projects/{id}/submission/{submission_service_id} | Update Submission Service


# **add_project_member**
> bool add_project_member(username, id)

Assign Project Member

Assigns the provided user as a member of the specified Project.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
username = 'username_example' # str | Username of desired member
id = 'id_example' # str | ID of project

try:
    # Assign Project Member
    api_response = api_instance.add_project_member(username, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_project_member: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
username = 'username_example' # str | Username of desired member
id = 'id_example' # str | ID of project

try:
    # Assign Project Member
    api_response = api_instance.add_project_member(username, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_project_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username of desired member | 
 **id** | **str**| ID of project | 

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
**400** | Invalid project ID or username supplied |  -  |
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_role_to_project_member**
> bool add_role_to_project_member(id, username, role)

Assign Role to Member

Assigns the provided role to the specified member of the Project.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
username = 'username_example' # str | Username of project member
role = 'role_example' # str | Project role to add

try:
    # Assign Role to Member
    api_response = api_instance.add_role_to_project_member(id, username, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_role_to_project_member: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
username = 'username_example' # str | Username of project member
role = 'role_example' # str | Project role to add

try:
    # Assign Role to Member
    api_response = api_instance.add_role_to_project_member(id, username, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_role_to_project_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of project | 
 **username** | **str**| Username of project member | 
 **role** | **str**| Project role to add | 

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
**400** | Invalid project ID, username, or project role supplied |  -  |
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_submission_service_to_project**
> bool add_submission_service_to_project(id, input_submission_service_for_project)

Add Submission Service

Adds a new Submission Service to the list of available services for the specified Project.<br> <br> This Submission Service will act as a template for all Project members submitting to the Service. Members will be able to override the credentials used when submitting to this Service, but will not be able to override the Host or Port of the Service.<br> <br> If the Service's endpoint is an SFTP host, a submitting member will only be able to override the remote path if one has not already been defined in this default Submission Service.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
input_submission_service_for_project = cons3rt.InputSubmissionServiceForProject() # InputSubmissionServiceForProject | The submission service

try:
    # Add Submission Service
    api_response = api_instance.add_submission_service_to_project(id, input_submission_service_for_project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_submission_service_to_project: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
input_submission_service_for_project = cons3rt.InputSubmissionServiceForProject() # InputSubmissionServiceForProject | The submission service

try:
    # Add Submission Service
    api_response = api_instance.add_submission_service_to_project(id, input_submission_service_for_project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_submission_service_to_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of project | 
 **input_submission_service_for_project** | [**InputSubmissionServiceForProject**](InputSubmissionServiceForProject.md)| The submission service | 

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
**400** | Invalid project ID or data supplied |  -  |
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_trusted_project1**
> bool add_trusted_project1(id, trustedid)

Assign Trusted Project to Project

Adds the target Project as a Trusted Partner of the specified Project.<br> <br> Doing so makes the target Project eligible to be selected as trusted when sharing certain Assets.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
trustedid = 'trustedid_example' # str | ID of trusted project

try:
    # Assign Trusted Project to Project
    api_response = api_instance.add_trusted_project1(id, trustedid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_trusted_project1: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
trustedid = 'trustedid_example' # str | ID of trusted project

try:
    # Assign Trusted Project to Project
    api_response = api_instance.add_trusted_project1(id, trustedid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_trusted_project1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of project | 
 **trustedid** | **str**| ID of trusted project | 

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
**400** | Invalid project ID or target project ID supplied |  -  |
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> str create_project(input_project_full=input_project_full)

Create a Project

Creates a single Project.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
input_project_full = cons3rt.InputProjectFull() # InputProjectFull | The Project to create (optional)

try:
    # Create a Project
    api_response = api_instance.create_project(input_project_full=input_project_full)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->create_project: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
input_project_full = cons3rt.InputProjectFull() # InputProjectFull | The Project to create (optional)

try:
    # Create a Project
    api_response = api_instance.create_project(input_project_full=input_project_full)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_project_full** | [**InputProjectFull**](InputProjectFull.md)| The Project to create | [optional] 

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

# **delete_project**
> bool delete_project(id, force=force)

Delete Project

Deletes a single Project with the given ID.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
force = False # bool | Delete all dependencies (optional) (default to False)

try:
    # Delete Project
    api_response = api_instance.delete_project(id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_project: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
force = False # bool | Delete all dependencies (optional) (default to False)

try:
    # Delete Project
    api_response = api_instance.delete_project(id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of project | 
 **force** | **bool**| Delete all dependencies | [optional] [default to False]

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
**400** | Invalid project ID supplied |  -  |
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_host_configuration_metrics**
> str get_host_configuration_metrics(id, start, end, interval=interval, interval_unit=interval_unit)

Retrieve Metrics

Returns metric data for Deployment Runs launched by members of the specified Project.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
start = 56 # int | Interval start time, specified in seconds since epoch
end = 56 # int | Interval end time, specified in seconds since epoch
interval = 1 # int | Number of intervals (optional) (default to 1)
interval_unit = 'HOURS' # str | Interval unit (optional) (default to 'HOURS')

try:
    # Retrieve Metrics
    api_response = api_instance.get_host_configuration_metrics(id, start, end, interval=interval, interval_unit=interval_unit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_host_configuration_metrics: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
start = 56 # int | Interval start time, specified in seconds since epoch
end = 56 # int | Interval end time, specified in seconds since epoch
interval = 1 # int | Number of intervals (optional) (default to 1)
interval_unit = 'HOURS' # str | Interval unit (optional) (default to 'HOURS')

try:
    # Retrieve Metrics
    api_response = api_instance.get_host_configuration_metrics(id, start, end, interval=interval, interval_unit=interval_unit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_host_configuration_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of project | 
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
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> FullProject get_project(id)

Retrieve Project

Returns a single Project by the given ID.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project

try:
    # Retrieve Project
    api_response = api_instance.get_project(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project

try:
    # Retrieve Project
    api_response = api_instance.get_project(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of project | 

### Return type

[**FullProject**](FullProject.md)

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
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_virt_realms**
> list[MinimalVirtualizationRealm] get_project_virt_realms(id)

List Virtualization Realms

Returns a collection of the Virtualization Realms accessible by the specified Project.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project

try:
    # List Virtualization Realms
    api_response = api_instance.get_project_virt_realms(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project_virt_realms: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project

try:
    # List Virtualization Realms
    api_response = api_instance.get_project_virt_realms(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project_virt_realms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of project | 

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
**400** | Invalid project ID supplied |  -  |
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> list[MinimalProject] get_projects(maxresults=maxresults, page=page)

List Joined Projects

Returns a collection of the user's relevant Projects matching a specified query.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

try:
    # List Joined Projects
    api_response = api_instance.get_projects(maxresults=maxresults, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_projects: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

try:
    # List Joined Projects
    api_response = api_instance.get_projects(maxresults=maxresults, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**400** | Invalid query parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects_expanded**
> list[MinimalProject] get_projects_expanded(maxresults=maxresults, page=page)

List Unjoined Projects

Returns a collection of public Projects the user has not joined.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

try:
    # List Unjoined Projects
    api_response = api_instance.get_projects_expanded(maxresults=maxresults, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_projects_expanded: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

try:
    # List Unjoined Projects
    api_response = api_instance.get_projects_expanded(maxresults=maxresults, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_projects_expanded: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**400** | Invalid query parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_machine_count_metrics**
> str get_virtual_machine_count_metrics(id, start, end, interval=interval, interval_unit=interval_unit)

Retrieve Virtual Machine Metrics

Returns metric data for Virtual Machines launched by members of the specified Project.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
start = 56 # int | Interval start time, specified in seconds since epoch
end = 56 # int | Interval end time, specified in seconds since epoch
interval = 1 # int | Number of intervals (optional) (default to 1)
interval_unit = 'HOURS' # str | Interval unit (optional) (default to 'HOURS')

try:
    # Retrieve Virtual Machine Metrics
    api_response = api_instance.get_virtual_machine_count_metrics(id, start, end, interval=interval, interval_unit=interval_unit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_virtual_machine_count_metrics: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
start = 56 # int | Interval start time, specified in seconds since epoch
end = 56 # int | Interval end time, specified in seconds since epoch
interval = 1 # int | Number of intervals (optional) (default to 1)
interval_unit = 'HOURS' # str | Interval unit (optional) (default to 'HOURS')

try:
    # Retrieve Virtual Machine Metrics
    api_response = api_instance.get_virtual_machine_count_metrics(id, start, end, interval=interval, interval_unit=interval_unit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_virtual_machine_count_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of project | 
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
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_members**
> list[UserProject] list_members(id, membership_state=membership_state, role=role, name=name, maxresults=maxresults, page=page)

List Members

Returns a collection of the users that are members of the specified Project.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
membership_state = 'membership_state_example' # str | Project membership state type (optional)
role = 'role_example' # str | Project member role type (optional)
name = 'name_example' # str | User name to search for (optional)
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

try:
    # List Members
    api_response = api_instance.list_members(id, membership_state=membership_state, role=role, name=name, maxresults=maxresults, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->list_members: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
membership_state = 'membership_state_example' # str | Project membership state type (optional)
role = 'role_example' # str | Project member role type (optional)
name = 'name_example' # str | User name to search for (optional)
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

try:
    # List Members
    api_response = api_instance.list_members(id, membership_state=membership_state, role=role, name=name, maxresults=maxresults, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->list_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of project | 
 **membership_state** | **str**| Project membership state type | [optional] 
 **role** | **str**| Project member role type | [optional] 
 **name** | **str**| User name to search for | [optional] 
 **maxresults** | **int**| Maximum number of results to return | [optional] [default to 40]
 **page** | **int**| Requested page number | [optional] [default to 0]

### Return type

[**list[UserProject]**](UserProject.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid project ID supplied |  -  |
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_submission_serivces_for_project**
> list[SubmissionService] list_submission_serivces_for_project(id)

List Submission Services

Returns a collection of the available Submission Services for the specified Project.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project

try:
    # List Submission Services
    api_response = api_instance.list_submission_serivces_for_project(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->list_submission_serivces_for_project: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project

try:
    # List Submission Services
    api_response = api_instance.list_submission_serivces_for_project(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->list_submission_serivces_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of project | 

### Return type

[**list[SubmissionService]**](SubmissionService.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid project ID supplied |  -  |
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_project_member**
> bool remove_project_member(username, id)

Unassign Member from Project

Removes the provided member from the specified Project.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
username = 'username_example' # str | Username of desired member
id = 'id_example' # str | ID of project

try:
    # Unassign Member from Project
    api_response = api_instance.remove_project_member(username, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->remove_project_member: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
username = 'username_example' # str | Username of desired member
id = 'id_example' # str | ID of project

try:
    # Unassign Member from Project
    api_response = api_instance.remove_project_member(username, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->remove_project_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username of desired member | 
 **id** | **str**| ID of project | 

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
**400** | Invalid project ID or username supplied |  -  |
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_role_from_project_member**
> bool remove_role_from_project_member(id, username, role)

Unassign Role from Member

Removes the provided Role from the specified member of the Project.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
username = 'username_example' # str | Username of project member
role = 'role_example' # str | Project role to remove

try:
    # Unassign Role from Member
    api_response = api_instance.remove_role_from_project_member(id, username, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->remove_role_from_project_member: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
username = 'username_example' # str | Username of project member
role = 'role_example' # str | Project role to remove

try:
    # Unassign Role from Member
    api_response = api_instance.remove_role_from_project_member(id, username, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->remove_role_from_project_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of project | 
 **username** | **str**| Username of project member | 
 **role** | **str**| Project role to remove | 

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
**400** | Invalid project ID, username, or project role supplied |  -  |
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_submission_service_from_project**
> bool remove_submission_service_from_project(id, submission_service_id)

Remove Submission Service

Removes the provided Submission Service from the list of available Services for the specified Project.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
submission_service_id = 'submission_service_id_example' # str | ID of submission service

try:
    # Remove Submission Service
    api_response = api_instance.remove_submission_service_from_project(id, submission_service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->remove_submission_service_from_project: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
submission_service_id = 'submission_service_id_example' # str | ID of submission service

try:
    # Remove Submission Service
    api_response = api_instance.remove_submission_service_from_project(id, submission_service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->remove_submission_service_from_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of project | 
 **submission_service_id** | **str**| ID of submission service | 

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
**400** | Invalid project ID or submission service supplied |  -  |
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_trusted_project1**
> bool remove_trusted_project1(id, trustedid)

Unassign Trusted Project from Project

Removes the target Project from the specified Project's list of Trusted Partners.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
trustedid = 'trustedid_example' # str | ID of trusted project

try:
    # Unassign Trusted Project from Project
    api_response = api_instance.remove_trusted_project1(id, trustedid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->remove_trusted_project1: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
trustedid = 'trustedid_example' # str | ID of trusted project

try:
    # Unassign Trusted Project from Project
    api_response = api_instance.remove_trusted_project1(id, trustedid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->remove_trusted_project1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of project | 
 **trustedid** | **str**| ID of trusted project | 

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
**400** | Invalid project ID or target project ID supplied |  -  |
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_project_invitation**
> str request_project_invitation(id, email)

Create Invitation Code

Creates an Invitation Code to be used by a new user at the time of creation to automatically associate them with the specified Project.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
email = 'email_example' # str | Email address of invitee

try:
    # Create Invitation Code
    api_response = api_instance.request_project_invitation(id, email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->request_project_invitation: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
email = 'email_example' # str | Email address of invitee

try:
    # Create Invitation Code
    api_response = api_instance.request_project_invitation(id, email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->request_project_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of project | 
 **email** | **str**| Email address of invitee | 

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
**400** | Invalid project ID or email address supplied |  -  |
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_project_default_power_schedule**
> bool set_project_default_power_schedule(id, power_schedule=power_schedule)

Update Default Power Schedule

Updates the default Power Schedule for Deployment Runs launched by members of the specified Project.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
power_schedule = cons3rt.PowerSchedule() # PowerSchedule | The desired power schedule (optional)

try:
    # Update Default Power Schedule
    api_response = api_instance.set_project_default_power_schedule(id, power_schedule=power_schedule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_project_default_power_schedule: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
power_schedule = cons3rt.PowerSchedule() # PowerSchedule | The desired power schedule (optional)

try:
    # Update Default Power Schedule
    api_response = api_instance.set_project_default_power_schedule(id, power_schedule=power_schedule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_project_default_power_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of project | 
 **power_schedule** | [**PowerSchedule**](PowerSchedule.md)| The desired power schedule | [optional] 

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
**400** | Invalid project ID or power scheduled supplied |  -  |
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_project_default_virtualization_realm**
> bool set_project_default_virtualization_realm(id, virtualizationrealmid)

Update Default Virtualization Realm

Updates the default Virtualization Realm for the specified Project.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
virtualizationrealmid = 'virtualizationrealmid_example' # str | ID of virtualization realm

try:
    # Update Default Virtualization Realm
    api_response = api_instance.set_project_default_virtualization_realm(id, virtualizationrealmid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_project_default_virtualization_realm: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
virtualizationrealmid = 'virtualizationrealmid_example' # str | ID of virtualization realm

try:
    # Update Default Virtualization Realm
    api_response = api_instance.set_project_default_virtualization_realm(id, virtualizationrealmid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_project_default_virtualization_realm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of project | 
 **virtualizationrealmid** | **str**| ID of virtualization realm | 

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
**400** | Invalid project ID or virtualization realm ID supplied |  -  |
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_project_itar_information**
> bool set_project_itar_information(id, message=message)

Set Asset Export Restriction

Sets the Export Restriction of Assets created within the specified Project.<br> <br> Once a Project is labeled as ITAR-restricted, this cannot be changed.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
message = 'message_example' # str | Additional information about the export restriction (optional)

try:
    # Set Asset Export Restriction
    api_response = api_instance.set_project_itar_information(id, message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_project_itar_information: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
message = 'message_example' # str | Additional information about the export restriction (optional)

try:
    # Set Asset Export Restriction
    api_response = api_instance.set_project_itar_information(id, message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_project_itar_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of project | 
 **message** | **str**| Additional information about the export restriction | [optional] 

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
**400** | Invalid project ID or export restriction supplied |  -  |
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> bool update_project(id, input_project_update=input_project_update)

Update Project

Updates the content of a single Project with the given ID.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
input_project_update = cons3rt.InputProjectUpdate() # InputProjectUpdate | The modified Project (optional)

try:
    # Update Project
    api_response = api_instance.update_project(id, input_project_update=input_project_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->update_project: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
input_project_update = cons3rt.InputProjectUpdate() # InputProjectUpdate | The modified Project (optional)

try:
    # Update Project
    api_response = api_instance.update_project(id, input_project_update=input_project_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of project | 
 **input_project_update** | [**InputProjectUpdate**](InputProjectUpdate.md)| The modified Project | [optional] 

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
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_submission_service**
> bool update_submission_service(id, submission_service_id, input_submission_service_for_project)

Update Submission Service

Updates an existing Submission Service in the specified Project.<br> <br> This Submission Service will act as a template for all Project members submitting to the Service. Members will be able to override the credentials used when submitting to this Service, but will not be able to override the Host or Port of the Service.<br> <br> If the Service's endpoint is an SFTP Host, a submitting member will only be able to override the remote path if one has not already been defined in this default Submission Service.

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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
submission_service_id = 'submission_service_id_example' # str | ID of submission service
input_submission_service_for_project = cons3rt.InputSubmissionServiceForProject() # InputSubmissionServiceForProject | The submission service

try:
    # Update Submission Service
    api_response = api_instance.update_submission_service(id, submission_service_id, input_submission_service_for_project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->update_submission_service: %s\n" % e)
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
api_instance = cons3rt.ProjectsApi(cons3rt.ApiClient(configuration))
id = 'id_example' # str | ID of project
submission_service_id = 'submission_service_id_example' # str | ID of submission service
input_submission_service_for_project = cons3rt.InputSubmissionServiceForProject() # InputSubmissionServiceForProject | The submission service

try:
    # Update Submission Service
    api_response = api_instance.update_submission_service(id, submission_service_id, input_submission_service_for_project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->update_submission_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of project | 
 **submission_service_id** | **str**| ID of submission service | 
 **input_submission_service_for_project** | [**InputSubmissionServiceForProject**](InputSubmissionServiceForProject.md)| The submission service | 

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
**400** | Invalid project ID, submission service ID, or data supplied |  -  |
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

