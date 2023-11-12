import mysql.connector
from decouple import config

# Read database connection details from .env file
db_config = {
    'user': config('DATABASE_USER'),
    'password': config('DATABASE_PASSWORD'),
    'host': config('DATABASE_HOST'),
    'port': config('DATABASE_PORT', cast=int),
    'database': config('DATABASE_NAME'),
}

# Establish a connection to the database
connection = mysql.connector.connect(**db_config)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Example: Execute a simple query
cursor.execute("SELECT * FROM monarchs")

# Fetch the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()

print('mysql script completed')
