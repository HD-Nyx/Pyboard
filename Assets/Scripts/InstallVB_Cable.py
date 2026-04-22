import os, sys

def Install():
    print("Installing...")
    os.system("winget list VBAudio.VBCable")

def Uninstall():
    print("Uninstalling...")
    os.system("winget uninstall VBAudio.VBCable")