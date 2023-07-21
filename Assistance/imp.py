from tkinter import *

root = Tk()
t=StringVar()

t.set("aaa")
o=Text(root,textvariable =t)
o.pack()

root.mainloop()