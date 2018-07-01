import cx_Oracle
import os

try:
    os.environ['PATH'] = r'C:\Python34\instantclient_12_2'
    con = cx_Oracle.connect("hr", "hr", "localhost/xe")
    print("Connected To Oracle")
except Exception as ex:
    print("Could not connect to database. Error : ", ex)
else:
    con.close()
