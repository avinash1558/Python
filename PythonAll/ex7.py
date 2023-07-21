from pygame import mixer
from datetime import datetime
from time import time
def loader(file,stoper):
    mixer.init()
    mixer.music.load(music.mp3)
    mixer.music.play()
    while 1:
        a=input()
        if a==stoper:
            mixer.music.stop()
            break
def log(message):
    f=open('avi.txt','a')
    f.write(f"{message} : {datetime.now()}\n")

time_start_water=time()
time_start_eye=time()
time_start_ex=time()

time_end_water=4*60
time_end_eye=6*60
time_end_ex=8*60

while 1:
    if time()-time_start_water > time_end_water:
        print("stop the music type w")
        loader('water.mp3', 'w')
        log('pani pi liya')
        time_start_water=time()

    if time()-time_start_eye > time_end_eye:
        print("stop the music type e")
        loader('eye.mp3', 'e')
        log('aram kar liya')
        time_start_eye=time()

    if time()-time_start_ex > time_end_ex:
        print("stop the music type w")
        loader('ex.mp3', 'w')
        log('ex kar liya')
        time_start_ex=time()

