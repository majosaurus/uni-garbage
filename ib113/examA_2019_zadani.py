# 1) Implementujte funkci ciphersum(num), ktera vrati seznam vsech prirozenych
# cisel mensich nez num takovych, ze jejich ciferny soucet je roven cislu 5.
# (10 bodu)
#
# :param num Maximalni cislo po ktere se hleda seznam cisel takovych, ze jejich
#       ciferny soucet je roven cislu 5.
# :return Seznam vsech prirozenych cisel mensich nez num takovych, ze jejich
#       ciferny soucet je roven cislu 5.


def ciphersum(num):
    all_nums = []

    for i in range(1, num + 1):
        if digits_sum(i) == 5:
            all_nums.append(i)

    print(all_nums)


def digits_sum(num):
    total = 0

    if num < 10:
        return num

    while num:
        total += num % 10
        num = num // 10

    return total


# 2) Napiste funkci table(n), ktera vypise tabulku cisel n krat n podle
# nasledujiciho vzoru pro n = 5:
# 1 2 3 4 5
# 2 3 4 5 1
# 3 4 5 1 2
# 4 5 1 2 3
# 5 1 2 3 4
# 13 bodu

# :param n Pocet radku a sloupcu tabulky, ktere se maji vypsat.


def table(n):
    lst = []

    for i in range(1, n + 1):
        lst.append(i)

    for i in range(n):
        for i in range(len(lst)):
            print(lst[i], end=" ")

        print()
        lst.append(lst.pop(0))

"""(i+j) mod n + 1, end"""
# 3) Vytvorte funkci is_super_increasing(check_list), ktera overi, zda je
# zadany seznam super-rostouci (uvazujeme pouze prirozena cisla, tj. cela
# cisla vetsi nez nula). Seznam je super-rostouci, pokud kazdy prvek je ostre
# vetsi nez soucet predchozich prvku. Funkce vraci True, pokud je seznam
# super-rostouci, False pokud neni a None pro prazdny seznam
# (13 bodu)

# :param check_list Seznam, ktery se testuje.
# :return True, pokud je seznam super-rostouci, False pokud neni a None pro
#       prazdny seznam.


def is_super_increasing(check_list):
    total = 0

    if len(check_list) == 0:
        return None

    for i in range(len(check_list)):
        if total >= check_list[i]:
            return False

        total += check_list[i]

    return True


# 4) Implementujte funkci unique_chars(first, second), ktera vraci vsechny
# unikatni pismena (tj. takova, ktera jsou v obou retezcich dohromady obsazena
# prave jednou.
# (14 bodu)

# :param first Prvni testovany retezec.
# :param second Druhy testovany retezec.
# :return Retezec, ktery obsahuje unikatni pismena z obou retezcu.


def unique_chars(first, second):  # Funkce nekontroluje, zda jsou duplikaty v jednom retezci. Nestihla jsem.
    unique = ""
    counter = 0

    for char in first:
        if char in second:
            unique = unique
        else:
            unique += char

    for char in second:
        if char not in first:
            unique += char

    print(unique)



# 5) Napiste funkci print_letter_N(size), ktera pomoci "textove grafiky"
# vypise pismeno N o zadane velikosti size. Vas vystup by mel odpovidat ukazce
#  vystupu.
# Pozn. size udava pocet radku i pocet sloupcu. Dodrzujte vzory uvedene
# v zadani.
# (15 bodu)

# :param size pocet radku i pocet sloupcu do kterych se kresli

# Napriklad pro size = 5:
# . . . #
# # . . #
# . # . #
# . . # #
# . . . #


def print_letter_N(size):
    for i in range(size):
        for j in range(1, size + 1):
            if j == 1 or j == size:
                print("#", end=" ")

            elif j == i + 1 and i != 0:
                print("#", end=" ")

            else:
                print(".", end=" ")

        print()


# 6) Implementujte funkci diagonal_sum(matrix), ktera vrati soucet prvku na
# hlavni a vedlejsi diagonale ctvercove matice. Poyor, prvek na obou
# diagonalach se pocita jen jednou! Pro prazdnou matici vraci None.
# (15 bodu)

# :param matrix ctvercova matice (seznam seznamu), ktera obsahuje cela cisla
#       typu int.
# :return soucet hodnot prvku na hlavni a vedlejsi diagonale ctvercove matice,
#       pokud matice obsahuje alespon jeden prvek (prvek na obou diagonalach se
#       pocita jen jednou). Jinak vraci None.

def diagonal_sum(matrix):
    total = 0
    size = len(matrix)

    if len(matrix) == 0:
        return None

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == i or i + j == size - 1:
                total += matrix[i][j]

    return total


# diagonal_sum([[0, 1, 2], [2, 1, 3], [5, 4, 3]])


# Implementujte funkci bonus_points(text), kde vstupem je retezec tvaru
# "Petr:3,Pavel:5,Jana:8,Petr:4,Martina:3" udavajici kolik ziskali studenti
# bonusovych bodu (jmeno se muze vyskytovat vickrat). Vypiste studenty
# v poradi podle souctu ziskanych bodu.
# (20 bodu)

# :param text vstupni text ve formatu:
#       jmeno:pocet_bonusovych_bodu,jmeno2:pocet_bonusovych_bodu,...
#       kde se jmena mohou opakovat.


def bonus_points(text):
    pass  # TODO
