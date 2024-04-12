#!/usr/bin/python3
"""
Script that displays all values in the states table
"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], charset="utf8")

    cur = conn.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id"

    cur.execute(query, (sys.argv[4],))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
