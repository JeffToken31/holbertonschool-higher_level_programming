#!/usr/bin/python3
"""
This module use mysqldb to connect with database
it allow to user to shearch states by argument
"""
import sys
import MySQLdb


if __name__ == '__main__':
    """
    This function filter keep args to filter states
    with a guard for sql injection
    """

    if len(sys.argv) != 5:
        print("Incorrecte call to scripts")
        exit()

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute(
        """
        SELECT * FROM states WHERE name = '{}'
        ORDER BY states.id ASC;
        """.format(sys.argv[4])
        )

    rows = cur.fetchall()

    for row in rows:
        print("{}".format(row))

    cur.close()
    db.close()
