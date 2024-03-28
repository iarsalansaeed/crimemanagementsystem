import mysql.connector
from datetime import datetime
import uuid

# Establish the database connection
conn = mysql.connector.connect(host='localhost', user='root', password='arsalan123', database='cms')

# Check if the connection is successful
if conn.is_connected():
    print("Connected to the database.")
else:
    print("Failed to connect to the database.")

# Create a cursor object
my_cursor = conn.cursor()

# Insert query
insert_query = """
INSERT INTO criminal1 (Case_id, Criminal_no, Criminal_name, Nick_name, arrest_date, dateOfcrime, address, age, occupation, BirthMark, crimeType, fatherName, gender, wanted)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Insert 50 unique rows
for i in range(50):
    # Generate unique values for each column
    case_id = str(uuid.uuid4())
    criminal_no = str(uuid.uuid4())
    criminal_name = 'Nikil' + str(i)
    nick_name = 'Niku' + str(i)
    arrest_date = datetime.now().strftime('%Y-%m-%d')
    date_of_crime = datetime.now().strftime('%Y-%m-%d')
    address = 'Eat side chawl, Bombay, India'
    age = 30
    occupation = 'Labour'
    birth_mark = 'Mole on left cheek'
    crime_type = 'Robbery'
    father_name = 'Tripati'
    gender = 'Male'
    wanted = 'Yes'

    # Execute the insert query with unique dummy data
    my_cursor.execute(insert_query, (case_id, criminal_no, criminal_name, nick_name, arrest_date, date_of_crime, address, age, occupation, birth_mark, crime_type, father_name, gender, wanted))

# Commit the transaction
conn.commit()

# Close cursor and connection
my_cursor.close()
conn.close()
