import pyodbc as db

server = 'azure-jbatty.database.windows.net'
database = 'azure-jbatty'
username = 'xxx'
password = 'xxx'
port = 1433
driver = '{ODBC Driver 13 for SQL Server}'

connectionstring = f'DRIVER={driver};SERVER={server};PORT={port};DATABASE={database};UID={username};PWD={password}'

connection = db.connect(connectionstring)
cursor = connection.cursor()
