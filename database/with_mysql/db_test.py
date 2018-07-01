import mysql.connector

try:
    # open database connection
    con = mysql.connector.connect(host="localhost", user="root", password="9866850403", database="")
    print("Connetion successful!")
except mysql.connector.Error as err:
    print("Some error is there!", err)
finally:
    # disconnect from db server
    con.close()
