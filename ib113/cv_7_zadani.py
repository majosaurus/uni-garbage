from random import randint

# Napiste funkci guess_number_human(upper_bound), ktera umoznuje hrat
# s pocitacem hru na hadani cisla: pocitac si mysli cislo (cele cislo
# v intervalu [1, upper_bound]), hrac se ho snazi uhodnout. Po kazdem pokusu
# dostane hrac od pocitace informaci, zda je hledane cislo mensi nebo vetsi
# nez to, ktere si tipnul.


def guess_number_human(upper_bound):
    lower_bound = 1
    random_num = randint(lower_bound, upper_bound)
    player_num = -1

    while random_num != player_num:
        player_num = int(input("Zadej svuj tip: "))

        if random_num < player_num:
            print("Moje cislo je mensi.")
            upper_bound = player_num

        if random_num > player_num:
            print("Moje cislo je vetsi.")
            lower_bound = player_num

    print("Uhodl jsi moje cislo.")


# guess_number_human(10)


# Napiste funkci guess_number_pc(upper_bound), ktera umoznuje hrat s pocitacem
# hru na hadani cisla, tentokrat si vsak cislo mysli uzivatel a pocitac hada.
# Po kazdem pokusu si pocitac vyzada od uzivatele informaci, zda je myslene
# cislo vetsi nebo mensi nez to, ktere si pocitac tipnul.

# Mysli si cislo od 1 do 10.
# Je cislo 5 mensi (0), rovno (1), nebo vetsi (2) nez tvoje cislo?
# 2
# Je cislo 2 mensi (0), rovno (1), nebo vetsi (2) nez tvoje cislo?
# 2
# Tvoje cislo je 1.


def guess_number_pc(upper_bound):
    lower_bound = 1
    player_choice = -1

    while player_choice != 1:
        half_num = (lower_bound + upper_bound) // 2
        player_choice = int((input("Je cislo {} mensi (0), rovno (1) nebo vetsi (2) nez tvoje cislo?".format(half_num))))

        if player_choice == 0:
            upper_bound = half_num - 1

        if player_choice == 2:
            lower_bound = half_num + 1

    print("Uhodl jsem tve cislo.")


# guess_number_pc(10)

# Napiste funkci binary_search(needle, haystack), ktera zjisti, zda se hodnota
# needle nachazi ve vzestupne usporadanem seznamu haystack. Funkce musi mit
# logaritmickou casovou slozitost.


def binary_search(needle, haystack):
    lower_bound = 0
    upper_bound = len(haystack) - 1

    while lower_bound <= upper_bound:
        half_index = (lower_bound + upper_bound) // 2

        if haystack[half_index] < needle:
            lower_bound = half_index + 1

        elif haystack[half_index] > needle:
            upper_bound = half_index - 1

        else:
            return True

    return False


print(binary_search(5, [1, 2, 5, 8]))  # True
print(binary_search(4, [1, 2, 5, 8]))  # False

# Vylepsete predchozi funkci tak, aby vracela index pozice, kde se hledany
# prvek nachazi. Pokud prvek v seznamu neni, vratte -1.


def binary_search_position(needle, haystack):
    return 0  # TODO


print(binary_search_position(5, [1, 2, 5, 8]))  # 2
print(binary_search_position(4, [1, 2, 5, 8]))  # -1
