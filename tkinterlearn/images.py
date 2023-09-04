from tkinter import *
from PIL import ImageTk,Image


root  = Tk()
root.title('haha')

# root.iconbitmap()
button_quit = Button(root,text="Exit",command=root.quit)
button_quit.pack()


my_img = ImageTk.PhotoImage(Image.open('a.png'))
my_label = Label(image=my_img)
my_label.pack()

root.mainloop()