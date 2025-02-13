#!/usr/bin/python3
'''script that lists all states from the database hbtn_0e_0_usa'''
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306)

    state = sys.argv[4]

    cursor = db.cursor()

    cursor.execute('''SELECT cities.name
    FROM cities
    INNER JOIN states ON cities.state_id=state_id
    WHERE states.name=%s
    ORDER BY cities.id;''', (state,))

    result = cursor.fetchall()

    city_names = [row[0] for row in result]
    cities_str = ', '.join(city_names)

    print(cities_str)

    cursor.close()
    db.close()
