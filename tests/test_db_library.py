import sqlite3
from db_library import update_difficulty

def test_update_difficulty_updates_the_value(test_db):
    """Verifies that difficulty of a word is updated correctly in the database"""
    #Arrange
    connection = sqlite3.connect(test_db)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO palabras (id, palabra, traduccion, categoria) VALUES(?,?,?,?)",
                   (1, "wort", "palabra", "categoria"))
    connection.commit()
    connection.close()

    #Act
    update_difficulty(1, 2)

    #Assert
    connection = sqlite3.connect(test_db)
    cursor = connection.cursor()
    cursor.execute("SELECT dificultad FROM palabras WHERE id = ?", (1,))
    row = cursor.fetchone()
    connection.close()
    assert row[0] == 2


