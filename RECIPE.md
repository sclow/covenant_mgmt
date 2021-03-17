Hi All, 
I am aware several people have had problems with Covenant and in general the advice has been "restart" or "delete database".

Neither of which felt like they were "good" solutions and were at best reacting/responding rather than resolving.
So I have done (quite a lot) of digging to try to get the "ultimate" Covenant recipe; including working inside the swagger_api and experimenting with both the core (cobbr) and ZPS forks.

My conclusions so far:
* DB access in Covenant can cause significant memory spikes, the OOM-Killer in Kali will terminate those threads leaving you with inconsistent database content.
  * This is noticeable with the "Stage-0" grunt's never completing
* ZPS version of Covenant is much better than 0.6 Core, however lots of movement in the "dev" branch mean it is worth watching (but not using at this moment)
  * Rasta; thanks for putting the fork together it is a significant improvement!!
* The kali.sh script deploys the MS repo for Ubuntu 19.04
  * Kali seems better aligned to Debian 10, which contains dotnet 18.7 instead of 18.4
* "dotnet run" launches the Covenant framework in "debugging mode"; this is great for troubleshooting .... but uses more memory.
  * Publishing and running Covenant in release mode improves performance.

So my recipe for "better" Covenant experience would be:

0: Back everything up! (snapshots /copies / whatever floats your boat)

1: Increase RAM for Kali (8Gb good, 16+ better :))

2: Remove Dotnet from Ubuntu 19.04 repo:
```
sudo apt remove dotnet*
sudo apt remove aspnetcore*
```
3: Install Debian 10 Microsoft Repo
```
wget https://packages.microsoft.com/config/debian/10/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
```
4: Install dotnet form Deb 10 repo
```
sudo apt-get update; \
  sudo apt-get install -y apt-transport-https && \
  sudo apt-get update && \
  sudo apt-get install -y dotnet-sdk-3.1 aspnetcore-runtime-3.1 dotnet-runtime-3.1
```
5: Clean and rebuild Covenant solution with the new runtime
```
cd /opt/Covenant/Covenant
/usr/bin/dotnet clean
/usr/bin/dotnet build
/usr/bin/dotnet run
```
6: Check Covenant works with your existing DB and everything is as expected.

7: Compile and test a Production release of Coventant
```
/usr/bin/dotnet publish -c Release
/usr/bin/dotnet /opt/Covenant/Covenant/bin/Release/netcoreapp3.1/Covenant.dll
```
8: If you get improved performance; feel free to use the attached covenant.service systemd unit file.

If you have any feedback on how this works for you I would be really interested; cant guarantee anything but have had much better experiences with Cov after making these changes. 
