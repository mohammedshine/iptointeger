import colorama
import ipaddress

from colorama import Fore, Style
#print(Fore.GREEN + 'Enter the IP: ')
print(f"{Fore.GREEN}Enter the IP{Style.RESET_ALL}")
a = input()
adr = ipaddress.ip_address(a)
print(f"{Fore.GREEN}Result:{Style.RESET_ALL}")
print(int(adr))
