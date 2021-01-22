# swagger_client.CovenantUserApiApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](CovenantUserApiApi.md#create_user) | **POST** /api/users | 
[**create_user_role**](CovenantUserApiApi.md#create_user_role) | **POST** /api/users/{id}/roles/{rid} | 
[**delete_user**](CovenantUserApiApi.md#delete_user) | **DELETE** /api/users/{id} | 
[**delete_user_role**](CovenantUserApiApi.md#delete_user_role) | **DELETE** /api/users/{id}/roles/{rid} | 
[**edit_user**](CovenantUserApiApi.md#edit_user) | **PUT** /api/users | 
[**edit_user_password**](CovenantUserApiApi.md#edit_user_password) | **PUT** /api/users/logon | 
[**get_current_user**](CovenantUserApiApi.md#get_current_user) | **GET** /api/users/current | 
[**get_role**](CovenantUserApiApi.md#get_role) | **GET** /api/roles/{rid} | 
[**get_roles**](CovenantUserApiApi.md#get_roles) | **GET** /api/roles | 
[**get_user**](CovenantUserApiApi.md#get_user) | **GET** /api/users/{id} | 
[**get_user_role**](CovenantUserApiApi.md#get_user_role) | **GET** /api/users/{id}/roles/{rid} | 
[**get_user_roles**](CovenantUserApiApi.md#get_user_roles) | **GET** /api/users/{id}/roles | 
[**get_users**](CovenantUserApiApi.md#get_users) | **GET** /api/users | 
[**get_users_roles**](CovenantUserApiApi.md#get_users_roles) | **GET** /api/users/roles | 
[**login**](CovenantUserApiApi.md#login) | **POST** /api/users/login | 


# **create_user**
> CovenantUser create_user(body=body)



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
api_instance = swagger_client.CovenantUserApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.CovenantUserRegister() # CovenantUserRegister |  (optional)

try:
    api_response = api_instance.create_user(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CovenantUserApiApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CovenantUserRegister**](CovenantUserRegister.md)|  | [optional] 

### Return type

[**CovenantUser**](CovenantUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_role**
> StringIdentityUserRole create_user_role(id, rid)



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
api_instance = swagger_client.CovenantUserApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
rid = 'rid_example' # str | 

try:
    api_response = api_instance.create_user_role(id, rid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CovenantUserApiApi->create_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **rid** | **str**|  | 

### Return type

[**StringIdentityUserRole**](StringIdentityUserRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(id)



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
api_instance = swagger_client.CovenantUserApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.delete_user(id)
except ApiException as e:
    print("Exception when calling CovenantUserApiApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_role**
> delete_user_role(id, rid)



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
api_instance = swagger_client.CovenantUserApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
rid = 'rid_example' # str | 

try:
    api_instance.delete_user_role(id, rid)
except ApiException as e:
    print("Exception when calling CovenantUserApiApi->delete_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **rid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_user**
> CovenantUser edit_user(body=body)



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
api_instance = swagger_client.CovenantUserApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.CovenantUser() # CovenantUser |  (optional)

try:
    api_response = api_instance.edit_user(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CovenantUserApiApi->edit_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CovenantUser**](CovenantUser.md)|  | [optional] 

### Return type

[**CovenantUser**](CovenantUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_user_password**
> CovenantUser edit_user_password(body=body)



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
api_instance = swagger_client.CovenantUserApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.CovenantUserLogin() # CovenantUserLogin |  (optional)

try:
    api_response = api_instance.edit_user_password(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CovenantUserApiApi->edit_user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CovenantUserLogin**](CovenantUserLogin.md)|  | [optional] 

### Return type

[**CovenantUser**](CovenantUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user**
> CovenantUser get_current_user()



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
api_instance = swagger_client.CovenantUserApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CovenantUserApiApi->get_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CovenantUser**](CovenantUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> IdentityRole get_role(rid)



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
api_instance = swagger_client.CovenantUserApiApi(swagger_client.ApiClient(configuration))
rid = 'rid_example' # str | 

try:
    api_response = api_instance.get_role(rid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CovenantUserApiApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rid** | **str**|  | 

### Return type

[**IdentityRole**](IdentityRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roles**
> list[IdentityRole] get_roles()



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
api_instance = swagger_client.CovenantUserApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_roles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CovenantUserApiApi->get_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[IdentityRole]**](IdentityRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> CovenantUser get_user(id)



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
api_instance = swagger_client.CovenantUserApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CovenantUserApiApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CovenantUser**](CovenantUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_role**
> StringIdentityUserRole get_user_role(id, rid)



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
api_instance = swagger_client.CovenantUserApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
rid = 'rid_example' # str | 

try:
    api_response = api_instance.get_user_role(id, rid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CovenantUserApiApi->get_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **rid** | **str**|  | 

### Return type

[**StringIdentityUserRole**](StringIdentityUserRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_roles**
> list[StringIdentityUserRole] get_user_roles(id)



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
api_instance = swagger_client.CovenantUserApiApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_user_roles(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CovenantUserApiApi->get_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**list[StringIdentityUserRole]**](StringIdentityUserRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> list[CovenantUser] get_users()



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
api_instance = swagger_client.CovenantUserApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CovenantUserApiApi->get_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CovenantUser]**](CovenantUser.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_roles**
> list[StringIdentityUserRole] get_users_roles()



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
api_instance = swagger_client.CovenantUserApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_users_roles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CovenantUserApiApi->get_users_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[StringIdentityUserRole]**](StringIdentityUserRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> CovenantUserLoginResult login(body=body)



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
api_instance = swagger_client.CovenantUserApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.CovenantUserLogin() # CovenantUserLogin |  (optional)

try:
    api_response = api_instance.login(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CovenantUserApiApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CovenantUserLogin**](CovenantUserLogin.md)|  | [optional] 

### Return type

[**CovenantUserLoginResult**](CovenantUserLoginResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

