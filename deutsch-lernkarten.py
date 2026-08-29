from db_library import next_word, update_difficulty

def show_translation(word: dict) -> None:
    """Shows the translation of the given word"""
    print("-" * 30)
    print(f"{word['traduccion']}\n")

    if word["categoria"] == "verbo":
        if 'conjugacion' in word:
            print("Conjugaciones irregulares:")
            for k, v in word["conjugacion"].items():
                print(f"{k}: {v}")
            print()
        else:
            print("El verbo es regular\n")

    if 'plural' in word is not None:
        print(f"Plural:{word['plural']}\n")

    print("Ejemplos:")
    for ejemplo in word["ejemplos"]:
        print(ejemplo["de"])
        print(ejemplo["es"])
        print()
    print("-" * 30)



def main() -> None:
    """Main function"""
    print("-" * 40)
    print("   Willkommen auf Deutsch-Lernkarten")
    print("-" * 40)
    print()


    active: bool = True
    while active:
        current_word: dict = next_word()

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
                    update_difficulty(current_word["id"], difficulty)
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