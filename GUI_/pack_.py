from tkinter import *
root = Tk()
root.geometry("744x133")
root.title("My GUI With Harry")

title_label = Label(text ='''
Abdul Rashid Salim Salman Khan is playback singer and television p''')

# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady

# title_label.pack(side=BOTTOM, anchor ="sw", fill=X)
title_label.pack(side=LEFT, fill=Y, padx=34, pady=34)

f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
f2.pack(side=TOP, fill="x")

l = Label(f1, text="Project Tkinter - Pycharm")
l.pack( pady=142)

l = Label(f2, text="Welcome to sublime text", font="Helvetica 16 bold", fg="red", pady=22)
l.pack()

root.mainloop()


