import sys 
    
print(sys.version)

# def print_to_stderr(*a): 
#     # Here a is the array holding the objects 
#     # passed as the arguement of the function 
#     print(*a, file = sys.stderr) 
  
# print_to_stderr("Hello World") 

for line in sys.stdin: 
    if 'q' == line.rstrip(): 
        break
    print(f'Input : {line}') 
  
print("Exit") 