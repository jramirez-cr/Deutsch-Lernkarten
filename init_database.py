import sqlite3

#Create Tables for the program

create_palabras: str = """
CREATE TABLE IF NOT EXISTS palabras (
    id INTEGER PRIMARY KEY,
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
create_conju: str = """
CREATE TABLE IF NOT EXISTS conjugaciones (
    id         INTEGER PRIMARY KEY, 
    palabra_id INTEGER NOT NULL REFERENCES palabras(id) ON DELETE CASCADE,
    pronombre  TEXT    NOT NULL, 
    valor      TEXT    NOT NULL, 
    UNIQUE (palabra_id, pronombre)
);
"""

create_oraciones: str = """
CREATE TABLE IF NOT EXISTS oraciones
(
    id         INTEGER PRIMARY KEY,
    palabra_id INTEGER NOT NULL REFERENCES palabras (id) ON DELETE CASCADE,
    texto_de   TEXT    NOT NULL,
    texto_es   TEXT    NOT NULL 
);
"""

connection = sqlite3.connect('data/lernkarten.db')

cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")
cursor.execute(create_palabras)
cursor.execute(create_conju)
cursor.execute(create_oraciones)


connection.commit()


connection.close()

