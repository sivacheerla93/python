import sqlite3

try:
    con = sqlite3.connect(r"d:\Education\git_workspace\python\database\hr.db")
    cur = con.cursor()

    cur.execute("select max(empid) from emp")
    largest_id = cur.fetchone()
    name = input("Enter name: ")
    salary = input("Enter salary: ")
    dept_id = input("Enter dept id: ")

    cur.execute("insert into emp values(?,?,?,?)", (largest_id[0] + 1, name, salary, dept_id))
    con.commit()

    if cur.rowcount == 1:
        print("Employee added!")
    else:
        print("Employee not added!")

    cur.close()
except Exception as ex:
    print("Error: ", ex)
finally:
    con.close()
