#!/usr/bin/python3
"""Display values of states table by user input, prevent MySQL injection"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    # Create connection to MySQL server
    conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                           user=argv[1], passwd=argv[2], db=argv[3])
    # Prepare a cursor object
    cur = conn.cursor()

    # Execute the SQL query
    cur.execute("""
        SELECT *
        FROM states
        WHERE name = %s
        ORDER BY states.id ASC""", (argv[4], ))

    # Fetch all the rows
    query_rows = cur.fetchall()

    # Print the rows
    for row in query_rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    conn.close()
