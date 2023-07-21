
from tkinter import *
import tkinter.messagebox as tmsg

root =Tk()
root.geometry("655x333")

def hello():
    print("Hello tkinter Buttons")

def name():
    print("Name is harry")
    
# frame = Frame(root, borderwidth=10, bg="grey", relief=SUNKEN)
# frame.pack(side=LEFT, anchor="nw")

# b1 = Button(frame, fg="red", text="Print now", command=hello)
# b1.pack(side=LEFT, padx=23)

# b2 = Button(frame, fg="red", text="Tell me name now", command=name)
# b2.pack(side=LEFT, padx=23)

# b3 = Button(frame, fg="red", text="Print now")
# b3.pack(side=LEFT, padx=23)

# b4 = Button(frame, fg="red", text="Print now")
# b4.pack(side=LEFT, padx=23)


# def getvals():
#     print(f"The value of username is {uservalue.get()}")
#     print(f"The value of password is {passvalue.get()}")

# uservalue = StringVar()
# passvalue = StringVar()

# userentry = Entry(root, textvariable = uservalue)
# passentry = Entry(root, textvariable = passvalue)

# userentry.grid(row=0, column=1)
# passentry.grid(row=1, column=1)

# Button(text="Submit", command=getvals).grid()



def order():
    tmsg.showinfo("Order Received!", f"We have received your order for {var.get()}. Thanks for ordering")

# var = IntVar()
var = StringVar()
var.set("Dosa")
# var.set(1)
Label(root, text = "What would you like to have sir?",font="lucida 19 bold",
      justify=LEFT, padx=14).pack()
radio = Radiobutton(root, text="Dosa", padx=14, variable=var, value="Dosa").pack(anchor="w")
radio = Radiobutton(root, text="Idly", padx=14, variable=var, value="Idly").pack(anchor="w")
radio = Radiobutton(root, text="Paratha", padx=14, variable=var, value="Paratha").pack(anchor="w")
radio = Radiobutton(root, text="Samosa", padx=14, variable=var, value="Samosa").pack(anchor="w")

Button(text="Order Now", command=order).pack()


foodservicevalue = IntVar()
foodservice = Checkbutton(text="Want to prebook your meals?", variable = foodservicevalue)
foodservice.grid(row=6, column=3)

root.mainloop()
