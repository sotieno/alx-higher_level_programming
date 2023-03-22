#!/usr/bin/python3
"""Lists all cities by state"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    # Create connection to MySQL server
    conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                           user=argv[1], passwd=argv[2], db=argv[3])
    # Prepare cursor object
    cur = conn.cursor()

    # Execute the SQL query
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        LEFT JOIN states
        ON cities.state_id = states.id
        ORDER BY cities.id ASC;
        """)

    # Fetch all the rows
    query_rows = cur.fetchall()

    # Print the rows
    for row in query_rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    conn.close()
