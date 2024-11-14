import pyodbc


try:

    connection_string="DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=my_database;UID=my_username;PWD=my_password"
    connection=pyodbc.connect(connection_string)
    cursor=connection.cursor()
    cursor.execute("select * from student")  #data stored in cursor, becoz this select cmd will return data

    for row in cursor:
        print(row[0],row[1],row[2])
    cursor.close()
    connection.close()

except Exception as e:
    print(e, 'is an issue')

print("fininished................")