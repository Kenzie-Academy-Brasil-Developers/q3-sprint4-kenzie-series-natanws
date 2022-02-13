from http import HTTPStatus
import psycopg2
from flask import request
from . import config
from psycopg2 import sql

class Series:
    @staticmethod
    def create_table():
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        query = "CREATE TABLE IF NOT EXISTS ka_series(id BIGSERIAL PRIMARY KEY, serie VARCHAR(100) NOT NULL UNIQUE, seasons INTEGER NOT NULL, released_date DATE NOT NULL, genre VARCHAR(50) NOT NULL, imdb_rating FLOAT NOT NULL);"

    @staticmethod
    def create_series():
        data = request.get_json()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        new_data = (data["serie"],data["seasons"],data["released_date"],data["genre"],data["imdb_rating"],)
        query = "CREATE TABLE IF NOT EXISTS ka_series(id BIGSERIAL PRIMARY KEY, serie VARCHAR(100) NOT NULL UNIQUE, seasons INTEGER NOT NULL, released_date DATE NOT NULL, genre VARCHAR(50) NOT NULL, imdb_rating FLOAT NOT NULL); INSERT INTO ka_series (serie, seasons, released_date, genre, imdb_rating) VALUES (%s, %s, %s, %s, %s);"
        cur.execute(query, new_data)
        conn.commit()

        cur.close()
        conn.close()

        return data
    
    @staticmethod
    def get_all_series():
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        cur.execute(
            """
                CREATE TABLE IF NOT EXISTS ka_series(
                    id              BIGSERIAL PRIMARY KEY, 
                    serie           VARCHAR(100) NOT NULL UNIQUE, 
                    seasons         INTEGER NOT NULL, 
                    released_date   DATE NOT NULL, 
                    genre           VARCHAR(50) NOT NULL, 
                    imdb_rating     FLOAT NOT NULL);
                SELECT * FROM ka_series;
            """
        )
        
        getting_data = cur.fetchall()

        FIELDNAMES = ["id", "serie", "seasons", "released_date", "genre", "imdb_rating"]
        processed_data = [dict(zip(FIELDNAMES, row)) for row in getting_data]

        conn.commit()
        cur.close()
        conn.close()

        return processed_data
    def get_series_by_id(id):
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        query = f"SELECT * FROM ka_series WHERE id = {id};"

        cur.execute(query)

        serie = cur.fetchone()

        conn.commit()
        cur.close()
        conn.close()

        return serie