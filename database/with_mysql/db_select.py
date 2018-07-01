import mysql.connector

# open database connection
con = mysql.connector.connect(host="localhost", user="root", password="9866850403", database="world")

# prepare a cursor object using cursor() method
cur = con.cursor()

# execute SQL query using execute() metod
cur.execute("select * from country")

for row in cur.fetchall():
    print(row[0], row[1])

# close cursor object
cur.close()

# disconnect from db server
con.close()
