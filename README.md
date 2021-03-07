# Covenant Management
## Configuration file
You will need to set up a config.yml file (based on the example with this project), the config file itself should be relatively readable however the key stanzas are as follows:

* connection - How the management scripts should connect to your Covenant Instance
* listeners - Listeners you want to deploy and start
* launchers - Pre-configure launchers to work with hosted listeners
* hosted_files - Files you want to host on specific URL's within a listener
* profiles - Listener Profiles (in case you dont want to use the defaults)
* templates - GRUNT templates in JSON that you have modified.

## Patch Covenant API
Versions of Covenant without the PR https://github.com/cobbr/Covenant/pull/284 will have issues with the API when creating custom profiles. 

This is due to the default values applied to new listener profiles also being applied to changed / custom profiles via the API. The result is a URL deadlock that causes GRUNTS to perform poorly / become lost.

Apply the PR and rebuild covenant as you start your exercise. 

```sudo dotnet run```


## Setup Covenant
Typically you will need to log onto Covenant *once* to set up the first user and password. 

Once that has been configured (and set in config.yml) you can run an entire configuration exercise using the command:

```./setup_covenant.py```

You will see it stepping through each stage of the configuration and if it comes into difficulties hopefully give error messages that will help you troubleshoot.

### Covenant with SSL
It can be very useful to run Covenant over an HTTPS (instead of HTTP) listener. 
This "just" needs you to create a PFX file with known password that can be applied to the listener. 

In most circumstances you will want to use a valid cert (especially if domain fronting) as it will allow you to perform certificate validation (pinning).

However, if you want a quick and dirty SSL certificate for testing, consider running:

```certs/makeCert.sh```

### Custom GRUNT Templates
One of the nice features of Covenant is the ability to modify / extend the templates to your taste.

It can be desireable to configure and test templates in a lab environment before using them on an exercise.

The easiest way to edit a template is to copy the code from a Grunt variant and import it into Visual Studio Console App (.NET Framework) as a new project. 

Once you have working code copy it back to that Covenant using the Web GUI for testing. 

Once you are happy with your Custom GRUNT template use the swagger_api to back the templates up using the following procedure:

E.g. for a Covenant instance running on "https://kali:7443/" you can access the Swagger UI at "https://kali:7443/swagger/", authenticate (POST /api/users/login) and set your Bearer to allow other commands.

* Authenticate!
* GET (​/api​/implanttemplates​/{id}) Each of your templates (by default only 4)
* Save the template to templates/${TemplateName}.json (expanding ${TemplateName} as you do so)
* Configure the "templates" stanza of config.yml to point to "${TemplateName}.json" (or whatever name you saved it as) within the "templates/" folder.
* Run ```./setup_covenant.py``` to deploy custom templates with your configuration.

**Note:** Templates defined in this section will overwrite whatever is in your current Covenant instance without prompting. 
Test carefully in a Lab before using custom Templates on a live exercise; think very carefully before updating the templates whilst "inflight".

#### ZPS fork / Cobbr (core) 0.6
The relationship between a template and the type of implant it applies to cannot be updated via the API (fixed in dev / 0.7), therefore when you modify a template you break that link, hence you cannot use that template to build a launcher.
This can be simply fixed by opening each template and recreating that link (e.g. to HTTP/Bridge) as needed (see https://github.com/cobbr/Covenant/issues/158).

If you fail to recreate these links then you won't be able to create a launcher that uses that template (potentially 'crashing' the UI). Recreating the link resolves that issue.

#### Core (Cobbr) Dev
The template code assumes that launchers already exist for each launcher type; this is true for 0.6 and ZPS fork but the db initialisation for Dev does not create them (nor is that trivial via the API). 

Either create manually or apply the ZPS.sql to your database to have them created.

## Cleanup Dead / Hidden Grunts
Performance issues can appear if the Covenant DB starts to get too large; if you have a lot of dead / hidden GRUNTS that you are no longer using you can purge them using the command:

```./cleanup_grunts.py```

**Note**: If you purge Grunts you lose part of your audit trail.

## Change Killdate on current Grunts
There are times when you want to change the end date of an exercise (e.g. terminate it early or extend it by a few days).

You can use the command:

```./change_grunt_kill_date.py``` 

To change the kill date of all active Grunts (or just those on a specific listener).

Follow the prompts and use ISO conformant Date/Times.
Experiment before you run it on a live exercise!

## Change Sleeptime on current Grunts
It can be handy during an engagement to "go quiet" for a period of time. 
Therefore it is nice to be able to make all current Grunts sleep for a period of time.

The command:
```./change_grunt_sleep_time.py``` 
Can be used to mass-change the "delay" time on all Grunts (or just those on a specific listner).

Note: whilst you *can* reduce the sleep time for all Grunts (e.g. to 1 second), this will significantly degrade any ability to evade monitoring.


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
