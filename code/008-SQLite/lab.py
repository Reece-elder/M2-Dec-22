import sqlite3 as sqlite

conn = sqlite.connect("penguin-db")

cursor = conn.cursor()

# sql_file = open("penguin.sql")
# sql_string = sql_file.read()
# cursor.executescript(sql_string)

# print(cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall())
# print(cursor.execute("SELECT * FROM penguins").fetchall())

def runQuery(query):
    data = cursor.execute(query)
    return data

def addPenguin():
    query = "INSERT INTO penguins (fish_eaten, dancing, penguin_name) VALUES (123, true, 'new_penguin');"
    runQuery(query)
    return True

def delPenguin(id):
    query = f"DELETE FROM penguins WHERE penguin_id = {id}"
    runQuery(query)
    return True

def viewAllPenguins():
    query = "SELECT * FROM penguins"
    data = runQuery(query)
    return data.fetchall()

def viewPenguinId(id):
    query = f"SELECT * FROM penguins WHERE penguin_id = {id}"
    data = runQuery(query)
    return data.fetchall()

def updatePenguinNameById(id, value):
    query = f"UPDATE penguins SET penguin_name = {value} WHERE penguin_id = {id}"
    data = runQuery(query)
    return data.fetchall()

def updatePenguinId(id, field, value):
    query = f"UPDATE penguins SET {field} = {value} WHERE penguin_id = {id}"
    data = runQuery(query)
    return data.fetchall()

def createPenguin(fish, dancing, name):
    query = f"INSERT INTO penguins (fish_eaten, dancing, penguin_name) VALUES ({fish}, {dancing}, '{name}');"
    data = runQuery(query)
    return data.fetchall()

# createPenguin(50, False, "Geoff")
print(viewAllPenguins()) # Returns a list
# How can I display all of my data in a list?
for penguin in viewAllPenguins():
    print(penguin[3])

print(viewPenguinId(5))

# CRUD app - Foundation of ALL SOFTWARE EVER 
# Create
# Read
# Update
# Delete 


conn.commit()

