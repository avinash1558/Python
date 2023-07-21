import time
def function():
    book='q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m'
    time.sleep(10)

    while 1:
        t=yield
        if t in book:
            print('yes i am inside of book')
        else:
            print('try again')
#  create decoreter
decorater=function()
# start 
next(decorater)
# SEND value to yield
decorater.send(input())
decorater.send(input())
decorater.send(input())
decorater.send(input())