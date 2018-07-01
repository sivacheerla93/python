import sqlite3

try:
    con = sqlite3.connect(r"d:\Education\git_workspace\python\database\hr.db")
    cur = con.cursor()
    id = input("Enter employee id: ")
    salary = input("Enter new salary: ")

    cur.execute("update emp set salary = ? where empid = ?", (salary, id))

    if cur.rowcount == 1:
        print("Updated salary!")
        con.commit()
    else:
        print("sorry! Employee not found!!")
    cur.close()
except Exception as ex:
    print("Error: ", ex)
finally:
    con.close()
