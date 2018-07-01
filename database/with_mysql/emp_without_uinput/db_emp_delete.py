import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="9866850403", database="mock")

cur = con.cursor()

sql = """DELETE FROM EMPLOYEE WHERE FIRST_NAME='Siva'"""
try:
    cur.execute(sql)
    con.commit()

    read = "select * from employee"
    cur.execute(read)
    results = cur.fetchall()
    print(results)
except mysql.connector.Error as err:
    print("Error! ", err)
    con.rollback()
cur.close()
con.close()
