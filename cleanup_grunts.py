#!/usr/bin/python3
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import requests, json
requests.packages.urllib3.disable_warnings() 
import os.path
from os import path
import bios
import sys


config_file = 'config.yml'

if  path.isfile(config_file):
    covenant = bios.read(config_file)
    covenant_admin_url = covenant['connection']['covenant_admin_url']
    covenant_user = covenant['connection']['covenant_user']
    covenant_pass = covenant['connection']['covenant_pass']

configuration = swagger_client.Configuration()
configuration.host = covenant_admin_url
configuration.username = covenant_user
configuration.password = covenant_pass
configuration.verify_ssl = False
configuration.get_basic_auth_token = True
configuration.debug = False

CovenantUserLogin = swagger_client.models.CovenantUserLogin
covenant_http_user = CovenantUserLogin(user_name=covenant_user, password=covenant_pass)


authenticate_api=swagger_client.CovenantUserApiApi(swagger_client.ApiClient(configuration))
try:
    # Attempt to login
    authentication_response=authenticate_api.login(body=covenant_http_user)

except ApiException as e:
    print("Could not authenticate: %s\n" % e)


if authentication_response.covenant_token:
    print("Authentication Succeeded")
    
else:
    print("Authentication Failed")
    exit()

configuration.api_key['Authorization'] = authentication_response.covenant_token
configuration.api_key_prefix['Authorization'] = 'Bearer'
user_api=swagger_client.CovenantUserApiApi(swagger_client.ApiClient(configuration))
listener_api=swagger_client.ListenerApiApi(swagger_client.ApiClient(configuration))
print("Authenticated as: '" + user_api.get_current_user().user_name +"'")
print("")

# Iterate through all current grunts
grunt_api=swagger_client.GruntApiApi(swagger_client.ApiClient(configuration))

for grunt in grunt_api.get_grunts():
    #print(str(grunt.listener_id) + " " +str(grunt.listener) + " " + str(grunt.status) + " " + str(grunt.name) )
    if grunt.status == "exited" or grunt.status == "hidden":
        print("Deleted (" + grunt.status + ") Grunt: " + grunt.name)
        try:
            grunt_api.delete_grunt(grunt.id)
        except ApiException as e:
            print("Could not delete grunt: %s\n" % e)

    else:
        print("Ignoring (" + grunt.status + ") Grunt:" + grunt.name)

print("")
print("All Done")