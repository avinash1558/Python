# pip install pytube
from pytube import YouTube,Playlist
link="https://youtu.be/8bjS1sgR6ug"
you=YouTube(link)


# print(you.title)
# print(you.thumbnail_url)
# print(you.description)

# you_down=you.streams.filter(only_video=True)
you_down=you.streams.all()
print(type(you_down))
vid=list(enumerate(you_down))
for i in vid:
    print(i)
print()
s=int(input("enter :..."))
you_down[s].download()
print("end")

# you_down=you.streams.filter(only_video=True)
# you_down=you.streams.filter(only_audio=True)

# vid=list(enumerate(you_down))
# for i in vid:
#     print(i)
# print()
# s=int(input("enter :..."))
# # you_down[s].download()
# print("end")


# py=Playlist("https://youtube.com/playlist?list=PLghY5cMt_RfTcuz0yizZ-W_iDC8XStYgC")

# for p in py.videos:
#     print(p)
#     a=p.streams.filter(only_audio=True)
#     print(a)
    # p.streams.first().download()


