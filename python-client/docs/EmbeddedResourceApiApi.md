# swagger_client.EmbeddedResourceApiApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_embedded_resource**](EmbeddedResourceApiApi.md#create_embedded_resource) | **POST** /api/embeddedresources | 
[**delete_embedded_resource**](EmbeddedResourceApiApi.md#delete_embedded_resource) | **DELETE** /api/embeddedresources/{id} | 
[**edit_embedded_resource**](EmbeddedResourceApiApi.md#edit_embedded_resource) | **PUT** /api/embeddedresources | 
[**get_embedded_resource**](EmbeddedResourceApiApi.md#get_embedded_resource) | **GET** /api/embeddedresources/{id} | 
[**get_embedded_resources**](EmbeddedResourceApiApi.md#get_embedded_resources) | **GET** /api/embeddedresources | 


# **create_embedded_resource**
> EmbeddedResource create_embedded_resource(body=body)



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
api_instance = swagger_client.EmbeddedResourceApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmbeddedResource() # EmbeddedResource |  (optional)

try:
    api_response = api_instance.create_embedded_resource(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmbeddedResourceApiApi->create_embedded_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmbeddedResource**](EmbeddedResource.md)|  | [optional] 

### Return type

[**EmbeddedResource**](EmbeddedResource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_embedded_resource**
> delete_embedded_resource(id)



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
api_instance = swagger_client.EmbeddedResourceApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_instance.delete_embedded_resource(id)
except ApiException as e:
    print("Exception when calling EmbeddedResourceApiApi->delete_embedded_resource: %s\n" % e)
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

# **edit_embedded_resource**
> EmbeddedResource edit_embedded_resource(body=body)



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
api_instance = swagger_client.EmbeddedResourceApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.EmbeddedResource() # EmbeddedResource |  (optional)

try:
    api_response = api_instance.edit_embedded_resource(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmbeddedResourceApiApi->edit_embedded_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmbeddedResource**](EmbeddedResource.md)|  | [optional] 

### Return type

[**EmbeddedResource**](EmbeddedResource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_embedded_resource**
> EmbeddedResource get_embedded_resource(id)



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
api_instance = swagger_client.EmbeddedResourceApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_embedded_resource(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmbeddedResourceApiApi->get_embedded_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**EmbeddedResource**](EmbeddedResource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_embedded_resources**
> list[EmbeddedResource] get_embedded_resources()



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
api_instance = swagger_client.EmbeddedResourceApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_embedded_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmbeddedResourceApiApi->get_embedded_resources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EmbeddedResource]**](EmbeddedResource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

