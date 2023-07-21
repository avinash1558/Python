import threading
import time

def setInterval(func,n):
    while(1):
        time.sleep(n)
        func()

def foo():
    print ("hello")

# using
setInterval(foo,3)