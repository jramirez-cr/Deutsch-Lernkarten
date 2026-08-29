import sqlite3
import random


DB_PATH: str = "data/lernkarten.db"
WEIGHTS: dict[int, int] = {0:4, 1:1, 2:3, 3:5}

def get_connection(db_path: str = DB_PATH) -> sqlite3.Connection:
    """Establish a connection to the database."""
    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    connection.row_factory = sqlite3.Row
    return connection

def next_word() -> dict:
    """Get the next word from the database."""
    connection = get_connection(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("SELECT id, dificultad FROM palabras")
    rows = cursor.fetchall()
    ids = [row["id"] for row in rows]
    weights = [WEIGHTS[row["dificultad"]] for row in rows]
    chosen_id = random.choices(ids, weights=weights, k=1)[0]
    cursor.execute("SELECT * FROM palabras WHERE id = ?", (chosen_id,))
    word = cursor.fetchone()
    connection.close()
    complete_word = load_details(dict(word))
    return complete_word

def load_details(word: dict) -> dict:
    """Loads the details of word from the database."""
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT texto_de AS de, texto_es as es FROM oraciones WHERE palabra_id = ?", (word["id"],))
    sentences = [dict(row) for row in cursor.fetchall()]
    cursor.execute("SELECT pronombre, valor FROM conjugaciones WHERE palabra_id = ?", (word["id"],))
    conjugations = {row["pronombre"]: row["valor"] for row in cursor.fetchall()}
    word["ejemplos"] = sentences
    if conjugations:
        word["conjugacion"] = conjugations
    connection.close()
    return word

def update_difficulty(word_id: int, difficulty: int) -> None:
    """Updates the difficulty of the word from the database."""
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE palabras SET dificultad = ?, ultima_vez = CURRENT_TIMESTAMP WHERE id = ?", (difficulty, word_id))
    connection.commit()
    connection.close()
