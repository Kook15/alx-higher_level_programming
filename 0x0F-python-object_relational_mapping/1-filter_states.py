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

    cursor = db.cursor()

    cursor.execute('SELECT * FROM states WHERE (name LIKE "N%") ORDER BY id;')

    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()
