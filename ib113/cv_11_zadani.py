import random
import re

# Vypiste, kolikrat se v textu vyskytuji jednotliva pismena.
# https://www.fi.muni.cz/IB111/sbirka/_downloads/devatero_pohadek.txt
# Tip: pro overeni, ze je dany znak pismeno, muzete pouzit funkci isalpha.


"""def freq_analysis(filename):
    letter_dict = {}

    with open("devatero_pohadek.txt", "r") as text:
        for line in text:
            for char in line:
                if char.isalpha():
                    if char in letter_dict:
                        letter_dict[char] += 1
                    else:
                        letter_dict[char] = 1
        print(letter_dict)"""


# freq_analysis('devatero_pohadek.txt')


def find_regexp(regexp, filename="slovnik.txt"):
    with open(filename, "r", encoding="utf-8") as my_file:
        for line in my_file:
            if re.search(regexp, line):
                strip_line = line.rstrip()
                print(strip_line, end=", ")
    print("\n")




# Vypsat vsechny retezce, ktere obsahuji podretezec 'oo'
find_regexp(r'.oo.')
# Vypsat vsechny retezce, ktere zacinaji na 'e' a konci na 'le'
# Vypise pouze erteple, elle, emile,
find_regexp(r'^e.*le$')
# Vypsat vsechny retezce, ktere obsahuji 'a', 'e', 'i', 'o', 'u' v tomto
# poradi (ale ne nutne za sebou, napr. akademickou)
find_regexp(r'a.*e.*i.*o.*u')
# Vypsat vsechny retezce, ktere obsahuji podretezec delky 4
# tvoreny z pismen "rst" (napr. bratrstvi)
find_regexp(r'[rst]{4}')
# Vypsat vsechny retezce, dve 'u' vzdalena od sebe 8 pozic (napr. 'uhlovodiku')
find_regexp(r'u[^u]{8}u')
# Obsahuji pismeno 'u' na druhe i predposledni pozici (napr. 'luxus')
find_regexp(r'^[^u][u].*[u].$')
# Krome prvniho a posledniho pismene, kde muze byt libovolne pismeno, obsahuji
# pouze samohlasky a maji presne 5 pismen (napr. 'foyer')
find_regexp(r'^.[aeiou]{3}.$')


# Napiste funkci text_imitation(filename, length), ktera analyzuje text
# v souboru filename. Funkce pak vygeneruje pseudo-nahodny text o length
# slovech. Text se generuje po slovech. Dalsi generovane slovo se nahodne
# vybira z tech, ktere v puvodnim textu po naposledy vygenerovanem slove
# nasledovaly.


def text_imitation(filename, length):
    pass # TODO
"""{"word":[slovo1, slovo2, slovo3]} - delka seznamu, nahodne vyberu, nebo mnozina"""


text_imitation('devatero_pohadek.txt', 7)
print()

# Pro kazde pismeno v textu vypiste 5 pismen, ktere za nim nasleduji nejcasteji
"""{"analyzovany znak":{"following znak":kolikrat nasledovalo}}"""

def cond_freq_analysis(filename):
    pass  # TODO


cond_freq_analysis('devatero_pohadek.txt')
