import sqlite3
import pytest
from db_library import update_difficulty, load_details
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

def test_load_details_verb_returns_conjugations_and_examples(test_db: Path) -> None:
    """Verifies that details of verbs conjugations and examples are returned correctly"""
    #Arrange
    word_id = insert_word(test_db, "verbo_irregular_con_todo")

    #Act
    complete_word = load_details({"id" : word_id})

    #Assert
    assert "ejemplos" in complete_word
    assert len(complete_word["ejemplos"]) == 2
    assert "conjugacion" in complete_word
    assert complete_word["conjugacion"]["du"] == "fährst"

def test_load_details_word_without_examples_returns_empty_list(test_db: Path) -> None:
    """Verifies that details of words without examples returns empty list"""
    #Arrange
    word_id = insert_word(test_db, "palabra_sin_ejemplos")

    #Act
    word_without_examples = load_details({"id" : word_id})

    #Assert
    assert word_without_examples["ejemplos"] == []
    assert "conjugacion" not in word_without_examples

def test_load_details_regular_verb_returns_examples_not_conjugations(test_db: Path) -> None:
    """Verifies that regular verbs examples are returned correctly without conjugations"""
    #Arrange
    word_id = insert_word(test_db, "verbo_regular")

    #Act
    verb = load_details({"id" : word_id})

    #Assert
    assert "conjugacion" not in verb
    assert len(verb["ejemplos"]) == 1
