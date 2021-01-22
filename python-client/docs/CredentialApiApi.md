# swagger_client.CredentialApiApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_hash_credential**](CredentialApiApi.md#create_hash_credential) | **POST** /api/credentials/hashes | 
[**create_password_credential**](CredentialApiApi.md#create_password_credential) | **POST** /api/credentials/passwords | 
[**create_ticket_credential**](CredentialApiApi.md#create_ticket_credential) | **POST** /api/credentials/tickets | 
[**delete_credential**](CredentialApiApi.md#delete_credential) | **DELETE** /api/credentials/{id} | 
[**edit_hash_credential**](CredentialApiApi.md#edit_hash_credential) | **PUT** /api/credentials/hashes | 
[**edit_password_credential**](CredentialApiApi.md#edit_password_credential) | **PUT** /api/credentials/passwords | 
[**edit_ticket_credential**](CredentialApiApi.md#edit_ticket_credential) | **PUT** /api/credentials/tickets | 
[**get_credential**](CredentialApiApi.md#get_credential) | **GET** /api/credentials/{id} | 
[**get_credentials**](CredentialApiApi.md#get_credentials) | **GET** /api/credentials | 
[**get_hash_credential**](CredentialApiApi.md#get_hash_credential) | **GET** /api/credentials/hashes/{id} | 
[**get_hash_credentials**](CredentialApiApi.md#get_hash_credentials) | **GET** /api/credentials/hashes | 
[**get_password_credential**](CredentialApiApi.md#get_password_credential) | **GET** /api/credentials/passwords/{id} | 
[**get_password_credentials**](CredentialApiApi.md#get_password_credentials) | **GET** /api/credentials/passwords | 
[**get_ticket_credential**](CredentialApiApi.md#get_ticket_credential) | **GET** /api/credentials/tickets/{id} | 
[**get_ticket_credentials**](CredentialApiApi.md#get_ticket_credentials) | **GET** /api/credentials/tickets | 


# **create_hash_credential**
> CapturedHashCredential create_hash_credential(body=body)



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
api_instance = swagger_client.CredentialApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.CapturedHashCredential() # CapturedHashCredential |  (optional)

try:
    api_response = api_instance.create_hash_credential(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApiApi->create_hash_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CapturedHashCredential**](CapturedHashCredential.md)|  | [optional] 

### Return type

[**CapturedHashCredential**](CapturedHashCredential.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_password_credential**
> CapturedPasswordCredential create_password_credential(body=body)



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
api_instance = swagger_client.CredentialApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.CapturedPasswordCredential() # CapturedPasswordCredential |  (optional)

try:
    api_response = api_instance.create_password_credential(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApiApi->create_password_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CapturedPasswordCredential**](CapturedPasswordCredential.md)|  | [optional] 

### Return type

[**CapturedPasswordCredential**](CapturedPasswordCredential.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ticket_credential**
> CapturedTicketCredential create_ticket_credential(body=body)



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
api_instance = swagger_client.CredentialApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.CapturedTicketCredential() # CapturedTicketCredential |  (optional)

try:
    api_response = api_instance.create_ticket_credential(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApiApi->create_ticket_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CapturedTicketCredential**](CapturedTicketCredential.md)|  | [optional] 

### Return type

[**CapturedTicketCredential**](CapturedTicketCredential.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_credential**
> delete_credential(id)



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
api_instance = swagger_client.CredentialApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_instance.delete_credential(id)
except ApiException as e:
    print("Exception when calling CredentialApiApi->delete_credential: %s\n" % e)
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

# **edit_hash_credential**
> CapturedHashCredential edit_hash_credential(body=body)



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
api_instance = swagger_client.CredentialApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.CapturedHashCredential() # CapturedHashCredential |  (optional)

try:
    api_response = api_instance.edit_hash_credential(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApiApi->edit_hash_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CapturedHashCredential**](CapturedHashCredential.md)|  | [optional] 

### Return type

[**CapturedHashCredential**](CapturedHashCredential.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_password_credential**
> CapturedPasswordCredential edit_password_credential(body=body)



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
api_instance = swagger_client.CredentialApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.CapturedPasswordCredential() # CapturedPasswordCredential |  (optional)

try:
    api_response = api_instance.edit_password_credential(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApiApi->edit_password_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CapturedPasswordCredential**](CapturedPasswordCredential.md)|  | [optional] 

### Return type

[**CapturedPasswordCredential**](CapturedPasswordCredential.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_ticket_credential**
> CapturedTicketCredential edit_ticket_credential(body=body)



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
api_instance = swagger_client.CredentialApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.CapturedTicketCredential() # CapturedTicketCredential |  (optional)

try:
    api_response = api_instance.edit_ticket_credential(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApiApi->edit_ticket_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CapturedTicketCredential**](CapturedTicketCredential.md)|  | [optional] 

### Return type

[**CapturedTicketCredential**](CapturedTicketCredential.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credential**
> CapturedCredential get_credential(id)



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
api_instance = swagger_client.CredentialApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_credential(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApiApi->get_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CapturedCredential**](CapturedCredential.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credentials**
> list[CapturedCredential] get_credentials()



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
api_instance = swagger_client.CredentialApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_credentials()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApiApi->get_credentials: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CapturedCredential]**](CapturedCredential.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hash_credential**
> CapturedHashCredential get_hash_credential(id)



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
api_instance = swagger_client.CredentialApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_hash_credential(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApiApi->get_hash_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CapturedHashCredential**](CapturedHashCredential.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hash_credentials**
> list[CapturedHashCredential] get_hash_credentials()



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
api_instance = swagger_client.CredentialApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_hash_credentials()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApiApi->get_hash_credentials: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CapturedHashCredential]**](CapturedHashCredential.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_password_credential**
> CapturedPasswordCredential get_password_credential(id)



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
api_instance = swagger_client.CredentialApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_password_credential(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApiApi->get_password_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CapturedPasswordCredential**](CapturedPasswordCredential.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_password_credentials**
> list[CapturedPasswordCredential] get_password_credentials()



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
api_instance = swagger_client.CredentialApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_password_credentials()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApiApi->get_password_credentials: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CapturedPasswordCredential]**](CapturedPasswordCredential.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ticket_credential**
> CapturedTicketCredential get_ticket_credential(id)



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
api_instance = swagger_client.CredentialApiApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_response = api_instance.get_ticket_credential(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApiApi->get_ticket_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CapturedTicketCredential**](CapturedTicketCredential.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ticket_credentials**
> list[CapturedTicketCredential] get_ticket_credentials()



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
api_instance = swagger_client.CredentialApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_ticket_credentials()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialApiApi->get_ticket_credentials: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CapturedTicketCredential]**](CapturedTicketCredential.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

