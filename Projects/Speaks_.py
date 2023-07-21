# pip install gtts

import os,time,playsound

from gtts import gTTS

def speak(text):
    tts=gTTS(text=text,lang="en")
    filename="avinash.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
speak("Hello avinash Sharma")
print("end")