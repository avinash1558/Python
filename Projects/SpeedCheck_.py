# pip install speedtest-cli
from tkinter import *
import speedtest

def Test():
    sp=speedtest.Speedtest()
    sp.get_servers()
    down=str(round(sp.download()/(10**6),3))+"Mbps"
    up=str(round(sp.upload()/(10**6),3))+"Mbps"
    print("avinash")
    l1.config(text=down)
    l2.config(text=up)
root=Tk()
root.title("Speed Test")
root.geometry("400x700")
Label(root,text="Speed Test",bg="grey",fg="white",height=3,width=70,font="Helvetica 20 bold").pack(padx=10,pady=10)
Label(root,text="Download",bg="brown",fg="white",height=3,width=70,font="Helvetica 15 bold").pack(padx=10,pady=10)
l1=Label(root,text="00 Mbps",bg="red",fg="white",height=3,width=70,font="Helvetica 15 bold")
l1.pack(padx=10,pady=10)
Label(root,text="Upload",bg="brown",fg="white",height=3,width=70,font="Helvetica 15 bold").pack(padx=10,pady=10)
l2=Label(root,text="00 Mbps",bg="red",fg="white",height=3,width=70,font="Helvetica 15 bold")
l2.pack(padx=10,pady=10)
Button(root,text="Test",fg="white",bg="grey",relief=RIDGE,height=3,width=70,command=Test).pack(padx=40,pady=10)
root.mainloop()