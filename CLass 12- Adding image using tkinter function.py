"""import cv2
image = cv2.imread('4.jpg')
cv2.imshow('window1',image)
image11 = cv2.resize(image,(400,300))
cv2.imwrite('image44.jpg',image11)
cv2.waitKey(0)"""
from tkinter import *
from PIL import Image,ImageTk
window = Tk()
window.geometry('500x500')
window.config(bg='blue')
image = Image.open("image11.jpg")
image11 = ImageTk.PhotoImage(image)
image2 = Image.open("image22.jpg")
image22 = ImageTk.PhotoImage(image2)
image3 = Image.open("image33.jpg")
image33 = ImageTk.PhotoImage(image3)
image4 = Image.open("image11.jpg")
image44 = ImageTk.PhotoImage(image4)
images_list = [image11,image22,image33,image44]
a = 0
L1 = Label(window, image=images_list[a])
L1.place(x=50,y=50)
def next():
    global a
    L1 = Label(window, image=images_list[a])
    L1.place(x=50, y=50)
    a+=1
    if a>3:
        a=0
def previous():
    global a
    L1 = Label(window,image=images_list[a])
    L1.place(x=50,y=50)
    a-=1
    if a==-5:
        a=-1


b1 = Button(window,text='⏩',font = ('cursive',15,'bold'),command = next)
b1.place(x=250,y=380)
b2 = Button(window,text='🔙',font = ('cursive',15,'bold'),command = previous)
b2.place(x=150,y=380)






window.mainloop()

