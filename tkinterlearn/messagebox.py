from tkinter import *
from tkinter import messagebox

root  = Tk()
root.title("message box")

def show():
    messagebox.showinfo('title','something')

Button(root,text='show message',command=show).pack()


root.mainloop()