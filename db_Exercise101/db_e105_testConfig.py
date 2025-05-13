import configparser
import os

config = configparser.ConfigParser()
config.read('config/config.ini')

db_host = config['database']['host']
db_port = config['database']['port']
db_user = config['database']['username']
db_password = os.environ.get('DB_PASSWORD', config['database']['password']) #Use environment variable if set
db_name = config['database']['database']

print(f"Connecting to {db_host}:{db_port} as {db_user} to database {db_name}")
