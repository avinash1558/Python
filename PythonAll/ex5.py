# health management system
print()
print('         Health management system')
print()
user=input("Lock -l  and Retrieve - r :")
if user=='r' or user=='retrieve':
    while(1):
        print("Which one diet show you want")
        print("a for avinash, r for rohot and s for sharma")
        name=input()
        if name=='avinash' or name=='a':
            p=open('a.txt')
            print(p.read())
            break
        elif name=='sharma'or name=='s':
            p=open('s.txt')
            print(p.read())
            break
        elif name=='rohit'or name=='r':
            p=open('r.txt')
            print(p.read())
            break
        else:
            print("Check it is not defind")
else:
    print("Welcome to Health management")
    user1=input('Enter name : ')
    while(1):
        def gettime():
            import datetime
            return datetime.datetime.now()
        n=gettime()
        file=user1+".txt"
        f=open(file,"a")
        user2=input('Enter diet : ')
        u=str(n)+" "+user2+"\n"
        f.write(u)
        print("You response save")
        print()
        print("You want add new diet")
        print("(Yes for y and No for n)")
        diet=input()
        if diet=='y' or diet=='yes':
            print("Ok")
        else:
            break