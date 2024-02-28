import os
from tools.network.wifi_scan import scan_wifi
from text.text import text
def clear_screen():
    # Check the operating system and clear the screen accordingly
    if os.name == "posix":  # For Linux and macOS
        os.system("clear")
    elif os.name == "nt":   # For Windows
        os.system("cls")

def menu():
    while True:
        clear_screen()  # Clear the screen before displaying the menu
        text()
        print("[1] Network")
        print("[2] ?")
        print("[3] Exit")

        selection = input("Enter your selection: ")
        if selection == "1":
            # Clear the screen before running the selected tool
            clear_screen()
            scan_wifi()
            input("Press Enter to return to the menu...")
        elif selection == "2":
            clear_screen()
            print("?")
            input("Press Enter to return to the menu...")
        elif selection == "3":
            break
        else:
            input("Press Enter to continue...")
menu()
