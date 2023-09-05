from tkinter import *

root  = Tk()
root.title("radio button")
radio_frame = LabelFrame(root,padx=100,pady=50)
radio_frame.pack()
MODES = ['腊肠','榴莲','洋葱','芝士']
pizza = StringVar()
pizza.set('芝士')
def select(value):
    Label(root,text=value).pack()
for mode in MODES:
    Radiobutton(radio_frame,text=mode,variable=pizza,value=mode).pack(anchor=W)    
select_button = Button(root,text='order',command=lambda:select(pizza.get()))
select_button.pack()

root.mainloop()