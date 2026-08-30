import sqlite3

#Create Tables for the program

with open("schema.sql", "r", encoding="utf-8") as schema:
    sql_schema = schema.read()

connection = sqlite3.connect('data/lernkarten.db')
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")
cursor.executescript(sql_schema)
connection.commit()
connection.close()

