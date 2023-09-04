from tkinter import *

root  = Tk()

def myClick():
    myLabel = Label(root,text="Look!")
    myLabel.pack()

myButton = Button(root,text="click me",padx=50,pady=50,command=myClick,fg="red")
myButton.pack()

root.mainloop()