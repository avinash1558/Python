import random

a=int(input('Enter the First range : \n'))
b=int(input('Enter the Second range : \n'))
rendomNumber=random.randint(a, b)
players=0
player1=0
player2=0
attempt=8
while (players<2):
    attempt=8
    num=int(input(f'Enter the geussing player {players+1} number please : \n'))
    print(f'You have attempt time {attempt}')
    while (attempt>0):
        if (num<rendomNumber):
            num=int(input('Enter heigher geussing number please : \n'))
            attempt=attempt-1
            print(f'You have attempt time {attempt}')
        elif (num>rendomNumber):
            num=int(input('Enter lower geussing number please : \n'))
            attempt=attempt-1
            print(f'You have attempt time {attempt}')
        elif (num==rendomNumber):
            print(f'player {players+1} geuss the number in {attempt} attempt')
            players=players+1
            if players==0:
                player1=attempt
            else :
                player2=attempt
            break
if player1>player2:
    print(" Winner is player2 ")
elif player1==player2:
    print(" drow of game ")
else:
    print(" Winner is player1 ")