#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], charset="utf8")

    cur = conn.cursor()

    query = "SELECT cities.name FROM cities \
             INNER JOIN states ON cities.state_id = states.id \
             WHERE states.name = %s"

    cur.execute(query, (sys.argv[4],))

    rows = cur.fetchall()

    city_names = [row[0] for row in rows]

    print(", ".join(city_names))

    cur.close()
    conn.close()
