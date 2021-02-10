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
import uuid
from dateutil.parser import parse

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
listener_api=swagger_client.ListenerApiApi(swagger_client.ApiClient(configuration))

current_user = user_api.get_current_user()

print("Authenticated as: '" + current_user.user_name +"'")
print("")

grunt_api=swagger_client.GruntApiApi(swagger_client.ApiClient(configuration))
grunt_command_api = swagger_client.GruntCommandApiApi(swagger_client.ApiClient(configuration))
grunt_task_api=swagger_client.GruntTaskApiApi(swagger_client.ApiClient(configuration))
grunt_tasking_api=swagger_client.GruntTaskingApiApi(swagger_client.ApiClient(configuration))
grunt_command_output_api = swagger_client.CommandOutputApiApi(swagger_client.ApiClient(configuration))

# Iterate through all current listeners
current_listeners = listener_api.get_listeners()
grunt_tasks = grunt_task_api.get_grunt_tasks()

# Set the date we want Grunts to terminate
userDT = input("Enter new delay time in seconds: ")



try :
    delaytime = int(userDT)
    
except Exception as e:
    delaytime = covenant['connection']['default_grunt_delay_time']
    print("Couldn't parse that input, will use the default of '" + str(delaytime) + "' seconds.")


print("Will configured grunt's to use: '" + str(delaytime))
print("")

# Identify "Delay" Task
# Find first object in list that matches value..
task = next((x for x in grunt_tasks if x.name == "Delay" ), None)
if task:
    task_id = task.id 
else:
    print("Could not find task 'Delay'")
    exit()

print("Current Listeners: ")
for listener in current_listeners:
        print(str(listener.id) + ": " + str(listener.name))

print("")
current_listener_input = input("Select Listener ID, or '0' for all listeners: ")

try:
    current_listener_id = int(current_listener_input)
except Exception as e:
        print("Please enter an integer, couldnt use '" + current_listener_input +  "' because: %s\n" % e)
        exit()

# Iterate through all current grunts update them if on selected listener
for grunt in grunt_api.get_grunts():
    if current_listener_id == 0 or grunt.listener_id == current_listener_id:
        # current_listener_id is an the same as our grunt.listener_id
        # OR it is zero (do for all grunts) 
        delaycommand = "Delay /seconds:\"" + str(delaytime) + "\""
        

        grunt_command = CovenantGruntCommand(command=delaycommand,
                                                command_time=datetime.now(),
                                                command_output_id=grunt_command_output_api.create_command_output().id,
                                                user_id=str(current_user.id),
                                                grunt_id=grunt.id
                                            )


        try:
            grunt_command_output = grunt_command_api.create_grunt_command(body=grunt_command)
            grunt_tasking = CovenantGruntTasking(name=str(uuid.uuid4().hex),
                                            grunt_id=grunt.id,
                                            grunt_task_id=task.id,
                                            grunt_command_id=grunt_command_output.id
                                        )

            grunt_tasking_output = grunt_tasking_api.create_grunt_tasking(body=grunt_tasking)
            
            print("Updated Grunt: '" + grunt.name + "' to have delay time  of '" + str(delaytime) + "' via tasking: '" + str(grunt_tasking_output.id) + "'")
        except ApiException as e:
            print("Could not update grunt: %s\n" % e)

    else:
        print("Ignoring Grunt: '" + grunt.name + "' as it is not on selected listener(s)")

print("")
print("All Done")