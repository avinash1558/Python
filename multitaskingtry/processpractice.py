import multiprocessing
import time
NUM=0
def cal_sqr(n,result,l):
    l.acquire()
    time.sleep(3)
    result[1]=n*n
    l.release()

def cal_cube(n,l):
    time.sleep(3)
    
if __name__ =="__main__":
    number =10
    t=time.time()
    lock=multiprocessing.Lock()
    result=multiprocessing.Array("i",2)
    t1=multiprocessing.Process(target=cal_sqr,args=(number,result,lock))
    t2=multiprocessing.Process(target=cal_cube,args=(number,lock))
    t1.start()
    t2.start()
    print(t1.daemon,"   ",t2,"   ",result[:])

    t1.join()
    t2.join()
    print(time.time()-t)
    print(t1.daemon,"   ",t2,"   ",result[:])


# import multiprocessing
# import time
# NUM=0
# def cal_sqr(n,result):
#     result[1]=n*n
#     time.sleep(3)
   
#     return n*n
# def cal_cube(n):
#     time.sleep(3)
#     return n*n*n
# if __name__ =="__main__":
#     number =10
#     t=time.time()
#     result=multiprocessing.Array("i",2)
#     t1=multiprocessing.Process(target=cal_sqr,args=(number,result))
#     t2=multiprocessing.Process(target=cal_cube,args=(number,))
#     t1.start()
#     t2.start()
    

    # t1.join()
    # t2.join()
    # print(time.time()-t)
    # print(t1.daemon,"   ",t2,"   ",result[:])