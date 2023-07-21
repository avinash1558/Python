"""
C:\\Windows\\notepad.exe
C:\Users\avina\Downloads
C:\Users\avina\Music
C:\Program Files\Google\Chrome\Application\chrome.exe
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chrome.exe

"""




{
    "Names":{
        "DeviceName":"Assistence",
        "MyName":"Avinash",
        "FriendName":"I"
    },
    "Mail":{
        "smtp":"smtp.gmail.com",
        "smtphost":587,
        "Emailid":"as0223080@gmail.com",
        "Emailpassword":"gnnlaeyadbpqkljp"
    }
}

def speak2(str):
    try:
        gtt = gTTS(text=str, lang="en", slow=False)
        filename = f"{random_word()}avn.mp3"
        gtt.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[1].id)
        engine.setProperty("rate", 120)
        engine.say(str)
        engine.runAndWait()

def speak1(str):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.setProperty("rate", 120)
    engine.say(str)
    engine.runAndWait()


def Restart():
    os.system("shutdown /r /t 15")

def Shutdown():
    os.system("shutdown /s /t 10")

def Speedtest():
    sp=speedtest.Speedtest()
    sp.get_servers()
    down=str(round(sp.download()/(10**6),3))+"Mbps"
    up=str(round(sp.upload()/(10**6),3))+"Mbps"
    speed=f"Download Speed : {down} And Upload Speed {up}"
    return speed

def PhoneNumber(number):
    phonenumber=phonenumbers.parse(number)
    time=timezone.time_zones_for_number(phonenumber)
    company=carrier.name_for_number(phonenumber,"en")
    add=geocoder.description_for_number(phonenumber,"en")
    detail=f"Timezone : {time} \n Company : {company} \n Address : {add}"
    return detail

def Youtube(link,type):
    video_type=Listening()
    if "playlist" in video_type:
        playlist=Playlist(link)
        check="audio"
        video_q=1

        for video in playlist:

            if "audio" in check:
                video_stream=video.streams.filter(only_audio=True)
                video_stream[video_q+2].download()

            elif "video" in check:
                video_stream=video.streams.filter(only_video=True)
                video_stream[1].download()
    else:
        youtube=YouTube(link)
        title=youtube.title
        check="audio"
        video_q=1
        if "audio" in check:
            video=youtube.streams.filter(only_audio=True)
            video[video_q+2].download()

        elif "video" in check:
            video=youtube.streams.filter(only_video=True)
            video[1].download()
    
def History():
    pass

def Details():
    pass

                # if ".com" in sentence:
                #     if "www" in sentence:
                #         if " " in sentence:
                #             sentence.replace(" ","")
                #             filloutput("Openinng...../")
                #             time.sleep(0.5)
                #             filloutput("Openinng..........|")
                #             time.sleep(0.5)
                #             filloutput("Done....")
                #             Opensite(sentence)
                #         else:
                #             filloutput("Openinng...../")
                #             time.sleep(0.5)
                #             filloutput("Openinng..........|")
                #             time.sleep(0.5)
                #             filloutput("Done....")
                #             Opensite(sentence)

                #     else:
                #         if " " in sentence:
                #             sentence.replace(" ","")
                #             filloutput("Openinng...../")
                #             time.sleep(0.5)
                #             filloutput("Openinng..........|")
                #             time.sleep(0.5)
                #             filloutput("Done....")
                #             Opensite(f"www.{sentence}")
                #         else:
                #             filloutput("Openinng...../")
                #             time.sleep(0.5)
                #             filloutput("Openinng..........|")
                #             time.sleep(0.5)
                #             filloutput("Done....")
                #             Opensite(f"www.{sentence}")
                
                # elif "www." in sentence:
                #     if ".com" in sentence:
                #         if " " in sentence:
                #             sentence.replace(" ","")
                #             filloutput("Openinng...../")
                #             time.sleep(0.5)
                #             filloutput("Openinng..........|")
                #             time.sleep(0.5)
                #             filloutput("Done....")
                #             Opensite(sentence)
                #         else:
                #             filloutput("Openinng...../")
                #             time.sleep(0.5)
                #             filloutput("Openinng..........|")
                #             time.sleep(0.5)
                #             filloutput("Done....")
                #             Opensite(sentence)

                #     else:
                #         if " " in sentence:
                #             sentence.replace(" ","")
                #             filloutput("Openinng...../")
                #             time.sleep(0.5)
                #             filloutput("Openinng..........|")
                #             time.sleep(0.5)
                #             filloutput("Done....")
                #             Opensite(f"{sentence}.com")
                #         else:
                #             filloutput("Openinng...../")
                #             time.sleep(0.5)
                #             filloutput("Openinng..........|")
                #             time.sleep(0.5)
                #             filloutput("Done....")
                #             Opensite(f"{sentence}.com")
                # elif "www" in sentence:
                #     if ".com" in sentence:
                #         if " " in sentence:
                #             sentence.replace(" ","")
                #             sentence.replace("www","www.")
                #             filloutput("Openinng...../")
                #             time.sleep(0.5)
                #             filloutput("Openinng..........|")
                #             time.sleep(0.5)
                #             filloutput("Done....")
                #             Opensite(sentence)
                #         else:
                #             sentence.replace("www","www.")
                #             filloutput("Openinng...../")
                #             time.sleep(0.5)
                #             filloutput("Openinng..........|")
                #             time.sleep(0.5)
                #             filloutput("Done....")
                #             Opensite(sentence)

                #     else:
                #         if " " in sentence:
                #             sentence.replace(" ","")
                #             sentence.replace("www","www.")

                #             filloutput("Openinng...../")
                #             time.sleep(0.5)
                #             filloutput("Openinng..........|")
                #             time.sleep(0.5)
                #             filloutput("Done....")
                #             Opensite(f"{sentence}.com")
                #         else:
                #             sentence.replace("www","www.")
                #             filloutput("Openinng...../")
                #             time.sleep(0.5)
                #             filloutput("Openinng..........|")
                #             time.sleep(0.5)
                #             filloutput("Done....")
                #             Opensite(f"{sentence}.com")
                """




