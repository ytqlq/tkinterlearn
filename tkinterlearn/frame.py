from tkinter import *

root  = Tk()
root.title('frame')

myframe = LabelFrame(root,text='my label frame',padx=100,pady=10)
myframe.pack(padx=10,pady=5)

b = Button(myframe,text="click",padx=10,pady=10)
b.pack(padx=50)


root.mainloop()