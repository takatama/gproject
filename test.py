import sqlite3

conn = sqlite3.connect('gdb.db')
for row in conn.execute('SELECT * FROM questions'):
    print(row)
