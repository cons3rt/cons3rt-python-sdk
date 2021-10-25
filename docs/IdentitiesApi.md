# cons3rt.IdentitiesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_identity**](IdentitiesApi.md#create_identity) | **POST** /api/drs/{id}/host/{hostid}/identity | Create a host identity
[**delete_identity**](IdentitiesApi.md#delete_identity) | **DELETE** /api/drs/{id}/host/{hostid}/identity | Delete host identity
[**delete_identity_by_id**](IdentitiesApi.md#delete_identity_by_id) | **DELETE** /api/drs/{id}/host/{hostid}/identity/{username} | Deletes identity for specified user
[**get_identities**](IdentitiesApi.md#get_identities) | **GET** /api/drs/{id}/host/{hostid}/identities | Get Host Identities
[**get_identity**](IdentitiesApi.md#get_identity) | **GET** /api/drs/{id}/host/{hostid}/identity | Get Host Identity For User


# **create_identity**
> list[BaseIdentity] create_identity(id, hostid, cloud_resource_object)

Create a host identity

Creates an identity for the deployment run host with access to the resources requested by the user

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
    api_instance = cons3rt.IdentitiesApi(api_client)
    id = 'id_example' # str | ID of deployment run
hostid = 'hostid_example' # str | ID of host
cloud_resource_object = [cons3rt.CloudResourceObject()] # list[CloudResourceObject] | The cloud resources to be accessed by the host identity

    try:
        # Create a host identity
        api_response = api_instance.create_identity(id, hostid, cloud_resource_object)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IdentitiesApi->create_identity: %s\n" % e)
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
    api_instance = cons3rt.IdentitiesApi(api_client)
    id = 'id_example' # str | ID of deployment run
hostid = 'hostid_example' # str | ID of host
cloud_resource_object = [cons3rt.CloudResourceObject()] # list[CloudResourceObject] | The cloud resources to be accessed by the host identity

    try:
        # Create a host identity
        api_response = api_instance.create_identity(id, hostid, cloud_resource_object)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IdentitiesApi->create_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment run | 
 **hostid** | **str**| ID of host | 
 **cloud_resource_object** | [**list[CloudResourceObject]**](CloudResourceObject.md)| The cloud resources to be accessed by the host identity | 

### Return type

[**list[BaseIdentity]**](BaseIdentity.md)

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

# **delete_identity**
> bool delete_identity(id, hostid)

Delete host identity

Deletes the identity of a deployment run host.

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
    api_instance = cons3rt.IdentitiesApi(api_client)
    id = 'id_example' # str | ID of deployment run
hostid = 'hostid_example' # str | ID of host

    try:
        # Delete host identity
        api_response = api_instance.delete_identity(id, hostid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IdentitiesApi->delete_identity: %s\n" % e)
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
    api_instance = cons3rt.IdentitiesApi(api_client)
    id = 'id_example' # str | ID of deployment run
hostid = 'hostid_example' # str | ID of host

    try:
        # Delete host identity
        api_response = api_instance.delete_identity(id, hostid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IdentitiesApi->delete_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment run | 
 **hostid** | **str**| ID of host | 

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
**400** | Invalid deployment run ID, host id, or query parameter supplied |  -  |
**404** | Deployment run, host, or identity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identity_by_id**
> list[BaseIdentity] delete_identity_by_id(id, hostid, username)

Deletes identity for specified user

Deletes an identity for a user specified by name

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
    api_instance = cons3rt.IdentitiesApi(api_client)
    id = 'id_example' # str | ID of deployment run
hostid = 'hostid_example' # str | ID of host
username = 'username_example' # str | Username of the identity to be deleted

    try:
        # Deletes identity for specified user
        api_response = api_instance.delete_identity_by_id(id, hostid, username)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IdentitiesApi->delete_identity_by_id: %s\n" % e)
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
    api_instance = cons3rt.IdentitiesApi(api_client)
    id = 'id_example' # str | ID of deployment run
hostid = 'hostid_example' # str | ID of host
username = 'username_example' # str | Username of the identity to be deleted

    try:
        # Deletes identity for specified user
        api_response = api_instance.delete_identity_by_id(id, hostid, username)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IdentitiesApi->delete_identity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment run | 
 **hostid** | **str**| ID of host | 
 **username** | **str**| Username of the identity to be deleted | 

### Return type

[**list[BaseIdentity]**](BaseIdentity.md)

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
**404** | Deployment run, host, or identity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identities**
> list[BaseIdentity] get_identities(id, hostid)

Get Host Identities

Returns a collection of identities for the deployment run host

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
    api_instance = cons3rt.IdentitiesApi(api_client)
    id = 'id_example' # str | ID of deployment run
hostid = 'hostid_example' # str | ID of host

    try:
        # Get Host Identities
        api_response = api_instance.get_identities(id, hostid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IdentitiesApi->get_identities: %s\n" % e)
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
    api_instance = cons3rt.IdentitiesApi(api_client)
    id = 'id_example' # str | ID of deployment run
hostid = 'hostid_example' # str | ID of host

    try:
        # Get Host Identities
        api_response = api_instance.get_identities(id, hostid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IdentitiesApi->get_identities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment run | 
 **hostid** | **str**| ID of host | 

### Return type

[**list[BaseIdentity]**](BaseIdentity.md)

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

# **get_identity**
> list[CloudResourceAccessListing] get_identity(id, hostid)

Get Host Identity For User

Returns the deployment run host identity for the user, if one exists.

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
    api_instance = cons3rt.IdentitiesApi(api_client)
    id = 'id_example' # str | ID of deployment run
hostid = 'hostid_example' # str | ID of host

    try:
        # Get Host Identity For User
        api_response = api_instance.get_identity(id, hostid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IdentitiesApi->get_identity: %s\n" % e)
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
    api_instance = cons3rt.IdentitiesApi(api_client)
    id = 'id_example' # str | ID of deployment run
hostid = 'hostid_example' # str | ID of host

    try:
        # Get Host Identity For User
        api_response = api_instance.get_identity(id, hostid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IdentitiesApi->get_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of deployment run | 
 **hostid** | **str**| ID of host | 

### Return type

[**list[CloudResourceAccessListing]**](CloudResourceAccessListing.md)

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

