# 234 242
def palindromeFunction(n):
    n=n+1
    while not check(n):
        n+=1
    return n
def check(n):
    return str(n)==str(n)[::-1]
test=int(input('No. of time are you test : '))
num1=[]
for i in range(test):
    num1.append(int(input("Enter the number : \n")))
for i in range(test):
    # 123
    print(f"Next palindrome for {num1[i]} is {palindromeFunction(num1[i])}")