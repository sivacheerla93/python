import mysql.connector
import requests
import re

try:
    con = mysql.connector.connect(host="localhost", user="root", password="9866850403", database="mock")
    cur = con.cursor()

    print("Connection successful!")

    cur.execute("truncate countries")
    con.commit()
    print("Countries table truncated! New data will be inserted!!")

    resp = requests.get("https://restcountries.eu/rest/v2/all")
    for country in resp.json():
        if not re.fullmatch(r"[a-zA-Z]+", country["capital"]):
            continue
        if not re.fullmatch(r"[a-zA-Z]+", country["name"]):
            continue
        print("{:5s}{:60s}{}".format(country["alpha2Code"], country["name"], country["capital"]))
        cur.execute(
            "insert into countries values('{}','{}','{}')".format(country["alpha2Code"], country["name"],
                                                                  country["capital"]))
        if cur.rowcount == 1:
            con.commit()
            print("Inserted to countries table...!")
        else:
            con.rollback()
    cur.close()
except Exception as ex:
    print("Error occured: ", ex)
finally:
    con.close()
    print()
    print("Countries data insertion completed!")
