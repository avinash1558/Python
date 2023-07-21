def polidromeFunction(n):
    if n>10:
        n+=1
        while(check(n)):
            n+=1
        return n
    else :
        return n

def check(n):
    if str(n)== str(n)[::-1]:
        return False
    else:
        return True

if __name__=='__main__':
    test=int(input('No. of time are you test : '))
    num1=[]
    for i in range(test):
        num1.append(int(input("Enter the number : \n")))
    newList=[]
    for i in range(test):
        newList.append(polidromeFunction(num1[i]))
        if num1[i]>10:
            print(f'The polindrome of {num1[i]} is {polidromeFunction(num1[i])}')
        else:
            print(f'{num1[i]} is not greater then 10')
    print(f'{num1} it\'s old list and new list is {newList}')