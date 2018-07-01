import os
import cx_Oracle

try:
    os.environ['PATH'] = r'C:\Python34\instantclient_12_2'
    con = cx_Oracle.connect("hr", "hr", "localhost/xe")
    cur = con.cursor()
    # take input from user
    empid = input("Enter employee id :")
    salary = input("Enter new salary : ")
    cur.execute("update employees set salary = :salary where employee_id = :id", salary=salary, id=empid)
    if cur.rowcount == 1:
        print("Updated Salary!")
        con.commit()
    else:
        print("Sorry! Employee not found!")

    cur.close()
except Exception as ex:
    print("Error : ", ex)
finally:
    con.close()
