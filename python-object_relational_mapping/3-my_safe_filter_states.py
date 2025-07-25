#!/usr/bin/python3
"""
This module use mysqldb to connect with database
it allow to user to shearch states by argument
with protection of sql injection
"""
import MySQLdb as ms
import sys


def main():

    if len(sys.argv) != 5:
        print("Incorrecte call to scripts")
        return 1

    try:
        db = ms.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
        )
    except ms.MySQLError as e:
        print("connection failed: {}".format(e))
        return 1

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = %s "
        "ORDER BY states.id ASC", [sys.argv[4]]
        )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
