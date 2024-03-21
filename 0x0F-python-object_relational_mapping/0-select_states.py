#!/usr/bin/env python3
import sys
import MySQLdb

connection = MySQLdb.connect(host='localhost:3306',
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
cursor = connection.cursor()
cursor.execute('SELECT `id`,`name` FROM states ORDER BY `id`')
all_states = cursor.fetchall()
for state in all_states:
    print(state)
