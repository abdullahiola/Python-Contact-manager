import sqlite3

connection = sqlite3.connect('./phonenumber1.db')

# create a cursor for executing queries
cursor = connection.cursor()

# to execute a query

query_string = '''
CREATE TABLE if not exists contact(
    `contactId` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `firstname` TEXT NOT NULL,
    `lastName` TEXT,
    `email` TEXT,
    `phone` TEXT NOT NULL
)
'''

cursor.execute(query_string)

# to close a database connection
# connection.close()
