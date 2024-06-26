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
    state = sys.argv[4]
    statement = 'SELECT cities.name FROM states JOIN cities ' \
        'ON states.id = cities.state_id ' \
        'WHERE states.name = %s'
    cur = db.cursor()
    cur.execute(
        statement,
        (state,)
    )
    results = cur.fetchall()
    formatted_result = ', '.join([row[0] for row in results])
    print(formatted_result)
