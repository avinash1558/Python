# pip install gtts, pywhatkit , SpeechRecognition,pyttsx3 , phonenumbers,wikipedia ,pywhatkit,pytube
# pip install googletrans==4.0.0rc1,pygame
# pip install speedtest-cli,pyjokes
# datetime, webbrowser, os, smtplib,json,time,re

from tkinter import *
from datetime import datetime
from gtts import gTTS
from playsound import playsound
from googletrans import Translator, LANGUAGES
from phonenumbers import carrier, timezone, geocoder
from pytube import YouTube, Playlist
import os
import json
import random
import time
import phonenumbers
import pyttsx3
import speech_recognition as sp
import smtplib
import pyjokes
import speedtest
import pywhatkit
import re
import webbrowser

def jsonchange(cla,change,value):
    jscode={}
    # print(type(jscode))
    with open("C:\\Users\\avina\\OneDrive\\Desktop\\codes\\Python\\Assistance\\Assistance.json","r") as r:
        jscode=json.load(r)

    jscode[cla].update({change:value})
    with open("C:\\Users\\avina\\OneDrive\\Desktop\\codes\\Python\\Assistance\\Assistance.json","w") as w:
        json.dump(jscode,w,indent=10)

def emailVerifyer(email):
    vrf = re.search(r"[a-zA-Z0-9]+@gmail.com", email)
    if (vrf == None):
        speak("This is invalid Email ID ")
        return "no"
    else:
        return "yes"

def H_jokes(index):
    li = ["पप्पू अपनी पत्नी से-  अच्छा ये बताओ 'बिदाई' के समय तुम  लड़कियां इतनी रोती क्यों हो?   पत्नी- 'पागल' अगर तुझे पता चले...  अपने घर से दूर ले जाकर कोई तुमसे  'बर्तन मंजवाएगा' तो तू  क्या    नाचेगा...", "बैंक की cashier ने खिड़की पर खड़े आदमी को कहा 'पैसे नहीं है'   ग्राहक: और दो मोदी माल्या को पैसा, सारे पैसे लेकर भाग गए विदेश में    कैशियर ने खिड़की में से हाथ निकाला और उसकी गर्दन दबोच कर कहा 'साले बैंक में तो है तेरे खाते में हीं है' भिखारी  ", "    जज : घर में मालिक होते हुए तूने चोरी कैसे की?    चोर : साहब, आपकी नौकरी अच्छी है, और सैलरी     भी अच्छी है, फिर आप ये सब सीख कर क्या करोगे?    ", " पब्लिक टॉयलेट में लिखा था    'दुनिया चांद पर पहुंच गयी और तू यहीं पर बैठा है'    पप्पू ने अपना दिमाग लगाया और नीचे लिखा    'चांद पर पानी नहीं था इसलिए वापस आ गया'    ", "    पति- प्यास लगी है पानी लेके आओ..    पत्नी- क्यों ना आज तुम्हें मटर पनीर     और शाही पुलाव बनाकर लाऊं...    पति- वाह वाह...!    मुंह में पानी आ गया..    पत्नी- आ गया ना मुंह में पानी   बस इसी से काम चला लो..    ", "  टीचर- टिटू बताओ..   अकबर ने कब तक शासन किया था ?   टिटू- सर जी..   पेज नंबर 14 से लेकर पेज नंबर 22 तक..।    ", "    गोलू- जानू, तुम दिन पर दिन    खूबसूरत होती जा रही हो...    पत्नी (खुश होकर)- तुमने कैसे जाना ?    गोलू- तुम्हें देखकर...    रोटियां भी जलने लगी हैं   ", "टिल्लू (लड़की से)- मैं 18 साल का हूं   और तुम ?    लड़की- मैं भी 18 साल की हूं...   टिल्लू- तो फिर चलो ना, इसमें शरमाना क्या..    लड़की- कहां ?    टिल्लू- अरे पगली..    वोट देने और कहां..", "    मां- बेटा क्या कर रहे हो    पप्पू- पढ़ रहा हूं मां..    - शाबास! बेटा क्या पढ़ रहे हो..?    पप्पू- आपकी होने वाली बहु के SMS", "    टीचर- बच्चों कोई ऐसा वाक्य सुनाओ     जिसमें हिंदी, पंजाबी, उर्दू और अंग्रेजी का प्रयोग हो..    पप्पू- सर ..    'इश्क दी गली विच ल No entry'", "    पत्नी- पूजा किया कीजिए,    बड़ी बलांए टल जाती हैं...    टिटू- हां... तुम्हारे    पिताजी ने बहुत की होगी     उनकी टल गई और मेरे पल्ले पड़ गई..।", "  जिस तरह अच्छी हवा, अच्छा   खानपान किसी भी इंसान के सेहतमंद रहने के लिए जरूरी होता है, उसी   प्रकार आपकी हंसी भी आपको स्वस्थ रखने में अहम भूमिका निभाती है। अगर   आप सुबह-शाम हंसने की आदत डाल लें तो कोई भी बीमारी, चाहे मानसिक हो या  शारीरिक आपके पास भी नहीं आएगी। इसीलिए हम आपके लिए कुछ ऐसे मजेदार  चुटकुले लेकर आए हैं, जिन्हें पढ़ने के बाद आप हंसते-हंसते लोटपोट हो    जाएंगे। तो चलिए शुरू करते हैं हंसने-हंसाने का ये सिलसिला...",
          "पापा- तेरा रिजल्ट आ गया, पास हुआ या फेल?    चिंटू- प्रिंसिपल का बेटा फेल हो गया    पापा- तुम?    चिंटू- मेजर साहब का बेटा भी फेल हो गया     पापा- और तुम?    चिंटू- डॉक्टर साहब का बेटा भी फेल हो गया   पापा गुस्से से- बेवकूफ, मैं तुमसे पूछ रहा हूं तुम्हारे रिजल्ट का क्या हुआ?   चिंटू -तो आप कौन से प्रधानमंत्री हो जो आपका बेटा पास हो जाएगा..."]
    filloutput(li[index])
    return li[index]

def random_word():
    wordli = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s",
              "d", "f", "g", "h", "j", "k", "lz", "x", "c", "v", "b", "n", "m"]
    random_word = random.choice(wordli)
    return random_word

def lanreturning(sreq,req):
    jscode={}
    # print(type(jscode))
    with open("C:\\Users\\avina\\OneDrive\\Desktop\\codes\\Python\\Assistance\\Assistance.json","r") as r:
        jscode=json.load(r)
        return jscode[sreq][req]
    

def Listening():
    r_word = ""
    r = sp.Recognizer()
    with sp.Microphone() as source:
        r.energy_threshold = 200
        lan=lanreturning("Language","support")
        taptext.set(Translate("Listening....","en",lan))
        taptospeak.update()
        speak(Translate("Speak Please...","en",lan))
        audio = r.listen(source, 60)
    try:
        lis_word = r.recognize_google(audio, language='en-in')
        showtext = f"Your Query :{lis_word}"
        r_word = lis_word.lower()
    except Exception as e:
        showtext = f"You didn't say anything"
        speak(Translate("You didnot say anything","en",lan))

        r_word = "none"
    taptext.set("Tap to speak....")
    taptospeak.update()
    filloutput(showtext)

    return r_word


def filloutput(text):
    outputShow.config(state="normal")
    outputShow.delete(1.0, END)
    outputShow.insert(END, text)
    outputShow.config(state="disabled")
    outputShow.update()

def lancode(lan):
    dict={
        "en":"English" , "ar": "Arabic" , "bn": "Bengali" , "de": "German" , "en-in": "English India" , "en-au": "English Australia" , "en-gb": "English UK" , "gu": "Gujarati" , "hi": "Hindi" , "ja": "Japanese" , "ml": "Malayalam" , "mr": "Marathi" , "ne": "Nepali" , "nl": "Dutch" , "ru": "Russian" , "ta": "Tamil" , "te": "Telugu" , "ur": "Urdu"
    }
    for k ,v in dict.items():
        if lan==v:
            return k
    else:
        return -1    
    
def changelan():
    speak("i have to support following languages")
    speak("English , Arabic , Bengali , German ,English India , English Australia , English UK , Gujarati , Hindi , Japanese , Malayalam , Marathi , Nepali , Dutch , Russian ,Tamil, Telugu , Urdu")
    filloutput("English , Arabic , Bengali , German ,English India , English Australia , English UK , Gujarati , Hindi , Japanese , Malayalam , Marathi , Nepali , Dutch , Russian ,Tamil, Telugu , Urdu")
    while True:
        speak("tell which language you want to change from output box")
        sentence=Listening()
        time.sleep(0.5)
        if sentence == "none":
            filloutput("English , Arabic , Bengali , German ,English India , English Australia , English UK , Gujarati , Hindi , Japanese , Malayalam , Marathi , Nepali , Dutch , Russian ,Tamil, Telugu , Urdu")
        if sentence != "none":
            texts=sentence
            li = [i for i in LANGUAGES.values()]
            slan = None
            for i in li:
                if i in texts:
                    slan = i
            if slan != None:
                lanscode=lancode(slan)
                if lanscode==-1:
                    speak("that language is not supported")
                elif lanscode != -1:
                    jsonchange("Language","support",lanscode)
            break







def speak(str, lang="en", speed=False):
    gtt = gTTS(text=str, lang=lang, slow=speed)
    filename = f"{random_word()}avn.mp3"
    gtt.save(filename)
    playsound(filename)
    os.remove(filename)
    time.sleep(0.5)


def Welcome():
    hours = datetime.datetime.now().hour
    if hours >= 6 and hours <= 12:
        return "Good morning"
    elif hours >= 12 and hours <= 17:
        return "Good afternoon"
    elif hours >= 17 and hours <= 19:
        return "Good evening"
    else:
        return "hello"


def Mail(subject, body, to):
    with open("C:\\Users\\avina\\OneDrive\\Desktop\\codes\\Python\\Assistance\\Assistance.json", "r") as read:
        js = json.load(read)
        Mail = js["Mail"]
        Emailid = Mail["Emailid"]
        Emailpassword = Mail["Emailpassword"]
        smtps = Mail["smtp"]
        smtphost = Mail["smtphost"]
    server = smtplib.SMTP(smtps, smtphost)
    server.starttls()
    server.login(Emailid, Emailpassword)
    message = f"Subject : {subject}\n\n{body}"
    server.sendmail(Emailid, to, message)
    print("avian")


def Opensite(site):
    webbrowser.open(site)


def E_Jokes(j_lan="en"):
    '''
        category: str
        Choices: 'neutral', 'chuck', 'all', 'twister'
        lang: str
        Choices: 'en', 'de', 'es', 'gl', 'eu', 'it'
    '''
    if j_lan == "en":
        MyJoke = pyjokes.get_joke(language=j_lan, category="all")
        filloutput(MyJoke)
        return MyJoke


def calltran():
    while True:
        speak("Which language do you want to translate")
        sentence = Listening()
        if sentence != "none":
            tran = sentence
            speak("please check output box")
            while True:
                speak("this is correct or not")
                sentence = Listening()
                filloutput(tran)
                if "yes" in sentence:
                    str = tran.split("to")
                    li = [i for i in LANGUAGES.values()]
                    slan = None
                    dlan = None
                    for i in li:
                        if i in str[0]:
                            slan = i
                        if i in str[1]:
                            dlan = i
                    if slan != None and dlan != None:
                        while True:
                            speak("what you have to traslate")
                            sentence = Listening()
                            tran = sentence
                            if sentence != "none":
                                speak("please check output box")
                                while True:
                                    speak("this is correct or not")
                                    sentence = Listening()
                                    if "yes" in sentence:
                                        out = Translate(tran, slan, dlan)
                                        filloutput(out)
                                        # speak("")
                                        break
                                    elif "not" in sentence or "no" in sentence:
                                        speak("Please speak again")
                                        speak("what you have to traslate")
                                        sentence = Listening()
                                        tran = sentence
                                        speak("please check output box")
                                break
                    else:
                        speak("sir you have spoken wrong language")
                        speak("please sir speak again")
                        calltran()
                    break
                elif "not" in sentence or "no" in sentence:
                    speak("please sir speak again")
                    calltran()

                elif "exit" in sentence or "i didnot want " in sentence or "i not want translation" in sentence or "i didn't want" in sentence:
                    return

            break
        elif "exit" in sentence or "i didnot want " in sentence or "i not want translation" in sentence or "i didn't want" in sentence:
            return


def Translate(text, slan="en", dlan="en"):
    trans = Translator()
    tran = trans.translate(text, src=slan, dest=dlan)
    return tran.text



def Mainloop():
    os.system("cls")
    t = 1
    speak("What is your query")
    sentence = Listening()
    sentence = Translate(sentence)
    if t == 2:
        pass
    elif "open google" in sentence:
        speak("I am opening google ")
        filloutput("Openinng...../")
        time.sleep(0.5)
        filloutput("Openinng..........|")
        time.sleep(0.5)
        webbrowser.open("https://www.google.co.in")
        filloutput("Done....")
    elif "search on google" in sentence:
        while True:
            speak("only tell me thing ,which you have to search")
            sentence = Listening()
            search = sentence
            if sentence != "none":
                speak("check output box")
                speak("this thing you have to search")
                while True:
                    speak("yes or not")
                    sentence = Listening()
                    if "yes" in sentence:
                        speak(f"i am searching {search} on google")
                        filloutput("Searching..../")
                        time.sleep(0.5)
                        filloutput("Searching...........|")
                        time.sleep(0.5)
                        filloutput("Done...")
                        pywhatkit.search(search)
                        speak1 = pywhatkit.info(
                            search, lines=2, return_value=True)
                        speak("according to first website")
                        speak(speak1)
                        filloutput(speak1)
                        break

                    elif "exit" in sentence or "not want to send email" in sentence or "not want to send mail" in sentence or "didnt send mail" in sentence or "didnt send email" in sentence or "didn't send email" in sentence or "didn't send mail" in sentence or "didnot send email" in sentence or "didnot send mail" in sentence:
                        break
                    if "not" in sentence or "no" in sentence:
                        speak("Say again")
                        break
                break

    elif "i want translation" in sentence:
        calltran()

    elif "what is the time" in sentence or "today time" in sentence:
        time = datetime.now().strftime("%I : %M : %S  %p")
        filloutput(f"Today Time :- {time}")
        speak(f"Today Time :- {time}")

    elif "open website" in sentence or "open site" in sentence:
        while True:
            speak("what you have to open")
            sentence = Listening()
            if sentence != "none":
                if ".com" in sentence:
                    if " " in sentence:
                        sentence.replace(" ", "")
                        filloutput("Openinng...../")
                        time.sleep(0.5)
                        filloutput("Openinng..........|")
                        time.sleep(0.5)
                        filloutput("Done....")
                        Opensite(sentence)
                else:
                    sentence.replace(" ", "")
                    Opensite(f"{sentence}.com")
                break

    elif "joke in hindi" in sentence or "jokes in hindi" in sentence:
        speak1(H_jokes(random_index))
    elif "joke in english" in sentence or "jokes in english" in sentence or "joke" in sentence or "i want to hear the joke" in sentence:
        speak(E_Jokes())

    elif "send email" in sentence or "send mail" in sentence:
        btn.config(command=getinput)
        while True:
            speak("Sir   you   have   to   send   mail")
            speak("you   want   or  not")
            sentence = Listening()
            if "yes" in sentence:
                speak(
                    "input   email  id  by  using  inputbox,  to whom  you  to  send  mail")
                break
            elif "no" in sentence:
                break
    elif "bye" in sentence or "exit" in sentence or "by" in sentence:
        exit(0)
    else:
        speak("Sorry sir   i  didnot  understand \n please  click the  mic and speak again")


def getinput():
    if (n == 1):
        intv = InputValue.get()
        InputValue.set("")
        outputShow.delete(1.0, END)
        outputShow.insert(END, intv)
        speak("Please check this email id is correct")
        while 1:
            speak("yes or not")
            sentence = Listening()
            if "yes" in sentence:
                var = emailVerifyer(intv)
                if var == "yes":
                    speak("tell  me  the  subject  first")
                    sub = Listening()
                    speak("and now tell  me  the  message , which you want to send")
                    mes = Listening()
                    speak("Yes sir Mail is sending")
                    filloutput("Sending...../")
                    time.sleep(0.5)
                    filloutput("Sending..........|")
                    time.sleep(0.5)
                    filloutput("Done....")

                    Mail(sub, mes, intv)
                    break
                elif var == "no":
                    speak(
                        "input   email  id  by  using  inputbox,  to whom  you  to  send  mail")
                    break
            elif "exit" in sentence or "not want to send email" in sentence or "not want to send mail" in sentence or "didnt send mail" in sentence or "didnt send email" in sentence or "didn't send email" in sentence or "didn't send mail" in sentence or "didnot send email" in sentence or "didnot send mail" in sentence:
                break
            elif "no" in sentence:
                break


if __name__ == "__main__":

    os.system("cls")
    random_index = random.randint(0, 12)
    Bg = "#c6c4c4"

    with open("C:\\Users\\avina\\OneDrive\\Desktop\\codes\\Python\\Assistance\\Assistance.json", "r") as read:
        js = json.load(read)
        Name = js["Names"]
        D_name = Name["DeviceName"]

    root = Tk()

    taptext = StringVar()
    taptext.set("Tap to speak....")
    root.config(bg=Bg)
    root.geometry("450x600")
    root.title("Assistence...")
    root.iconbitmap(
        "C:\\Users\\avina\\OneDrive\\Desktop\\codes\\Python\\Assistance\\juk.ico")
    BtnImg1 = PhotoImage(
        file="C:\\Users\\avina\\OneDrive\\Desktop\\codes\\Python\\Assistance\\mic.png")
    BtnImg2 = PhotoImage(
        file="C:\\Users\\avina\\OneDrive\\Desktop\\codes\\Python\\Assistance\\mic2.png")

    Label(root, bg=Bg).pack(pady=9)

    Btn = Button(image=BtnImg1, bg=Bg, borderwidth=0, width=122,
                 height=122, anchor="s", command=Mainloop)
    Btn.pack(padx=165, pady=10)

    btn = Button(text="⇉", borderwidth=0, width=5, height=2)
    btn.place(x=400, y=210)

    taptospeak = Label(textvariable=taptext, bg=Bg, font="Helvetica 12 bold")
    taptospeak.pack()

    # InputValue.set()
    Label(root, bg=Bg).pack(pady=10)
    inputLable = Label(root, text="Input :-", bg=Bg,
                       font="Helvetica 20 bold", anchor="w", width=35, padx=6)
    inputLable.pack()
    InputValue = StringVar()

    inputEntry = Entry(root, textvariable=InputValue, width=39,
                       font="Helvetica 15 bold", fg="#e60909")
    inputEntry.pack()

    outputLabel = Label(root, text="Output :-", bg=Bg,
                        font="Helvetica 20 bold", anchor="w", width=45, padx=6, pady=10)
    outputLabel.pack()

    outputShow = Text(root, wrap=WORD, font="Helvetica 15 bold",
                      state="disabled", width=38, padx=6, height=9, fg="#00ff29")
    outputShow.pack()
    root.mainloop()
