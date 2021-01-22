# Covenant Management


## Getting Swagger Client

### Extract Swagger.json file

* Start Covenant
* Download https://kali:7443/swagger/v1/swagger.json
* Visit https://editor.swagger.io
* File -> Import File
* Download python-client and unzip to working folder

#### Fix Regex
Two of the models in the client mis-interpret the regex used for parsing IP addresses:

* python-client/swagger_client/models/listener.py
* python-client/swagger_client/models/http_listener.py

The regex:
```
if bind_address is not None and not re.search(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', bind_address):  # noqa: E501
            raise ValueError(r"Invalid value for `bind_address`, must be a follow pattern or equal to `/^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/`")  # noqa: E501
```

Should actually be:
```
if bind_address is not None and not re.search(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', bind_address):  # noqa: E501
            raise ValueError(r"Invalid value for `bind_address`, must be a follow pattern or equal to `/^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/`")  # noqa: E501
```

In this case the "\\" used to escape the period in the IP is also being escaped.

### Install swagger_client
```
cd python_client && python3 setup.py install 
```