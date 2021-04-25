#!/var/www/ThingsWeOwn/ThingsWeOwn/venv/bin/ python3
# # Things we own database
# Postgress database to keep inventory of all of the things that we own in preparation for moving.
#
# Schema design saved on [DBDesigner](https://app.dbdesigner.net/designer/schema/401855).
# TODO: Update, generic moved and more complex full.

# imports
import psycopg2
from psycopg2.extras import RealDictCursor
import pandas as pd
from contextlib import contextmanager
from typing import Dict
from dotenv import load_dotenv
from pathlib import Path
import os


env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

# **Variables**
#
# Declaring databse variables to allow for connection.

# Variables
database = os.getenv("DATABASE")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
host = os.getenv("DB_HOST")
host = "localhost"
port = os.getenv("DB_PORT")

# ## Context manager
#
# Create a context manager to handle connection to the postgres database and ensure that it is closed.

# Database context manger


@contextmanager
def connect(database=database, user=user, password=password, host=host, port=port):
    conn = psycopg2.connect(database=database, user=user,
                            password=password, host=host, port=port)
    try:
        yield conn
    finally:
        conn.close()

# ## Setup functions
#
# - Create tables
# - Execute script


def execute_script(cur, script):
    with open(script) as s:
        query = s.read()
        cur.execute(query)


def create_tables(sql_path="./scripts/HouseMoving_postgres_create.sql"):
    with connect() as conn:
        cur = conn.cursor()
        execute_script(cur, sql_path)
        conn.commit()

# ## Insert functions
#
# - add_person()


def add_person(name: str, priority: int) -> Dict[str, int]:
    with connect() as conn:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            f"INSERT INTO \"Person\" values (\'{name.lower()}\', {priority});")
        conn.commit()
        cur.execute(
            f"SELECT * FROM \"Person\" WHERE \"Name\" = '{name.lower()}';")
        data = cur.fetchone()
    return data


def add_room(house: str, room: str) -> Dict[str, str]:
    with connect() as conn:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            f"INSERT INTO \"House\" values (\'{house.lower()} {room.lower()}\',\'{house.lower()}\', \'{room.lower()}\');")
        conn.commit()
        cur.execute(
            f"SELECT * FROM \"House\" WHERE \"House_pk\" = \'{house.lower()} {room.lower()}\';")
        data = cur.fetchone()
    return data


def add_item(name: str, room: str, owner: str, value=0, quant: int = 1,
             size: str = 'medium', priority: int = 0, fragile: bool = False,
             owned: bool = True, moved: bool = False, keeping: bool = True,
             notes: str = ""):
    with connect() as conn:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(f"""
            INSERT INTO \"Item\" values(
                \'{name.lower()}\',
                {quant},
                \'{size.lower()}\',
                {priority},
                {fragile},
                {owned},
                {moved},
                {keeping},
                {value},
                \'{owner.lower()}\',
                \'{notes}\',
                \'{room.lower()}\'
                )""")
        conn.commit()
        cur.execute(
            f"SELECT * FROM \"Item\" WHERE \"ItemName\" = \'{name.lower()}\';")
        data = cur.fetchone()
    return data

# ## Select functions
#
# - Select all
#


def select_all(table_name="Items"):
    with connect() as conn:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        execute_script(cur, "./scripts/select_all.sql")
        data = cur.fetchall()
    return data


def get_room_options():
    with connect() as conn:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT DISTINCT \"Room\" FROM \"House\";")
        data = cur.fetchall()
    return data


def get_house_options():
    with connect() as conn:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT DISTINCT \"HouseName\" FROM \"House\";")
        data = cur.fetchall()
    return data


def get_person_options():
    with connect() as conn:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT DISTINCT \"Name\" FROM \"Person\";")
        data = cur.fetchall()
    return data


def get_people():
    with connect() as conn:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM \"Person\";")
        data = cur.fetchall()
    return data


def get_rooms():
    with connect() as conn:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM \"House\";")
        data = cur.fetchall()
    return data


def get_items():
    with connect() as conn:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM \"Item\";")
        data = cur.fetchall()
    return data

# ## Delete functions


def delete_person(name):
    with connect() as conn:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            f"SELECT * FROM \"Person\" WHERE \"Name\" = \'{name.lower()}\';")
        data = cur.fetchone()
        cur.execute(
            f"DELETE FROM \"Person\" WHERE \"Name\" = \'{name.lower()}\';")
        conn.commit()
    return data


def delete_item(ItemName):
    with connect() as conn:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            f"SELECT * FROM \"Item\" WHERE \"ItemName\" = \'{ItemName.lower()}\';")
        data = cur.fetchone()
        cur.execute(
            f"DELETE FROM \"Item\" WHERE \"ItemName\" = \'{ItemName.lower()}\';")
        conn.commit()
    return data


def delete_room(house_room):
    with connect() as conn:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            f"SELECT * FROM \"House\" WHERE \"House_pk\" = \'{house_room.lower()}\';")
        data = cur.fetchone()
        cur.execute(
            f"DELETE FROM \"House\" WHERE \"House_pk\" = \'{house_room.lower()}\';")
        conn.commit()
    return data


def drop_all():
    print("DROP IT LIKE ITS HOT!")
    with connect() as conn:
        cur = conn.cursor()
        execute_script(cur, "./scripts/drop_all.sql")
        conn.commit()
