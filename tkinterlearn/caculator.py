from  tkinter import *

root = Tk()
# root.title = "My caculator"
root.title("simple caculator")

tag = [None]
global res 
res = 0

e = Entry(root,width=40,borderwidth=5)
e.grid(row=0,column=0,columnspan=4)
# e.pack()

def enternum(number):
    forenum = e.get()
    e.delete(0,END)
    e.insert(0,forenum+str(number))
    
def click_add():
    try:
        forenum = int(e.get())
    except ValueError:
        forenum = 0
    print(forenum)    
    e.delete(0,END)
    process(forenum) 
    print(res)   
    tag[0] = '+'
    
def click_substract():
    try:
        forenum = int(e.get())
    except ValueError:
        forenum = 0 
    print(forenum)  
    e.delete(0,END)
    process(forenum)   
    print(res)    
    tag[0] = '-'
    
def click_multiply():
    try:
        forenum = int(e.get())
    except ValueError:
        forenum = 0  
    print(forenum)  
    e.delete(0,END)
    process(forenum)
    print(res)       
    tag[0] = '*'
    
def click_divide():
    try:
        forenum = int(e.get())
    except ValueError:
        forenum = 0
    print(forenum)   
    e.delete(0,END)
    process(forenum) 
    print(res)      
    tag[0] = '/'
    
def equal():
    try:
        forenum = int(e.get())
    except ValueError:
        forenum = 0    
    print(forenum)
    e.delete(0,END)
    process(forenum)
    print(res)    
    e.insert(0,str(res))
    tag[0] = None


def process(forenum):
    global res
    if not tag[0]:
        res = forenum
    elif tag[0] == '+':
        res = forenum + res
    elif tag[0] == '-':
        res = res - forenum
    elif tag[0] == '*':
        res = res * forenum
    elif tag[0] == '/':
        try:
            res = round(res/forenum)
        except ZeroDivisionError:
            e.delete(0,END)
            e.insert(0,"Error")
            
def click_clear():
    e.delete(0,END) 


button1 = Button(root,text="1",padx=40,pady=20,command=lambda:enternum(1))
button2 = Button(root,text="2",padx=40,pady=20,command=lambda:enternum(2))
button3 = Button(root,text="3",padx=40,pady=20,command=lambda:enternum(3))
button4 = Button(root,text="4",padx=40,pady=20,command=lambda:enternum(4))
button5 = Button(root,text="5",padx=40,pady=20,command=lambda:enternum(5))
button6 = Button(root,text="6",padx=40,pady=20,command=lambda:enternum(6))
button7 = Button(root,text="7",padx=40,pady=20,command=lambda:enternum(7))
button8 = Button(root,text="8",padx=40,pady=20,command=lambda:enternum(8))
button9 = Button(root,text="9",padx=40,pady=20,command=lambda:enternum(9))
button0 = Button(root,text="0",padx=40,pady=20,command=lambda:enternum(0))
button_add = Button(root,text="+",padx=40,pady=20,command=click_add)
button_substract = Button(root,text="-",padx=40,pady=20,command=click_substract)
button_multiply = Button(root,text="*",padx=40,pady=20,command=click_multiply)
button_divide = Button(root,text="/",padx=40,pady=20,command=click_divide)
button_equal = Button(root,text='=',padx=40,pady=20,command=equal)
button_clear = Button(root,text='CE',padx=40,pady=20,command=click_clear)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=0)
button_add.grid(row=1,column=3)
button_substract.grid(row=2,column=3)
button_multiply.grid(row=3,column=3)
button_divide.grid(row=4,column=3)
button_equal.grid(row=4,column=2)
button_clear.grid(row=4,column=1)

root.mainloop()