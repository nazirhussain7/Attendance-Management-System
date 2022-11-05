import sqlite3
from tkinter import messagebox

conn = sqlite3.connect('Form.db')
with conn:
        cursor = conn.cursor()
        cursor.execute("delete from att ")
        conn.commit()
        cursor.execute("select * from sendloc")
        rows1 = cursor.fetchall()
        for row1 in rows1:
            SN = row1[0]
            cursor.execute("select * from sendloc where sname=?",(SN,))
            rows = cursor.fetchall()
            for row in rows:
                SR = row[2]
                L = row[3]
                ctr= row[4]
                cursor.execute("select * from sendloc")
                rows2 = cursor.fetchall()
                for row2 in rows2:
                    ctr1 = row2[4]
                print(ctr)
                print(ctr1)
                if ctr!=ctr1:
                    print("Not")
                else:
                    conn = sqlite3.connect('Form.db')
                    with conn:
                        cursor = conn.cursor()


                        cursor.execute('INSERT INTO att(sname) VALUES(?)',(SN,))
                        conn.commit()


