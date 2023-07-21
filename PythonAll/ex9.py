import requests
import json
import time
def speak(str):
    import win32com.client
    speak=win32com.client.Dispatch('SAPI.SpVoice')
    speak.Speak(str)
# speak('rohit sharma ka naam totala hai or pagal hai')
data=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=a94e1ea58f46410c9d41dd2a54d40663").text
news=json.loads(data)
newsArticle=news['articles']
speak('i am avinash sharma ')
speak('now i read news title ')
for SPEAK in newsArticle:
    speak(SPEAK['title'])
    speak('wait for a second')
    time.sleep(3)
    speak('next news is ')
    time.sleep(0.5)
speak('thanks i will se you leter')