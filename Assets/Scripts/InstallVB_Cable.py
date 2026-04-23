import subprocess
import os

# Apprently winget can't install it, wish it was bash
# Just have to package the setup EXE and run it

InstallerPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Libraries/VBCABLE_Setup_x64.exe"))

def Install():
    print("Installing...")
    subprocess.run(["powershell","Start-Process", InstallerPath,"-Verb", "RunAs","-Wait"], check=True)

def Uninstall():
    print("Uninstalling...")
    os.system("winget uninstall VBAudio.VBCable")

