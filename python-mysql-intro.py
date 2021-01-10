from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="sakila",
    ) as connection:
        print(connection)

        select_actors_query = """select * from actor limit 5"""
        with connection.cursor() as cursor:
            cursor.execute(select_actors_query)
            for actor in cursor.fetchall():
                print(actor)
except Error as e:
    print(e)