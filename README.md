# G502-GShift.py  
Linux script that triggers application specific commands.   
Simply use [Logitech Onboard Memory Manager](https://support.logi.com/hc/en-us/articles/360059641133-Onboard-Memory-Manager) to set an unused keyboard key to your GShift function (or really any button), and then bind that keycode in you distro's keyboard settings to activate this script.    

I have some example commands/syntax in the script already, for you to copy.    
the format to use for each window's command is:  
```
("WMCLASS", "WINDOW TITLE WITH SUPPORT FOR * WILDCARDS"): "COMMAND TO RUN",
```
