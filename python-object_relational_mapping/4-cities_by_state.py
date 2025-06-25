#!/usr/bin/python3
"""
This module use mysqldb to connect with database
"""
import MySQLdb as ms
import sys


def main():
    """
    This function display all cities by states
    """

    if len(sys.argv) != 4:
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
                SELECT cities.id, cities.name, states.name
                FROM cities
                INNER JOIN states ON states.id = cities.state_id
                ORDER BY cities.id ASC
                """)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
