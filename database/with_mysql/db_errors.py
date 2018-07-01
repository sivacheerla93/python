import mysql.connector
from mysql.connector import errorcode

try:
    con = mysql.connector.connect(host="localhost", user="root", password="9866850403", database="world")
    print("Connection successful! No errors found!!")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Access denied/wrong user name or password!")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exists!")
    else:
        print(err)
finally:
    con.close()
