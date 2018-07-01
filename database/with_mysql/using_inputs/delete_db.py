import mysql.connector

try:
    con = mysql.connector.connect(host="localhost", user="root", password="9866850403")
    cur = con.cursor()

    # list existing databases to choose one to delete!
    cur.execute("show databases")
    existing_dbs = cur.fetchall()
    print("Existing databases are as follows: ")
    for row in existing_dbs:
        print(row[0])

    # delete a db from existing databases!
    delete_db = (input("Enter database name to delete: ")).lower()
    cur.execute("show databases like '%s'" % delete_db)
    show_db_to_delete = cur.fetchall()
    db = ""
    for row in show_db_to_delete:
        db = row[0]
    if db == delete_db:
        print("'{}'".format(delete_db), "database exists!")
        confirm = input("Are you sure to delete db '{}'? (yes or no): ".format(delete_db))
        if confirm == 'yes':
            sql = ("drop database {}".format(delete_db))
            cur.execute(sql)
            print("'{}' database deleted successfully!".format(delete_db))
        elif confirm == 'no':
            print("'{}'".format(delete_db), "database not deleted!")
        else:
            print("Invalid option! try again!!")
            con.rollback()
    else:
        print("'{}' database not exists!".format(delete_db))
except mysql.connector.Error as err:
    print("Error found: ", err)
else:
    cur.close()
    con.commit()
    con.close()
    print("Thank you! See you again!!")
