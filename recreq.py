from tkinter import *
import sqlite3
from tkinter import messagebox

import os


from PIL import ImageTk, Image
root = Tk()
root.geometry('400x500')
root.title("View Loc")
root.configure(bg='#2F5D04')
Candname = StringVar()
ctr = StringVar()


def cancel():
    root.destroy()


def database():

    conn = sqlite3.connect('Form.db')
    with conn:
        cursor = conn.cursor()

        cursor.execute("select * from sendreq")

        results = cursor.fetchall()


        for row in results:
                 Libcontect_label = Label(root, text=row, font=("bold", 10))
                 Libcontect_label.pack(pady=15, padx=10)


    conn.close()


label_0 = Label(root, justify=LEFT, text="View Request",bg="white", width=10, font=("bold", 15))
label_0.place(x=5, y=1)





Button(root, text='Show', width=5,height=2, bg='blue', fg='white', command=database).place(x=150, y=450)
Button(root, text='Cancel', width=5, height=2,bg='blue', fg='white', command=cancel).place(x=200, y=450)
print("Result")

root.mainloop()
