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
from datetime import datetime, timedelta
import shortuuid
from dateutil.parser import parse
import enquiries
import re

def edit_launcher(config):
    if str(config.type) == "msBuild":
        generated = launcher_api.edit_ms_build_launcher(body=config)
    elif str(config.type) == "powerShell":
        generated = launcher_api.edit_power_shell_launcher(body=config)
    elif str(config.type) == "shellCode":
        generated = launcher_api.edit_shell_code_launcher(body=config)
    elif str(config.type) == "serviceBinary":
        # generated = launcher_api.edit_binary_launcher(body=config)
        generated = None
    elif str(config.type) == "binary":
        generated = launcher_api.edit_binary_launcher(body=config)
    elif str(config.type) == "installUtil":
        generated = launcher_api.edit_install_util_launcher(body=config)
    elif str(config.type) == "wmic":
        generated = launcher_api.edit_wmic_launcher(body=config)
    elif str(config.type) == "regsvr32":
        generated = launcher_api.edit_regsvr32_launcher(body=config)
    elif str(config.type) == "mshta":
        generated = launcher_api.edit_mshta_launcher(body=config)
    elif str(config.type) == "cscript":
        generated = launcher_api.edit_cscript_launcher(body=config)
    elif str(config.type) == "wscript":
        generated = launcher_api.edit_wscript_launcher(body=config)
    else:
        print("Don't know how to handle launcher of type: " + str(config.type))
        exit()
    
    return generated


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
CovenantGruntCommand = swagger_client.models.GruntCommand
CovenantGruntCommandOutput = swagger_client.models.CommandOutput
CovenantGruntTask = swagger_client.models.GruntTask
CovenantGruntTasking = swagger_client.models.GruntTasking

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
launcher_api=swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))
listener_api=swagger_client.ListenerApiApi(swagger_client.ApiClient(configuration))

current_user = user_api.get_current_user()

print("Authenticated as: '" + current_user.user_name +"'")
print("")

grunt_api=swagger_client.GruntApiApi(swagger_client.ApiClient(configuration))
grunt_command_api = swagger_client.GruntCommandApiApi(swagger_client.ApiClient(configuration))

# Iterate through all current launchers
current_launchers = launcher_api.get_launchers()

# Iterate through all current listeners
current_listeners = listener_api.get_listeners()

# Set the date we want Grunts to terminate
print("Enter the ISO date/time that you want New Grunts to terminate.")
userDT = input("Use a format such as: '" + str(datetime.now()) + "': ")

try :
    parse(userDT)
    killdate = parse(userDT)
    
except Exception as e:
    config_days = covenant['connection']['default_kill_days_from_now']
    print("Couldn't parse that input, will use the default of '" + str(config_days) + "' days from now.")
    killdate=datetime.now() + timedelta(days=config_days)

print("Will configure Launcher's to use: '" + str(killdate))
print("")

if current_listeners : 
    options=[]
    for listener in current_listeners:
        if listener.status == "active":
            string_listener = str(listener.id) + ": " + listener.name
            print(string_listener)
            options.append(string_listener)
        else:
            print("Listener: " + listener.name + " with id: " + str(listener.id) + " is not active.")
            print("Will not select this listener as the default.")

    choice = enquiries.choose("Select your default listner: ", options)
    choices = re.split(r':\s', choice)
    default_listener_id = int(choices[0])

else:
    print("You need to have a default listener, create one and try again...")
    exit()

print("If no listner_id already selected, will use: " + str(default_listener_id))

for launcher in current_launchers:
    if launcher.kill_date:
        print("Launcher: (" + str(launcher.id) + ") " + launcher.name + " current kill_date: " + str(launcher.kill_date))
        launcher.kill_date = killdate
        if launcher.listener_id == 0: 
            launcher.listener_id = default_listener_id
    
        try: 
            createdlauncher = edit_launcher(launcher)
            if createdlauncher:
                print("Launcher: (" + str(launcher.id) + ") " + launcher.name + " new kill_date: " + str(launcher.kill_date))
            else:
                print("Launcher not updated.")
                print("If this was the serviceBinary that is expected with the current API.")
                print("If not, this is an unknown error.")

        except ApiException as e:
            print("Could not update launcher: %s\n" % e)
        
    else:
        print("Launcher: " + launcher.name + " has no kill_date.")

print("")
print("All Done")