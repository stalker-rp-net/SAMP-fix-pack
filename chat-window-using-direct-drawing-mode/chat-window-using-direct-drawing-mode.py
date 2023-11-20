import os
from winreg import *

# Win 10 and earlier compability (OneDrive)
def getDocumentsFolder():
    reg = ConnectRegistry(None, HKEY_CURRENT_USER)
    key = OpenKey(reg, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
    name = QueryValueEx(key, 'Personal')[0]
    return name

SAMPConfigPath = os.path.join(getDocumentsFolder(), 'GTA San Andreas User Files', 'SAMP', 'sa-mp.cfg')

if os.path.exists(SAMPConfigPath):
    with open(SAMPConfigPath, 'r') as file:
        file_content = file.read()
        updated_content = file_content.replace('directmode=1', 'directmode=0')
    with open(SAMPConfigPath, 'w') as file:
        file.write(updated_content)
else:
    print("[RU] Игра не установлена. Папка с настройками мультиплеера не найдена.")
    print("[EN] The game is not installed. Multiplayer settings folder not found.")