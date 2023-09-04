from tkinter import *

root  = Tk()

myLabel1 = Label(root,text="Hello World!")
myLabel2= Label(root,text="Hello World!2")
# myLabel5= Label(root,text="Hello World!5")
# myLabel.pack()
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=5)
# myLabel5.grid(row=2,column=1)

root.mainloop()