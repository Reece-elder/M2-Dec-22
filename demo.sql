-- Show me all Tables I've got
--SELECT * FROM INFORMATION_SCHEMA.TABLES;

--Viewing Data, we can view data with SELECT * FROM <table name>
--SELECT * FROM dept;

-- Pass in the * to see all columns, or specify the columns you want to see
--SELECT dept_name, sales_target FROM dept;

-- Sort all of the records by order_value
--SELECT * FROM sale ORDER BY order_value;

--SELECT * FROM sale WHERE order_value > 4;
-- Show all sales where contact code is MM

--SELECT * FROM sale WHERE contact_code = 'MM';

--select * from sale where company_order_no = 'AC12'; 

SELECT * FROM dept;

-- To insert data into a table you need to know what type of data its expecting
-- varchar - text, letters and numbers can have UP TO its bracket length, but can be lower
-- char(12) - text and letters but MUST be that character length 
-- INSERT INTO dept VALUES(6, 'QA teaching', 'Reece Elder', 50.52);

-- Updating records requires the use of SET and WHERE 
-- Update a record WHERE id = 6
UPDATE dept SET dept_name = 'QA Engineering' WHERE dept_no = 6;

-- Delete from table where ID = 
DELETE dept WHERE dept_no = 6;

DELETE dept WHERE dept_no > 0;

-- Creating our own SQL Table
CREATE TABLE item ( 
item_id int NOT NULL, 
item_name varchar(30) NOT NULL, 
price decimal(10, 2) NOT NULL,
PRIMARY KEY(item_id)
);

INSERT INTO item VALUES (1, 'PSP', 89.50);
SELECT * FROM item;

