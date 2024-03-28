import yaml
import mysql.connector

def execute_dsl_update_record(command, parameters_list):
    if command != "UPDATE_RECORD":
        print("Invalid command")
        return
    
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='arsalan123', database='cms')
        if conn.is_connected():
            print("Connected to the database.")
        else:
            print("Failed to connect to the database.")
            return
        
        my_cursor = conn.cursor()
        sql_query = f"UPDATE criminal1 SET \
            Criminal_no=%s, \
            Criminal_name=%s, \
            Nick_name=%s, \
            arrest_date=%s, \
            dateOfcrime=%s, \
            address=%s, \
            age=%s, \
            occupation=%s, \
            BirthMark=%s, \
            crimeType=%s, \
            fatherName=%s, \
            gender=%s, \
            wanted=%s \
            WHERE Case_id=%s"
        
        for parameters in parameters_list:
            values = (
                parameters['criminal_no'], 
                parameters['name'], 
                parameters['nickname'], 
                parameters['arrest_date'], 
                parameters['date_of_crime'], 
                parameters['address'], 
                parameters['age'], 
                parameters['occupation'], 
                parameters['birthmark'], 
                parameters['crime_type'], 
                parameters['father_name'], 
                parameters['gender'], 
                parameters['wanted'], 
                parameters['case_id']
            )
            my_cursor.execute(sql_query, values)
        
        conn.commit()
        print("Records updated successfully")
    except Exception as e:
        print("Error:", str(e))
    finally:
        conn.close()

# Load YAML file
with open('update_record.yaml', 'r') as yaml_file:
    yaml_content = yaml.load(yaml_file, Loader=yaml.FullLoader)

# Execute DSL command
dsl_command = yaml_content['UpdateRecord']['Command']
dsl_parameters = yaml_content['UpdateRecord']['Parameters']

# Example usage:
dsl_parameters_example = [
    {
        "case_id": "3232",
        "criminal_no": "4343",
        "name": "John Doe",
        "nickname": "JD",
        "arrest_date": "2024-03-28",
        "date_of_crime": "2024-03-25",
        "address": "123 Main St",
        "age": "30",
        "occupation": "Programmer",
        "birthmark": "Mole on left cheek",
        "crime_type": "Theft",
        "father_name": "Michael Doe",
        "gender": "Male",
        "wanted": "No"
    },
    {
        "case_id": "343",
        "criminal_no": "222",
        "name": "Jane Smith",
        "nickname": "JS",
        "arrest_date": "2024-03-29",
        "date_of_crime": "2024-03-26",
        "address": "456 Oak St",
        "age": "35",
        "occupation": "Teacher",
        "birthmark": "Scar on forehead",
        "crime_type": "Assault",
        "father_name": "David Smith",
        "gender": "Female",
        "wanted": "Yes"
    }
]

execute_dsl_update_record(dsl_command, dsl_parameters_example)
