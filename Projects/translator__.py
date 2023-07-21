# pip install googletrans==4.0.0rc1

from googletrans import Translator,LANGUAGES
from tkinter import *
from tkinter import ttk


def change(text="type",src="English",dest="Hindi"):
    # print("1")
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    tran1=trans.translate(text,src=src1,dest=dest1)
    return tran1.text
    

def data():
    # print("1")
    s=comb_sor.get()
    d=comb_dest.get()
    m=Sor_txt.get(1.0,END)

    Text_get=change(text=m,src=s,dest=d)
    Dest_txt.delete(1.0,END)
    Dest_txt.insert(END,Text_get)
    # print("!")
# data()
# tran=Translator()
# tran1=tran.translate("alive","en","hi")
# print(tran1)


root=Tk()
root.title("Translator")
root.geometry("500x700")

root.config(bg="red")

lab_txt=Label(root,text="Translator",font="Helvetica 40 bold")
lab_txt.place(x=100,y=40,height=50,width=300)
frame=Frame(root).pack(side=BOTTOM)
lab_txt=Label(root,text="Source Text",font="Helvetica 20 bold",bg="red")
lab_txt.place(x=100,y=100,height=50,width=300)
Sor_txt=Text(frame,font="Helvetica 20 bold",wrap=WORD)
Sor_txt.place(x=15,y=140,height=200,width=470)

list_text=list(LANGUAGES.values())
comb_sor=ttk.Combobox(frame,value=list_text)
comb_sor.place(x=15,y=350,height=40,width=100)
comb_sor.set("english")

button_change=Button(frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=160,y=350,height=40,width=185)

comb_dest=ttk.Combobox(frame,value=list_text)
comb_dest.place(x=385,y=350,height=40,width=100)
comb_dest.set("hindi")

lab_txt=Label(root,text="Dest Text",font="Helvetica 20 bold",bg="red")
lab_txt.place(x=100,y=400,height=50,width=300)
Dest_txt=Text(frame,font="Helvetica 20 bold",wrap=WORD)
Dest_txt.place(x=15,y=440,height=200,width=470)
root.mainloop()