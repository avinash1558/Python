# set the Text widget to Not Editable mode
# text_box.config(state='disabled')

# text_box.config(state='normal') 
# set the Text widget to Editable mode
from pygame import mixer
from gtts import gTTS
from googletrans import Translator, LANGUAGES
from datetime import datetime
import json
import playsound
print(playsound.__version__)

print(datetime.now().strftime("%H : %M : %S : %I : %p" ))
i=1
# print(LANGUAGES.values().__contains__)

lcode=""
# li=[]
# jscode=""
# with open("C:\\Users\\avina\\OneDrive\\Desktop\\codes\\Python\\Assistance\\Assistence.json","w") as l:
#     # global jscode
#     json.dump()



# i=10
# def inr():
#     global i
#     i=i+i
#     print(i)
# inr()

# def lancode(lan):
#     dict={
#         "en":"English" , "ar": "Arabic" , "bn": "Bengali" , "de": "German" , "en-in": "English India" , "en-au": "English Australia" , "en-gb": "English UK" , "gu": "Gujarati" , "hi": "Hindi" , "ja": "Japanese" , "ml": "Malayalam" , "mr": "Marathi" , "ne": "Nepali" , "nl": "Dutch" , "ru": "Russian" , "ta": "Tamil" , "te": "Telugu" , "ur": "Urdu"
#     }
#     for k ,v in dict.items():
#         if lan==v:
#             print(k)


# lancode("Hindi")
# with open ("C:\\Users\\avina\\OneDrive\\Desktop\\codes\\Python\\Assistance\\Assistence.json","r") as rw1:
#     js=json.load(rw1)
#     Friend=js["Names"]["FriendName"]
#     Friend="ssss"
#     # dictionary ={
#     # "name" : "sathiyajith",
#     # "rollno" : 56,
#     # "cgpa" : 8.6,
#     # "phonenumber" : "9976770500"
#     #     }
#     # json.dump(Friend,rw)
#     # print(js["Names"]["FriendName"])

# with open ("C:\\Users\\avina\\OneDrive\\Desktop\\codes\\Python\\Assistance\\Assistence.json","w") as rw:

#     Friend="ssss"
#     # dictionary ={
#     # "name" : "sathiyajith",
#     # "rollno" : 56,
#     # "cgpa" : 8.6,
#     # "phonenumber" : "9976770500"
#     #     }
#     json.dump(Friend,rw)
    # print(js["Names"]["FriendName"])


# def Translate(text,slan="en",dlan="en"):
#     trans = Translator()
#     tran = trans.translate(text, src=slan, dest=dlan)
#     return tran.text
# #     speak1(tran.text, lan)

# def speak(str):
#     print(str)
# def calltran():
#     while True:
#         speak("Which language do you want to translate")
#         sentence = "english to hindi"
#         if sentence != "none":
#             tran=sentence
#             speak("please check output box")
#             while True:
#                 speak("this is correct or not")
#                 sentence="yes"
#                 # filloutput(tran)
#                 if "yes" in sentence:
#                     str=tran.split("to")
#                     slan=None
#                     dlan=None
#                     li=[i for i in LANGUAGES.values()]
#                     for i in li:
        
#                         if i in str[0]:
#                             slan=i
#                         if i in str[1]:
#                             dlan=i
#                     if slan != None and dlan !=None:
#                         while True:
#                             speak("what you have to traslate")
#                             sentence="i am avinash"
#                             tran=sentence
#                             speak("please check output box")
#                             if sentence !="none":
#                                 while True:
#                                     speak("this is correct or not")
#                                     sentence="yes"
#                                     if "yes" in sentence:
#                                         out=Translate(tran,slan,dlan)
#                                         print(out)
#                                         # filloutput(out)
#                                         # speak("")
#                                         break
#                                     elif "not" in sentence or "no" in sentence:
#                                         speak("Please speak again")
#                                         speak("what you have to traslate")
#                                         sentence="i am avinash"
#                                         tran=sentence
#                                         speak("please check output box")
#                                 break
#                     else:
#                         speak("sir you have spoken wrong language")
#                         speak("please sir speak again")
#                     break
#                         # calltran() 
#                 elif "not" in sentence or "no" in sentence:
#                     speak("please sir speak again")

#                     break
                        

#                 elif "exit" in sentence or "i didnot want " in sentence or "i not want translation" in sentence or "i didn't want" in sentence:
#                     return
#             break
#         elif "exit" in sentence or "i didnot want " in sentence or "i not want translation" in sentence or "i didn't want" in sentence:
#             return 


# calltran()


# # print(LANGUAGES.values())
# li=[i for i in LANGUAGES.values()]
# # for i in LANGUAGES.values():
# str="i want translation hindi to english"
# str=str.split("to")
# print(str)
# for i in li:
#     if i in str[0] :
#         print(i)
#     if i in str[1] :
#         print(i)
# while 1:
#     if i==1:
#         print("if 1")
#         if i==1:
#             if 1:
#                 print("if2")
#                 break

# print(li)

# def sop(str):
#     mixer.init()
#     gtt=gTTS(text=str,lang="en",slow=False)
#     filename=f"{i}avn.mp3"
#     gtt.save(filename)
#     with open(filename) as paly:
#         print(paly)
#         mixer.music.load(paly)
#         mixer.music.play()


# while True:
#     pass
#     # sop("help")