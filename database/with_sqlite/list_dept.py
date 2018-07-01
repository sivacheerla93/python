import sqlite3

try:
    con = sqlite3.connect(r"d:\Education\git_workspace\python\database\hr.db")
    cur = con.cursor()
    cur.execute("select * from dept order by id")

    for row in cur.fetchall():
        print(row[0], row[1])

    cur.close()
except Exception as ex:
    print("Error: ", ex)
finally:
    con.close()
