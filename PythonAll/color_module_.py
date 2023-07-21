from colorama import Fore, Back, Style

print(Back.GREEN + 'and with a green background')
print(Fore.RED + 'some red text')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

# def prRed(skk): 
#     print("\033[91m {}\033[00m" .format(skk))
# def prGreen(skk): 
#     print("\033[92m {}\033[00m" .format(skk))
# def prYellow(skk): 
#     print("\033[93m {}\033[00m" .format(skk))
# def prLightPurple(skk): 
#     print("\033[94m {}\033[00m" .format(skk))
# def prPurple(skk):
#     print("\033[95m {}\033[00m" .format(skk))
# def prCyan(skk): 
#     print("\033[96m {}\033[00m" .format(skk))
# def prLightGray(skk): 
#     print("\033[97m {}\033[00m" .format(skk))
# def prBlack(skk): 
#     print("\033[98m {}\033[00m" .format(skk))
 
# prCyan("Hello World, ")
# prYellow("It's")
# prGreen("Geeks")
# prRed("For")
# prLightPurple("Geeks")
# prLightGray("Geeks")
# prPurple("Geeks")
# prBlack("Geeks")

# def print_format_table():
#     """
#     prints table of formatted text format options
#     """
#     for style in range(8):
#         for fg in range(30, 38):
#             s1 = ''
#             for bg in range(40, 48):
#                 format = ';'.join([str(style), str(fg), str(bg)])
#                 s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
#             print(s1)
#         print('\n')
 
# print_format_table()