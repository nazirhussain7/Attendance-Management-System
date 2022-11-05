import datetime as dt
import sqlite3

date=dt.datetime.now()

# Format the date
format_date=f"{date:%a, %b %d %Y}"


conn = sqlite3.connect('Form.db')
with conn:

    cur = conn.cursor()
    cur.execute("SELECT * FROM sendloc where tdate=?", (format_date,))
    rows = cur.fetchall()
    for row in rows:
        a1 = row[2]
        a2 = row[3]
        a3=row[4]
        if int(a3)==3:


