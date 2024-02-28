import subprocess

def scan_wifi():
    while True:
        print("[1] Linux")
        print("[2] Windows")
        print("[3] Exit")
        print("")
        
        os_selection = input("Enter your selection:")
        if os_selection == "1":
            try:
                nw_linux = subprocess.check_output(["iwlist", "wlan0", "scan"])
                decode_linux = nw_linux.decode('utf-8')
                print(decode_linux)
            except subprocess.CalledProcessError:
                print("Error: Failed to execute command on Linux.")

        elif os_selection == "2":
            try:
                nw_windows = subprocess.check_output(["netsh", "wlan", "show", "network"])
                decode_windows = nw_windows.decode('ascii')
                print(decode_windows)
            except subprocess.CalledProcessError:
                print("Error: Failed to execute command on Windows.")
        if os_selection == "3":
            break
