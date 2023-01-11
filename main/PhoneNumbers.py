import sqlite3

conn = sqlite3.connect("cl24")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS DE_PHONE_NUMBERS")
cur.execute("CREATE TABLE DE_PHONE_NUMBERS(MatricNo INTEGER UNIQUE FOREIGN KEY, PhoneNo TEXT)")
conn.commit()
conn.close()
print("Table has been created")