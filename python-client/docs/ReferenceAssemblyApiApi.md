# swagger_client.ReferenceAssemblyApiApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reference_assembly**](ReferenceAssemblyApiApi.md#create_reference_assembly) | **POST** /api/referenceassemblies | 
[**delete_reference_assembly**](ReferenceAssemblyApiApi.md#delete_reference_assembly) | **DELETE** /api/referenceassemblies/{id} | 
[**edit_reference_assembly**](ReferenceAssemblyApiApi.md#edit_reference_assembly) | **PUT** /api/referenceassemblies | 
[**get_reference_assemblies**](ReferenceAssemblyApiApi.md#get_reference_assemblies) | **GET** /api/referenceassemblies | 
[**get_reference_assembly**](ReferenceAssemblyApiApi.md#get_reference_assembly) | **GET** /api/referenceassemblies/{id} | 


# **create_reference_assembly**
> ReferenceAssembly create_reference_assembly(body=body)



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
api_instance = swagger_client.ReferenceAssemblyApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.ReferenceAssembly() # ReferenceAssembly |  (optional)

try:
    api_response = api_instance.create_reference_assembly(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceAssemblyApiApi->create_reference_assembly: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReferenceAssembly**](ReferenceAssembly.md)|  | [optional] 

### Return type

[**ReferenceAssembly**](ReferenceAssembly.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reference_assembly**
> delete_reference_assembly(id)



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
api_instance = swagger_client.ReferenceAssemblyApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_instance.delete_reference_assembly(id)
except ApiException as e:
    print("Exception when calling ReferenceAssemblyApiApi->delete_reference_assembly: %s\n" % e)
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

# **edit_reference_assembly**
> ReferenceAssembly edit_reference_assembly(body=body)



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
api_instance = swagger_client.ReferenceAssemblyApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.ReferenceAssembly() # ReferenceAssembly |  (optional)

try:
    api_response = api_instance.edit_reference_assembly(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceAssemblyApiApi->edit_reference_assembly: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReferenceAssembly**](ReferenceAssembly.md)|  | [optional] 

### Return type

[**ReferenceAssembly**](ReferenceAssembly.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_assemblies**
> list[ReferenceAssembly] get_reference_assemblies()



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
api_instance = swagger_client.ReferenceAssemblyApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_reference_assemblies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceAssemblyApiApi->get_reference_assemblies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ReferenceAssembly]**](ReferenceAssembly.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_assembly**
> ReferenceAssembly get_reference_assembly(id)



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
api_instance = swagger_client.ReferenceAssemblyApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_reference_assembly(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceAssemblyApiApi->get_reference_assembly: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ReferenceAssembly**](ReferenceAssembly.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

