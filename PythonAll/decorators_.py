# DECORATOR
# def function(k):
#     print('avinash',k)
# fun=function
# fun('it')
def function(func):
    def f1():
        print('avinash')
        func()
        print('dane')
    return f1()
# @decl
def avi():
    print('it is another')
avi=function(avi)
avi()