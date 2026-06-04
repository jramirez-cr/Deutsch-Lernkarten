import sqlite3

connection = sqlite3.connect('data/lernkarten.db')

cursor = connection.cursor()

connection.close()

