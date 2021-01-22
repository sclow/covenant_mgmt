# swagger_client.ImplantTemplateApiApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_implant_template**](ImplantTemplateApiApi.md#create_implant_template) | **POST** /api/implanttemplates | 
[**delete_implant_template**](ImplantTemplateApiApi.md#delete_implant_template) | **DELETE** /api/implanttemplates/{id} | 
[**edit_implant_template**](ImplantTemplateApiApi.md#edit_implant_template) | **PUT** /api/implanttemplates | 
[**get_implant_template**](ImplantTemplateApiApi.md#get_implant_template) | **GET** /api/implanttemplates/{id} | 
[**get_implant_template_by_name**](ImplantTemplateApiApi.md#get_implant_template_by_name) | **GET** /api/implanttemplates/{name} | 
[**get_implant_templates**](ImplantTemplateApiApi.md#get_implant_templates) | **GET** /api/implanttemplates | 


# **create_implant_template**
> ImplantTemplate create_implant_template(body=body)



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
api_instance = swagger_client.ImplantTemplateApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.ImplantTemplate() # ImplantTemplate |  (optional)

try:
    api_response = api_instance.create_implant_template(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImplantTemplateApiApi->create_implant_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImplantTemplate**](ImplantTemplate.md)|  | [optional] 

### Return type

[**ImplantTemplate**](ImplantTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_implant_template**
> delete_implant_template(id)



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
api_instance = swagger_client.ImplantTemplateApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_instance.delete_implant_template(id)
except ApiException as e:
    print("Exception when calling ImplantTemplateApiApi->delete_implant_template: %s\n" % e)
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

# **edit_implant_template**
> ImplantTemplate edit_implant_template(body=body)



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
api_instance = swagger_client.ImplantTemplateApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.ImplantTemplate() # ImplantTemplate |  (optional)

try:
    api_response = api_instance.edit_implant_template(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImplantTemplateApiApi->edit_implant_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImplantTemplate**](ImplantTemplate.md)|  | [optional] 

### Return type

[**ImplantTemplate**](ImplantTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_implant_template**
> ImplantTemplate get_implant_template(id)



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
api_instance = swagger_client.ImplantTemplateApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_implant_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImplantTemplateApiApi->get_implant_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ImplantTemplate**](ImplantTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_implant_template_by_name**
> ImplantTemplate get_implant_template_by_name(name)



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
api_instance = swagger_client.ImplantTemplateApiApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_response = api_instance.get_implant_template_by_name(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImplantTemplateApiApi->get_implant_template_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ImplantTemplate**](ImplantTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_implant_templates**
> list[ImplantTemplate] get_implant_templates()



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
api_instance = swagger_client.ImplantTemplateApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_implant_templates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImplantTemplateApiApi->get_implant_templates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImplantTemplate]**](ImplantTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

