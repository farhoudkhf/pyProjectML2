import configparser
import os
import psycopg2

config = configparser.ConfigParser()
config.read('config/config.ini')

db_host = config['database']['host']
db_port = config['database']['port']
db_user = config['database']['username']
db_password = os.environ.get('DB_PASSWORD', config['database']['password']) #Use environment variable if set
db_name = config['database']['database']

#establishing the connection
conn = psycopg2.connect(
   database=db_name, user=db_user, password=db_password, host=db_host, port= db_port
)

#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving data
# cursor.execute('''SELECT * from product''')
sql = '''SELECT * from product'''

cursor.execute(sql)
column_names = [desc[0] for desc in cursor.description]
for i in column_names:
    print(i)

#Fetching 1st row from the table
result = cursor.fetchone();
print(result)



#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()
