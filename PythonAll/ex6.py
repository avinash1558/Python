# water , sneck and gun
import random

def game(c,u):
    if c=='gun' and (u=='water' or u=='w'):
        return 1
    elif c=='gun' and (u=='sneck' or u=='s'):
        return -1
    elif c=='water' and (u=='sneck' or u=='s'):
        return 1
    elif c=='water' and (u=='gun' or u=='g'):
        return -1
    elif c=='sneck' and (u=='water' or u=='w'):
        return -1
    elif c=='sneck' and (u=='gun' or u=='g'):
        return 1
    elif c=='gun' and (u=='gun' or u=='g'):
        return 0
    elif c=='water' and (u=='water' or u=='w'):
        return 0
    elif c=='sneck' and (u=='sneck' or u=='s'):
        return 0
    else:
        return 2
def check(n):
    if n==1:
        print("               YOU WIN THE GAME")
    elif n==-1:
        print("               YOU LOSE THE GAME")
    elif n==0:
        print("                 GAME DROW")
    else:
        print('              YOU CHOICE WRONG ')
        print('            ------TRY AGEAN------')
print('---------------------------------------------------')
print('               WATER , SNECK AND GUN')
print('---------------------------------------------------')
print('                                       LIFE : * * *')
bk=0
s=3
while(1):
    ran=['gun','water','sneck']
    computer=random.choice(ran)
    print('               YOU CHOOSE ANY ONE ')
    user=input("        WATER(w) ,SNECK(s) and GUN(g) :")
    a=game(computer, user)
    print("              COMPUTER CHOOSE ","(",computer.upper(),")")
    check(a)

    if a == -1:
        bk = bk+1

    if a==2 :
        print(end="")
    elif bk ==3:  
        print("                  GAME OVER")
    bl=input('      CONTINUE TO PLAY YES(y) AND NO(n) :')
    print('---------------------------------------------------')
    if a==-1:
        s-=1

    if bl =='n' or bk ==3:
        break
    else:
        if s==3:
            print('                                       LIFE : * * *')
        elif s==2:
            print('                                       LIFE : * * ')
        else:
            print('                                       LIFE : * ')
    
        

    
        

# # water , sneck and gun
# import random

# def game(c,u):
#     if c=='gun' and (u=='water' or u=='w'):
#         return 1
#     elif c=='gun' and (u=='sneck' or u=='s'):
#         return -1
#     elif c=='water' and (u=='sneck' or u=='s'):
#         return 1
#     elif c=='water' and (u=='gun' or u=='g'):
#         return -1
#     elif c=='sneck' and (u=='water' or u=='w'):
#         return -1
#     elif c=='sneck' and (u=='gun' or u=='g'):
#         return 1
#     elif c=='gun' and (u=='gun' or u=='g'):
#         return 0
#     elif c=='water' and (u=='water' or u=='w'):
#         return 0
#     elif c=='sneck' and (u=='sneck' or u=='s'):
#         return 0
#     else:
#         return 2
# def check(n):
#     if n==1:
#         print("               YOU WIN THE GAME")
#     elif n==-1:
#         print("              YOU LOSE THE GAME")
#     elif n==0:
#         print("                  GAME DROW")
#     else:
#         print('              YOU CHOICE WRONG ')
#         print('           -----TRY AGEAN-----')
# print('-------------------------------------------------------')
# print('               WATER , SNECK AND GUN')
# print('-------------------------------------------------------')
# while(1):
#     ran=['gun','water','sneck']
#     computer=random.choice(ran)
#     print('              YOU CHOOSE ANY ONE ')
#     user=input("        WATER(w) ,SNECK(s) and GUN(g) : ")
#     a=game(computer, user)
#     check(a)
#     if a==1 and a==0:    
#         bl=input('      CONTINUE TO PLAY YES(y) AND NO(n) : ')
#     print('-------------------------------------------------------')
#     if bl =='n':
#         break
    
