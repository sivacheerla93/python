import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="9866850403", database="mock")

cur = con.cursor()

sql = """INSERT INTO EMPLOYEE(
    FIRST_NAME,
    LAST_NAME,
    AGE,
    SEX,
    INCOME) VALUES ("Siva", "Cheerla", 24, "M", 2000)"""
try:
    cur.execute(sql)
    con.commit()
except:
    con.rollback()
cur.close()
con.close()
