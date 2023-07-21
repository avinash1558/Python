import threading
import time
NUM=0
def cal_sqr(n):
    time.sleep(3)
    global NUM
    NUM=n*n
    print(NUM)
    return n*n
def cal_cube(n):
    time.sleep(3)
    return n*n*n

number =10
t=time.time()
t1=threading.Thread(target=cal_sqr,args=(number,))
t2=threading.Thread(target=cal_cube,args=(number,))
t1.start()
t2.start()
print(t1.daemon,"   ",t2,"   ",NUM)

t1.join()
t2.join()
print(time.time()-t)
