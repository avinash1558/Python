import random
def rohanMultipleTable(n):
    i=0
    rendomNumber=random.randint(1,9)
    print("It is rohan table")
    while (i<10):
        if i==rendomNumber:
            print(f'{n}  X {i+1}  : {(i+1)*n+10}')
            rohanlist.append((i+1)*n+10)
        elif i==9:
            print(f'{n} X {i+1}  : {(i+1)*n}')
            rohanlist.append((i+1)*n)
        else:
            print(f'{n}  X {i+1}  : {(i+1)*n}')
            rohanlist.append((i+1)*n)
        i+=1

def checkTable(a,b):
    print("\nIt is creacte table")
    i=0
    while (i<10):
        if i==9:
            print(f'{a} X {i+1}  : {(i+1)*a}')
            checklist.append((i+1)*a)
        else:
            print(f'{a}  X {i+1}  : {(i+1)*a}')
            checklist.append((i+1)*a)
        i+=1
    c=0
    while (c<10):
        if checklist[c] != rohanlist[c]:
            print(f"{a}  X {c+1} :{rohanlist[c]} is wrong and write is {a}  X {c+1} :{checklist[c]}")
        c+=1
    if rohanlist==checklist:
        print('rohan list is good working')
    else:
        print('rohan list is not working')
                    
number =int(input("Enter the which you want multi. : "))
checklist=[]
rohanlist=[]
rohanMultipleTable(number)
checkTable(number,rohanlist)

