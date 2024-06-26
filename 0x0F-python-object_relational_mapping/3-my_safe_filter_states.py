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
    statement = "SELECT * FROM states WHERE name = %s ORDER BY ID ASC"
    query_object = str(sys.argv[4])
    cur = db.cursor()
    cur.execute(
        statement,
        (query_object,)
    )
    for name in cur.fetchall():
        print(name)
