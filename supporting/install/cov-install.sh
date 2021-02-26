#!/bin/bash
# Check for Root
checkroot()
{
if [ `whoami` != 'root' ]
  then
    echo "You must be root to do this."
    exit
fi
}

# Color  Variables
green='\e[32m'
blue='\e[34m'
clear='\e[0m'

# Color Functions
ColorGreen(){
	echo -ne $green$1$clear
}
ColorBlue(){
	echo -ne $blue$1$clear
}

menu(){
echo -ne "
Pick Covenant Version to Install
$(ColorGreen '1)') Cobbr Master (0.6 currently) 
$(ColorGreen '2)') Cobbr Dev 
$(ColorGreen '3)') Zeropointsecurity Master  
$(ColorGreen '4)') Zeropointsecurity Master + Patch 284  
$(ColorGreen '0)') Exit
$(ColorBlue 'Choose an option:') "
        read a
        case $a in
	        1) remove-cov; git clone --recurse-submodules https://github.com/cobbr/Covenant.git ; ver="Cobbr Master"; start-cov;;
	        2) remove-cov; git clone --branch dev --single-branch --recurse-submodules https://github.com/cobbr/Covenant.git ;ver="Cobbr Dev"; start-cov;;
	        3) remove-cov; git clone --recurse-submodules https://github.com/ZeroPointSecurity/Covenant.git; ver="ZPS Master"; start-cov;;
	        4) remove-cov; git clone --recurse-submodules https://github.com/ZeroPointSecurity/Covenant.git; patch-284; ver="ZPS Master + Patch 284"; start-cov;;

		0) exit 0 ;;
		*) echo -e "Option does not exist.";;
        esac
}

remove-cov()
{
  echo "#### Reinstalling Covenant ####"
  echo "# Removing #"
  systemctl stop covenant.service
  rm -rf /opt/Covenant 
  echo "# Reinstalling #"
  cd /opt
}
 start-cov()
 {
  echo "# Attempting Build #"
  cd /opt/Covenant/Covenant
  echo $ver > /opt/Covenant/installed-version.txt
  dotnet build
  echo "# Starting Service #"
  systemctl start covenant.service
  echo ""
  echo "Installed Covenant version:"
  cat /opt/Covenant/installed-version.txt
  echo ""
  echo "#### Done ####"
}

patch-284()
{
  echo "#### Applying Patch 284 ####"
  echo "# Creating backups #"
  cp /opt/Covenant/Covenant/Components/Profiles/HttpProfileForm.razor /opt/Covenant/Covenant/Components/Profiles/HttpProfileForm.razor.bak
  cp /opt/Covenant/Covenant/Models/Listeners/Profile.cs /opt/Covenant/Covenant/Models/Listeners/Profile.cs.bak 
  echo "# Patching files #"
  wget https://raw.githubusercontent.com/sclow/Covenant/35b7b501c0201168c014311ee3c3a4e14190a5db/Covenant/Components/Profiles/HttpProfileForm.razor -O /opt/Covenant/Covenant/Components/Profiles/HttpProfileForm.razor
  wget https://raw.githubusercontent.com/sclow/Covenant/35b7b501c0201168c014311ee3c3a4e14190a5db/Covenant/Models/Listeners/Profile.cs -O /opt/Covenant/Covenant/Models/Listeners/Profile.cs
  echo "# Setting privileges #"
  chmod 644 /opt/Covenant/Covenant/Components/Profiles/HttpProfileForm.razor
  chmod 644 /opt/Covenant/Covenant/Models/Listeners/Profile.cs
}

clear 
checkroot
menu


