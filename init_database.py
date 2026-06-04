import sqlite3

#Create Table

create_palabras: str = """
CREATE TABLE IF NOT EXISTS palabras (
id INTEGER NOT NULL PRIMARY KEY,
palabra TEXT NOT NULL,
traduccion TEXT NOT NULL,
categoria TEXT NOT NULL,
nivel TEXT NOT NULL DEFAULT 'A1',
plural TEXT,
dificultad INTEGER NOT NULL DEFAULT 0 CHECK (dificultad IN (0, 1 ,2 ,3)),
aciertos INTEGER NOT NULL DEFAULT 0,
fallos INTEGER NOT NULL DEFAULT 0,
ultima_vez TIMESTAMP
); 
"""


connection = sqlite3.connect('data/lernkarten.db')

cursor = connection.cursor()

cursor.execute(create_palabras)
connection.commit()


connection.close()

