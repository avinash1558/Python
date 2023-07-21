##faulty calculeter
## 23+12=3  34/4=3  43*4=3  34-4=3
while 1:
    num1 = int(input("Enter first number please : "))
    op = input("Enter op.(+,-,/,*) please : ")
    num2 = int(input("Enter second number please : "))
    print("                            _____")
    if op == "+":
        if num1 == 23 and num2 == 12:
            print("The addition of number is : 3")
        else:
            print("The addition of number is : ", num1 + num2)

    elif op == "/":
        if num1 == 34 and num2 == 4:
            print("The subtraction of number is : 3")
        else:
            print("The subtraction of number is : ", num1 / num2)
    elif op == "*":
        if num1 == 43 and num2 == 12:
            print("The multiply of number is : 3")
        else:
            print("The multiply of number is : ", num1 * num2)

    elif op == "-":
        if num1 == 23 and num2 == 12:
            print("The division of number is : 3")
        else:
            print("The division of number is : ", num1 - num2)
    c = input("You want continue \nYes--any key and No--n")
    if c == "n":
        break
