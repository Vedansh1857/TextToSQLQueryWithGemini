import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table
cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""
cursor.execute(table_info)

## Insert Some more records
cursor.execute('''
    INSERT INTO student (NAME, CLASS, SECTION, MARKS) VALUES 
    ('Alice Johnson', '10', 'A', 85),
    ('Bob Smith', '10', 'A', 78),
    ('Charlie Brown', '10', 'B', 92),
    ('Diana Prince', '10', 'B', 88),
    ('Evan Wright', '10', 'C', 74),
    ('Fiona Davis', '10', 'C', 81),
    ('George Clark', '11', 'A', 69),
    ('Hannah Moore', '11', 'A', 90),
    ('Ian White', '11', 'B', 87),
    ('Jenna Adams', '11', 'B', 75),
    ('Kyle Thompson', '11', 'C', 82),
    ('Laura Baker', '11', 'C', 94),
    ('Michael Wilson', '12', 'A', 76),
    ('Nina Scott', '12', 'A', 88),
    ('Oliver Turner', '12', 'B', 91),
    ('Paula Lee', '12', 'B', 84),
    ('Quinn Hall', '12', 'C', 79),
    ('Rachel Young', '12', 'C', 85),
    ('Sam Harris', '9', 'A', 73),
    ('Tina King', '9', 'A', 81),
    ('Umar Collins', '9', 'B', 95),
    ('Vera Martin', '9', 'B', 89),
    ('Will Rogers', '9', 'C', 78),
    ('Xena Phillips', '9', 'C', 82),
    ('Yara Edwards', '8', 'A', 91),
    ('Zack Foster', '8', 'A', 86),
    ('Ava Reed', '8', 'B', 77),
    ('Ben Green', '8', 'B', 80),
    ('Cara Bell', '8', 'C', 88),
    ('Dean Parker', '8', 'C', 85),
    ('Ella Evans', '7', 'A', 83),
    ('Frank Hughes', '7', 'A', 79),
    ('Grace Ward', '7', 'B', 91),
    ('Henry Cook', '7', 'B', 84),
    ('Ivy Sanders', '7', 'C', 76),
    ('Jack Ross', '7', 'C', 88),
    ('Kate Nelson', '6', 'A', 77),
    ('Leo Diaz', '6', 'A', 92),
    ('Mia Perez', '6', 'B', 81),
    ('Noah Carter', '6', 'B', 85),
    ('Olivia Myers', '6', 'C', 87),
    ('Paul Murphy', '6', 'C', 79),
    ('Riley Hughes', '5', 'A', 74),
    ('Sophia Brooks', '5', 'A', 89),
    ('Thomas Simmons', '5', 'B', 91),
    ('Uma Rivera', '5', 'B', 78)
'''
)

## Display All the records
print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes in the databse
connection.commit()
connection.close()