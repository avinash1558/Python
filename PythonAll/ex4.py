# pattern
num=int(input("Enter number of row :"))
s=1
c=num-1
while(s<=num):#1<=3     #  *       
    a=1                 # ***
    p=1                 #******
    while (a<=c):#2
        print(" ",end="")
        a+=1
    c-=1
    while (p<=2*s-1):#
        print("*",end="")  
        p+=1
    print()    
    s+=1  
s=num-1
k=1
while(s>=1):#2>=1   # ***       
    a=1             #  *            
    while (a<=k):#2
        print(" ",end="")
        a+=1
    k+=1
    p=1
    while (p<=2*s-1):#
        print("*",end="")  
        p+=1
    print()    
    s-=1  

# num=int(input("Enter number of row :"))
# new=int(input("Any number for true and 0 for false :"))
# tf=bool(new)
# if tf==True:
#     a=1
#     while(a<=num):
#         print(a*"*")
#         a+=1        
# else: 
#     d=num
#     while(d>=1):
#         print(d*"*")
#         d-=1

# if tf==True:
#     a=1
#     b=1
#     while(a<num+1):
#         b=1
#         while(b<a+1):
#             print("*",end="")
#             b=b+1
#         a=a+1
#         print()
# else: 
#     c=num
#     d=1
#     while(c>=1):
#         d=1
#         while(d<=c):
#             print("*",end="")
#             d=d+1
#         c=c-1
#         print()

# for
# if tf==True:
#     # *      #3
#     # **
#     # ***
#     # 1 to 1,2,3 to (3+1 stop) 
#     for i in range(1,num+1):
#         for j in range(1,i+1):
#             print('*',end="")
#         print()
# elif tf==False:
#     # 3 to   3,2,1 to   (0 stop)  by -1  
#     for i in range(num,0,-1):
#         for j in range(1,i+1):
#             print('*',end="")
#         print()