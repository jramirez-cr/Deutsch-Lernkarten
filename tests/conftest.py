import pytest
import sqlite3
import pathlib

SCHEMA_PATH = pathlib.Path(__file__).parent.parent / 'schema.sql'

@pytest.fixture
def test_db(tmp_path, monkeypatch):
    db_file = tmp_path / "test.db"

    monkeypatch.setattr("db_library.DB_PATH", str(db_file)) #

    with open(SCHEMA_PATH, "r", encoding= "utf-8") as schema:
        sql_schema = schema.read()

    connection = sqlite3.connect(db_file)

    connection.executescript(sql_schema)
    connection.commit()
    connection.close()

    yield db_file


