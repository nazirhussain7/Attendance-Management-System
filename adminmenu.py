import tkinter
from tkinter import *
import sqlite3
import os




import image
from PIL import ImageTk, Image

root = Tk()
root.geometry('1366x768')
root.title("Attendance")


Un = StringVar()
Pw = StringVar()
canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back.png')
photo = ImageTk.PhotoImage(img)
canv.create_image(1,1, anchor=NW, image=photo)

def back():
    root.destroy()
    os.system('python main.py')
def sms():
    os.system('python sms.py')
def result():
    os.system('python result.py')
def recreq():
    os.system('python recreq.py')
def getloc():
    conn = sqlite3.connect('Form.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("delete from sendloc")
        conn.commit()
    os.system('python txtdata.py')
def map():
    os.system('python map.py')
def verify():
    os.system('python verify.py')
def att():
    os.system('python attfile.py')
Button(root, text='Receive Request', width=20, height=2, bg='yellow', fg='black', command=recreq).place(x=100, y=500)
Button(root, text='Send Request To Student', width=20, height=2, bg='yellow', fg='black', command=sms).place(x=300, y=500)
Button(root, text='Get Student Location', width=20, height=2, bg='yellow', fg='black', command=getloc).place(x=500, y=500)
Button(root, text='Generate MAP', width=20, bg='yellow', height=2, fg='black', command=map).place(x=700, y=500)
Button(root, text='CrossVerify', width=20, bg='yellow', height=2, fg='black', command=verify).place(x=900, y=500)
Button(root, text='Attendance', width=20, bg='yellow', height=2, fg='black', command=att).place(x=1100, y=500)
root.mainloop()
