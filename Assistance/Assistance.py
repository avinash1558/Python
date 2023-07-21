import time         
from tkinter import *
from gtts import gTTS
from playsound import playsound
from googletrans import Translator, LANGUAGES
from phonenumbers import carrier, timezone, geocoder
from pytube import YouTube, Playlist
import phonenumbers
from datetime import datetime
import pyttsx3
import speech_recognition as sp
import speedtest
import pyjokes
import pywhatkit
import webbrowser
import os
import json
import random
import smtplib
import re

def Jsonchange(mainname,subname,value):
    """
    for changing values in json file
    """
    jscode={}
    with open("C:\\Users\\avinash sharma\\Desktop\\codes\\Python\\Assistance\\Assistance.json","r") as r:
        jscode=json.load(r)

    jscode[mainname].update({subname:value})
    with open("C:\\Users\\avinash sharma\\Desktop\\codes\\Python\\Assistance\\Assistance.json","w") as w:
        json.dump(jscode,w,indent=10)

def Emailverifyer(emailid):
    """
    Verifying email id is correct or not
    """
    vrf = re.search(r"[a-zA-Z0-9]+@gmail.com", emailid)
    if (vrf == None):
        speak("This is invalid Email ID ")
        return "no"
    else:
        return "yes"

def H_jokes(index):
    """
    its provide hindi jokes by static method
    """
    li = ["पप्पू अपनी पत्नी से-  अच्छा ये बताओ 'बिदाई' के समय तुम  लड़कियां इतनी रोती क्यों हो?   पत्नी- 'पागल' अगर तुझे पता चले...  अपने घर से दूर ले जाकर कोई तुमसे  'बर्तन मंजवाएगा' तो तू  क्या    नाचेगा...", "बैंक की cashier ने खिड़की पर खड़े आदमी को कहा 'पैसे नहीं है'   ग्राहक: और दो मोदी माल्या को पैसा, सारे पैसे लेकर भाग गए विदेश में    कैशियर ने खिड़की में से हाथ निकाला और उसकी गर्दन दबोच कर कहा 'साले बैंक में तो है तेरे खाते में हीं है' भिखारी  ", "    जज : घर में मालिक होते हुए तूने चोरी कैसे की?    चोर : साहब, आपकी नौकरी अच्छी है, और सैलरी     भी अच्छी है, फिर आप ये सब सीख कर क्या करोगे?    ", " पब्लिक टॉयलेट में लिखा था    'दुनिया चांद पर पहुंच गयी और तू यहीं पर बैठा है'    पप्पू ने अपना दिमाग लगाया और नीचे लिखा    'चांद पर पानी नहीं था इसलिए वापस आ गया'    ", "    पति- प्यास लगी है पानी लेके आओ..    पत्नी- क्यों ना आज तुम्हें मटर पनीर     और शाही पुलाव बनाकर लाऊं...    पति- वाह वाह...!    मुंह में पानी आ गया..    पत्नी- आ गया ना मुंह में पानी   बस इसी से काम चला लो..    ", "  टीचर- टिटू बताओ..   अकबर ने कब तक शासन किया था ?   टिटू- सर जी..   पेज नंबर 14 से लेकर पेज नंबर 22 तक..।    ", "    गोलू- जानू, तुम दिन पर दिन    खूबसूरत होती जा रही हो...    पत्नी (खुश होकर)- तुमने कैसे जाना ?    गोलू- तुम्हें देखकर...    रोटियां भी जलने लगी हैं   ", "टिल्लू (लड़की से)- मैं 18 साल का हूं   और तुम ?    लड़की- मैं भी 18 साल की हूं...   टिल्लू- तो फिर चलो ना, इसमें शरमाना क्या..    लड़की- कहां ?    टिल्लू- अरे पगली..    वोट देने और कहां..", "    मां- बेटा क्या कर रहे हो    पप्पू- पढ़ रहा हूं मां..    - शाबास! बेटा क्या पढ़ रहे हो..?    पप्पू- आपकी होने वाली बहु के SMS", "    टीचर- बच्चों कोई ऐसा वाक्य सुनाओ     जिसमें हिंदी, पंजाबी, उर्दू और अंग्रेजी का प्रयोग हो..    पप्पू- सर ..    'इश्क दी गली विच ल No entry'", "    पत्नी- पूजा किया कीजिए,    बड़ी बलांए टल जाती हैं...    टिटू- हां... तुम्हारे    पिताजी ने बहुत की होगी     उनकी टल गई और मेरे पल्ले पड़ गई..।", "  जिस तरह अच्छी हवा, अच्छा   खानपान किसी भी इंसान के सेहतमंद रहने के लिए जरूरी होता है, उसी   प्रकार आपकी हंसी भी आपको स्वस्थ रखने में अहम भूमिका निभाती है। अगर   आप सुबह-शाम हंसने की आदत डाल लें तो कोई भी बीमारी, चाहे मानसिक हो या  शारीरिक आपके पास भी नहीं आएगी। इसीलिए हम आपके लिए कुछ ऐसे मजेदार  चुटकुले लेकर आए हैं, जिन्हें पढ़ने के बाद आप हंसते-हंसते लोटपोट हो    जाएंगे। तो चलिए शुरू करते हैं हंसने-हंसाने का ये सिलसिला...", "पापा- तेरा रिजल्ट आ गया, पास हुआ या फेल?    चिंटू- प्रिंसिपल का बेटा फेल हो गया    पापा- तुम?    चिंटू- मेजर साहब का बेटा भी फेल हो गया     पापा- और तुम?    चिंटू- डॉक्टर साहब का बेटा भी फेल हो गया   पापा गुस्से से- बेवकूफ, मैं तुमसे पूछ रहा हूं तुम्हारे रिजल्ट का क्या हुआ?   चिंटू -तो आप कौन से प्रधानमंत्री हो जो आपका बेटा पास हो जाएगा..."]
    joketext=Translate(li[index],"hi","en")
    filloutput(joketext)
    return joketext

def Randomalphabet():
    """
    give random alphabet which use for speak function
    """
    wordli = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s","d", "f", "g", "h", "j", "k", "l","z", "x", "c", "v", "b", "n", "m"]
    randomalphabet = random.choice(wordli)
    return randomalphabet

def speak(str, speed=False):
    """
    its take string and speak that string
    """
    lancode=Jsondata("Language","support")
    lang=lancode
    transtr=Translate(str,"en",lancode)
    gtt = gTTS(text=transtr, lang=lang, slow=speed)
    filename = f"{Randomalphabet()}avn.mp3"
    gtt.save(filename)
    playsound(filename)
    os.remove(filename)
    time.sleep(0.5)

def Jsondata(mainname,subname):
    """
    is give language code from json file
    """
    jscode={}
    with open("C:\\Users\\avinash sharma\\Desktop\\codes\\Python\\Assistance\\Assistance.json","r") as r:
        jscode=json.load(r)
        return jscode[mainname][subname]
    
def Listening():
    """
    take voice as a input and give string
    """
    recgnizeword = ""
    r = sp.Recognizer()
    lancode=Jsondata("Language","support")
    with sp.Microphone() as source:
        r.energy_threshold = 200
        taptext.set(Translate("Listening....","en",lancode))
        taptospeak.update()
        speak("Speak Please...")
        audio = r.listen(source)
    try:
        lis_word = r.recognize_google(audio, language='en-in')
        recgnizeword = lis_word.lower()
        showtext = f"Your Query : {recgnizeword}"
    except Exception as e:
        showtext = "You didn't say anything"
        speak("You didnot say anything")
        recgnizeword = "none"
    taptext.set(Translate("Tap to speak....","en",lancode))
    taptospeak.update()
    filloutput(showtext)
    return recgnizeword

def filloutput(txt):
    """
    fill text in to output box
    """
    lan=Jsondata("Language","support")
    text=Translate(txt,"en",lan)
    outputShow.config(state="normal")
    outputShow.delete(1.0, END)
    outputShow.insert(END, text)
    outputShow.config(state="disabled")
    outputShow.update()

def lancode(lan):
    """
    its take langauges and the give language code
    """
    lans=lan.lower()
    dict={
        "en":"english" , "ar": "arabic" , "bn": "bengali" , "de": "german" , "en-in": "english india" , "en-au": "english australia" , "en-gb": "english uk" , "gu": "gujarati" , "hi": "hindi" , "ja": "japanese" , "ml": "malayalam" , "mr": "marathi" , "ne": "nepali" , "nl": "dutch" , "ru": "russian" , "ta": "tamil" , "te": "telugu" , "ur": "urdu"
    }
    for k ,v in dict.items():
        if lans==v:
            return k
    else:
        return -1    
    
def Changelanguageinjson():
    """
    its change language of assistance
    """
    speak("is support the following languages")
    speak("English , Arabic , Bengali , German ,English India , English Australia , English UK , Gujarati , Hindi , Japanese , Malayalam , Marathi , Nepali , Dutch , Russian ,Tamil, Telugu , Urdu")
    filloutput("English , Arabic , Bengali , German ,English India , English Australia , English UK , Gujarati , Hindi , Japanese , Malayalam , Marathi , Nepali , Dutch , Russian ,Tamil, Telugu , Urdu")
    lancode=Jsondata("Language","support")
    elsec1=Translate("exit","en",lancode)
    elsec2=Translate("i do not want","en",lancode)
    elsec3=Translate("do not want","en",lancode)
    elsec4=Translate("i can not","en",lancode)
    elsec5=Translate("not want","en",lancode)
    while True:
        speak("which of these languages to change")
        sentence=Listening()
        time.sleep(0.5)
        if sentence == "none":
            filloutput("English , Arabic , Bengali , German ,English India , English Australia , English UK , Gujarati , Hindi , Japanese , Malayalam , Marathi , Nepali , Dutch , Russian ,Tamil, Telugu , Urdu")
        if sentence != "none":
            texts=sentence
            li = ["English" , "Arabic" , "Bengali" , "German" ,"English India" , "English Australia" , "English UK" , "Gujarati" , "Hindi" , "Japanese" , "Malayalam" , "Marathi" , "Nepali" , "Dutch" , "Russian" ,"Tamil", "Telugu" , "Urdu"]
            lilower=[i.lower() for i in li]
            slan = None
            for i in lilower:
                if i in texts:
                    slan = i
            if slan != None:
                lanscode=lancode(slan)
                if lanscode==-1:
                    speak("this language is not supported")
                if lanscode != -1:
                    filloutput("Changing...../")
                    time.sleep(0.5)
                    filloutput("Changing..........|")
                    time.sleep(0.5)
                    Jsonchange("Language","support",lanscode)
                    filloutput("Done....")
                    break
            elif elsec1 in sentence or elsec2 in sentence or elsec3 in sentence or elsec4 in sentence or elsec5 in sentence:
                break
            else:
                speak("this language is not supported")

def Welcome():
    """
    its wish Good morning Good afternoon Good evening
    """
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
    """
    is use to send mail
    """
    with open("C:\\Users\\avinash sharma\\Desktop\\codes\\Python\\Assistance\\Assistance.json", "r") as read:
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

def Opensite(site):
    """
    it use open website
    """
    webbrowser.open(site)

def E_Jokes(j_lan="en"):
    '''
        its give jokes dynamicly
        category: str
        Choices: 'neutral', 'chuck', 'all', 'twister'
        lang: str
        Choices: 'en', 'de', 'es', 'gl', 'eu', 'it'
    '''
    if j_lan == "en":
        MyJoke = pyjokes.get_joke(language=j_lan, category="all")
        filloutput(MyJoke)
        return MyJoke

def Translate(text, slan="en", dlan="en"):
    """
    it is translate text in slan to dlan
    """
    trans = Translator()
    tran = trans.translate(text, src=slan, dest=dlan)
    return tran.text

def Collingtranslate():
    """
    its use to call translate function
    """
    lan=Jsondata("Language","support")
    ec3=Translate("exit","en",lan)
    ec4=Translate("did not want","en",lan)
    ec5=Translate("do not want","en",lan)
    ec6=Translate("not want","en",lan)
    checktext=Translate("yes","en",lan)
    checktexty=Translate("correct","en",lan)
    checktext1=Translate("not","en",lan)
    checktext2=Translate("no","en",lan)
    while True:
        speak("Which language do you want to translate")
        sentence =Translate(Listening(),lan,"en")
        speak("please check output box")
        tran = sentence
        if sentence !="none":
            while True: 
                speak("this is correct or not")
                sentence = Listening()
                if checktext in sentence or checktexty in sentence:
                    str = tran.split("to")
                    lanli = [i for i in LANGUAGES.values()]
                    li=[i.lower() for i in lanli]
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
                                    if checktext in sentence or checktexty in sentence:
                                        out = Translate(tran, slan, dlan)
                                        filloutput(out)
                                        # speak(f"{tran} to {out}")
                                        break
                                    elif checktext1 in sentence or checktext2 in sentence:
                                        speak("Please speak again")
                                        speak("what you have to traslate")
                                        sentence = Listening()
                                        tran = sentence
                                        speak("please check output box")
                                break
                    else:
                        speak("sir you have spoken wrong language")
                        speak("please sir speak again")
                        Collingtranslate()
                    break

                elif checktext1 in sentence or checktext2 in sentence:
                    speak("please sir speak again")
                    Collingtranslate()
                elif ec3 in sentence or ec4 in sentence or ec5 in sentence or ec6 in sentence:
                    return
            break

def breakmain():
    """
    break main loop
    """
    pass

def opencalcultor():
    pass

def Mainloop():
    """
    it is main loop of program
    """
    os.system("cls")
    t = 1
    speak("What is your query")
    sentence = Listening()
    lan=Jsondata("Language","support")
    check1=Translate("open google","en",lan)
    check2=Translate("search on google","en",lan)
    check3=Translate("yes","en",lan)
    check4=Translate("no","en",lan)
    check5=Translate("not","en",lan)
    check6=Translate("what is the time","en",lan)
    check7=Translate("today time","en",lan)
    check8=Translate("i want translation","en",lan)
    check8t=Translate("translation","en",lan)
    check9=Translate("open website","en",lan)
    check10=Translate("open site","en",lan)
    check11=Translate("translate","en",lan)
    check12=Translate("joke","en",lan)
    check13=Translate("i want joke","en",lan)
    check14=Translate("tell joke","en",lan)
    check15=Translate("say joke","en",lan)
    check16=Translate("send email","en",lan)
    check17=Translate("send mail","en",lan)
    c1=Translate("by","en",lan)
    c2=Translate("bye","en",lan)
    c3=Translate("stop","en",lan)
    check12e=Translate("joke","en",lan)
    check13e=Translate("i want joke","en",lan)
    check14e=Translate("tell joke","en",lan)
    check15e=Translate("say joke","en",lan)

    ec3=Translate("exit","en",lan)
    ec4=Translate("do not want","en",lan)
    ec5=Translate("not want to send mail","en",lan)
    ec6=Translate("did not want","en",lan)
    ec7=Translate("not want","en",lan)
    ec8=Translate("didnot want","en",lan)
                   

    if t == 2:
        pass

    elif check1 in sentence:
        Btn.config(command=breakmain)
        Btn.update()
        speak("I am opening google ")
        filloutput("Openinng...../")
        time.sleep(1)
        filloutput("Openinng..........|")
        time.sleep(0.5)
        webbrowser.open("https://www.google.co.in")
        filloutput("Done....")
        Btn.config(command=Mainloop)
        Btn.update()
    elif check2 in sentence:
        Btn.config(command=breakmain)
        Btn.update()
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
                    if check3 in sentence:
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

                    elif ec3 in sentence or ec4 in sentence or ec5 in sentence or ec6 in sentence or ec7 in sentence or ec8 in sentence:
                        break
                    elif check4 in sentence or check5 in sentence:
                        speak("Say again")
                        break
                break
        Btn.config(command=Mainloop)
        Btn.update()

    elif check8 in sentence or check8 in sentence or check11 in sentence:
        Btn.config(command=breakmain)
        Btn.update()
        Collingtranslate()
        Btn.config(command=Mainloop)
        Btn.update()
        
        

    elif check6 in sentence or check7 in sentence:
        Btn.config(command=breakmain)
        Btn.update()
        timing = datetime.now().strftime("%I : %M : %S  %p")
        filloutput(f"Today Time :- {timing}")
        speak(f"Today Time :- {timing}")
        Btn.config(command=Mainloop)
        Btn.update()
        
        

    elif check9 in sentence or check10 in sentence:
        Btn.config(command=breakmain)
        Btn.update()
        while True:
            speak("what you have to open")
            sentence = Listening()
            Translate(sentence,lan,"en")
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
        Btn.config(command=Mainloop)
        Btn.update()

    elif check12 in sentence or check13 in sentence or check14 in sentence or check15 in sentence:
        Btn.config(command=breakmain)
        Btn.update()
        speak1(H_jokes(random_index))
        Btn.config(command=Mainloop)
        Btn.update()
    elif check12e in sentence or check13e in sentence or check14e in sentence or check15e in sentence:
        Btn.config(command=breakmain)
        Btn.update()
        speak(E_Jokes())
        Btn.config(command=Mainloop)
        Btn.update()
    elif check16 in sentence or check17 in sentence:
        Btn.config(command=breakmain)
        Btn.update()
        btn.config(command=getinput)
        if check3 in sentence:
            speak("input   email  id  by  using  inputbox,  to whom  you  to  send  mail")
        Btn.config(command=Mainloop)
        Btn.update()
    elif ec3 in sentence or c1 in sentence or c2 in sentence or c3 in sentence:
        exit(0)
    else:
        Btn.config(command=breakmain)
        Btn.update()
        speak("Sorry sir   i  didnot  understand ")
        speak(" please  click the  mic and speak again")
        Btn.config(command=Mainloop)
        Btn.update()

def mailsubject():
    intv = InputValue.get()
    if len(intv)>3:
        Jsonchange("Mail","Subject",intv)
        btn.config(command=mailbody)
        btn.update()
        speak("use input box to give main body and press arrow button")

def mailbody():
    intv = InputValue.get()
    if len(intv)>3:
        subject=Jsondata("Mail","Subject")
        mailid=Jsondata("Mail","SenderID")
        btn.config(command=breakmain)
        btn.update()
        filloutput("Sending...../")
        time.sleep(0.5)
        filloutput("Sending..........|")
        time.sleep(0.5)
        Mail(subject, intv,mailid)
        filloutput("Done....")
        speak("Yes sir Mail is sended")

def getinput():
    """
    it is use for giving data to mail function
    """
    btn.config(command=breakmain)
    btn.update()
    lan=Jsondata("Language","support")
    ec3=Translate("exit","en",lan)
    ec4=Translate("did not want","en",lan)
    ec5=Translate("do not want","en",lan)
    ec6=Translate("not want","en",lan)
    ec7=Translate("didnot send mail","en",lan)
    ec8=Translate("didnot send email","en",lan)
    ec9=Translate("did not send mail","en",lan)
    ec10=Translate("did not send email","en",lan)
    checktext=Translate("yes","en",lan)
    checktexty=Translate("correct","en",lan)
    checktext1=Translate("not","en",lan)
    checktext2=Translate("no","en",lan)
    check12=Translate("writ","en",lan)
    check11=Translate("first","en",lan)
    check21=Translate("speak","en",lan)
    check22=Translate("second","en",lan)
    intv = InputValue.get()
    InputValue.set("")
    outputShow.delete(1.0, END)
    outputShow.insert(END, intv)
    speak("Please check this email id is correct")
    while 1:
        speak("yes or not")
        sentence = Listening()
        if checktext in sentence or checktexty in sentence:
            var = Emailverifyer(intv)
            if var == "yes":
                while True:
                    speak("you want to write option or speak option")
                    sentence=Listening()
                    if sentence!="none":
                        if check11 in sentence or check12 in sentence:
                            speak("use input box to give subject and press arrow button")
                            Jsonchange("Mail","SenderID",intv)
                            btn.config(command=mailsubject)
                            btn.update() 
                            break   

                        elif check21 in sentence or check22 in sentence:
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
                            Mail(sub, mes,intv)
                            break
                break
            elif var == "no":
                speak(
                    "input   email  id  by  using  inputbox,  to whom  you  to  send  mail")
                break
        elif ec3 in sentence or ec4 in sentence or ec5 in sentence or ec6 in sentence or ec7 in sentence or ec8 in sentence or ec9 in sentence or ec10 in sentence:
            break
        elif checktext1 in sentence or checktext2 in sentence:
            break


if __name__ == "__main__":

    os.system("cls")
    random_index = random.randint(0, 12)
    Bg = "#c6c4c4"

    with open("C:\\Users\\avinash sharma\\Desktop\\codes\\Python\\Assistance\\Assistance.json", "r") as read:
        js = json.load(read)
        Name = js["Names"]
        D_name = Name["DeviceName"]

    root = Tk()

    taptext = StringVar()
    taptext.set("Tap to speak....")
    root.config(bg=Bg)
    root.geometry("450x600")
    root.title("Assistance...")
    root.iconbitmap(
        "C:\\Users\\avinash sharma\\Desktop\\codes\\Python\\Assistance\\juk.ico")
    BtnImg1 = PhotoImage(
        file="C:\\Users\\avinash sharma\\Desktop\\codes\\Python\\Assistance\\mic.png")
    BtnImg2 = PhotoImage(
        file="C:\\Users\\avinash sharma\\Desktop\\codes\\Python\\Assistance\\mic2.png")

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
