#!/usr/bin/python3

"""
    This script prints query results
    filtering all entries that match given
    argument from a database table in the
    terminal
"""

if __name__ == "__main__":
    import sys
    import MySQLdb
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    query_object = str(sys.argv[4])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY ID ASC"
        .format(query_object)
    )
    for name in cur.fetchall():
        print(name)
