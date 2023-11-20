import winreg

def fix(newmodelcacheValue):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\SAMP")
        modelcacheValue, _ = winreg.QueryValueEx(key, "model_cache")
        if modelcacheValue:
            # If the parameter exists and is not empty
            winreg.SetValueEx(key, "model_cache", 0, winreg.REG_SZ, newmodelcacheValue)
        elif not modelcacheValue or modelcacheValue == "":  
            # If the parameter exists and is empty
            winreg.SetValueEx(key, "model_cache", 0, winreg.REG_SZ, newmodelcacheValue)
    except FileNotFoundError:
        # If the parameter does not exist
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\SAMP")
        winreg.SetValueEx(key, "model_cache", 0, winreg.REG_SZ, newmodelcacheValue)

# Checking for the existence of the HKEY_CURRENT_USER\Software\Stalker-RP.net folder
try:
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Stalker-RP.net")
    launcherPathValue, _ = winreg.QueryValueEx(key, "launcherPath")
    if launcherPathValue:
        newmodelcacheValue = launcherPathValue + "content/cache/"
        fix(newmodelcacheValue)
    else:
        # fix for other projects
        launcherPathValue = input("Type path to folder with model cache: ")
        fix(launcherPathValue)
except FileNotFoundError:
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, r"Software\SAMP")
