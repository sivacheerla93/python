import sqlite3

try:
    con = sqlite3.connect(r"d:\Education\git_workspace\python\database\hr.db")
    cur = con.cursor()
    cur.execute(
        "select empid, empname, salary, salary * .40, name from emp join dept on (emp.deptid = dept.id) order by empid")

    for row in cur.fetchall():
        print("%4d %-10s %5d %5d %-20s" % (row))

    cur.close()
except Exception as ex:
    print("Error: ", ex)
finally:
    con.close()
