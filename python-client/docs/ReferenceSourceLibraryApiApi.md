# swagger_client.ReferenceSourceLibraryApiApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reference_source_library**](ReferenceSourceLibraryApiApi.md#create_reference_source_library) | **POST** /api/referencesourcelibraries | 
[**delete_reference_source_library**](ReferenceSourceLibraryApiApi.md#delete_reference_source_library) | **DELETE** /api/referencesourcelibraries/{id} | 
[**edit_reference_source_library**](ReferenceSourceLibraryApiApi.md#edit_reference_source_library) | **PUT** /api/referencesourcelibraries | 
[**get_reference_source_libraries**](ReferenceSourceLibraryApiApi.md#get_reference_source_libraries) | **GET** /api/referencesourcelibraries | 
[**get_reference_source_library**](ReferenceSourceLibraryApiApi.md#get_reference_source_library) | **GET** /api/referencesourcelibraries/{id} | 


# **create_reference_source_library**
> ReferenceSourceLibrary create_reference_source_library(body=body)



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
api_instance = swagger_client.ReferenceSourceLibraryApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.ReferenceSourceLibrary() # ReferenceSourceLibrary |  (optional)

try:
    api_response = api_instance.create_reference_source_library(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceSourceLibraryApiApi->create_reference_source_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReferenceSourceLibrary**](ReferenceSourceLibrary.md)|  | [optional] 

### Return type

[**ReferenceSourceLibrary**](ReferenceSourceLibrary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reference_source_library**
> delete_reference_source_library(id)



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
api_instance = swagger_client.ReferenceSourceLibraryApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_instance.delete_reference_source_library(id)
except ApiException as e:
    print("Exception when calling ReferenceSourceLibraryApiApi->delete_reference_source_library: %s\n" % e)
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

# **edit_reference_source_library**
> ReferenceSourceLibrary edit_reference_source_library(body=body)



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
api_instance = swagger_client.ReferenceSourceLibraryApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.ReferenceSourceLibrary() # ReferenceSourceLibrary |  (optional)

try:
    api_response = api_instance.edit_reference_source_library(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceSourceLibraryApiApi->edit_reference_source_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReferenceSourceLibrary**](ReferenceSourceLibrary.md)|  | [optional] 

### Return type

[**ReferenceSourceLibrary**](ReferenceSourceLibrary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_source_libraries**
> list[ReferenceSourceLibrary] get_reference_source_libraries()



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
api_instance = swagger_client.ReferenceSourceLibraryApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_reference_source_libraries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceSourceLibraryApiApi->get_reference_source_libraries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ReferenceSourceLibrary]**](ReferenceSourceLibrary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_source_library**
> ReferenceSourceLibrary get_reference_source_library(id)



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
api_instance = swagger_client.ReferenceSourceLibraryApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_reference_source_library(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceSourceLibraryApiApi->get_reference_source_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ReferenceSourceLibrary**](ReferenceSourceLibrary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

