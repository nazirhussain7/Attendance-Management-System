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
Tdate=StringVar()
td=Tdate.get()
import datetime as dt
date=dt.datetime.now()

# Format the date
format_date=f"{date:%a, %b %d %Y}"
Tdate.set(format_date)

def cancel():
    root.destroy()


def database():

    conn = sqlite3.connect('Form.db')
    with conn:
        cursor = conn.cursor()
        td = Tdate.get()
        print(td)

        cursor.execute("select * from att where tdate=?",(td,))

        results = cursor.fetchall()


        for row in results:
                 Libcontect_label = Label(root, text=row, font=("bold", 15))
                 Libcontect_label.pack(pady=10, padx=10)


    conn.close()






label_3 = Label(root, text="Date", width=20,bg='white', font=("bold", 10))
label_3.place(x=800, y=350)
entry_6 = Entry(root, textvar=Tdate)
entry_6.place(x=1000, y=350)

Button(root, text='Show', width=5,height=2, bg='blue', fg='white', command=database).place(x=150, y=450)
Button(root, text='Cancel', width=5, height=2,bg='blue', fg='white', command=cancel).place(x=200, y=450)
print("Result")

root.mainloop()
