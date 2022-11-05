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
Cid = StringVar()
Sn = StringVar()
Tdate = StringVar()
def back():
    root.destroy()
    os.system('python main.py')
def reg():
    root.destroy()
    os.system('python register.py')
def sendrequest():
    sn = Sn.get()
    cid= Cid.get()
    tdate=Tdate.get()
    if sn=="":
        messagebox.showinfo("Attendance","Enter Staff Name")
    else:
        if cid == "":
          messagebox.showinfo("Attendance","Enter ClassID")
        else:
            conn = sqlite3.connect('Form.db')
            with conn:
                    cursor = conn.cursor()
                    cursor.execute('INSERT INTO sendreq(Sname,classid,tdate) VALUES(?,?,?)',(sn, cid,tdate))

                    conn.commit()
                    messagebox.showinfo("Attendance", "Request Sent")
#main program
import datetime as dt
date=dt.datetime.now()

# Format the date
format_date=f"{date:%a, %b %d %Y}"
Tdate.set(format_date)
label_0 = Label(root, text="Send Request to Server", bg='white', width=20, font=("bold", 20))
label_0.place(x=10, y=300)
label_1 = Label(root, text="Staff Name", width=20, bg='white', font=("bold", 10))
label_1.place(x=300, y=350)
entry_2 = Entry(root, textvar=Sn)
entry_2.place(x=500, y=350)
label_3 = Label(root, text="ClassId", width=20,bg='white', font=("bold", 10))
label_3.place(x=300, y=400)
entry_6 = Entry(root, textvar=Cid)
entry_6.place(x=500, y=400)
label_3 = Label(root, text="Date", width=20,bg='white', font=("bold", 10))
label_3.place(x=700, y=350)
entry_6 = Entry(root, textvar=Tdate)
entry_6.place(x=900, y=350)
Button(root, text='Submit', width=10, bg='gray', fg='white', command=sendrequest).place(x=400, y=450)

Button(root, text='Cancel', width=10, bg='gray', fg='white', command=back).place(x=500, y=450)

root.mainloop()
