import mysql.connector

# open database connection
con = mysql.connector.connect(host="localhost", user="root", password="9866850403", database="")

# prepare a cursor object using cursor() method
cur = con.cursor()

# execute SQL query using execute() metod
cur.execute("SELECT VERSION()")

# fetch a single row using fetchone() method.
data = cur.fetchone()

print("Database version: %s" % data)

# close cursor object
cur.close()

# disconnect from db server
con.close()
