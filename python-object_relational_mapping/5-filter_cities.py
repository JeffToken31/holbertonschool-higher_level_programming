#!/usr/bin/python3
"""
This module use mysqldb to connect with database
it allow to user to shearch states by argument
with protection of sql injection
"""
import MySQLdb as ms
import sys


def main():
    """
    This fonction use enumerate() to
    success in getting the correct output
    """
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

    cur.execute("""
                SELECT cities.name
                FROM cities
                INNER JOIN states ON states.id = cities.state_id
                WHERE states.name = %s
                ORDER BY cities.id ASC
                """, [sys.argv[4]])

    rows = cur.fetchall()
    for i, row in enumerate(rows):
        if i > 0:
            print(", ", end="")
        print(row[0], end="")
    print()

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
