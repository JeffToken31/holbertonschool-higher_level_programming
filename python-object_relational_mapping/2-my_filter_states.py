#!/usr/bin/python3
"""
This module use mysqldb to connect with database
it allow to user to shearch states by argument
"""
import MySQLdb as ms
import sys


if __name__ == '__main__':
    """
    This function filter keep args to filter states
    with a guard for sql injection
    """

    if len(sys.argv) != 5:
        print("Incorrecte call to scripts")
        sys.exit(1)

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
        sys.exit(1)

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = '{}'"
        "ORDER BY states.id ASC".format(sys.argv[4])
        )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
