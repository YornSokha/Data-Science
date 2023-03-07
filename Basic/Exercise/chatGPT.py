import subprocess
import os
import webbrowser

# define the path to the IntelliJ executable file
intellij_exe_path = r'C:\Program Files\JetBrains\IntelliJ IDEA 2022.1\bin\idea64.exe'

# open the IntelliJ IDE using subprocess module
# subprocess.Popen([intellij_exe_path])
subprocess.Popen('notepad.exe')



# Path to one note exe file
onenote_path = r"C:\Program Files\Microsoft Office\Office16\OUTLOOK.exe"

# Open OneNote app
# os.startfile(onenote_path)



# Replace the path with the correct path to the Teams executable on your system
path = "C:/Users/sokha.yorn/AppData/Local/Microsoft/Teams/current/Teams.exe" 

# Start Teams
# subprocess.Popen(path)






# set the location for the Chrome executable file if necessary
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

# open a new window on startup of Chrome
webbrowser.get(chrome_path).open_new('https://www.youtube.com/')
