import colorama
from colorama import Fore, Style

def text():
    print("\033c")
    colorama.init()

    logo = f"""
    {Fore.BLUE}  _____        _        _____                                    
    |  __ \      | |      |  __ \                                   
    | |  | | __ _| |_ __ _| |  | |_   _ _ __   __ _ _ __ ___   ___  
    | |  | |/ _` | __/ _` | |  | | | | | '_ \ / _` | '_ ` _ \ / _ \ 
    | |__| | (_| | || (_| | |__| | |_| | | | | (_| | | | | | | (_) |
    |_____/ \__,_|\__\__,_|_____/ \__, |_| |_|\__,_|_| |_| |_|\___/ 
                                    __/ |                            
                                |___/                             
    {Style.RESET_ALL}
    """

    print(logo)
text()