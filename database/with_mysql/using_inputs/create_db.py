import mysql.connector

# class insert_db:
#     def __init__(self):
#         self.name = input("Enter database name to create: ")
#
#
# a = insert_db()

name = input("Enter database name you want to create: ")
con = mysql.connector.connect(host="localhost", user="root", password="9866850403")
cur = con.cursor()

try:
    sql = ("create database {}".format(name))
    cur.execute(sql)
    print("New database '{}' created successfully!".format(name))
except mysql.connector.Error as err:
    print("Error found: ", err)
    con.rollback()

cur.close()
con.commit()
con.close()
