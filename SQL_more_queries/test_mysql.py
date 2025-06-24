#!/usr/bin/env python3
import MySQLdb

# Remplace par tes infos de connexion
db = MySQLdb.connect(
    host="localhost",
    user="jeff",
    passwd=" ",
    db="hbtn_0d_tvshows"
)

cur = db.cursor()
cur.execute("SELECT VERSION()")
row = cur.fetchone()
print("Version MySQL:", row[0])

db.close()
