# cons3rt.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_build_number**](DefaultApi.md#get_build_number) | **GET** /public/buildNumber | 
[**get_build_timestamp**](DefaultApi.md#get_build_timestamp) | **GET** /public/buildTimestamp | 
[**get_cons3rt_version**](DefaultApi.md#get_cons3rt_version) | **GET** /public/cons3rtVersion | 
[**get_revision**](DefaultApi.md#get_revision) | **GET** /public/revision | 
[**get_root_html**](DefaultApi.md#get_root_html) | **GET** /public | 
[**get_short_version**](DefaultApi.md#get_short_version) | **GET** /public/shortVersion | 
[**get_version**](DefaultApi.md#get_version) | **GET** /public/version | 
[**validate_credentials**](DefaultApi.md#validate_credentials) | **GET** /api/validatecredentials | 


# **get_build_number**
> str get_build_number()



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
    api_instance = cons3rt.DefaultApi(api_client)
    
    try:
        api_response = api_instance.get_build_number()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_build_number: %s\n" % e)
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
    api_instance = cons3rt.DefaultApi(api_client)
    
    try:
        api_response = api_instance.get_build_number()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_build_number: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_build_timestamp**
> str get_build_timestamp()



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
    api_instance = cons3rt.DefaultApi(api_client)
    
    try:
        api_response = api_instance.get_build_timestamp()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_build_timestamp: %s\n" % e)
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
    api_instance = cons3rt.DefaultApi(api_client)
    
    try:
        api_response = api_instance.get_build_timestamp()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_build_timestamp: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cons3rt_version**
> str get_cons3rt_version()



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
    api_instance = cons3rt.DefaultApi(api_client)
    
    try:
        api_response = api_instance.get_cons3rt_version()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_cons3rt_version: %s\n" % e)
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
    api_instance = cons3rt.DefaultApi(api_client)
    
    try:
        api_response = api_instance.get_cons3rt_version()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_cons3rt_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_revision**
> str get_revision()



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
    api_instance = cons3rt.DefaultApi(api_client)
    
    try:
        api_response = api_instance.get_revision()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_revision: %s\n" % e)
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
    api_instance = cons3rt.DefaultApi(api_client)
    
    try:
        api_response = api_instance.get_revision()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_revision: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root_html**
> str get_root_html()



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
    api_instance = cons3rt.DefaultApi(api_client)
    
    try:
        api_response = api_instance.get_root_html()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_root_html: %s\n" % e)
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
    api_instance = cons3rt.DefaultApi(api_client)
    
    try:
        api_response = api_instance.get_root_html()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_root_html: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_short_version**
> str get_short_version()



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
    api_instance = cons3rt.DefaultApi(api_client)
    
    try:
        api_response = api_instance.get_short_version()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_short_version: %s\n" % e)
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
    api_instance = cons3rt.DefaultApi(api_client)
    
    try:
        api_response = api_instance.get_short_version()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_short_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> str get_version()



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
    api_instance = cons3rt.DefaultApi(api_client)
    
    try:
        api_response = api_instance.get_version()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_version: %s\n" % e)
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
    api_instance = cons3rt.DefaultApi(api_client)
    
    try:
        api_response = api_instance.get_version()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_credentials**
> str validate_credentials()



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
    api_instance = cons3rt.DefaultApi(api_client)
    
    try:
        api_response = api_instance.validate_credentials()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->validate_credentials: %s\n" % e)
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
    api_instance = cons3rt.DefaultApi(api_client)
    
    try:
        api_response = api_instance.validate_credentials()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->validate_credentials: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [Username](../README.md#Username)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

