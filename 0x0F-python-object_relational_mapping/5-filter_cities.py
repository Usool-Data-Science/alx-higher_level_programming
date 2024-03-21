#!/usr/bin/python3
"""Lists all cities from the database"""
import MySQLdb
import sys

if __name__ == "__main__":
    user_state = sys.argv[4]
    connection = MySQLdb.connect(host='localhost',
                                 user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3])
    cursor = connection.cursor()
    cursor.execute("""
                   SELECT cities.name FROM cities
                   INNER JOIN states ON states.id = cities.state_id
                   WHERE states.name = (%s)
                   """, (user_state, ))
    all_cities = cursor.fetchall()
    city_list = [city[0] for city in all_cities]
    print(*city_list, sep=', ')
    cursor.close()
    connection.close()
