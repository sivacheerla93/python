import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="9866850403", database="mock")

cur = con.cursor()

sql = """select * from employee where first_name='Siva'"""
try:
    cur.execute(sql)
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
    print("Error! Unable to fetch data!!", err)
cur.close()
con.close()
