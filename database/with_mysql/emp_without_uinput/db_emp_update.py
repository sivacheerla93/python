import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="9866850403", database="mock")

cur = con.cursor()

sql = """UPDATE EMPLOYEE SET INCOME =10000 WHERE FIRST_NAME='Siva'"""
try:
    cur.execute(sql)
    con.commit()

    read = "select * from employee where first_name='Siva'"
    cur.execute(read)
    results = cur.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print("First name = %s, Last name = %s, Age = %d, Sex = %c, Income = %d" %
              (fname, lname, age, sex, income))
except mysql.connector.Error as err:
    print("Error! ", err)
    con.rollback()
cur.close()
con.close()
