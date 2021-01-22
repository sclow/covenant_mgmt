# swagger_client.CommandOutputApiApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**append_command_output**](CommandOutputApiApi.md#append_command_output) | **PUT** /api/commandoutputs/append/{id} | 
[**create_command_output**](CommandOutputApiApi.md#create_command_output) | **POST** /api/commandoutputs | 
[**delete_command_output**](CommandOutputApiApi.md#delete_command_output) | **DELETE** /api/commandoutputs/{id} | 
[**edit_command_output**](CommandOutputApiApi.md#edit_command_output) | **PUT** /api/commandoutputs | 
[**get_command_output**](CommandOutputApiApi.md#get_command_output) | **GET** /api/commandoutputs/{id} | 
[**get_command_outputs**](CommandOutputApiApi.md#get_command_outputs) | **GET** /api/commandoutputs | 


# **append_command_output**
> append_command_output(id, body=body)



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
api_instance = swagger_client.CommandOutputApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
body = 'body_example' # str |  (optional)

try:
    api_instance.append_command_output(id, body=body)
except ApiException as e:
    print("Exception when calling CommandOutputApiApi->append_command_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_command_output**
> CommandOutput create_command_output(body=body)



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
api_instance = swagger_client.CommandOutputApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.CommandOutput() # CommandOutput |  (optional)

try:
    api_response = api_instance.create_command_output(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandOutputApiApi->create_command_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommandOutput**](CommandOutput.md)|  | [optional] 

### Return type

[**CommandOutput**](CommandOutput.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_command_output**
> delete_command_output(id)



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
api_instance = swagger_client.CommandOutputApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_instance.delete_command_output(id)
except ApiException as e:
    print("Exception when calling CommandOutputApiApi->delete_command_output: %s\n" % e)
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

# **edit_command_output**
> CommandOutput edit_command_output(body=body)



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
api_instance = swagger_client.CommandOutputApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.CommandOutput() # CommandOutput |  (optional)

try:
    api_response = api_instance.edit_command_output(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandOutputApiApi->edit_command_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommandOutput**](CommandOutput.md)|  | [optional] 

### Return type

[**CommandOutput**](CommandOutput.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_command_output**
> CommandOutput get_command_output(id)



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
api_instance = swagger_client.CommandOutputApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_command_output(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandOutputApiApi->get_command_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CommandOutput**](CommandOutput.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_command_outputs**
> list[CommandOutput] get_command_outputs()



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
api_instance = swagger_client.CommandOutputApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_command_outputs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandOutputApiApi->get_command_outputs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CommandOutput]**](CommandOutput.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

