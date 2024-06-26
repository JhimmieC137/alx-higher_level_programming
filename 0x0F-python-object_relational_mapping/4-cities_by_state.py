#!/usr/bin/python3

"""
    This script prints query results
    filtering all cities
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
    statement = 'SELECT cities.id, cities.name, states.name '\
        'FROM states JOIN cities ON states.id = cities.state_id'
    cur = db.cursor()
    cur.execute(
        statement,
    )
    for name in cur.fetchall():
        print(name)
