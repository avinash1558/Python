# from PIL import Image
# img=Image.open("1r.png")
# img.show()
from tkinter import *
root=Tk()
p=PhotoImage(file="C:\\Users\\avina\\OneDrive\\Desktop\\codes\\Python\\Assistance\\1r.png")
Label(image=p).pack()
root.mainloop()