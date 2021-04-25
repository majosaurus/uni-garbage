czech = ["pes", "kočka", "řeřicha", "zázvor", "auto", "měkký", "pivo", "žízeň", "loď", "játra", "fronta", "krtek"]
english = ["dog", "cat", "watercress", "ginger", "car", "soft", "beer", "thirst", "boat", "kidney", "queue", "mole"]

word = input("Please, enter an English word to translate into Czech: ")

for i in range(len(english)):
    if word.lower() == english[i]:
        print("The English word " + word + " is " + czech[i] + " in Czech.")

print("Sorry, I don't know how to translate " + word + " to Czech.")
