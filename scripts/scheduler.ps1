 param (
    [string]$script,
     [string]$taskName = "Task"
 )
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-WindowStyle hidden C:\Users\monito\$script"
$date = (Get-Date).addSeconds(60)
$trigger = New-ScheduledTaskTrigger -Once -At $date
$principal = New-ScheduledTaskPrincipal -UserId "user" -RunLevel Highest
$settings = New-ScheduledTaskSettingsSet -DeleteExpiredTaskAfter 0
$task = ((New-ScheduledTask -Action $action -Trigger $trigger -Principal $principal -Settings $settings) | %{ $_.Triggers[0].EndBoundary = $date.AddSeconds(1).ToString('s') ; $_ })

Register-ScheduledTask -TaskName $taskName -InputObject $task

