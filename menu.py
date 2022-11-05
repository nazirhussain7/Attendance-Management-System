from tkinter import *
import sqlite3
import os
from tkinter import messagebox
from PIL import ImageTk, Image
root = Tk()
root.geometry('1366x768')
root.title("Login")
canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back1.png')
photo = ImageTk.PhotoImage(img)
canv.create_image(1,1, anchor=NW, image=photo)

def back():
    root.destroy()
    os.system('python main.py')
def sendreq():
    root.destroy()
    os.system('python sendreq.py')
#main program

Button(root, text='send Request', width=10, bg='gray', fg='white', command=sendreq).place(x=400, y=450)
#Button(root, text='Register', width=10, bg='gray', fg='white', command=reg).place(x=400, y=500)
Button(root, text='Cancel', width=10, bg='gray', fg='white', command=back).place(x=500, y=450)

root.mainloop()
