from tkinter import *
from PIL import ImageTk,Image


root  = Tk()
root.title('Pic viewer')
my_img1 = ImageTk.PhotoImage(Image.open('./images/a.png'))
my_img2 = ImageTk.PhotoImage(Image.open('./images/b.png'))
my_img3 = ImageTk.PhotoImage(Image.open('images/c.png'))
my_img4 = ImageTk.PhotoImage(Image.open('images/d.png'))

img_list = [my_img1,my_img2,my_img3,my_img4]

my_label = Label(image=img_list[0])
my_label.grid(row=0,column=0,columnspan=3)
# root.iconbitmap()

def forward(image_number):
    global button_forward
    global button_backward
    global my_label
    
    my_label.grid_forget()
    my_label = Label(image=img_list[image_number])
    my_label.grid(row=0,column=0,columnspan=3)   
    if image_number == len(img_list)-1:
        button_forward = Button(root,text='>>',state=DISABLED)
    else:
        button_forward = Button(root,text='>>',command=lambda:forward(image_number+1))
    if image_number ==0:
        button_backward = Button(root,text='<<',state=DISABLED)
    else:
        button_backward = Button(root,text='<<',command=lambda:back(image_number-1))
    button_forward.grid(row=1,column=2)
    button_backward.grid(row=1,column=0)
    
    
    
def back(image_number):
    global button_forward
    global button_backward
    global my_label
    my_label.grid_forget()
    my_label = Label(image=img_list[image_number])
    my_label.grid(row=0,column=0,columnspan=3)   
    if image_number == len(img_list)-1:
        button_forward = Button(root,text='>>',state=DISABLED)
    else:
        button_forward = Button(root,text='>>',command=lambda:forward(image_number+1))
    if image_number ==0:
        button_backward = Button(root,text='<<',state=DISABLED)
    else:
        button_backward = Button(root,text='<<',command=lambda:back(image_number-1))
    button_forward.grid(row=1,column=2)
    button_backward.grid(row=1,column=0)
    
   

button_quit = Button(root,text="Exit",command=root.quit)
button_forward = Button(root,text=">>",command=lambda:forward(1))
button_backward = Button(root, text="<<",state=DISABLED)

button_backward.grid(row=1,column=0)
button_forward.grid(row=1,column=2)
button_quit.grid(row=1,column=1)








root.mainloop()