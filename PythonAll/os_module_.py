# from os import system, name 
# # import sleep to show output for some time period
# from time import sleep  
# # define our clear function
# def clear():
  
#     # for windows
#     if name == 'nt':
#         _ = system('cls')
#     # for mac and linux(here, os.name is 'posix')
#     else:
#         _ = system('clear')
  
# # print out some text
# print('hello geeks\n'*10)
  
# # sleep for 2 seconds after printing output
# sleep(2)
  
# # now call function we defined above
# clear()
import os
# give current dire.
print(os.getcwd())
# change dire
# os.chdir("c://")
# print(os.listdir("c://"))
# os.mkdir('avinash')
# os.makedirs('avinash/ text')
# os.rename('a.txt', 'avi.txt')
# os.path.join('c://avinash')
print(os.path.exists('c://program file'))
print(os.path.isfile('c://program file'))