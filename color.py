import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset= True)

#without module
#print('\033[31m'+'some red text')

print(Fore.RED + 'some red text')
print(Back.GREEN + 'some green text')
print(Back.CYAN + 'cyan')
print(Style.BRIGHT + 'bright')
print(Fore.RED + Back.GREEN + 'red and green')
print(Style.DIM + 'dim')


'''
Fore, Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET;
Style: DIM, NORMAL, BRIGHT, RESET_ALL
'''
