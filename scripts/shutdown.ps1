 param (
    [int]$delay = 0,
    [string]$message = "Extinction de la machine"
 )

 shutdown /s /t $delay /c $message