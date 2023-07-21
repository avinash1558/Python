import random

def nameChange(n):
    namelist=[i.split(" ")[0] for i in n]
    sarnamelist=[i.split(" ")[1] for i in n]
    print(f"Change name is : ")
    for i in range(friends):
        Choice=random.choice(sarnamelist)
        namelist[i]+=f" {Choice}"
        sarnamelist.remove(Choice)
        print(f"{namelist[i]}")

friends=int(input('Enter number of friend : '))
friendList=[]
for f in range(friends):
    friendList.append(input('Enter name of friend : '))
nameChange(friendList)