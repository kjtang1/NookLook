from dotenv import load_dotenv
import os
import psycopg2

def connect_to_db():
    load_dotenv() # get db password
    password = os.getenv("DB_PASSWORD")

    connection = psycopg2.connect(
        dbname='nooklook',
        user='postgres',
        password=password,
        host='localhost',
        port='5432',
    )
    return connection

