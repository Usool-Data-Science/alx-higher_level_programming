#!/usr/bin/python3
"""
Selects all states in the states table.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    user_input = sys.argv[4]
    try:
        connection = MySQLdb.connect(host='localhost',
                                     user=sys.argv[1],
                                     passwd=sys.argv[2],
                                     db=sys.argv[3], port=3306)
        cursor = connection.cursor()
        cursor.execute("""SELECT `id`,`name` FROM states
                       WHERE `name` = '{}'
                       ORDER BY `id`""".format(user_input))
        all_states = cursor.fetchall()
        for state in all_states:
            print(state)
    except MySQLdb.Error as e:
        print(e)
    finally:
        cursor.close()
        connection.close()
