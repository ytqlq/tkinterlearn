from tkinter import *

root  = Tk()

e = Entry(root,width=50,borderwidth=5)
e.pack()
e.insert(0,"bye")

def myClick():
    myLabel = Label(root,text=e.get())
    myLabel.pack()

myButton = Button(root,text="click me",padx=50,pady=50,command=myClick,fg="red")
myButton.pack()

root.mainloop()