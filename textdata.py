import sqlite3

import unicodecsv


con = sqlite3.connect('Form.db')
cur = con.cursor()


with open('smsdata.txt', 'rb') as input_file:
    reader = unicodecsv.reader(input_file, delimiter=",")
    data = [row for row in reader]

cur.executemany("INSERT INTO sendloc (sname,classid,sreg,loc,scount,tdate) VALUES (?, ?, ?,?,?,?);", data)
con.commit()
