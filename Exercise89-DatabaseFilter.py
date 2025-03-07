# please download the database file database.db. The file contains a table with 50 countries name along with their area in sq km and population.
# please use python to print out those countries that have an area greater than 2,000,000.

# import sqlite3

# # Connect to the database file
# conn = sqlite3.connect("database.db")
# cur = conn.cursor()

# # Execute the SQL query
# cur.execute("SELECT * FROM countries WHERE area > 2000000")

# # Fetch and print the results
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# # Close the database connection
# conn.close()



import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

# List all tables in the database
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()

print("Tables in database:", tables)

conn.close()
