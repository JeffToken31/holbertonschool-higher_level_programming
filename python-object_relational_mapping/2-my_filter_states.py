#!/usr/bin/python3
"""
This module use mysqldb to connect with database
it allow to user to shearch states by argument
"""
import sys
import MySQLdb


def main():
    """
    This function filter keep args to filter states
    with a guard for sql injection
    """

    if len(sys.argv) != 5:
        print("Incorrect call to scripts")
        exit()

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
        )
    except MySQLdb.MySQLError as e:
        print("connection failed: {}".format(e))
        exit()

    cur = db.cursor()
    cur.execute(
        """
        SELECT * FROM states WHERE BINARY name = '{}'
        ORDER BY states.id ASC;
        """.format(sys.argv[4])
        )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
