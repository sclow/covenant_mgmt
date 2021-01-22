# swagger_client.LauncherApiApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_binary_launcher**](LauncherApiApi.md#edit_binary_launcher) | **PUT** /api/launchers/binary | 
[**edit_cscript_launcher**](LauncherApiApi.md#edit_cscript_launcher) | **PUT** /api/launchers/cscript | 
[**edit_install_util_launcher**](LauncherApiApi.md#edit_install_util_launcher) | **PUT** /api/launchers/installutil | 
[**edit_ms_build_launcher**](LauncherApiApi.md#edit_ms_build_launcher) | **PUT** /api/launchers/msbuild | 
[**edit_mshta_launcher**](LauncherApiApi.md#edit_mshta_launcher) | **PUT** /api/launchers/mshta | 
[**edit_power_shell_launcher**](LauncherApiApi.md#edit_power_shell_launcher) | **PUT** /api/launchers/powershell | 
[**edit_regsvr32_launcher**](LauncherApiApi.md#edit_regsvr32_launcher) | **PUT** /api/launchers/regsvr32 | 
[**edit_shell_code_launcher**](LauncherApiApi.md#edit_shell_code_launcher) | **PUT** /api/launchers/shellcode | 
[**edit_wmic_launcher**](LauncherApiApi.md#edit_wmic_launcher) | **PUT** /api/launchers/wmic | 
[**edit_wscript_launcher**](LauncherApiApi.md#edit_wscript_launcher) | **PUT** /api/launchers/wscript | 
[**generate_binary_hosted_launcher**](LauncherApiApi.md#generate_binary_hosted_launcher) | **POST** /api/launchers/binary/hosted | 
[**generate_binary_launcher**](LauncherApiApi.md#generate_binary_launcher) | **POST** /api/launchers/binary | 
[**generate_cscript_hosted_file_launcher**](LauncherApiApi.md#generate_cscript_hosted_file_launcher) | **POST** /api/launchers/cscript/hosted | 
[**generate_cscript_launcher**](LauncherApiApi.md#generate_cscript_launcher) | **POST** /api/launchers/cscript | 
[**generate_install_util_hosted_file_launcher**](LauncherApiApi.md#generate_install_util_hosted_file_launcher) | **POST** /api/launchers/installutil/hosted | 
[**generate_install_util_launcher**](LauncherApiApi.md#generate_install_util_launcher) | **POST** /api/launchers/installutil | 
[**generate_ms_build_hosted_file_launcher**](LauncherApiApi.md#generate_ms_build_hosted_file_launcher) | **POST** /api/launchers/msbuild/hosted | 
[**generate_ms_build_launcher**](LauncherApiApi.md#generate_ms_build_launcher) | **POST** /api/launchers/msbuild | 
[**generate_mshta_hosted_file_launcher**](LauncherApiApi.md#generate_mshta_hosted_file_launcher) | **POST** /api/launchers/mshta/hosted | 
[**generate_mshta_launcher**](LauncherApiApi.md#generate_mshta_launcher) | **POST** /api/launchers/mshta | 
[**generate_power_shell_hosted_file_launcher**](LauncherApiApi.md#generate_power_shell_hosted_file_launcher) | **POST** /api/launchers/powershell/hosted | 
[**generate_power_shell_launcher**](LauncherApiApi.md#generate_power_shell_launcher) | **POST** /api/launchers/powershell | 
[**generate_regsvr32_hosted_file_launcher**](LauncherApiApi.md#generate_regsvr32_hosted_file_launcher) | **POST** /api/launchers/regsvr32/hosted | 
[**generate_regsvr32_launcher**](LauncherApiApi.md#generate_regsvr32_launcher) | **POST** /api/launchers/regsvr32 | 
[**generate_shell_code_hosted_launcher**](LauncherApiApi.md#generate_shell_code_hosted_launcher) | **POST** /api/launchers/shellcode/hosted | 
[**generate_shell_code_launcher**](LauncherApiApi.md#generate_shell_code_launcher) | **POST** /api/launchers/shellcode | 
[**generate_wmic_hosted_file_launcher**](LauncherApiApi.md#generate_wmic_hosted_file_launcher) | **POST** /api/launchers/wmic/hosted | 
[**generate_wmic_launcher**](LauncherApiApi.md#generate_wmic_launcher) | **POST** /api/launchers/wmic | 
[**generate_wscript_hosted_file_launcher**](LauncherApiApi.md#generate_wscript_hosted_file_launcher) | **POST** /api/launchers/wscript/hosted | 
[**generate_wscript_launcher**](LauncherApiApi.md#generate_wscript_launcher) | **POST** /api/launchers/wscript | 
[**get_binary_launcher**](LauncherApiApi.md#get_binary_launcher) | **GET** /api/launchers/binary | 
[**get_cscript_launcher**](LauncherApiApi.md#get_cscript_launcher) | **GET** /api/launchers/cscript | 
[**get_install_util_launcher**](LauncherApiApi.md#get_install_util_launcher) | **GET** /api/launchers/installutil | 
[**get_launchers**](LauncherApiApi.md#get_launchers) | **GET** /api/launchers | 
[**get_ms_build_launcher**](LauncherApiApi.md#get_ms_build_launcher) | **GET** /api/launchers/msbuild | 
[**get_mshta_launcher**](LauncherApiApi.md#get_mshta_launcher) | **GET** /api/launchers/mshta | 
[**get_power_shell_launcher**](LauncherApiApi.md#get_power_shell_launcher) | **GET** /api/launchers/powershell | 
[**get_regsvr32_launcher**](LauncherApiApi.md#get_regsvr32_launcher) | **GET** /api/launchers/regsvr32 | 
[**get_shell_code_launcher**](LauncherApiApi.md#get_shell_code_launcher) | **GET** /api/launchers/shellcode | 
[**get_wmic_launcher**](LauncherApiApi.md#get_wmic_launcher) | **GET** /api/launchers/wmic | 
[**get_wscript_launcher**](LauncherApiApi.md#get_wscript_launcher) | **GET** /api/launchers/wscript | 


# **edit_binary_launcher**
> BinaryLauncher edit_binary_launcher(body=body)



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.BinaryLauncher() # BinaryLauncher |  (optional)

try:
    api_response = api_instance.edit_binary_launcher(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->edit_binary_launcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BinaryLauncher**](BinaryLauncher.md)|  | [optional] 

### Return type

[**BinaryLauncher**](BinaryLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_cscript_launcher**
> CscriptLauncher edit_cscript_launcher(body=body)



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.CscriptLauncher() # CscriptLauncher |  (optional)

try:
    api_response = api_instance.edit_cscript_launcher(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->edit_cscript_launcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CscriptLauncher**](CscriptLauncher.md)|  | [optional] 

### Return type

[**CscriptLauncher**](CscriptLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_install_util_launcher**
> InstallUtilLauncher edit_install_util_launcher(body=body)



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.InstallUtilLauncher() # InstallUtilLauncher |  (optional)

try:
    api_response = api_instance.edit_install_util_launcher(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->edit_install_util_launcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InstallUtilLauncher**](InstallUtilLauncher.md)|  | [optional] 

### Return type

[**InstallUtilLauncher**](InstallUtilLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_ms_build_launcher**
> MSBuildLauncher edit_ms_build_launcher(body=body)



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.MSBuildLauncher() # MSBuildLauncher |  (optional)

try:
    api_response = api_instance.edit_ms_build_launcher(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->edit_ms_build_launcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MSBuildLauncher**](MSBuildLauncher.md)|  | [optional] 

### Return type

[**MSBuildLauncher**](MSBuildLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_mshta_launcher**
> MshtaLauncher edit_mshta_launcher(body=body)



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.MshtaLauncher() # MshtaLauncher |  (optional)

try:
    api_response = api_instance.edit_mshta_launcher(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->edit_mshta_launcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MshtaLauncher**](MshtaLauncher.md)|  | [optional] 

### Return type

[**MshtaLauncher**](MshtaLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_power_shell_launcher**
> PowerShellLauncher edit_power_shell_launcher(body=body)



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.PowerShellLauncher() # PowerShellLauncher |  (optional)

try:
    api_response = api_instance.edit_power_shell_launcher(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->edit_power_shell_launcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PowerShellLauncher**](PowerShellLauncher.md)|  | [optional] 

### Return type

[**PowerShellLauncher**](PowerShellLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_regsvr32_launcher**
> Regsvr32Launcher edit_regsvr32_launcher(body=body)



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.Regsvr32Launcher() # Regsvr32Launcher |  (optional)

try:
    api_response = api_instance.edit_regsvr32_launcher(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->edit_regsvr32_launcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Regsvr32Launcher**](Regsvr32Launcher.md)|  | [optional] 

### Return type

[**Regsvr32Launcher**](Regsvr32Launcher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_shell_code_launcher**
> ShellCodeLauncher edit_shell_code_launcher(body=body)



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.ShellCodeLauncher() # ShellCodeLauncher |  (optional)

try:
    api_response = api_instance.edit_shell_code_launcher(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->edit_shell_code_launcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShellCodeLauncher**](ShellCodeLauncher.md)|  | [optional] 

### Return type

[**ShellCodeLauncher**](ShellCodeLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_wmic_launcher**
> WmicLauncher edit_wmic_launcher(body=body)



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.WmicLauncher() # WmicLauncher |  (optional)

try:
    api_response = api_instance.edit_wmic_launcher(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->edit_wmic_launcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WmicLauncher**](WmicLauncher.md)|  | [optional] 

### Return type

[**WmicLauncher**](WmicLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_wscript_launcher**
> WscriptLauncher edit_wscript_launcher(body=body)



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.WscriptLauncher() # WscriptLauncher |  (optional)

try:
    api_response = api_instance.edit_wscript_launcher(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->edit_wscript_launcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WscriptLauncher**](WscriptLauncher.md)|  | [optional] 

### Return type

[**WscriptLauncher**](WscriptLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_binary_hosted_launcher**
> BinaryLauncher generate_binary_hosted_launcher(body=body)



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.HostedFile() # HostedFile |  (optional)

try:
    api_response = api_instance.generate_binary_hosted_launcher(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->generate_binary_hosted_launcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostedFile**](HostedFile.md)|  | [optional] 

### Return type

[**BinaryLauncher**](BinaryLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_binary_launcher**
> BinaryLauncher generate_binary_launcher()



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.generate_binary_launcher()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->generate_binary_launcher: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BinaryLauncher**](BinaryLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_cscript_hosted_file_launcher**
> CscriptLauncher generate_cscript_hosted_file_launcher(body=body)



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.HostedFile() # HostedFile |  (optional)

try:
    api_response = api_instance.generate_cscript_hosted_file_launcher(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->generate_cscript_hosted_file_launcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostedFile**](HostedFile.md)|  | [optional] 

### Return type

[**CscriptLauncher**](CscriptLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_cscript_launcher**
> CscriptLauncher generate_cscript_launcher()



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.generate_cscript_launcher()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->generate_cscript_launcher: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CscriptLauncher**](CscriptLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_install_util_hosted_file_launcher**
> InstallUtilLauncher generate_install_util_hosted_file_launcher(body=body)



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.HostedFile() # HostedFile |  (optional)

try:
    api_response = api_instance.generate_install_util_hosted_file_launcher(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->generate_install_util_hosted_file_launcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostedFile**](HostedFile.md)|  | [optional] 

### Return type

[**InstallUtilLauncher**](InstallUtilLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_install_util_launcher**
> InstallUtilLauncher generate_install_util_launcher()



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.generate_install_util_launcher()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->generate_install_util_launcher: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InstallUtilLauncher**](InstallUtilLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_ms_build_hosted_file_launcher**
> MSBuildLauncher generate_ms_build_hosted_file_launcher(body=body)



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.HostedFile() # HostedFile |  (optional)

try:
    api_response = api_instance.generate_ms_build_hosted_file_launcher(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->generate_ms_build_hosted_file_launcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostedFile**](HostedFile.md)|  | [optional] 

### Return type

[**MSBuildLauncher**](MSBuildLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_ms_build_launcher**
> MSBuildLauncher generate_ms_build_launcher()



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.generate_ms_build_launcher()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->generate_ms_build_launcher: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MSBuildLauncher**](MSBuildLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_mshta_hosted_file_launcher**
> MshtaLauncher generate_mshta_hosted_file_launcher(body=body)



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.HostedFile() # HostedFile |  (optional)

try:
    api_response = api_instance.generate_mshta_hosted_file_launcher(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->generate_mshta_hosted_file_launcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostedFile**](HostedFile.md)|  | [optional] 

### Return type

[**MshtaLauncher**](MshtaLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_mshta_launcher**
> MshtaLauncher generate_mshta_launcher()



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.generate_mshta_launcher()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->generate_mshta_launcher: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MshtaLauncher**](MshtaLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_power_shell_hosted_file_launcher**
> PowerShellLauncher generate_power_shell_hosted_file_launcher(body=body)



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.HostedFile() # HostedFile |  (optional)

try:
    api_response = api_instance.generate_power_shell_hosted_file_launcher(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->generate_power_shell_hosted_file_launcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostedFile**](HostedFile.md)|  | [optional] 

### Return type

[**PowerShellLauncher**](PowerShellLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_power_shell_launcher**
> PowerShellLauncher generate_power_shell_launcher()



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.generate_power_shell_launcher()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->generate_power_shell_launcher: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PowerShellLauncher**](PowerShellLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_regsvr32_hosted_file_launcher**
> Regsvr32Launcher generate_regsvr32_hosted_file_launcher(body=body)



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.HostedFile() # HostedFile |  (optional)

try:
    api_response = api_instance.generate_regsvr32_hosted_file_launcher(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->generate_regsvr32_hosted_file_launcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostedFile**](HostedFile.md)|  | [optional] 

### Return type

[**Regsvr32Launcher**](Regsvr32Launcher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_regsvr32_launcher**
> Regsvr32Launcher generate_regsvr32_launcher()



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.generate_regsvr32_launcher()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->generate_regsvr32_launcher: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Regsvr32Launcher**](Regsvr32Launcher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_shell_code_hosted_launcher**
> ShellCodeLauncher generate_shell_code_hosted_launcher(body=body)



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.HostedFile() # HostedFile |  (optional)

try:
    api_response = api_instance.generate_shell_code_hosted_launcher(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->generate_shell_code_hosted_launcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostedFile**](HostedFile.md)|  | [optional] 

### Return type

[**ShellCodeLauncher**](ShellCodeLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_shell_code_launcher**
> ShellCodeLauncher generate_shell_code_launcher()



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.generate_shell_code_launcher()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->generate_shell_code_launcher: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ShellCodeLauncher**](ShellCodeLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_wmic_hosted_file_launcher**
> WmicLauncher generate_wmic_hosted_file_launcher(body=body)



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.HostedFile() # HostedFile |  (optional)

try:
    api_response = api_instance.generate_wmic_hosted_file_launcher(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->generate_wmic_hosted_file_launcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostedFile**](HostedFile.md)|  | [optional] 

### Return type

[**WmicLauncher**](WmicLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_wmic_launcher**
> WmicLauncher generate_wmic_launcher()



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.generate_wmic_launcher()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->generate_wmic_launcher: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WmicLauncher**](WmicLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_wscript_hosted_file_launcher**
> WscriptLauncher generate_wscript_hosted_file_launcher(body=body)



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.HostedFile() # HostedFile |  (optional)

try:
    api_response = api_instance.generate_wscript_hosted_file_launcher(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->generate_wscript_hosted_file_launcher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostedFile**](HostedFile.md)|  | [optional] 

### Return type

[**WscriptLauncher**](WscriptLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_wscript_launcher**
> WscriptLauncher generate_wscript_launcher()



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.generate_wscript_launcher()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->generate_wscript_launcher: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WscriptLauncher**](WscriptLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_binary_launcher**
> BinaryLauncher get_binary_launcher()



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_binary_launcher()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->get_binary_launcher: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BinaryLauncher**](BinaryLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cscript_launcher**
> CscriptLauncher get_cscript_launcher()



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_cscript_launcher()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->get_cscript_launcher: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CscriptLauncher**](CscriptLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_install_util_launcher**
> InstallUtilLauncher get_install_util_launcher()



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_install_util_launcher()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->get_install_util_launcher: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InstallUtilLauncher**](InstallUtilLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_launchers**
> list[Launcher] get_launchers()



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_launchers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->get_launchers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Launcher]**](Launcher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ms_build_launcher**
> MSBuildLauncher get_ms_build_launcher()



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_ms_build_launcher()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->get_ms_build_launcher: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MSBuildLauncher**](MSBuildLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mshta_launcher**
> MshtaLauncher get_mshta_launcher()



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_mshta_launcher()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->get_mshta_launcher: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MshtaLauncher**](MshtaLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_power_shell_launcher**
> PowerShellLauncher get_power_shell_launcher()



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_power_shell_launcher()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->get_power_shell_launcher: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PowerShellLauncher**](PowerShellLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_regsvr32_launcher**
> Regsvr32Launcher get_regsvr32_launcher()



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_regsvr32_launcher()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->get_regsvr32_launcher: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Regsvr32Launcher**](Regsvr32Launcher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shell_code_launcher**
> ShellCodeLauncher get_shell_code_launcher()



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_shell_code_launcher()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->get_shell_code_launcher: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ShellCodeLauncher**](ShellCodeLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wmic_launcher**
> WmicLauncher get_wmic_launcher()



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_wmic_launcher()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->get_wmic_launcher: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WmicLauncher**](WmicLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wscript_launcher**
> WscriptLauncher get_wscript_launcher()



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
api_instance = swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_wscript_launcher()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LauncherApiApi->get_wscript_launcher: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WscriptLauncher**](WscriptLauncher.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

