from tkinter import *
from PIL import ImageTk,Image

def open():
    top = Toplevel()
    top.title('The 2nd window')
    Label(top, image=img).pack()
    Button(top, text="close the 2nd window",command=top.destroy).pack()

    # lab.pack() 
    # bn2.pack()


root  = Tk()
root.title("The first window.")
bn1 = Button(root,text="Open the 2nd window.",command= open).pack()

img = ImageTk.PhotoImage(Image.open("images/a.png"))




root.mainloop()