# swagger_client.GruntCommandApiApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_grunt_command**](GruntCommandApiApi.md#create_grunt_command) | **POST** /api/commands | 
[**delete_grunt_command**](GruntCommandApiApi.md#delete_grunt_command) | **DELETE** /api/commands/{id} | 
[**edit_grunt_command**](GruntCommandApiApi.md#edit_grunt_command) | **PUT** /api/commands | 
[**get_grunt_command**](GruntCommandApiApi.md#get_grunt_command) | **GET** /api/commands/{id} | 
[**get_grunt_commands**](GruntCommandApiApi.md#get_grunt_commands) | **GET** /api/commands | 


# **create_grunt_command**
> GruntCommand create_grunt_command(body=body)



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
api_instance = swagger_client.GruntCommandApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.GruntCommand() # GruntCommand |  (optional)

try:
    api_response = api_instance.create_grunt_command(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntCommandApiApi->create_grunt_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GruntCommand**](GruntCommand.md)|  | [optional] 

### Return type

[**GruntCommand**](GruntCommand.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_grunt_command**
> delete_grunt_command(id)



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
api_instance = swagger_client.GruntCommandApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_instance.delete_grunt_command(id)
except ApiException as e:
    print("Exception when calling GruntCommandApiApi->delete_grunt_command: %s\n" % e)
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

# **edit_grunt_command**
> GruntCommand edit_grunt_command(body=body)



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
api_instance = swagger_client.GruntCommandApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.GruntCommand() # GruntCommand |  (optional)

try:
    api_response = api_instance.edit_grunt_command(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntCommandApiApi->edit_grunt_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GruntCommand**](GruntCommand.md)|  | [optional] 

### Return type

[**GruntCommand**](GruntCommand.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grunt_command**
> GruntCommand get_grunt_command(id)



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
api_instance = swagger_client.GruntCommandApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_grunt_command(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntCommandApiApi->get_grunt_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GruntCommand**](GruntCommand.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grunt_commands**
> list[GruntCommand] get_grunt_commands()



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
api_instance = swagger_client.GruntCommandApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_grunt_commands()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntCommandApiApi->get_grunt_commands: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GruntCommand]**](GruntCommand.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

