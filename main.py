from tkinter import *

from PIL import ImageTk, Image
import sqlite3
import os
root = Tk()
root.geometry('1366x768')
root.title("Attendance")


#root.configure(bg='#2F5D04 ')




def server():
     root.destroy()
     os.system('python server.py')

def register():
    root.destroy()
    os.system('python student.py')


def client():
    root.destroy()
    os.system('python client.py')


canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back.png')
photo = ImageTk.PhotoImage(img)
canv.create_image(1,1, anchor=NW, image=photo)

img1 = Image.open('server.png')
photo1 = ImageTk.PhotoImage(img1)
img2 = Image.open('client.jpg')
photo2 = ImageTk.PhotoImage(img2)
img3 = Image.open('register.jpg')
photo3 = ImageTk.PhotoImage(img3)

Button(root,  image=photo1, width=200,height=220, bg='black', fg='white',font=("bold", 20) ,command=server).place(x=300, y=500)

Button(root,  image=photo2, width=200, height=220,bg='black', fg='white', font=("bold", 20),command=client).place(x=500, y=500)
Button(root,  image=photo3, width=200, height=220,bg='black', fg='white', font=("bold", 20),command=register).place(x=700, y=500)



root.mainloop()
