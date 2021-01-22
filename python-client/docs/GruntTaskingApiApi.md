# swagger_client.GruntTaskingApiApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_grunt_tasking**](GruntTaskingApiApi.md#create_grunt_tasking) | **POST** /api/taskings | 
[**delete_grunt_tasking**](GruntTaskingApiApi.md#delete_grunt_tasking) | **DELETE** /api/taskings/{tid} | 
[**edit_grunt_tasking**](GruntTaskingApiApi.md#edit_grunt_tasking) | **PUT** /api/taskings | 
[**get_all_grunt_taskings**](GruntTaskingApiApi.md#get_all_grunt_taskings) | **GET** /api/taskings | 
[**get_grunt_tasking**](GruntTaskingApiApi.md#get_grunt_tasking) | **GET** /api/taskings/{tid} | 
[**get_grunt_tasking_by_name**](GruntTaskingApiApi.md#get_grunt_tasking_by_name) | **GET** /api/grunts/taskings/{taskingname} | 
[**get_grunt_taskings**](GruntTaskingApiApi.md#get_grunt_taskings) | **GET** /api/grunts/{id}/taskings | 
[**get_search_grunt_taskings**](GruntTaskingApiApi.md#get_search_grunt_taskings) | **GET** /api/grunts/{id}/taskings/search | 
[**get_search_uninitialized_grunt_taskings**](GruntTaskingApiApi.md#get_search_uninitialized_grunt_taskings) | **GET** /api/grunts/{id}/taskings/search/uninitialized | 
[**get_uninitialized_grunt_taskings**](GruntTaskingApiApi.md#get_uninitialized_grunt_taskings) | **GET** /api/grunts/{id}/taskings/uninitialized | 


# **create_grunt_tasking**
> GruntTasking create_grunt_tasking(body=body)



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
api_instance = swagger_client.GruntTaskingApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.GruntTasking() # GruntTasking |  (optional)

try:
    api_response = api_instance.create_grunt_tasking(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntTaskingApiApi->create_grunt_tasking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GruntTasking**](GruntTasking.md)|  | [optional] 

### Return type

[**GruntTasking**](GruntTasking.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_grunt_tasking**
> delete_grunt_tasking(tid)



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
api_instance = swagger_client.GruntTaskingApiApi(swagger_client.ApiClient(configuration))
tid = 56 # int | 

try:
    api_instance.delete_grunt_tasking(tid)
except ApiException as e:
    print("Exception when calling GruntTaskingApiApi->delete_grunt_tasking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tid** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_grunt_tasking**
> GruntTasking edit_grunt_tasking(body=body)



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
api_instance = swagger_client.GruntTaskingApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.GruntTasking() # GruntTasking |  (optional)

try:
    api_response = api_instance.edit_grunt_tasking(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntTaskingApiApi->edit_grunt_tasking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GruntTasking**](GruntTasking.md)|  | [optional] 

### Return type

[**GruntTasking**](GruntTasking.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_grunt_taskings**
> list[GruntTasking] get_all_grunt_taskings()



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
api_instance = swagger_client.GruntTaskingApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_grunt_taskings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntTaskingApiApi->get_all_grunt_taskings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GruntTasking]**](GruntTasking.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grunt_tasking**
> GruntTasking get_grunt_tasking(tid)



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
api_instance = swagger_client.GruntTaskingApiApi(swagger_client.ApiClient(configuration))
tid = 56 # int | 

try:
    api_response = api_instance.get_grunt_tasking(tid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntTaskingApiApi->get_grunt_tasking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tid** | **int**|  | 

### Return type

[**GruntTasking**](GruntTasking.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grunt_tasking_by_name**
> GruntTasking get_grunt_tasking_by_name(taskingname)



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
api_instance = swagger_client.GruntTaskingApiApi(swagger_client.ApiClient(configuration))
taskingname = 'taskingname_example' # str | 

try:
    api_response = api_instance.get_grunt_tasking_by_name(taskingname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntTaskingApiApi->get_grunt_tasking_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taskingname** | **str**|  | 

### Return type

[**GruntTasking**](GruntTasking.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grunt_taskings**
> list[GruntTasking] get_grunt_taskings(id)



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
api_instance = swagger_client.GruntTaskingApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_grunt_taskings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntTaskingApiApi->get_grunt_taskings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**list[GruntTasking]**](GruntTasking.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_grunt_taskings**
> list[GruntTasking] get_search_grunt_taskings(id)



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
api_instance = swagger_client.GruntTaskingApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_search_grunt_taskings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntTaskingApiApi->get_search_grunt_taskings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**list[GruntTasking]**](GruntTasking.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_uninitialized_grunt_taskings**
> list[GruntTasking] get_search_uninitialized_grunt_taskings(id)



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
api_instance = swagger_client.GruntTaskingApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_search_uninitialized_grunt_taskings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntTaskingApiApi->get_search_uninitialized_grunt_taskings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**list[GruntTasking]**](GruntTasking.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_uninitialized_grunt_taskings**
> list[GruntTasking] get_uninitialized_grunt_taskings(id)



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
api_instance = swagger_client.GruntTaskingApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_uninitialized_grunt_taskings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntTaskingApiApi->get_uninitialized_grunt_taskings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**list[GruntTasking]**](GruntTasking.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

