# Run This Script from Project Root to Install Application
import os
import site
import subprocess
from sys import platform

# Step 1: Give App Name & Icon Path
app_name = "my-app"
app_icon_path = "assets/icon.ico"

print(os.getcwd()) # Project root

def get_pkg_path(pkg, system):
    # Step 2: Provide Path to `site-packages`
    sp = site.getsitepackages()[0]
    if system == "mac":
        return f"{sp}/{pkg}:{pkg}/"
    if system == "win":
        return f"{sp}/{pkg};{pkg}/"

# Run Mac
if platform == "darwin":
    print("On Mac")
    # Run on Mac
    cmd_mac_str = f"""
pyinstaller --noconfirm --onedir -n '{app_name}' --windowed --add-data '{get_pkg_path("customtkinter", "mac")}' --icon='{app_icon_path}' app.py
cd dist
tar -czf {app_name}.tar.gz {app_name}.app
"""
    subprocess.run(cmd_mac_str, shell=True)
    # print(cmd_mac_str)

# Run Windows
if platform == "windows":
    print("On Windows")
    # Run on Win
    cmd_win_str = fr"""
pyinstaller --noconfirm --onefile -n {app_name} --windowed --add-data '{get_pkg_path("customtkinter", "win")}' --icon='{app_icon_path}' app.py
""" 
    # os.system(cmd_win_str)
    # Zip File
    # os.chdir("dist") 
    # os.system(f"powershell -Command Compress-Archive -Path {app_name}.exe -DestinationPath {app_name}-win.zip")
    print(cmd_win_str)
    #subprocess.run(cmd_win_str, shell=True) # Not work