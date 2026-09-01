import pytest
import sqlite3
import pathlib
from typing import Iterator

#Schema Path
SCHEMA_PATH = pathlib.Path(__file__).parent.parent / 'schema.sql'

#Fixture
@pytest.fixture
def test_db(tmp_path, monkeypatch) -> Iterator[pathlib.Path]:
    db_file = tmp_path / "test.db"

    monkeypatch.setattr("db_library.DB_PATH", str(db_file)) #

    with open(SCHEMA_PATH, "r", encoding= "utf-8") as schema:
        sql_schema = schema.read()

    connection = sqlite3.connect(db_file)

    connection.executescript(sql_schema)
    connection.commit()
    connection.close()

    yield db_file

#Scenario word bank
TEST_WORDS = {
    "sustantivo_nuevo": {
        "palabra": "Kaffee",
        "traduccion": "café",
        "categoria": "sustantivo",
        "dificultad": 0,
        "ejemplos": [
            {"de": "Ich trinke Kaffee.", "es": "Bebo café."},
            {"de": "Der Kaffee ist heiß.", "es": "El café está caliente."},
        ],
    },
    "sustantivo_con_plural": {
        "palabra": "Buch",
        "traduccion": "libro",
        "categoria": "sustantivo",
        "dificultad": 0,
        "plural": "Bücher",
        "ejemplos": [
            {"de": "Das Buch ist gut.", "es": "El libro es bueno."},
        ],
    },
    "verbo_irregular_con_todo": {
        "palabra": "fahren",
        "traduccion": "ir en vehículo",
        "categoria": "verbo",
        "dificultad": 0,
        "conjugacion": {
            "du": "fährst",
            "er/sie/es": "fährt",
        },
        "ejemplos": [
            {"de": "Ich fahre nach Berlin.", "es": "Voy a Berlín."},
            {"de": "Er fährt schnell.", "es": "Él conduce rápido."},
        ],
    },
    "palabra_sin_ejemplos": {
        "palabra": "schnell",
        "traduccion": "rápido",
        "categoria": "adjetivo",
        "dificultad": 0,
    },
    "verbo_regular": {
        "palabra": "arbeiten",
        "traduccion": "trabajar",
        "categoria": "verbo",
        "dificultad": 0,
        "ejemplos": [
            {"de": "Ich arbeite.", "es": "Trabajo."},
        ],
    },
}

def insert_word(db_path: pathlib.Path, scenario:str) -> int:
    """Insert a word from the scenario word bank into the database and returns its ID"""
    word = TEST_WORDS[scenario]
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO palabras (palabra, traduccion, categoria, plural, dificultad) VALUES(?,?,?,?,?)"
                   , (word["palabra"], word["traduccion"],
                      word["categoria"], word.get("plural"), word["dificultad"]))

    word_id = cursor.lastrowid #return value

    assert word_id is not None

    if "conjugacion" in word and isinstance(word["conjugacion"], dict):
        for pronombre, valor in word["conjugacion"].items():
            cursor.execute(
                "INSERT INTO conjugaciones (palabra_id, pronombre, valor) VALUES(?,?, ?)",
                (word_id, pronombre, valor),)

    if "ejemplos" in word and isinstance(word["ejemplos"], list):
        for ejemplo in word["ejemplos"]:
            cursor.execute("INSERT INTO oraciones (palabra_id, texto_de, texto_es) VALUES(?,?,?)",
        (word_id, ejemplo["de"], ejemplo["es"]))

    connection.commit()
    connection.close()

    return word_id



