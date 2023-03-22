#!/usr/bin/python3
"""Filter states by user input"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    # Create connection to MySQL server
    conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                           user=argv[1], passwd=argv[2], db=argv[3])
    # Prepare a cursor object
    cur = conn.cursor()

    # Use "format" method to create the SQL query with the user input
    q = """
        SELECT * FROM states
        WHERE name
        LIKE BINARY '{}'
        ORDER BY states.id ASC
        """

    q = q.format(argv[4])

    # Execute the SQL query
    cur.execute(q)

    # Fetch all the rows
    query_rows = cur.fetchall()

    # Print the rows
    for row in query_rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    conn.close()
