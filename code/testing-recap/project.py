import sqlite3 as sqlite

def connectDB(db_name):
    conn = sqlite.connect("db_name")
    return conn

def createCursor(conn):
    cursor = conn.cursor()
    return cursor

def commitDB(conn):
    conn.commit()
    return True

def createDB(cursor):
    sql_file = open("test.sql")
    sql_string = sql_file.read()
    cursor.executescript(sql_string)
    print(cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall())

# def runCode():
#     conn = connectDB("test-db")
#     cursor = createCursor(conn)
#     # createDB(cursor)
#     commitDB(conn)

conn = connectDB("test-db")
cursor = createCursor(conn)


def viewAllOrders():
    query = "SELECT * FROM orders"
    data = cursor.execute(query)
    return data.fetchall()

def createOrder(name, drink):
    query = f"INSERT INTO orders (customer_name, drink) VALUES ('{name}', '{drink}');"
    cursor.execute(query)
    return True

# When testing our functions we check what they return
# We validate what they return compared to what we expect they should return

print(viewAllOrders())

def test_viewAllOrders():
    # Arrange - I gather all resources needed for the test
    result = [] 
    expect = [(1, 'test name', 'test drink')]

    # Act - Run the thing I am testing
    result = viewAllOrders()

    # Assert - Checking what the test returned
    assert result == expect

def test_createOrder():
    # Arrange - I gather all resources needed for the test
    result = ""
    testName = "abc"
    testDrink = "123"

    # Act - Run the thing I am testing
    result = createOrder(testName, testDrink)

    # Assert - Checking what the test returned
    assert result == True
