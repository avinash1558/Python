import os
from tkinter import *

root=Tk()
root.title("ShutDown App")
# root.wm_iconbitmap("C:\\Users\\avina\\OneDrive\\Desktop\\codes\\Python\\Projects\\bg.jpg")
root.geometry("400x300")

def restart():
    os.system("shutdown /r /t 1")

def retime():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")



frame=Frame(root,background="grey",relief=SUNKEN,height=400,width=500)
frame.pack()
Button(frame,text="ShutDown",fg="white",bg="grey",relief=RIDGE,height=3,width=70,command=shutdown).pack(padx=40,pady=10)
Button(frame,text="Restart",fg="white",bg="grey",relief=RIDGE,height=3,width=70,command=restart).pack(padx=40,pady=10)
Button(frame,text="Restart Time",fg="white",bg="grey",relief=RIDGE,height=3,width=70,command=retime).pack(padx=40,pady=10)
Button(frame,text="Logout",fg="white",bg="grey",relief=RIDGE,height=3,width=70,command=logout).pack(padx=40,pady=10)

root.mainloop()