import re

# Nactete text ze souboru maj.txt a vypiste ho na obrazovku


def show_file_text():
    with open("maj.txt", "r") as text_file:
        for line in text_file:
            print(line, end="")


# show_file_text()

# Misto vypsani na obrazovku je zkopirujte do noveho souboru.


def copy_to_other_file():
    with open("maj.txt", "r") as maj:
        with open("output.txt", "w") as text:
            for line in maj:
                text.write(line)
            text.write("\n")

copy_to_other_file()

# Pote text ulozte do noveho souboru opacne (obratte poradi pismen – tj.
# posledni pismeno bude prvni v novem souboru, predposledni druhe, ...)


def reversed_copy():
    lst_line = []
    char_line = []

    with open("maj.txt", "r") as maj:
        with open("output.txt", "a") as text:
            for line in maj:
                lst_line.append(line)

            for line in lst_line:
                for char in line:
                    char_line.append(char)

            char_line = char_line[::-1]
            output = ""
            for lines in char_line:
                output += lines

            text.write(output)


reversed_copy()

# Obratte pouze poradi slov (posledni slovo bude na prvnim miste, predposledni
#  na druhem, ...), ale neobracejte poradi pismen v jednotlivych slovech


def reversed_words_copy():
    lst_line = []

    with open("maj.txt", "r") as maj:
        with open("output.txt", "a") as text:
            for line in maj:
                pass


reversed_words_copy()


# Nactete data ze souboru do vhodne struktury


def load_data():
    with open('sherlock-holmes.txt', 'r', encoding="utf-8") as file:
        dct = {}

        # nacitani dat do slovniku
        for line in file:
            clear_line = re.sub('\W+', ' ', line)  # nechat jen pismena

            for word in clear_line.split():
                if word:  # jen neprazdna slova
                    dct[word] = dct.get(word, 0) + 1

    return dct


# Top 10 nejcastejsich slov

def top_ten(data):
    max_value = 0
    value_list = []
    max_list = []

    for value in data.values():
        value_list.append(value)
        if value > max_value:
            max_value = value

    value_list.sort(reverse=True)

    for i in range(10):
        max_list.append(value_list[i])

    print(max_list)



# Top 10 nejcastejsich slov delky alespon 3 znaky


def top_ten_with_length_three(data):
    pass  # TODO


# Top n nejcastejsich slov delky alespon k znaku


def top_n_with_length_k(data, num, length):
    pass  # TODO


# Prumerna delka slova v textu


def word_average(data):
    pass  # TODO


LOADED_DATA = load_data()
top_ten(LOADED_DATA)
top_ten_with_length_three(LOADED_DATA)
top_n_with_length_k(LOADED_DATA, 5, 5)
print()
word_average(LOADED_DATA)
