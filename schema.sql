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
    ultima_vez TIMESTAMP);

CREATE TABLE IF NOT EXISTS conjugaciones (
    id         INTEGER PRIMARY KEY,
    palabra_id INTEGER NOT NULL REFERENCES palabras(id) ON DELETE CASCADE,
    pronombre  TEXT    NOT NULL,
    valor      TEXT    NOT NULL,
    UNIQUE (palabra_id, pronombre)
);

CREATE TABLE IF NOT EXISTS oraciones
(
    id         INTEGER PRIMARY KEY,
    palabra_id INTEGER NOT NULL REFERENCES palabras (id) ON DELETE CASCADE,
    texto_de   TEXT    NOT NULL,
    texto_es   TEXT    NOT NULL
);