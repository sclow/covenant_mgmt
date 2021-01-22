# swagger_client.GruntTaskApiApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_grunt_task**](GruntTaskApiApi.md#create_grunt_task) | **POST** /api/grunttasks | 
[**delete_grunt_task**](GruntTaskApiApi.md#delete_grunt_task) | **DELETE** /api/grunttasks/{id} | 
[**edit_grunt_task**](GruntTaskApiApi.md#edit_grunt_task) | **PUT** /api/grunttasks | 
[**get_grunt_task**](GruntTaskApiApi.md#get_grunt_task) | **GET** /api/grunttasks/{id} | 
[**get_grunt_tasks**](GruntTaskApiApi.md#get_grunt_tasks) | **GET** /api/grunttasks | 


# **create_grunt_task**
> GruntTask create_grunt_task(body=body)



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
api_instance = swagger_client.GruntTaskApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.GruntTask() # GruntTask |  (optional)

try:
    api_response = api_instance.create_grunt_task(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntTaskApiApi->create_grunt_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GruntTask**](GruntTask.md)|  | [optional] 

### Return type

[**GruntTask**](GruntTask.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_grunt_task**
> delete_grunt_task(id)



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
api_instance = swagger_client.GruntTaskApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_instance.delete_grunt_task(id)
except ApiException as e:
    print("Exception when calling GruntTaskApiApi->delete_grunt_task: %s\n" % e)
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

# **edit_grunt_task**
> GruntTask edit_grunt_task(body=body)



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
api_instance = swagger_client.GruntTaskApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.GruntTask() # GruntTask |  (optional)

try:
    api_response = api_instance.edit_grunt_task(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntTaskApiApi->edit_grunt_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GruntTask**](GruntTask.md)|  | [optional] 

### Return type

[**GruntTask**](GruntTask.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grunt_task**
> GruntTask get_grunt_task(id)



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
api_instance = swagger_client.GruntTaskApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_grunt_task(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntTaskApiApi->get_grunt_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GruntTask**](GruntTask.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grunt_tasks**
> list[GruntTask] get_grunt_tasks()



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
api_instance = swagger_client.GruntTaskApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_grunt_tasks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntTaskApiApi->get_grunt_tasks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GruntTask]**](GruntTask.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

