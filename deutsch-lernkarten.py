import json
import random

def get_word(w_list: list[dict]) -> dict:
    return random.choice(w_list)

def show_translation(word: dict) -> None:
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

def main() -> None:
    print("-" * 40)
    print("   Willkommen auf Deutsch-Lernkarten")
    print("-" * 40)
    print()

    with open("palabras_a1.json", "r", encoding="utf-8") as file:
        data: dict = json.load(file)
        word_list: list[dict] = data["palabras"]

        active: bool = True
        while active:
            current_word: dict = get_word(word_list)

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

            new_word: str = input("Nueva palabra: enter. Terminar: escriba 'salir'\n")

            if new_word == "salir":
                active = False
            elif new_word == "":
                continue
            else:
                print("Solo enter or 'salir'")

if __name__ == "__main__":
    main()
