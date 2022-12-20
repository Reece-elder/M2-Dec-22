CREATE TABLE orders (order_id INTEGER PRIMARY KEY AUTOINCREMENT, customer_name VARCHAR(40), drink VARCHAR(30));
INSERT INTO orders (customer_name, drink) VALUES ('test name', 'test drink');