# swagger_client.IndicatorApiApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_indicator**](IndicatorApiApi.md#create_indicator) | **POST** /api/indicators | 
[**delete_indicator**](IndicatorApiApi.md#delete_indicator) | **DELETE** /api/indicators/{id} | 
[**edit_indicator**](IndicatorApiApi.md#edit_indicator) | **PUT** /api/indicators | 
[**get_file_indicator**](IndicatorApiApi.md#get_file_indicator) | **GET** /api/indicators/files/{id} | 
[**get_file_indicators**](IndicatorApiApi.md#get_file_indicators) | **GET** /api/indicators/files | 
[**get_indicator**](IndicatorApiApi.md#get_indicator) | **GET** /api/indicators/{id} | 
[**get_indicators**](IndicatorApiApi.md#get_indicators) | **GET** /api/indicators | 
[**get_network_indicator**](IndicatorApiApi.md#get_network_indicator) | **GET** /api/indicators/networks/{id} | 
[**get_network_indicators**](IndicatorApiApi.md#get_network_indicators) | **GET** /api/indicators/networks | 
[**get_report**](IndicatorApiApi.md#get_report) | **GET** /api/indicators/results | 
[**get_target_indicator**](IndicatorApiApi.md#get_target_indicator) | **GET** /api/indicators/targets/{id} | 
[**get_target_indicators**](IndicatorApiApi.md#get_target_indicators) | **GET** /api/indicators/targets | 


# **create_indicator**
> Indicator create_indicator(body=body)



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
api_instance = swagger_client.IndicatorApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.Indicator() # Indicator |  (optional)

try:
    api_response = api_instance.create_indicator(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorApiApi->create_indicator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Indicator**](Indicator.md)|  | [optional] 

### Return type

[**Indicator**](Indicator.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_indicator**
> delete_indicator(id)



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
api_instance = swagger_client.IndicatorApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_instance.delete_indicator(id)
except ApiException as e:
    print("Exception when calling IndicatorApiApi->delete_indicator: %s\n" % e)
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

# **edit_indicator**
> Indicator edit_indicator(body=body)



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
api_instance = swagger_client.IndicatorApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.Indicator() # Indicator |  (optional)

try:
    api_response = api_instance.edit_indicator(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorApiApi->edit_indicator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Indicator**](Indicator.md)|  | [optional] 

### Return type

[**Indicator**](Indicator.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_indicator**
> FileIndicator get_file_indicator(id)



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
api_instance = swagger_client.IndicatorApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_file_indicator(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorApiApi->get_file_indicator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**FileIndicator**](FileIndicator.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_indicators**
> list[FileIndicator] get_file_indicators()



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
api_instance = swagger_client.IndicatorApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_file_indicators()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorApiApi->get_file_indicators: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileIndicator]**](FileIndicator.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indicator**
> Indicator get_indicator(id)



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
api_instance = swagger_client.IndicatorApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_indicator(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorApiApi->get_indicator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Indicator**](Indicator.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indicators**
> list[Indicator] get_indicators()



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
api_instance = swagger_client.IndicatorApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_indicators()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorApiApi->get_indicators: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Indicator]**](Indicator.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_indicator**
> NetworkIndicator get_network_indicator(id)



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
api_instance = swagger_client.IndicatorApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_network_indicator(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorApiApi->get_network_indicator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**NetworkIndicator**](NetworkIndicator.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_indicators**
> list[NetworkIndicator] get_network_indicators()



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
api_instance = swagger_client.IndicatorApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_network_indicators()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorApiApi->get_network_indicators: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NetworkIndicator]**](NetworkIndicator.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report**
> str get_report()



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
api_instance = swagger_client.IndicatorApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_report()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorApiApi->get_report: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_target_indicator**
> TargetIndicator get_target_indicator(id)



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
api_instance = swagger_client.IndicatorApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_target_indicator(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorApiApi->get_target_indicator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TargetIndicator**](TargetIndicator.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_target_indicators**
> list[TargetIndicator] get_target_indicators()



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
api_instance = swagger_client.IndicatorApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_target_indicators()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorApiApi->get_target_indicators: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TargetIndicator]**](TargetIndicator.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

