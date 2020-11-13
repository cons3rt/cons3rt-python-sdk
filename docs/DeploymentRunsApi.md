# cons3rt.DeploymentRunsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_category_to_deployment_run**](DeploymentRunsApi.md#add_category_to_deployment_run) | **PUT** /api/categories/{id}/run | Assign Category to Run
[**delete_deployment_run**](DeploymentRunsApi.md#delete_deployment_run) | **DELETE** /api/drs/{id} | Delete Deployment Run
[**download_deployment_run_test_report**](DeploymentRunsApi.md#download_deployment_run_test_report) | **GET** /api/drs/{id}/downloadreport | Download Report
[**download_host**](DeploymentRunsApi.md#download_host) | **GET** /api/drs/{id}/downloadhost | Download Host
[**get_deployment_run**](DeploymentRunsApi.md#get_deployment_run) | **GET** /api/drs/{id} | Retrieve Deployment Run
[**get_deployment_run_reports**](DeploymentRunsApi.md#get_deployment_run_reports) | **GET** /api/drs/{id}/reports | List Reports
[**get_deployment_runs**](DeploymentRunsApi.md#get_deployment_runs) | **GET** /api/deployments/{id}/runs | List Deployment Runs
[**get_deployment_runs1**](DeploymentRunsApi.md#get_deployment_runs1) | **GET** /api/drs | List Deployment Runs
[**get_host**](DeploymentRunsApi.md#get_host) | **GET** /api/drs/{id}/host/{hostid} | Retrieve Host
[**get_host_access**](DeploymentRunsApi.md#get_host_access) | **GET** /api/drs/{id}/host/{hostid}/access | List Host Access Logs
[**get_host_configuration_metrics**](DeploymentRunsApi.md#get_host_configuration_metrics) | **GET** /api/projects/{id}/metrics/hostconfiguration | Retrieve Metrics
[**get_host_instance_types**](DeploymentRunsApi.md#get_host_instance_types) | **GET** /api/drs/{id}/host/{hostid}/resize | List available instance types for host
[**perform_host_action**](DeploymentRunsApi.md#perform_host_action) | **PUT** /api/drs/{id}/hostaction | Execute Host Action
[**publish_deployment_run**](DeploymentRunsApi.md#publish_deployment_run) | **POST** /api/drs/{id}/publish | Publish Deployment Run
[**redeploy_container_asset**](DeploymentRunsApi.md#redeploy_container_asset) | **PUT** /api/drs/{id}/host/{hostid}/container | Re-deploy Container Asset
[**relaunch_deployment_run**](DeploymentRunsApi.md#relaunch_deployment_run) | **PUT** /api/drs/{id}/rerun | Relaunch Deployment Run
[**release_deployment_run**](DeploymentRunsApi.md#release_deployment_run) | **PUT** /api/drs/{id}/release | Release Deployment Run
[**remove_category_from_deployment_run**](DeploymentRunsApi.md#remove_category_from_deployment_run) | **DELETE** /api/categories/{id}/run | Unassign Category from deployment run
[**retest_deployment_run**](DeploymentRunsApi.md#retest_deployment_run) | **PUT** /api/drs/{id}/retest | Re-test Deployment Run
[**set_deployment_run_lock**](DeploymentRunsApi.md#set_deployment_run_lock) | **PUT** /api/drs/{id}/setlock | Update Lock
[**set_power_schedule_for_deployment_run**](DeploymentRunsApi.md#set_power_schedule_for_deployment_run) | **PUT** /api/drs/{id}/powerschedule | Update Power Schedule
[**unpublish_deployment_run**](DeploymentRunsApi.md#unpublish_deployment_run) | **DELETE** /api/drs/{id}/publish | Unpublish Deployment Run


# **add_category_to_deployment_run**
> bool add_category_to_deployment_run(id, runid)

Assign Category to Run

Assigns the Category as a filter tag to the provided Deployment Run.<br> <br> Altering the Category will affect future Run filtering.

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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of category
runid = 'runid_example' # str | ID of run to assign

    try:
        # Assign Category to Run
        api_response = api_instance.add_category_to_deployment_run(id, runid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->add_category_to_deployment_run: %s\n" % e)
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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of category
runid = 'runid_example' # str | ID of run to assign

    try:
        # Assign Category to Run
        api_response = api_instance.add_category_to_deployment_run(id, runid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->add_category_to_deployment_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of category | 
 **runid** | **str**| ID of run to assign | 

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
**400** | Invalid category ID or deplyoyment run ID supplied |  -  |
**404** | Category not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_deployment_run**
> bool delete_deployment_run(id, purge=purge)

Delete Deployment Run

Deletes a single inactive Deployment Run with the given ID.

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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run
purge = False # bool | Delete all dependencies of the deployment run (optional) (default to False)

    try:
        # Delete Deployment Run
        api_response = api_instance.delete_deployment_run(id, purge=purge)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->delete_deployment_run: %s\n" % e)
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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run
purge = False # bool | Delete all dependencies of the deployment run (optional) (default to False)

    try:
        # Delete Deployment Run
        api_response = api_instance.delete_deployment_run(id, purge=purge)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->delete_deployment_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment run | 
 **purge** | **bool**| Delete all dependencies of the deployment run | [optional] [default to False]

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
**400** | Invalid deployment run ID supplied |  -  |
**404** | Deployment run not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_deployment_run_test_report**
> download_deployment_run_test_report(id, file=file, number=number)

Download Report

Downloads a single Test Report for the specified Deployment Run.

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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run
file = 'file_example' # str | Report file name (optional)
number = 'number_example' # str | Report number (optional)

    try:
        # Download Report
        api_instance.download_deployment_run_test_report(id, file=file, number=number)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->download_deployment_run_test_report: %s\n" % e)
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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run
file = 'file_example' # str | Report file name (optional)
number = 'number_example' # str | Report number (optional)

    try:
        # Download Report
        api_instance.download_deployment_run_test_report(id, file=file, number=number)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->download_deployment_run_test_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment run | 
 **file** | **str**| Report file name | [optional] 
 **number** | **str**| Report number | [optional] 

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
**400** | Invalid ID supplied |  -  |
**404** | Deployment run not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_host**
> download_host(id, role, background=background)

Download Host

Downloads a single Host Bundle for the specified Deployment Run.<br> <br> Based on the background flag, the download will either be done in the foreground (false), background (true), or be determined by asset size (no value).<br> <br> If the background flag is set to true (or no value for the background flag is provided), and the host is larger than the site threshold, it will be prepared for download in the background and an email with a link to retrieve the asset will be sent.

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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run
role = 'role_example' # str | Name of host to bundle for download
background = False # bool | Force the download to happen in the background (optional) (default to False)

    try:
        # Download Host
        api_instance.download_host(id, role, background=background)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->download_host: %s\n" % e)
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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run
role = 'role_example' # str | Name of host to bundle for download
background = False # bool | Force the download to happen in the background (optional) (default to False)

    try:
        # Download Host
        api_instance.download_host(id, role, background=background)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->download_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment run | 
 **role** | **str**| Name of host to bundle for download | 
 **background** | **bool**| Force the download to happen in the background | [optional] [default to False]

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
**202** | Accepted |  -  |
**400** | Invalid ID or role supplied |  -  |
**404** | Deployment run not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_run**
> FullDeploymentRun get_deployment_run(id)

Retrieve Deployment Run

Returns a single Deployment Run by the given ID.

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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run

    try:
        # Retrieve Deployment Run
        api_response = api_instance.get_deployment_run(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->get_deployment_run: %s\n" % e)
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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run

    try:
        # Retrieve Deployment Run
        api_response = api_instance.get_deployment_run(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->get_deployment_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment run | 

### Return type

[**FullDeploymentRun**](FullDeploymentRun.md)

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
**404** | Deployment run not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_run_reports**
> list[str] get_deployment_run_reports(id)

List Reports

Returns a collection of the Test Reports for a single Deployment Run.

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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run

    try:
        # List Reports
        api_response = api_instance.get_deployment_run_reports(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->get_deployment_run_reports: %s\n" % e)
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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run

    try:
        # List Reports
        api_response = api_instance.get_deployment_run_reports(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->get_deployment_run_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment run | 

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
**400** | Invalid deployment run ID supplied |  -  |
**404** | Deployment run not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_runs**
> list[MinimalDeploymentRun] get_deployment_runs(id, maxresults=maxresults, page=page)

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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

    try:
        # List Deployment Runs
        api_response = api_instance.get_deployment_runs(id, maxresults=maxresults, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->get_deployment_runs: %s\n" % e)
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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

    try:
        # List Deployment Runs
        api_response = api_instance.get_deployment_runs(id, maxresults=maxresults, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->get_deployment_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment | 
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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    search_type = 'search_type_example' # str | Deployment run status
in_project = False # bool | Include project runs (optional) (default to False)
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

    try:
        # List Deployment Runs
        api_response = api_instance.get_deployment_runs1(search_type, in_project=in_project, maxresults=maxresults, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->get_deployment_runs1: %s\n" % e)
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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    search_type = 'search_type_example' # str | Deployment run status
in_project = False # bool | Include project runs (optional) (default to False)
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

    try:
        # List Deployment Runs
        api_response = api_instance.get_deployment_runs1(search_type, in_project=in_project, maxresults=maxresults, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->get_deployment_runs1: %s\n" % e)
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

# **get_host**
> MinimalDeploymentRunHost get_host(id, hostid)

Retrieve Host

Returns the specified Host in the Deployment Run by the given ID.

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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run
hostid = 'hostid_example' # str | ID of host

    try:
        # Retrieve Host
        api_response = api_instance.get_host(id, hostid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->get_host: %s\n" % e)
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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run
hostid = 'hostid_example' # str | ID of host

    try:
        # Retrieve Host
        api_response = api_instance.get_host(id, hostid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->get_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment run | 
 **hostid** | **str**| ID of host | 

### Return type

[**MinimalDeploymentRunHost**](MinimalDeploymentRunHost.md)

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
**404** | Deployment run not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_host_access**
> list[RemoteAccessSession] get_host_access(id, hostid, maxresults=maxresults, page=page)

List Host Access Logs

Returns a collection of the Host Access Logs for a single Deployment Run.

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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run
hostid = 'hostid_example' # str | ID of host
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

    try:
        # List Host Access Logs
        api_response = api_instance.get_host_access(id, hostid, maxresults=maxresults, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->get_host_access: %s\n" % e)
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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run
hostid = 'hostid_example' # str | ID of host
maxresults = 40 # int | Maximum number of results to return (optional) (default to 40)
page = 0 # int | Requested page number (optional) (default to 0)

    try:
        # List Host Access Logs
        api_response = api_instance.get_host_access(id, hostid, maxresults=maxresults, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->get_host_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment run | 
 **hostid** | **str**| ID of host | 
 **maxresults** | **int**| Maximum number of results to return | [optional] [default to 40]
 **page** | **int**| Requested page number | [optional] [default to 0]

### Return type

[**list[RemoteAccessSession]**](RemoteAccessSession.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid deployment run ID, host id, or query parameter supplied |  -  |
**404** | Deployment run or host not found |  -  |

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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
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
        print("Exception when calling DeploymentRunsApi->get_host_configuration_metrics: %s\n" % e)
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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
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
        print("Exception when calling DeploymentRunsApi->get_host_configuration_metrics: %s\n" % e)
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

# **get_host_instance_types**
> TargetInstanceTypes get_host_instance_types(id, hostid)

List available instance types for host

Returns a collection of available instance types for resizing a Deployment Run Host.

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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run
hostid = 'hostid_example' # str | ID of host

    try:
        # List available instance types for host
        api_response = api_instance.get_host_instance_types(id, hostid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->get_host_instance_types: %s\n" % e)
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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run
hostid = 'hostid_example' # str | ID of host

    try:
        # List available instance types for host
        api_response = api_instance.get_host_instance_types(id, hostid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->get_host_instance_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment run | 
 **hostid** | **str**| ID of host | 

### Return type

[**TargetInstanceTypes**](TargetInstanceTypes.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid deployment run ID, host id, or query parameter supplied |  -  |
**404** | Deployment run or host not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_host_action**
> bool perform_host_action(id, deploymentrunhostid, action, cpu=cpu, ram=ram, instance_type_name=instance_type_name)

Execute Host Action

Executes an action against the specified Host in the Deployment Run for the ID provided.

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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run
deploymentrunhostid = 'deploymentrunhostid_example' # str | ID of host
action = 'action_example' # str | Action to perform
cpu = 56 # int | Desired number of CPUs, if resizing host in a non instance type based virtualization realm (optional)
ram = 56 # int | Desired amount of RAM in Mebibytes, if resizing host in a non instance type based virtualization realm (optional)
instance_type_name = 'instance_type_name_example' # str | The instance type name to resize to, if resizing host in an instance type based virtualization realm (optional)

    try:
        # Execute Host Action
        api_response = api_instance.perform_host_action(id, deploymentrunhostid, action, cpu=cpu, ram=ram, instance_type_name=instance_type_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->perform_host_action: %s\n" % e)
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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run
deploymentrunhostid = 'deploymentrunhostid_example' # str | ID of host
action = 'action_example' # str | Action to perform
cpu = 56 # int | Desired number of CPUs, if resizing host in a non instance type based virtualization realm (optional)
ram = 56 # int | Desired amount of RAM in Mebibytes, if resizing host in a non instance type based virtualization realm (optional)
instance_type_name = 'instance_type_name_example' # str | The instance type name to resize to, if resizing host in an instance type based virtualization realm (optional)

    try:
        # Execute Host Action
        api_response = api_instance.perform_host_action(id, deploymentrunhostid, action, cpu=cpu, ram=ram, instance_type_name=instance_type_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->perform_host_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment run | 
 **deploymentrunhostid** | **str**| ID of host | 
 **action** | **str**| Action to perform | 
 **cpu** | **int**| Desired number of CPUs, if resizing host in a non instance type based virtualization realm | [optional] 
 **ram** | **int**| Desired amount of RAM in Mebibytes, if resizing host in a non instance type based virtualization realm | [optional] 
 **instance_type_name** | **str**| The instance type name to resize to, if resizing host in an instance type based virtualization realm | [optional] 

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
**400** | Invalid deployment run ID or host ID supplied |  -  |
**404** | Deployment run not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_deployment_run**
> bool publish_deployment_run(id)

Publish Deployment Run

Publishes the specified Deployment as a Composition.<br> <br> Consumers will be able to connect to the run, but will not be able to manage the composition.

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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run

    try:
        # Publish Deployment Run
        api_response = api_instance.publish_deployment_run(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->publish_deployment_run: %s\n" % e)
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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run

    try:
        # Publish Deployment Run
        api_response = api_instance.publish_deployment_run(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->publish_deployment_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment run | 

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
**400** | Invalid deployment run ID or data supplied |  -  |
**404** | Deployment run not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeploy_container_asset**
> bool redeploy_container_asset(id, hostid, installationid, input_container_component=input_container_component)

Re-deploy Container Asset

Re-deploys the specified Container Asset installation on the single Host in the specified Deployment Run.

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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run
hostid = 'hostid_example' # str | ID of host
installationid = 'installationid_example' # str | ID of container asset installation
input_container_component = cons3rt.InputContainerComponent() # InputContainerComponent | The updated Container Component definition (optional)

    try:
        # Re-deploy Container Asset
        api_response = api_instance.redeploy_container_asset(id, hostid, installationid, input_container_component=input_container_component)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->redeploy_container_asset: %s\n" % e)
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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run
hostid = 'hostid_example' # str | ID of host
installationid = 'installationid_example' # str | ID of container asset installation
input_container_component = cons3rt.InputContainerComponent() # InputContainerComponent | The updated Container Component definition (optional)

    try:
        # Re-deploy Container Asset
        api_response = api_instance.redeploy_container_asset(id, hostid, installationid, input_container_component=input_container_component)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->redeploy_container_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment run | 
 **hostid** | **str**| ID of host | 
 **installationid** | **str**| ID of container asset installation | 
 **input_container_component** | [**InputContainerComponent**](InputContainerComponent.md)| The updated Container Component definition | [optional] 

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
**400** | Invalid deployment run ID, host ID, or installation ID supplied |  -  |
**404** | Deployment run not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relaunch_deployment_run**
> str relaunch_deployment_run(id)

Relaunch Deployment Run

Launches a new Deployment Run with the same configuration as the specified Deployment Run.

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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run

    try:
        # Relaunch Deployment Run
        api_response = api_instance.relaunch_deployment_run(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->relaunch_deployment_run: %s\n" % e)
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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run

    try:
        # Relaunch Deployment Run
        api_response = api_instance.relaunch_deployment_run(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->relaunch_deployment_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment run | 

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
**400** | Invalid deployment run ID supplied |  -  |
**404** | Deployment run not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_deployment_run**
> bool release_deployment_run(id, force=force)

Release Deployment Run

Releases the Deployment Run for the ID provided.<br> <br> If the user is an Administrator, the force flag is honored.<br> <br> If the user is a non-Admin, the force flag is only honored in the event that a release request experiences an exception known to be resolved by a force.

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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run
force = False # bool | Force the release of this run (optional) (default to False)

    try:
        # Release Deployment Run
        api_response = api_instance.release_deployment_run(id, force=force)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->release_deployment_run: %s\n" % e)
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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run
force = False # bool | Force the release of this run (optional) (default to False)

    try:
        # Release Deployment Run
        api_response = api_instance.release_deployment_run(id, force=force)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->release_deployment_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment run | 
 **force** | **bool**| Force the release of this run | [optional] [default to False]

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
**400** | Invalid deployment run ID supplied |  -  |
**404** | Deployment run not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_category_from_deployment_run**
> bool remove_category_from_deployment_run(id, runid)

Unassign Category from deployment run

Removes the Category as a filter tag from the provided Run.<br> <br> Altering the Category will affect future run filtering.

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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of category
runid = 'runid_example' # str | ID of run to unassign

    try:
        # Unassign Category from deployment run
        api_response = api_instance.remove_category_from_deployment_run(id, runid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->remove_category_from_deployment_run: %s\n" % e)
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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of category
runid = 'runid_example' # str | ID of run to unassign

    try:
        # Unassign Category from deployment run
        api_response = api_instance.remove_category_from_deployment_run(id, runid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->remove_category_from_deployment_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of category | 
 **runid** | **str**| ID of run to unassign | 

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
**400** | Invalid category ID or run ID supplied |  -  |
**404** | Category not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retest_deployment_run**
> bool retest_deployment_run(id)

Re-test Deployment Run

Re-executes all Tests in the specified Deployment Run.

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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run

    try:
        # Re-test Deployment Run
        api_response = api_instance.retest_deployment_run(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->retest_deployment_run: %s\n" % e)
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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run

    try:
        # Re-test Deployment Run
        api_response = api_instance.retest_deployment_run(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->retest_deployment_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment run | 

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
**400** | Invalid deployment run ID supplied |  -  |
**404** | Deployment run not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_deployment_run_lock**
> bool set_deployment_run_lock(id, lock)

Update Lock

Update the Lock on a single Deployment Run with the given ID.

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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run
lock = True # bool | The desired lock state

    try:
        # Update Lock
        api_response = api_instance.set_deployment_run_lock(id, lock)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->set_deployment_run_lock: %s\n" % e)
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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run
lock = True # bool | The desired lock state

    try:
        # Update Lock
        api_response = api_instance.set_deployment_run_lock(id, lock)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->set_deployment_run_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment run | 
 **lock** | **bool**| The desired lock state | 

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
**400** | Invalid ID or lock supplied |  -  |
**404** | Deployment run not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_power_schedule_for_deployment_run**
> bool set_power_schedule_for_deployment_run(id, power_schedule=power_schedule)

Update Power Schedule

Updates the Power Schedule for a single Deployment Run with the given ID.

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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run
power_schedule = cons3rt.PowerSchedule() # PowerSchedule | The desired power schedule (optional)

    try:
        # Update Power Schedule
        api_response = api_instance.set_power_schedule_for_deployment_run(id, power_schedule=power_schedule)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->set_power_schedule_for_deployment_run: %s\n" % e)
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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run
power_schedule = cons3rt.PowerSchedule() # PowerSchedule | The desired power schedule (optional)

    try:
        # Update Power Schedule
        api_response = api_instance.set_power_schedule_for_deployment_run(id, power_schedule=power_schedule)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->set_power_schedule_for_deployment_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment run | 
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
**400** | Invalid ID or data supplied |  -  |
**404** | Deployment run not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpublish_deployment_run**
> bool unpublish_deployment_run(id)

Unpublish Deployment Run

Unpublishes the specified Deployment as a Composition.<br> <br> Consumers will no longer be able to connect to the run, and the run will no longer appear to consumers.

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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run

    try:
        # Unpublish Deployment Run
        api_response = api_instance.unpublish_deployment_run(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->unpublish_deployment_run: %s\n" % e)
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
    api_instance = cons3rt.DeploymentRunsApi(api_client)
    id = 'id_example' # str | ID of deployment run

    try:
        # Unpublish Deployment Run
        api_response = api_instance.unpublish_deployment_run(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentRunsApi->unpublish_deployment_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment run | 

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
**400** | Invalid deployment run ID or data supplied |  -  |
**404** | Deployment run not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

