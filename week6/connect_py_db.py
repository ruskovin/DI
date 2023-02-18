import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'tryhackme8'
DATABASE = 'Hollywood'

connection = psycopg2.connect(host=HOSTNAME, user= USERNAME, password = PASSWORD, dbname=DATABASE )

cursor = connection.cursor()

query1 = 'SELECT * from actors'
query2 = 'SELECT producers.prod_first_name, producers.prod_last_name, movies.movie_title From producers LEFT JOIN movies on movie_id = producer_movie_id'

cursor.execute(query1)
result = cursor.fetchall()

cursor.execute(query2)
result2 = cursor.fetchall()

connection.close()

for item in result:
    print(item)

print('********************************')
print('********************************')
print('********************************')
print('********************************')
print('********************************')

for item in result2:
    print(item)
