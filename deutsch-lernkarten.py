import json
import random

def load_progress() -> list:
    """Loads the progress json file or creates a list"""
    try:
        with open("data/progress.json", "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

def build_weights(w_list: list[dict], progress) -> dict:
    """Builds the weights of the words in the list"""
    weights: dict = {1:1, 2:3, 3:5}
    progress_map: dict = {item["id"]: item["difficulty"] for item in progress}

    weight_map:dict = {}
    for word in w_list:
        difficulty = progress_map.get(word["id"])
        weight_map[word["id"]] = 5 if difficulty is None else weights[difficulty]
    return weight_map

def get_word(w_list: list[dict], w_map: dict) -> dict:
    """Chooses a word from the list to be displayed"""
    ids: list = list(w_map.keys())
    weights: list = list(w_map.values())
    selected_id: int = random.choices(ids, weights = weights, k=1)[0]

    for word in w_list:
        if word["id"] == selected_id:
            return word

    return random.choice(w_list)

def show_translation(word: dict) -> None:
    """Shows the translation of the given word"""
    print("-" * 30)
    print(f"{word['traduccion']}\n")

    if 'conjugacion' in word:
        if word['conjugacion'] == "verbo regular":
            print("El verbo es regular.")
        else:
            print("Conjugaciones irregulares:")
            for k, v in word["conjugacion"].items():
                print(f"{k}: {v}")
            print()
    if 'plural' in word:
        print(f"Plural:{word['plural']}\n")

    print("Ejemplos:")
    for ejemplo in word["ejemplos"]:
        print(ejemplo["de"])
        print(ejemplo["es"])
        print()
    print("-" * 30)

def save_difficulty(dif: int, word: dict, progress: list) -> None:
    """Saves the given difficulty of the given word"""
    for i in progress:
        if i["id"] == word["id"]:
            i["difficulty"] = dif
            break
    else:
        progress.append({"id": word["id"], "difficulty": dif})

    with open("data/progress.json", "w", encoding="utf-8") as file:
        json.dump(progress, file, indent=4)

def main() -> None:
    """Main function"""
    print("-" * 40)
    print("   Willkommen auf Deutsch-Lernkarten")
    print("-" * 40)
    print()

    with open("data/palabras_a1.json", "r", encoding="utf-8") as file:
        data: dict = json.load(file)
        word_list: list[dict] = data["palabras"]

    progress: list[dict] = load_progress()
    weight_map: dict = build_weights(word_list, progress)

    active: bool = True
    while active:
        current_word: dict = get_word(word_list, weight_map)

        print("Das wort ist:")
        print("-" * 30)
        print(current_word["palabra"])
        print("-" * 30)

        show_loop: bool = True
        while show_loop:
            show: str = input("Enter para ver traducción:\n")
            if show == "":
                show_translation(current_word)
                show_loop = False
            else:
                print("No escriba nada, solo tecla enter.")

        ask_difficulty: bool = True
        while ask_difficulty:
            difficulty: int = int(input("¿Sé la traducción de la palabra?\n"
                            "La recuerdo [1], Más o menos [2], No la recordé [3]\n"))
            try:
                if difficulty < 1 or difficulty > 3:
                    print("Opción incorrecta")
                else:
                    save_difficulty(difficulty, current_word, progress)
                    ask_difficulty = False
            except ValueError:
                print("Error: Entrada no es un numero.")

        new_word_loop: bool = True
        while new_word_loop:
            new_word: str = input("Nueva palabra: enter. Terminar: escriba 'salir'\n")

            if new_word == "salir":
                new_word_loop = False
                active = False
            elif new_word == "":
                break
            else:
                print("Solo enter or 'salir'")

if __name__ == "__main__":
    main()