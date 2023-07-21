# pip install SpeechRecognition
# pip install wikipedia
# pip install pyttsx3     & pyaudiowheel
import wikipedia
import datetime
import webbrowser
import os
import smtplib
# from googlesearch import search
# setup for voice
# same time get error for pyaudio
# install pyaudio wheel
import speech_recognition as sr

import pyttsx3
# Sapi5, nsss, and espeak
engine = pyttsx3.init("sapi5")
# voice = engine.getProperty('voices')
# for female
# engine.setProperty('voice', voice[1].id)
# for male
# engine.setProperty('voice',voice[0].id)


def speak(str):
    engine.say(str)
    engine.runAndWait()

def welcome():
    hours = datetime.datetime.now().hour
    if hours >= 6 and hours <= 12:
        return "Good morning"
    elif hours >= 12 and hours <= 17:
        return "Good afternoon"
    elif hours >= 17 and hours <= 19:
        return "Good evening"
    else:
        return "hello"

def listening():
    # first recognizer
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak please....")
        speak("Speak please....")
        r.pause_threshold = 1
        r.energy_threshold = 400  # minimum audio energy to consider for recording

        audio = r.listen(source)
    try:
        # speak("Please Wait a second")
        print("Please Wait a second")
        # recognize_google
        query = r.recognize_google(audio, language='en-in')
        print(f'My Query : {query}')
    except Exception as e:
        print("again please")
        return "none"
    return query

def changeVoice():
    while(1):
        speak("you want male or female")
        setVoice=listening()
        if setVoice !="none":
            if "male" in setVoice or "man" in setVoice:
                # print("male")
                engine.setProperty('voice', voice[0].id)
                speak("i will change my vioce")
                
            elif "female" in setVoice:
                # print("female")
                engine.setProperty('voice', voice[1].id)
                speak("i will change my vioce")
            break

def sendMail(to, content):
    server=smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("as0223080@gmail.com", '8286585455')
    server.sendmail("as0223080@gmail.com", to, content)
    server.close()

def details(name):
    print("              take following argument")
    speak("detail for me, take following argument")
    print("1.  for your details then speak , what is my details")
    speak("1.  for your details then speak , what is my details")
    print("2.  for your name then speak , what is my name")
    speak("2.  for your name then speak , what is my name")
    print("3.  for details of me  then speak , open details")
    speak("3.  for details of me  then speak , open details")
    print("4.  search in wikipedia then speak ,  open wikipedia ")
    speak("4.  search in wikipedia then speak ,  open wikipedia")
    print("5.  search in google then speak ,  open google ")
    speak("5.  search in google then speak ,  open google")
    print("6.  search in youtube then speak ,  open youtube ")
    speak("6.  search in youtube then speak ,  open youtube ")
    print("7.  search in website then speak ,  open website ")
    speak("7.  search in website then speak ,  open website")
    print("8.  open vscode then speak ,  open vscode  / open code ")
    speak("8.  open vscode then speak ,  open vscode  / open code")
    print("9.  open photo folderthen speak ,  open photo")
    speak("9.  open photo folderthen speak ,  open photo")
    print("10.  for name then speak ,  what is your name")
    speak("10.  for name then speak ,  what is your name")
    print("11.  change my name then speak ,  change your name")
    speak("11.  change my name then speak ,  change your name")
    print("12.  sending mail then speak ,  send mail")
    speak("12.  sending mail then speak ,  send mail")
    print("13.  play music and video then speak ,  play music / play video")
    speak("13.  play music and video then speak ,  play music / play video")
    print("14.  changing voice of me then speak ,  change your voice")
    speak("14.  changing voice of me then speak ,  change your voice")
    print(f"15.  hii then speak ,  hi {name}")
    speak(f"15.  hii then speak ,  hi {name}")
    print(f"16.  hello then speak ,  hello {name}")
    speak(f"16.  hello then speak ,  hello {name}")
    print(f"17.  exit for program then speak ,  bye {name}")
    speak(f"17.  exit for program then speak ,  bye {name}")
    print(f"            its update day by day.....")
    speak(f"its update day by day ")

if __name__=="__main__":
    name='tom'
    myName=""
    myFather=""
    myMom=""
    myPhone=""
    speak(f'{welcome()} sir , i am {name},... how can i help you')
    speak('you want my detail yes or no')
    detail=listening().lower()
    if "yes" in detail:
        details(name)
    speak('what you want...')
    while True:
        sentence = listening().lower()
        # for opening webserver
        if ("open wikipedia" in sentence or "in wikipedia" in sentence):
            while (1):
                speak("you want search anything yes or no")
                # https://en.wikipedia.org/wiki/Rahul_Dravid
                sentence=listening().lower()
                if sentence !="none":
                    if "yes" in sentence:
                        while(1):
                            speak("What you want to search...")
                            sentence=listening()
                            if sentence !="none":
                                sentence=[i for i in sentence.split(" ")]
                                s="_".join(sentence)
                                result = wikipedia.summary(s, sentences=3)
                                webbrowser.open(f"https://en.wikipedia.org/wiki/{s}")
                                speak("According to wikipedia")
                                print(result)
                                speak(result)
                                break
                    else:
                        webbrowser.open('https://en.wikipedia.org')
                    break
    
        elif ("open your details" in sentence or "open your detail" in sentence):
            details(name)
        elif ("open youtube" in sentence or "in open youtube" in sentence):
            # https://www.youtube.com/results?search_query=app
            while (1):
                speak("you want search anything yes or no")
                sentence=listening().lower()
                if sentence !="none":
                    if "yes" in sentence:
                        while(1):
                            speak("What you want to search...")
                            sentence=listening()
                            if sentence !="none":
                                sentence=[i for i in sentence.split(" ")]
                                s="_".join(sentence)
                                webbrowser.open(f"https://www.youtube.com/results?search_query={s}")
                                break
                    else:
                        webbrowser.open('youtube.com')
                    break

        elif ("open google" in sentence or "in open google" in sentence):
            while (1):
                speak("you want search anything yes or no")
                sentence=listening().lower()
                if sentence !="none":
                    if "yes" in sentence:
                        while(1):
                            # 
                            speak("What you want to search...")
                            sentence=listening()
                            if sentence !="none":
                                sentence=[i for i in sentence.split(" ")]
                                s="_".join(sentence)
                                str1=f"https://www.google.com/search?q={s}&sxsrf=ALeKk02S6o1Nf82mpino-Jfgd4o2pVni3Q%3A1628328040627&source=hp&ei=aFAOYd6MI4f8wQOdpomQCA&iflsig=AINFCbYAAAAAYQ5eeFAuj4NS9WDcBw1gU7BqcBP9uh_h&oq={s}&gs_lcp=Cgdnd3Mtd2l6EAMyDgguEIAEEMcBENEDEJMCMg0ILhCxAxDHARCjAhAKMgcIABCABBAKMgcIABCxAxAKMgoIABCxAxCDARAKMgcIABCxAxAKMgoIABCxAxCDARAKMgUIABCABDINCC4QgAQQxwEQ0QMQCjIHCAAQsQMQCjoUCC4QgAQQsQMQgwEQxwEQ0QMQkwI6CAguELEDEIMBOggIABCxAxCDAToRCC4QgAQQsQMQgwEQxwEQowI6CAgAEIAEELEDOgsIABCABBCxAxCDAToOCC4QgAQQsQMQxwEQowI6DgguELEDEIMBEMcBEKMCOhEILhCABBCxAxDHARCjAhCTAjoICC4QgAQQsQM6DggAEIAEELEDEIMBEMkDOgUIABCSA1DhJlj7LGDhNGgBcAB4AIABpAaIAcgWkgEJMy0xLjEuMS4ymAEAoAEBsAEA&sclient=gws-wiz&ved=0ahUKEwje4L7Typ7yAhUHfnAKHR1TAoIQ4dUDCAc&uact=5"
                                webbrowser.open(f"{str1}")
                                break
                    else:
                        webbrowser.open('google.com')
                    break

        elif ("open website" in sentence):
            while (1):
                speak("Only speak website name...")
                sentence=listening().lower()
                if sentence !="none":
                    sentence=[i for i in sentence.split(" ")]
                    s="_".join(sentence)
                    if ".com" in sentence or " " in sentence:
                        if ".com" in sentence:
                            s= s.replace(".com", "")
                        if ".com" in sentence:
                            s= s.replace(" ", "")
                        webbrowser.open(f'{s}.com')
                    else:
                        sentence=[i for i in sentence.split(" ")]
                        s="_".join(sentence)
                        webbrowser.open(f'{s}.com')
                    break
        # open app
        elif ("open code" in sentence or "open vscode" in sentence):
            codepath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif ("open photos" in sentence or "open photo" in sentence):
            codepath = "C:\\Users\\HP\\Pictures"
            os.startfile(codepath)
        # for name related
        elif ("what is your name" in sentence or "what's your name" in sentence):
            speak(f'i am {name},... how can i help you')
        elif "change your name" in sentence:
            while(1):
                speak("what name you want say...")
                name=listening()
                if name != "none":
                    break
        elif "what is my name" in sentence:
            while(1):
                if myName=="":
                    speak("i will not have your name")
                    speak("please give me your name")
                    if myName=="":
                        while(1):
                            speak("what is you name")
                            myName=listening()
                            if myName!="none":
                                break

                    break
                else:
                    speak(f"you tell me, you name is {myName}")    
                    break
              
        elif "what is my details" in sentence or "what is my detail" in sentence or "my detail" in sentence or "my details" in sentence:
            while(1):
                if myFather=="":
                    speak("i will not have your details")
                    speak("please give me your details")
                    while(1):
                        if myName=="":
                            while(1):
                                speak("what is you name")
                                myName=listening()
                                if myName!="none":
                                    break
                        if myFather=="":
                            while(1):
                                speak("what is you father name")
                                myFather=listening()
                                if myFather!="none":
                                    break
                        if myMom=="":
                            while(1):
                                speak("what is you mom name")
                                myMom=listening()
                                if myMom!="none":
                                    break
                        if myPhone=="":
                            while(1):
                                speak("what is you Phone number")
                                myPhone=listening()
                                if 5<=len(myPhone):
                                    break
                    break
                else:
                    speak(f"you tell me , you name is {myName}")    
                    speak(f"you tell me , you father name is {myFather}")    
                    speak(f"you tell me , you mom name is {myMom}")    
                    speak(f"you tell me , you phone name is {myPhone}")
                    break

        # play anything
        elif "play music" in sentence:
            musicDir="C:\\Users\\HP\\Desktop\\code\\video\\Python"
            song=os.listdir(musicDir)
            os.startfile(os.path.join(musicDir, song[0]))
        elif "play video" in sentence:
            musicDir="C:\\Users\\HP\\Desktop\\code\\video\\Python"
            song=os.listdir(musicDir)
            os.startfile(os.path.join(musicDir, song[0]))
        elif ("send mail" in sentence or "send email" in sentence):
            while (1):
                try:
                    speak("what sude i send")
                    sentence=listening()
                    if sentence != "none":
                        email=input("Enter email id to sender : ")
                        sendMail(email,sentence)
                        speak("Email is send ...")
                        break
                    # stdd=sssssss
                except Exception as e:
                    speak("sorry my friend , i am not able to send mail")

        elif "change your voice" in sentence:
            changeVoice()
        elif f"bye {name}" in sentence or f"by {name}" in sentence or f"buy {name}" in sentence or f"exit" in sentence or f"buy" in sentence or f"bye" in sentence or  f"by" in sentence :
            speak(f"good bye sir ,have a good day...")
            break
        elif f"hi {name}" in sentence:
            speak(f"hii sir ,have a good day...")
        elif f"hello {name}" in sentence:
            speak(f"hello sir ,have a good day...")
        else:
            speak("Sorry sir i am not understand ...")