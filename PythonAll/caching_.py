import time
# step 1 import lru_cache from functools
from functools import lru_cache
# TODO: step 2 @lru_cache max time for run after then not take time
@lru_cache(maxsize=3)
def sleeper(n):
    time.sleep(n)
    return n

if __name__=='__main__':
    print('1st run')
    sleeper(4)
    print('2nd run')
    sleeper(5)
    print('3nd run')
    sleeper(6)
    print('4nd run')
    print('after run')
    sleeper(4)
    print('2nd run')
    sleeper(5)
    print('3nd run')
    sleeper(6)
    print('4nd run')
    