l=10#global variable
# def func() :
#     a=12#local variable
#     l=112#local variable 
#     print(l,' and',a)
# func()
# l=10#global variable
def func() :
    a=12#local variable
    global l
    l=20
    print(l,' and',a)
func()
print(l)
# nested function
# l=12
# def func() :
#     l=10#local variable
#     a=12#local variable
#     def nested():
#         global l #it is create global var
#         l=20
#         print(l,' and',a)
#     nested()
# func()
# print(l,' and')
