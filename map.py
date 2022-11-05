import datetime as dt
import sqlite3
from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.geometry('1000x500')




root.title("Map")




date=dt.datetime.now()
root.configure(bg="white")
# Format the date
format_date=f"{date:%a, %b %d %Y}"
L1=StringVar()
L2=StringVar()
L3=StringVar()
L4=StringVar()

conn = sqlite3.connect('Form.db')
with conn:

    cur = conn.cursor()
    cur.execute("SELECT * FROM sendloc " )
    rows = cur.fetchall()
    for row in rows:
        a1 = row[2]
        a2 = row[3]

        print(a1,", ",a2)
        aa=a1 + "   " + a2
        Libcontect_label = Label(root, text=aa, font=("bold", 15))
        Libcontect_label.pack(pady=10, padx=10)



l1=Label(root,text="Generated Student Location Map",bg="white",font=("BOLD",15),fg="red")
l1.place(x=50,y=100)
root.mainloop()
