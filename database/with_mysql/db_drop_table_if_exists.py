import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="9866850403", database="mock")

cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS STUDENT")

sql = "CREATE TABLE STUDENT (NAME CHAR(30) NOT NULL, CLASS CHAR(5), AGE INT(3), GENDER CHAR(8), MARKS INT(10))"

cur.execute(sql)

cur.close()
con.close()
