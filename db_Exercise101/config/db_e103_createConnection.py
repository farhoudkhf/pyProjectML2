import psycopg2

conn = psycopg2.connect(database = "mydbproject01", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "1122",
                        port = 5432)

