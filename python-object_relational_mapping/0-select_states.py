#!/usr/bin/python3
"""
This module use mysqldb to connect with database
"""
import MySQLdb as ms
import sys



db = ms.connect(
    host = "localhost",
    port = 3306,
    user = sys.argv[1],
    password = sys.argv[2],
    database = sys.argv[3]
)

cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
db.close()
