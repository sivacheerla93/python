import mysql.connector

try:
    host_name = "localhost"
    user_name = "root"
    pwd = "9866850403"
    db_name = ""

    con = mysql.connector.connect(host=host_name, user=user_name, password=pwd, database=db_name)
    cur = con.cursor()

    sql = "show databases"
    cur.execute(sql)
    existing_dbs = cur.fetchall()
    print("Existing databases are as follows: ")
    for row in existing_dbs:
        print(row[0])

    print()
    db_name = (input("Enter a database name from the list to fetch tables: ")).lower()
    sql2 = ("use {}".format(db_name))
    cur.execute(sql2)
    print("'{}' database selected".format(db_name))

    sql3 = "show tables"
    cur.execute(sql3)
    table_list = cur.fetchall()
    print("Tables list in the database that you've selected '{}' are as follows:".format(db_name))
    for row in table_list:
        print(row[0])

    print()
    get_table_proprties = input("Enter a table name to get properties: ").lower()
    sql4 = ("describe {}".format(get_table_proprties))
    cur.execute(sql4)
    get_table_proprties_op = cur.fetchall()
    for row in get_table_proprties_op:
        print(row[0], row[1], row[2])

    print()
    table_name = input("Enter a table name to get details: ").lower()
    sql5 = ("select * from {}".format(table_name))
    cur.execute(sql5)
    table_data = cur.fetchall()
    for row in table_data:
        print("%5s %30s %15s %15s" % (row[0], row[1], row[2], row[3]))
except mysql.connector.Error as err:
    print(err)
else:
    cur.close()
    con.close()
