# swagger_client.GruntApiApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compile_grunt_executor**](GruntApiApi.md#compile_grunt_executor) | **GET** /api/grunts/{id}/compileexecutor | 
[**create_grunt**](GruntApiApi.md#create_grunt) | **POST** /api/grunts | 
[**delete_grunt**](GruntApiApi.md#delete_grunt) | **DELETE** /api/grunts/{id} | 
[**edit_grunt**](GruntApiApi.md#edit_grunt) | **PUT** /api/grunts | 
[**get_grunt**](GruntApiApi.md#get_grunt) | **GET** /api/grunts/{id} | 
[**get_grunt_by_guid**](GruntApiApi.md#get_grunt_by_guid) | **GET** /api/grunts/guid/{guid} | 
[**get_grunt_by_name**](GruntApiApi.md#get_grunt_by_name) | **GET** /api/grunts/{name} | 
[**get_grunt_by_original_server_guid**](GruntApiApi.md#get_grunt_by_original_server_guid) | **GET** /api/grunts/originalguid/{serverguid} | 
[**get_grunts**](GruntApiApi.md#get_grunts) | **GET** /api/grunts | 
[**get_outbound_grunt**](GruntApiApi.md#get_outbound_grunt) | **GET** /api/grunts/{id}/outbound | 
[**get_path_to_child_grunt**](GruntApiApi.md#get_path_to_child_grunt) | **GET** /api/grunts/{id}/path/{cid} | 
[**interact_grunt**](GruntApiApi.md#interact_grunt) | **POST** /api/grunts/{id}/interact | 


# **compile_grunt_executor**
> str compile_grunt_executor(id)



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
api_instance = swagger_client.GruntApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.compile_grunt_executor(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntApiApi->compile_grunt_executor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_grunt**
> Grunt create_grunt(body=body)



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
api_instance = swagger_client.GruntApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.Grunt() # Grunt |  (optional)

try:
    api_response = api_instance.create_grunt(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntApiApi->create_grunt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Grunt**](Grunt.md)|  | [optional] 

### Return type

[**Grunt**](Grunt.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_grunt**
> delete_grunt(id)



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
api_instance = swagger_client.GruntApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_instance.delete_grunt(id)
except ApiException as e:
    print("Exception when calling GruntApiApi->delete_grunt: %s\n" % e)
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

# **edit_grunt**
> Grunt edit_grunt(body=body)



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
api_instance = swagger_client.GruntApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.Grunt() # Grunt |  (optional)

try:
    api_response = api_instance.edit_grunt(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntApiApi->edit_grunt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Grunt**](Grunt.md)|  | [optional] 

### Return type

[**Grunt**](Grunt.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grunt**
> Grunt get_grunt(id)



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
api_instance = swagger_client.GruntApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_grunt(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntApiApi->get_grunt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Grunt**](Grunt.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grunt_by_guid**
> Grunt get_grunt_by_guid(guid)



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
api_instance = swagger_client.GruntApiApi(swagger_client.ApiClient(configuration))
guid = 'guid_example' # str | 

try:
    api_response = api_instance.get_grunt_by_guid(guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntApiApi->get_grunt_by_guid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  | 

### Return type

[**Grunt**](Grunt.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grunt_by_name**
> Grunt get_grunt_by_name(name)



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
api_instance = swagger_client.GruntApiApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_response = api_instance.get_grunt_by_name(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntApiApi->get_grunt_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**Grunt**](Grunt.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grunt_by_original_server_guid**
> Grunt get_grunt_by_original_server_guid(serverguid)



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
api_instance = swagger_client.GruntApiApi(swagger_client.ApiClient(configuration))
serverguid = 'serverguid_example' # str | 

try:
    api_response = api_instance.get_grunt_by_original_server_guid(serverguid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntApiApi->get_grunt_by_original_server_guid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serverguid** | **str**|  | 

### Return type

[**Grunt**](Grunt.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grunts**
> list[Grunt] get_grunts()



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
api_instance = swagger_client.GruntApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_grunts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntApiApi->get_grunts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Grunt]**](Grunt.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outbound_grunt**
> Grunt get_outbound_grunt(id)



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
api_instance = swagger_client.GruntApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_outbound_grunt(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntApiApi->get_outbound_grunt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Grunt**](Grunt.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_path_to_child_grunt**
> list[str] get_path_to_child_grunt(id, cid)



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
api_instance = swagger_client.GruntApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
cid = 56 # int | 

try:
    api_response = api_instance.get_path_to_child_grunt(id, cid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntApiApi->get_path_to_child_grunt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **cid** | **int**|  | 

### Return type

**list[str]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **interact_grunt**
> GruntCommand interact_grunt(id, body=body)



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
api_instance = swagger_client.GruntApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
body = 'body_example' # str |  (optional)

try:
    api_response = api_instance.interact_grunt(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GruntApiApi->interact_grunt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | **str**|  | [optional] 

### Return type

[**GruntCommand**](GruntCommand.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

