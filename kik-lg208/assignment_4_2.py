'''Function prints a translation of an English word into Czech. If it does not know what the
translation is, it prints an error message. After entering word "crap", the function refuses
to translate this word into Czech and it ends.'''
def main():
    word = ""
    czWord = ""
    
    while word.lower() != "crap":
        word = input("Please, enter an English word to translate into Czech: ")
        czWord = eng2cz(word)
        
        if czWord == "" and word != "crap":
            print("Sorry, I don't know how to translate " + word + " to Czech.")

        if czWord != "":
            print("The English word " + word + " is " + czWord + " in Czech.")
    
    print("I refuse to translate that word. Bye!")


'''Function translates an English word to Czech using linear search in lists.'''
def eng2cz(word):
    czech = ["pes", "kočka", "řeřicha", "zázvor", "auto", "měkký", "pivo", "žízeň", "loď", "játra", "fronta", "krtek"]
    english = ["dog", "cat", "watercress", "ginger", "car", "soft", "beer", "thirst", "boat", "kidney", "queue", "mole"]

    for i in range(len(english)):
        if word.lower() == english[i]:
            return czech[i]

    return ""

main()
