import mysql.connector

# Establish the database connection
conn = mysql.connector.connect(host='localhost', username='root', password='arsalan123', database='cms')

# Check if the connection is successful
if conn.is_connected():
    print("Connected to the database.")
else:
    print("Failed to connect to the database.")

# Create a cursor object
my_cursor = conn.cursor()

# Dummy data for insertion
dummy_data = {
    'Case_id': '2',
    'Criminal_no': '3423',
    'Criminal_name': 'John Doe',
    'Nick_name': 'Johnny',
    'arrest_date': '2024-02-14',
    'dateOfcrime': '2024-02-10',
    'address': '123 Main Street, City, Country',
    'age': 30,
    'occupation': 'Software Engineer',
    'BirthMark': 'Mole on left cheek',
    'crimeType': 'Robbery',
    'fatherName': 'Michael Doe',
    'gender': 'Male',
    'wanted': 'Yes'
}

# Insert query
insert_query = """
INSERT INTO criminal1 (Case_id, Criminal_no, Criminal_name, Nick_name, arrest_date, dateOfcrime, address, age, occupation, BirthMark, crimeType, fatherName, gender, wanted)
VALUES (%(Case_id)s, %(Criminal_no)s, %(Criminal_name)s, %(Nick_name)s, %(arrest_date)s, %(dateOfcrime)s, %(address)s, %(age)s, %(occupation)s, %(BirthMark)s, %(crimeType)s, %(fatherName)s, %(gender)s, %(wanted)s)
"""

# Execute the insert query with dummy data
my_cursor.execute(insert_query, dummy_data)

# Commit the transaction
conn.commit()

# Close cursor and connection
my_cursor.close()
conn.close()
