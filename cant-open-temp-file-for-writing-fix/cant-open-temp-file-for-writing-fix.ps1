if (Test-Path "HKCU:\Software\Stalker-RP.net") {
    $launcherPathValue = Get-ItemProperty -Path "HKCU:\Software\Stalker-RP.net" -Name "launcherPath"
    if ($launcherPathValue -ne $null -and $launcherPathValue -ne "") {
        $newmodelcacheValue = $launcherPathValue.launcherPath + "content/cache/"

        if (Test-Path "HKCU:\Software\SAMP") {
            $modelcacheValue = Get-ItemProperty -Path "HKCU:\Software\SAMP" -Name "model_cache"
            if ($modelcacheValue -ne $null) {
                Set-ItemProperty -Path "HKCU:\Software\SAMP" -Name "model_cache" -Value $newmodelcacheValue
            } elseif ($modelcacheValue -eq "") {
                Set-ItemProperty -Path "HKCU:\Software\SAMP" -Name "model_cache" -Value $newmodelcacheValue
            }
            else {
                New-ItemProperty -Path "HKCU:\Software\SAMP" -Name "model_cache" -Value $newmodelcacheValue
            }
        } else {
            New-Item -Path "HKCU:\Software\SAMP" -Force
            New-ItemProperty -Path "HKCU:\Software\SAMP" -Name "model_cache" -Value $newmodelcacheValue
        }
    } else {
        Remove-Item "HKCU:\Software\SAMP" -Recurse
    }
} else {
    Remove-Item "HKCU:\Software\SAMP" -Recurse
}