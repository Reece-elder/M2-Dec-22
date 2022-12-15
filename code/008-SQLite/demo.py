# Importing sqlite3 from libraries and calls it sqlite
import sqlite3 as sqlite

# Made our connection 
# connection = pyodbc.connect("192.78.36.58:mysql:3306/user/password")
connection = sqlite.connect("new-db") # If it doesn't exist.. create it

# cursor is an object created from our connection
local_cursor = connection.cursor() # .cursor() returns a cursor we can use 

admin_query = "SELECT * FROM sqlite_master"
create_query = "CREATE TABLE dogs (dog_id int NOT NULL, colour VARCHAR(20), breed VARCHAR(30), bark BOOLEAN, PRIMARY KEY(dog_id))"

def runQuery(query):
    data = local_cursor.execute(query) # our cursor should run our query
    return data

# def createQuery(query):
#     local_cursor.execute(query)
#     return True

# runQuery(create_query)

# fetchall() works like readlines(), reads the data from the file
# print(runQuery(admin_query).fetchall())

# Insert data into our table
insert_query = f"INSERT into dogs VALUES(2, 'Tri Colour', 'Corgi', true)"
select_query = "SELECT * FROM dogs"
runQuery(insert_query)
print(runQuery(select_query).fetchall())

# Sqlite ONLY persists data if it is commited
connection.commit()
