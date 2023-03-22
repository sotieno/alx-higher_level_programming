#!/usr/bin/python3
"""Lists all states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Create connection to MySQL server
    conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                           user=argv[1], passwd=argv[2], db=argv[3])
    # Prepare a cursor object
    cur = conn.cursor()

    # Execute the SQL query
    cur.execute("""SELECT * FROM states ORDER BY states.id ASC""")

    # Fetch all the rows
    query_rows = cur.fetchall()

    # Print the rows
    for row in query_rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    conn.close()
