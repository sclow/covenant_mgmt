# swagger_client.ListenerApiApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bridge_listener**](ListenerApiApi.md#create_bridge_listener) | **POST** /api/listeners/bridge | 
[**create_hosted_file**](ListenerApiApi.md#create_hosted_file) | **POST** /api/listeners/{id}/hostedfiles | 
[**create_http_listener**](ListenerApiApi.md#create_http_listener) | **POST** /api/listeners/http | 
[**delete_hosted_file**](ListenerApiApi.md#delete_hosted_file) | **DELETE** /api/listeners/{id}/hostedfiles/{hfid} | 
[**delete_listener**](ListenerApiApi.md#delete_listener) | **DELETE** /api/listeners/{id} | 
[**edit_bridge_listener**](ListenerApiApi.md#edit_bridge_listener) | **PUT** /api/listeners/bridge | 
[**edit_hosted_file**](ListenerApiApi.md#edit_hosted_file) | **PUT** /api/listeners/{id}/hostedfiles | 
[**edit_http_listener**](ListenerApiApi.md#edit_http_listener) | **PUT** /api/listeners/http | 
[**edit_listener**](ListenerApiApi.md#edit_listener) | **PUT** /api/listeners | 
[**get_bridge_listener**](ListenerApiApi.md#get_bridge_listener) | **GET** /api/listeners/bridge/{id} | 
[**get_hosted_file**](ListenerApiApi.md#get_hosted_file) | **GET** /api/listeners/{id}/hostedfiles/{hfid} | 
[**get_hosted_files**](ListenerApiApi.md#get_hosted_files) | **GET** /api/listeners/{id}/hostedfiles | 
[**get_http_listener**](ListenerApiApi.md#get_http_listener) | **GET** /api/listeners/http/{id} | 
[**get_listener**](ListenerApiApi.md#get_listener) | **GET** /api/listeners/{id} | 
[**get_listener_type**](ListenerApiApi.md#get_listener_type) | **GET** /api/listeners/types/{id} | 
[**get_listener_types**](ListenerApiApi.md#get_listener_types) | **GET** /api/listeners/types | 
[**get_listeners**](ListenerApiApi.md#get_listeners) | **GET** /api/listeners | 


# **create_bridge_listener**
> BridgeListener create_bridge_listener(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ListenerApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.BridgeListener() # BridgeListener |  (optional)

try:
    api_response = api_instance.create_bridge_listener(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListenerApiApi->create_bridge_listener: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BridgeListener**](BridgeListener.md)|  | [optional] 

### Return type

[**BridgeListener**](BridgeListener.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_hosted_file**
> HostedFile create_hosted_file(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ListenerApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
body = swagger_client.HostedFile() # HostedFile |  (optional)

try:
    api_response = api_instance.create_hosted_file(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListenerApiApi->create_hosted_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**HostedFile**](HostedFile.md)|  | [optional] 

### Return type

[**HostedFile**](HostedFile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_http_listener**
> HttpListener create_http_listener(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ListenerApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.HttpListener() # HttpListener |  (optional)

try:
    api_response = api_instance.create_http_listener(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListenerApiApi->create_http_listener: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HttpListener**](HttpListener.md)|  | [optional] 

### Return type

[**HttpListener**](HttpListener.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_hosted_file**
> delete_hosted_file(id, hfid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ListenerApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
hfid = 56 # int | 

try:
    api_instance.delete_hosted_file(id, hfid)
except ApiException as e:
    print("Exception when calling ListenerApiApi->delete_hosted_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **hfid** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_listener**
> delete_listener(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ListenerApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_instance.delete_listener(id)
except ApiException as e:
    print("Exception when calling ListenerApiApi->delete_listener: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_bridge_listener**
> BridgeListener edit_bridge_listener(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ListenerApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.BridgeListener() # BridgeListener |  (optional)

try:
    api_response = api_instance.edit_bridge_listener(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListenerApiApi->edit_bridge_listener: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BridgeListener**](BridgeListener.md)|  | [optional] 

### Return type

[**BridgeListener**](BridgeListener.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_hosted_file**
> HostedFile edit_hosted_file(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ListenerApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
body = swagger_client.HostedFile() # HostedFile |  (optional)

try:
    api_response = api_instance.edit_hosted_file(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListenerApiApi->edit_hosted_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**HostedFile**](HostedFile.md)|  | [optional] 

### Return type

[**HostedFile**](HostedFile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_http_listener**
> HttpListener edit_http_listener(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ListenerApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.HttpListener() # HttpListener |  (optional)

try:
    api_response = api_instance.edit_http_listener(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListenerApiApi->edit_http_listener: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HttpListener**](HttpListener.md)|  | [optional] 

### Return type

[**HttpListener**](HttpListener.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_listener**
> Listener edit_listener(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ListenerApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.Listener() # Listener |  (optional)

try:
    api_response = api_instance.edit_listener(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListenerApiApi->edit_listener: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Listener**](Listener.md)|  | [optional] 

### Return type

[**Listener**](Listener.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bridge_listener**
> BridgeListener get_bridge_listener(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ListenerApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_bridge_listener(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListenerApiApi->get_bridge_listener: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**BridgeListener**](BridgeListener.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hosted_file**
> HostedFile get_hosted_file(id, hfid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ListenerApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
hfid = 56 # int | 

try:
    api_response = api_instance.get_hosted_file(id, hfid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListenerApiApi->get_hosted_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **hfid** | **int**|  | 

### Return type

[**HostedFile**](HostedFile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hosted_files**
> list[HostedFile] get_hosted_files(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ListenerApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_hosted_files(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListenerApiApi->get_hosted_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**list[HostedFile]**](HostedFile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_http_listener**
> HttpListener get_http_listener(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ListenerApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_http_listener(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListenerApiApi->get_http_listener: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**HttpListener**](HttpListener.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listener**
> Listener get_listener(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ListenerApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_listener(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListenerApiApi->get_listener: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Listener**](Listener.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listener_type**
> ListenerType get_listener_type(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ListenerApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_listener_type(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListenerApiApi->get_listener_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ListenerType**](ListenerType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listener_types**
> list[ListenerType] get_listener_types()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ListenerApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_listener_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListenerApiApi->get_listener_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ListenerType]**](ListenerType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listeners**
> list[Listener] get_listeners()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ListenerApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_listeners()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListenerApiApi->get_listeners: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Listener]**](Listener.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

