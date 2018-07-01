import sqlite3

try:
    con = sqlite3.connect(r"c:\program files\sqlite3\databases\python.db")
    print("Connected Sqlite!")
except Exception as ex:
    print("Couldn't not connect to database. Error: ", ex)
else:
    con.close()
