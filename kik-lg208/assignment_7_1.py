eng2cz = {"dog": "pes", "cat": "kočka", "ginger": "zázvor", "beer": "pivo", "say": "říct", \
          "thirst": "žízeň", "boat": "loď", "watercress": "řeřicha", "car": "auto", "spoon": "lžíce", \
          "wolf": "vlk", "milk": "mléko", "one": "jedna"} # global variable containing eng to cz translations

def eng_to_cz(word):
    """If the word is known by the dictionary, it is returned by this function.
    Otherwise an empty string is returned."""

    if word in eng2cz:
        return eng2cz[word]

    return ""


def unknown(unknown_word, translation):
    """If a word is not known by the dictionary, it is added by the user. Input
    prompt is in the main function."""

    eng2cz[unknown_word] = translation
    return 0


def main():
    """The main function asks the user to enter an English word to translate into Czech.
    If it is known by the dictionary, it is printed. The user is asked for another one.
    If the word is not in the dictionary, the user is asked to provide a translation.
    The translation is then stored in the dictionary. When user hits enter, the program
    ends."""

    word = " "
    czWord = ""
    
    while word != "":
        word = input("Please, enter an English word to translate into Czech: ").lower()
        czWord = eng_to_cz(word)
        
        if czWord == "" and word != "":
            print("Sorry, I don't know how to translate " + word + " to Czech.")
            translation = input("Please, teach me what the Czech translation of " + word + " is: ").lower()
            unknown(word, translation)

        if czWord != "":
            print("The English word " + word + " is " + czWord + " in Czech.")
        
        if word == "":
            print("Goodbye!")
    
main()
