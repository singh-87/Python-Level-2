from tkinter import *
from ttkbootstrap import *
window = Tk()
window.geometry("750x500")
window.maxsize(width = 750,height = 500)
style = Style(theme = "cyborg")
l1 = Label(window,text = "NUMBER 1 = ",bootstyle="inverse-danger",font = ('arial',20,'bold'))
l1.place(x = 30,y=50)
e1 = Entry(window,bootstyle = "success",font = ('arial',15,'bold'))
e1.place(x = 230,y=50)
l2 = Label(window,text = "NUMBER 2 = ",bootstyle="inverse-danger",font = ('arial',20,'bold'))
l2.place(x = 30,y=100)
e2 = Entry(window,bootstyle = "success",font = ('arial',15,'bold'))
e2.place(x = 230,y=100)
l3 = Label(window,text = "RESULT = ",bootstyle="inverse-danger",font = ('arial',20,'bold'))
l3.place(x = 30,y=300)
e3 = Entry(window,bootstyle = "success",font = ('arial',15,'bold'))
e3.place(x = 230,y=300)
def add():
    a = int(e1.get())
    b = int(e2.get())
    result = a+b
    e3.delete(0, END)
    e3.insert(END,result)
def minus():
    a = int(e1.get())
    b = int(e2.get())
    result = a-b
    e3.delete(0, END)
    e3.insert(END,result)
def multiply():
    a = int(e1.get())
    b = int(e2.get())
    result = a*b
    e3.delete(0, END)
    e3.insert(END,result)
def divide():
    a = int(e1.get())
    b = int(e2.get())
    result = a/b
    e3.delete(0,END)
    e3.insert(END,result)

b1 = Button(window,bootstyle = "success",text = '➕',width = 12,command = add)
b1.place(x=50,y = 200)
b2 = Button(window,bootstyle = "warning",text = '➖',width = 12,command = minus)
b2.place(x=220,y = 200)
b3 = Button(window,bootstyle = "info",text = '❌',width = 12,command = multiply)
b3.place(x=420,y = 200)
b4 = Button(window,bootstyle = "primary",text = '➗',width = 12,command = divide)
b4.place(x=620,y = 200)








window.mainloop()