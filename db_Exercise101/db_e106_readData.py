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

# print(f"Connecting to {db_host}:{db_port} as {db_user} to database {db_name}")
# ----


#establishing the connection
conn = psycopg2.connect(
   database=db_name, user=db_user, password=db_password, host=db_host, port= db_port
)

#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving data
cursor.execute('''SELECT * from product''')

#Fetching 1st row from the table
result = cursor.fetchone();
print(result)

#Fetching 1st row from the table
result = cursor.fetchall();
print(result)

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()