#!/usr/bin/env python3
import subprocess
import fnmatch
import time

commands = {
    ("FreeTube", "*- FreeTube"): "xdotool key ctrl+r",

    ("goofcord", "GoofCord"): "xdotool key alt+shift+Up",
    ("goofcord", "*Discord |*"): "xdotool key alt+shift+Up",
    ("firefox", "*Discord |*"):  "xdotool key alt+shift+Up",
    ("discord", "*- Discord*"):  "xdotool key alt+shift+Up",

    ("steam_app_782330", "*DOOMEternal*"): "xdotool key 'g+f'; xdotool key 'g'",

    ("gamescope", "*HELLDIVERS*"):        "xdotool key i",
    ("steam_app_553850", "*HELLDIVERS*"): "xdotool key i",
}

def get_active_window():
    win_id = subprocess.check_output(["xdotool", "getactivewindow"]).decode().strip()
    win_class = subprocess.check_output(["xdotool", "getwindowclassname", win_id]).decode().strip()
    win_name = subprocess.check_output(["xdotool", "getwindowname", win_id]).decode().strip()
    return win_id, win_class, win_name

def send_keys(command):
    """Send keys to the active window after a small delay."""
    time.sleep(0.2)
    print(f"Executing: {command}")
    subprocess.Popen(["/bin/bash", "-c", command])

def main():
    win_id, window_class, window_name = get_active_window()
    print(f"Active Window: class={window_class}, title={window_name}, id={win_id}")

    # Try to match against rules
    for (class_pattern, title_pattern), command in commands.items():
        if fnmatch.fnmatch(window_class, class_pattern) and fnmatch.fnmatch(window_name, title_pattern):
            send_keys(command)
            return

    # Fallback: autorandr switch
#    current_layout = subprocess.check_output(["autorandr", "--current"]).decode().strip()
#    if current_layout == ".tv":
#        print("Switching layout to .dual")
#        subprocess.Popen(["autorandr", "--load", ".dual"])
#    else:
#        print("No matching rule found.")

if __name__ == "__main__":
    main()
