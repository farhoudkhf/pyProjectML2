import mysql.connector

mydb = mysql.connector.connect(
  host="your_host",
  user="your_user",
  password="your_password",
  database="your_database"
)

print(mydb)