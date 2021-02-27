#!/usr/bin/python3
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import requests, json, urllib3
urllib3.disable_warnings() 
import os.path
from os import path
import bios
import sys
import uuid
import netifaces as ni
from datetime import datetime, timedelta
import base64

def getConnectionAddresses(listenerObject):
    if listenerObject['connectAddressesType'] == "manual":
        return listenerObject['connectAddresses']
    else:
        ip = ni.ifaddresses(listenerObject['connectAddressesInterface'])[ni.AF_INET][0]['addr']
        ipaddresses=[]
        ipaddresses.append(ip)

        return ipaddresses

def str2bool(s):
    return s.lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']

def create_launcher(config):
    # This def needs to be re-written to create launchers in cobbr's version
    # Otherwise we cannot update an existing launcher
    if str(config.type) == "powerShell":
        #FUBAR'd
        newLauncher = launcher_api.generate_power_shell_launcher()
        config.id = newLauncher.id
        generated = launcher_api.edit_power_shell_launcher_with_http_info(body=config)
    elif str(config.type) == "":
        generated = "second thing"
    elif str(config.type) == "":
        generated = "third thing"
    else:
        print("Don't know how to handle launcher of type: " + str(config.type))
        exit()
    return generated
    
def edit_launcher(config):
    if str(config.type) == "msBuild":
        generated = launcher_api.edit_ms_build_launcher(body=config)
    elif str(config.type) == "powerShell":
        generated = launcher_api.edit_power_shell_launcher(body=config)
    elif str(config.type) == "shellCode":
        generated = launcher_api.edit_shell_code_launcher(body=config)
    elif str(config.type) == "serviceBinary":
        #generated = launcher_api.edit_power_shell_launcher(body=config)
        generated = "uh oh, dont know this one!"
        exit()
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

# Check our hosting files actually exist (If we have any) 
if covenant['hosted_files'] is not None:
    for hosted_file in covenant['hosted_files']:
        hosted_file_object = covenant['hosted_files'][hosted_file]

        if not path.isfile(hosted_file_object['SrcFile']):
            print("Could not find source file '" + hosted_file_object['SrcFile'] + "' for '" + hosted_file_object['HostedURI'] + "'")
            exit()

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

CovenantHttpProfile = swagger_client.models.HttpProfile
CovenantListenerType = swagger_client.models.ListenerType
CovenantListener = swagger_client.models.Listener
CovenantHTTPListener = swagger_client.models.HttpListener
CovenantLauncher = swagger_client.models.Launcher
CovenantHostedFile = swagger_client.models.HostedFile
CovenantProfile = swagger_client.models.Profile
CovenantHttpProfile = swagger_client.models.HttpProfile
CovenantHttpProfileHeader = swagger_client.models.HttpProfileHeader
CovenantImplantTemplate = swagger_client.models.ImplantTemplate


user_api=swagger_client.CovenantUserApiApi(swagger_client.ApiClient(configuration))
listener_api=swagger_client.ListenerApiApi(swagger_client.ApiClient(configuration))
profile_api=swagger_client.ProfileApiApi(swagger_client.ApiClient(configuration))
launcher_api=swagger_client.LauncherApiApi(swagger_client.ApiClient(configuration))
implant_template_api=swagger_client.ImplantTemplateApiApi(swagger_client.ApiClient(configuration))


print("Authenticated as: '" + user_api.get_current_user().user_name +"'")
print("")

print("Deploying Custom Listener Profiles:")
for profile in covenant['profiles']:
    profileObject = covenant['profiles'][profile]

    print("Creating Listener Profile: " + str(profileObject['name']))
    if profileObject['type'] == "HTTP":
        print("Attempting to handle HTTP profile: " + str(profileObject['name']))
    else:
        print("Cannot handle profiles of type: " + str(profileObject['type']))

    listener_profiles = profile_api.get_profiles()
    current_profile = next((x for x in listener_profiles if x.name == str(profileObject['name']) ), None)
    
    if current_profile:
        print("Updating existing profile")
        profile_id=current_profile.id


        covenant_profile = CovenantHttpProfile(id=profile_id,
                                            name=str(profileObject['name']),
                                            description=str(profileObject['description']),
                                            type=str(profileObject['type']),
                                            http_get_response=str(profileObject['httpGetResponse']),
                                            http_post_request=profileObject['httpPostRequest'],
                                            http_post_response=profileObject['httpPostResponse'], 
                                            http_urls=profileObject['httpUrls'],
                                            http_request_headers=profileObject['httpRequestHeaders'], 
                                            http_response_headers=profileObject['httpResponseHeaders'], 
                                            message_transform=str(profileObject['messageTransform'])
                                        )
    else:
        print("Creating new profile")
        covenant_profile = CovenantHttpProfile(name=str(profileObject['name']),
                                            description=str(profileObject['description']),
                                            type=str(profileObject['type']),
                                            http_get_response=str(profileObject['httpGetResponse']),
                                            http_post_request=profileObject['httpPostRequest'],
                                            http_post_response=profileObject['httpPostResponse'], 
                                            http_urls=profileObject['httpUrls'],
                                            http_request_headers= profileObject['httpRequestHeaders'], 
                                            http_response_headers= profileObject['httpResponseHeaders'], 
                                            message_transform=str(profileObject['messageTransform'])
                                        )

    print()
    
    try:
        if current_profile:
            covenantprofile = profile_api.edit_http_profile(body=covenant_profile)
        else:
            covenantprofile = profile_api.create_http_profile(body=covenant_profile)
        
    except ApiException as e:
        print("Could Not Create Custom Listener Profiles: %s\n" % e)

print("Deploying Custom Grunt Templates:")
if covenant['templates'] is not None:
    for template in covenant['templates']:
        templateObject = covenant['templates'][template]

        template_file = "templates/"+str(templateObject['file'])
        compatibleListenerTypesArray = []

        if  path.isfile(template_file):
            with open(template_file) as f:
                template_configuration = json.load(f)
                print("Attempting to deploy template for: " + template)
                for compatibleListenerType in template_configuration["compatibleListenerTypes"]:
                    compatibleListenerTypesArray.append(compatibleListenerType)
                
                custom_template = CovenantImplantTemplate ( id= template_configuration["id"],
                                                            name= template_configuration["name"],
                                                            description= template_configuration["description"],
                                                            implant_direction= template_configuration["implantDirection"],
                                                            language= template_configuration["language"],
                                                            stager_code= template_configuration["stagerCode"],
                                                            executor_code= template_configuration["executorCode"],
                                                            comm_type= template_configuration["commType"],
                                                            compatible_dot_net_versions= template_configuration["compatibleDotNetVersions"],
                                                            compatible_listener_types= compatibleListenerTypesArray
                                    )

                try:
                    implant_template_api.edit_implant_template(body=template_configuration)
                except ApiException as e:
                    print("Could not create grunt template: %s\n" % e)
                        
        else:
            print("Could not find template file: " + template_file)
            exit()

print("")

print("Creating Listeners:")
listener_types = listener_api.get_listener_types()
listener_profiles = profile_api.get_profiles()

for listener in covenant['listeners']:
    listenerObject = covenant['listeners'][listener]
    if listenerObject['listenerType'] == "HTTP":
        print("Creating HTTP Listener: " + str(listenerObject['name']))
        
        profile = next((x for x in listener_profiles if x.name == str(listenerObject['profile'])), None)
        if profile:
            profile_id = profile.id 
            http_profile = profile_api.get_http_profile(profile.id)
        
        listenertype = next((x for x in listener_types if x.name == str(listenerObject['listenerType'])), None)
        if listenertype:
            listenertype_id = listenertype.id      
        
        covenantlistner = CovenantHTTPListener(name=str(listenerObject['name']), 
                                            guid=str(uuid.uuid4().hex), 
                                            description=str(listenerObject['description']), 
                                            bind_address=listenerObject['bindAddress'],
                                            bind_port=listenerObject['bindPort'], 
                                            connect_addresses=getConnectionAddresses(listenerObject), 
                                            connect_port=listenerObject['connectPort'], 
                                            profile_id=profile_id, 
                                            urls=http_profile.http_urls,
                                            listener_type_id=listenertype_id, 
                                            use_ssl=str2bool(str(listenerObject['useSSL'])),
                                            ssl_certificate=listenerObject['sslCertificate'],
                                            ssl_certificate_password=listenerObject['sslCertificatePassword'],
                                            ssl_cert_hash=listenerObject['sslCertHash'],
                                            status=listenerObject['status'] )

        try:
            listener_api.create_http_listener_with_http_info(body=covenantlistner)
        except ApiException as e:
            print("Could not create listener: %s\n" % e)
            
    elif listenerObject['listenerType'] == "bridge":
        # deal with the bridge
        print("Dont know how to handle bridges yet")
    else:
        print ("Unknown listener type")

covenant_launchers = launcher_api.get_launchers()
implant_templates = implant_template_api.get_implant_templates()
listeners = listener_api.get_listeners()

for existinglistener in listeners:
    if existinglistener.status == "uninitialized":
        print("Uninitialized Listener: '" + existinglistener.name + "' found, attempting to delete it.")
        try:
            listener_api.delete_listener(existinglistener.id)
        except ApiException as e:
            print("Could not delete listener: %s\n" % e)

print("")

for boom in covenant_launchers:
    pprint(boom.type)

exit()
print("Building Launchers:")
for launcher in covenant['launchers']:
    launcherObject = covenant['launchers'][launcher]
    
    implant_template = next((x for x in implant_templates if x.name == str(launcherObject['ImplantTemplate'])), None)
    if implant_template:
        implant_template_id = implant_template.id
    
    listener = next((x for x in listeners if x.status == "active" and x.name == str(launcherObject['ListenerName'])), None)
    if listener:
        listener_id=listener.id
        
    # Find first object in list that matches value..
    covenantLauncherType = next((x for x in covenant_launchers if x.type == str(launcherObject['LauncherType'])), None)
    if covenantLauncherType:
        print("Updating existing launcher: " + str(covenantLauncherType.name))
    else:
        print("Attempting to create new launcher: " + str(launcherObject['LauncherType']))

    covenantlauncher = CovenantLauncher(    name=str(launcher), 
                                            type=str(launcherObject['LauncherType']), 
                                            dot_net_version=str(launcherObject['DotNetVersion']),
                                            kill_date=str(datetime.now() + timedelta(days=launcherObject['LifeInDays'])), 
                                            listener_id=listener_id , 
                                            implant_template_id=implant_template_id
                                        )
    try:
        if covenantLauncherType:
            print("Attempting to update " + str(launcherObject['LauncherType']) + " Launcher")
            createdlauncher = edit_launcher(covenantlauncher)
        else:
            print("Attempting to create " + str(launcherObject['LauncherType']) + " Launcher")
            createdlauncher = create_launcher(covenantlauncher)


        if createdlauncher and str(launcherObject['LauncherType']) == "powerShell":
            print("Attempting to generate powershell from launcher")
            try:
                generatedlauncher = launcher_api.generate_power_shell_launcher()
            except ApiException as e:
                print("Could not create launcher: %s\n" % e)

            if str(launcherObject['HostedURI']):
                print("Attempting to host launcher on: " + str(launcherObject['HostedURI']))
                
                base64_command="".join( chr(x) for x in base64.b64encode(str(generatedlauncher.power_shell_code).encode()))
                
                hosted_files = listener_api.get_hosted_files(listener_id)
                hostedfile = next((x for x in hosted_files if x.path == str(launcherObject['HostedURI']) ), None)
                
                if hostedfile:
                    hostedfile_id=hostedfile.id
                    hosted_launcher = CovenantHostedFile( 
                                                        id=hostedfile_id,  
                                                        listener_id = listener_id, 
                                                        path = str(launcherObject['HostedURI']),
                                                        content = base64_command
                                                        )
                else:
                    hosted_launcher = CovenantHostedFile(   
                                                        listener_id = listener_id, 
                                                        path = str(launcherObject['HostedURI']),
                                                        content = base64_command
                                                        )

                print()
            
                try:
                    if hostedfile:
                        hostedlauncher = listener_api.edit_hosted_file(listener_id, body=hosted_launcher)
                    else:
                        hostedlauncher = listener_api.create_hosted_file(listener_id, body=hosted_launcher)
                    
                except ApiException as e:
                    print("Could not create hosted launcher: %s\n" % e)

    except ApiException as e:
        print("Could not create launcher: %s\n" % e)            

print("")
if covenant['hosted_files'] is not None:
    print("Hosting files:")   
    for hosted_file in covenant['hosted_files']:
        hosted_file_object = covenant['hosted_files'][hosted_file]
        print("Attempting to host: '" + hosted_file_object['SrcFile'] + "' as '" + hosted_file_object['HostedURI'] + "' on listener '" + hosted_file_object['ListenerName'] + "'")
        
        with open(hosted_file_object['SrcFile'], "rb") as image_file:
            base64_file_contents = "".join( chr(x) for x in base64.b64encode(image_file.read()))
            
        
        listener = next((x for x in listeners if x.status == "active" and x.name == str(hosted_file_object['ListenerName'])), None)
        if listener:
            listener_id=listener.id

        hosted_files = listener_api.get_hosted_files(listener_id)
        hostedfile = next((x for x in hosted_files if x.path == str(hosted_file_object['HostedURI']) ), None)
                
        if hostedfile:
            hostedfile_id=hostedfile.id
            file_to_host = CovenantHostedFile( 
                                                id=hostedfile_id,  
                                                listener_id = listener_id, 
                                                path = str(hosted_file_object['HostedURI']),
                                                content = base64_file_contents
                                                )
        else:
            file_to_host = CovenantHostedFile(   
                                                listener_id = listener_id, 
                                                path = str(hosted_file_object['HostedURI']),
                                                content = base64_file_contents
                                                )

        try:
            if hostedfile:
                file_hosted = listener_api.edit_hosted_file(listener_id, body=file_to_host)
            else:
                file_hosted = listener_api.create_hosted_file(listener_id, body=file_to_host)
            
        except ApiException as e:
            print("Could not create hosted file: %s\n" % e)
else:
    print("No files defined for hosting")
print("")
print("All Done")
