#Migrates data from the json files I had.

import json
import sqlite3

with open("data/palabras_a1.json", "r", encoding="utf-8") as json_file:
    complete_dict = json.load(json_file)
palabras = complete_dict["palabras"]

connection = sqlite3.connect("data/lernkarten.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

for i in palabras:
    cursor.execute(
        "INSERT INTO palabras (id, palabra, traduccion, categoria, nivel, plural) VALUES(?,?,?,?,?,?)",
    (i["id"], i["palabra"], i["traduccion"], i["categoria"], i["nivel"], i.get("plural")),
    )
    if "conjugacion" in i and isinstance(i["conjugacion"], dict):
        for pronombre, valor in i["conjugacion"].items():
            cursor.execute(
                "INSERT INTO conjugaciones (palabra_id, pronombre, valor) VALUES(?,?, ?)",
                (i["id"], pronombre, valor),
            )
    for ejemplo in i.get("ejemplos", []):
        cursor.execute(
        "INSERT INTO oraciones (palabra_id, texto_de, texto_es) VALUES(?,?,?)",
        (i["id"], ejemplo["de"], ejemplo["es"]),
        )

connection.commit()
connection.close()