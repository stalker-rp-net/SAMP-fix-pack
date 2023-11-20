$documentsPath = (Get-ItemProperty -Path 'Registry::HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders').Personal
$SAMPConfigPath = Join-Path -Path $documentsPath -ChildPath "GTA San Andreas User Files\SAMP\sa-mp.cfg"

if (Test-Path -Path $SAMPConfigPath) {
    (Get-Content $SAMPConfigPath) | ForEach-Object { $_ -replace 'directmode=1', 'directmode=0' } | Set-Content $SAMPConfigPath
} else {
    Write-Host "[RU] Игра не установлена. Папка с настройками мультиплеера не найдена."
    Write-Host "[EN] The game is not installed. Multiplayer settings folder not found."
}
