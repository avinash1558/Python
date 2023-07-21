size=int(input("Enter the size of list : "))
li=[]
for i in range(size):
    li.append(int(input('Enter list number one by one : ')))
first=li[:]
first.reverse()
second=li[::-1]
temp=[]
third=li[:]
for i in range(int(size/2)):
    temp.append(third[i])
    third[i]=third[size-i-1]
    third[size-1-i]=temp[i]
print('original list element : ',li)
print('1st reverse : ',first)
print("2nd reverse : ",second)
print("3rd reverse : ",third)
