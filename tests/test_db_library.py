import sqlite3
import pytest
from db_library import update_difficulty
from pathlib import Path
from tests.conftest import insert_word


def test_update_difficulty_updates_the_value(test_db: Path) -> None:
    """Verifies that difficulty of a word is updated correctly in the database"""
    #Arrange
    word_id = insert_word(test_db, "sustantivo_nuevo")


    #Act
    update_difficulty(word_id, 2)

    #Assert
    connection = sqlite3.connect(test_db)
    cursor = connection.cursor()
    cursor.execute("SELECT dificultad FROM palabras WHERE id = ?", (word_id,))
    row = cursor.fetchone()
    connection.close()
    assert row[0] == 2

def test_update_difficulty_invalid_value_raises_error(test_db: Path) -> None:
    """Verifies that difficulty of a word cannot be outside valid range"""
    #Arrange
    word_id = insert_word(test_db, "sustantivo_nuevo")

    #Act/Assert

    with pytest.raises(sqlite3.IntegrityError):
        update_difficulty(word_id, 5)

    connection = sqlite3.connect(test_db)
    cursor = connection.cursor()
    cursor.execute("SELECT dificultad FROM palabras WHERE id = ?", (word_id,))
    row = cursor.fetchone()
    connection.close()
    assert row[0] == 0
