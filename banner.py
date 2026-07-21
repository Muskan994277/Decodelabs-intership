from colorama import Fore, Style

def show_banner():
    print(Fore.CYAN + "=" * 55)
    print(Fore.GREEN + Style.BRIGHT + "      🤖 RULE-BASED AI CHATBOT 🤖")
    print(Fore.CYAN + "=" * 55)
    print(Fore.YELLOW + "Developer : Muskan")
    print(Fore.YELLOW + "Language  : Python")
    print(Fore.YELLOW + "Version   : 1.0")
    print(Fore.CYAN + "-" * 55)
    print(Fore.WHITE + "Type 'help' to see commands.")
    print(Fore.WHITE + "Type 'exit' to close chatbot.")
    print(Fore.CYAN + "=" * 55)