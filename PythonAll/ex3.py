a= 12
nguess=0
print("Enter you number 0 to 30")
while(1):
    num=int(input())
    nguess+=1
    if(num<a):
        print("Heigher number please")
        print("You have",9-nguess," attempt ")
    elif(num>a):
        print("lower number please")
        print("You have",9-nguess," attemp ")
    else:
        print("You win \nIn",nguess,"attempt")
        break
    if(nguess==9):
        print("Game over")
        break
    

