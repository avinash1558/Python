import argparse
import sys
def cal(a):
    if a.o=='add':
        return a.x+a.y
    elif a.o=='sub':
        return a.x-a.y
    elif a.o=='mul':
        return a.x*a.y
    elif a.o=='div':
        return a.x/a.y
    else:
        return "avinash create command"

parse=argparse.ArgumentParser()
parse.add_argument('--x',type=float,default=2.0,help='sorry for that')
parse.add_argument('--y',type=float,default=5.0,help='sorry for that')
parse.add_argument('--o',type=str,default='add',help='sorry for that')
a=parse.parse_args()
sys.stdout.write(str(cal(a)))
#./creat_command.py --x 34 --y 45 --o add