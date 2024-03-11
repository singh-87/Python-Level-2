from tkinter import *
window = Tk()
window.geometry("350x500")
window.title("Sign-up app")
window.config(bg = 'cyan')
#Creating label,button,entry and text widget
label = Label(window,text = "Username:",font = ("ariel",15,'bold'),width = 50)
label.pack()
e1 = Entry(window,font = ("ariel",15,'bold'),width = 50)
e1.pack(pady=10)
label2 = Label(window,text = "Email address:",font = ("ariel",15,'bold'),width = 50)
label2.pack()
e2 = Entry(window,font = ("ariel",15,'bold'),width = 50)
e2.pack(pady=10)
label3 = Label(window,text = "Password:",font = ("ariel",15,'bold'),width = 50)
label3.pack()
e3 = Entry(window,show = '*',font = ("ariel",15,'bold'),width = 50)
e3.pack(pady=10)
def signup():
    txt.delete(1.0,END)
    name = e1.get()
    email = e2.get()
    password = e3.get()
    if name!='' and email!='' and password!='':
        msg = f"Hi {name}\n\nYour account is created"
    else:
        msg = "Please enter all the\nrequirements above"
    txt.insert(END,msg)

btn = Button(window,text = "Sign up",font = ("ariel",15,'bold'),bg = 'black',fg = 'white',command = signup)
btn.pack(pady = 10)
txt = Text(window,font = ("ariel",15,'bold'))
txt.pack()






window.mainloop()