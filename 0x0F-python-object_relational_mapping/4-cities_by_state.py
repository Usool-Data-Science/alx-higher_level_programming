#!/usr/bin/python3
"""Lists all cities from the database"""
import MySQLdb
import sys

if __name__ == "__main__":
    connection = MySQLdb.connect(host='localhost',
                                 user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3])
    cursor = connection.cursor()
    cursor.execute("""
                   SELECT cities.id, cities.name, states.name FROM cities
                   INNER JOIN states ON states.id = cities.state_id
                   ORDER BY cities.id
                   """)
    all_cities = cursor.fetchall()
    for city in all_cities:
        print(city)

    cursor.close()
    connection.close()
