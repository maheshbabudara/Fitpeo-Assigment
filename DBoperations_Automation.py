#Insert, Update, Delete:

import pyodbc

#Queries:
update_query= "update student set name='rony' where id=4"
delete_query= "Delete from student where id=3"

try:
    # Create connection string:
    connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=my_database;UID=my_username;PWD=my_password'

    # Connect to DB:
    connection = pyodbc.connect(connection_string)

    # create an curosr:
    cursor = connection.cursor()  # Cursore is an buffer Area or Temporay memory

    # Execute a SQL query through cursore
    # cursor.execute("insert into student (name,city) values('rony','bang')")
    cursor.execute(update_query)  # updating record
    cursor.execute(delete_query)  # deleting record

    connection.commit()  # will make permanent transcation/changes

    cursor.close()  # closing cursor
    connection.close()  # closing connection
except Exception as e:
    print(e, 'is an issue')

print("Finished")
