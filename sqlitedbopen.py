import sqlite3

    # Create a SQL connection to our SQLite database
con = sqlite3.connect('C:\\Users\\USER\\.ipython\\profile_default\\history.sqlite')

cur = con.cursor()

query = 'DELETE FROM sessions'
table_list = [a for a in cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
    # The result of a "cursor.execute" can be iterated over by row

# cur.execute(query)
for row in cur.execute("SELECT * from history"):
    print(row)
print(table_list)

    # Be sure to close the connection
con.close()