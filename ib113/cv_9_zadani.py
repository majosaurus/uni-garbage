# Napiste funkci, ktera nad 2D mrizkou (matici), vrati pocet nul v matici.


def count_zeros(matrix):
    zeros_found = 0

    for row in matrix:
        for el in row:
            if el == 0:
                zeros_found += 1

    return zeros_found


# Napiste funkci, ktera nad 2D mrizkou (matici), ktera najde sloupecek
# s nejvetsim souctem. Vysledek vratte jako dvojici (index sloupce, soucet)


def column_max_sum(matrix):
    max_sum = 0
    current_index = 0

    for i in range(len(matrix[0])):
        current_sum = 0

        for j in range(len(matrix)):
            current_sum += matrix[j][i]  # j se meni casteji, proto j jako prvni index

            if current_sum > max_sum:
                max_sum = current_sum
                current_index = i

    return current_index, max_sum


# Napiste funkci, ktera nad 2D mrizkou (matici), ktera najde souradnici
# nejvetsiho prvku. Vysledek vratte jako dvojici
# (index radku, index sloupce).


def max_element_coordinate(matrix):
    current_max = 0
    index_col = 0
    index_row = 0

    for i in range(len(matrix)):  # sloupec
        for j in range(len(matrix[i])):  # radek
            if matrix[i][j] > current_max:
                current_max = matrix[i][j]
                index_col, index_row = j, i

    return index_row, index_col


# Vytvorte funkci, ktera vrati transponovanou matici.
def transpose_matrix(matrix):
    new_matrix = []

    for i in range(len(matrix[0])):  # sloupec
        aux_list = []

        for j in range(len(matrix)):  # radek
            aux_list.append(matrix[j][i])

        new_matrix.append(aux_list)

    return new_matrix


# Vytvorte funkci, ktera zjisti, zda se nekde v matici vyskytuji dve nuly vedle
# sebe
def detect_adjacent_zeros(matrix):
    for i in range(len(matrix)):  # radek
        for j in range(len(matrix[i])):  # sloupecek
            return 0


# Napiste funkci, ktera zkontroluje, zda predany seznam obsahuje jen unikatni
# polozky. Pouzijte datovy typ mnozina
def unique_check(temp):
    set_from_list = set(temp)

    if len(set_from_list) == len(temp):
        return True

    return False


# Napiste funkci, ktera vrati soucet vsech hodnot ulozenych ve slovniku.
# Napr. d1 = {'a': 100, 'b': 200, 'c':300} => 600
def dict_sum(dct):
    total = 0

    for values in dct.values():
        total += values

    return total


# Napiste funkci, ktera vezme dva slovniky a vrati novy, ktery obsahuje jejich
# soucet. Tj. pokud oba slovniky obsahuji polozky se stejnym klicem, pak ve
# vyslednem slovniku bude u daneho klice soucet hodnot z obou slovniku
# (ostatni polozky jsou vlozeny beze zmeny).
# Napr. d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# => {'a': 400, 'b': 400, 'd': 400, 'c': 300}
def add_two_dictionaries(dct_1, dct_2):
    result = {}

    for key in dct_1.keys():
        if key in dct_2:
            value1 = dct_1[key]
            value2 = dct_2[key]
            result[key] = value1 + value2

        else:
            result[key] = dct_1[key]

    for key in dct_2.keys():
        if key not in dct_1.keys():
            result[key] = dct_2[key]

    return result


# Napiste funkci, ktera vrati seznam(!) vsech hodnot,ktere obsahuje dany
# slovnik (bez duplicit).
def unique_values(dct):
    set_dict = set()

    for values in dct.values():
        set_dict.add(values)

    return list(set_dict)


########################################################################
#               Nasleduje kod testu                                    #
########################################################################

ib113_column_max_sum_in = ([[2, 3, 4], [4, 2, 1]], [[1], [2], [3]],
                           [[1, 2, 3], [3, 3, 3], [1, 2, 2]], [[3, 5, 4]])
ib113_column_max_sum_out = ((0, 6), (0, 6), (2, 8), (1, 5))


def ib113_test_column_max_sum():
    print("Testovani funkce column_max_sum: ", end="")
    failure = False

    for i in range(len(ib113_column_max_sum_in)):
        res = column_max_sum(ib113_column_max_sum_in[i])
        if not isinstance(res, tuple):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu ntice, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_column_max_sum_out[i]:
            failure = True
            print("NOK")
            print("Pro vstup \"{}\" nebyl vracen spravny vysledek"
                  .format(ib113_column_max_sum_in[i]))
            print("Byl vracen vysledek: \"{}\"".format(res))
            print("Byl ocekavan vysledek: \"{}\""
                  .format(ib113_column_max_sum_out[i]))
            break

    if not failure:
        print("OK")


ib113_max_element_coordinate_in = ([[2, 3, 4], [4, 5, 1]], [[1], [2], [3]],
                                   [[4, 2, 3], [3, 3, 3], [1, 2, 2]],
                                   [[3, 5, 4]])
ib113_max_element_coordinate_out = ((1, 1), (2, 0), (0, 0), (0, 1))


def ib113_test_max_element_coordinate():
    print("Testovani funkce max_element_coordinate: ", end="")
    failure = False

    for i in range(len(ib113_max_element_coordinate_in)):
        res = max_element_coordinate(ib113_max_element_coordinate_in[i])
        if not isinstance(res, tuple):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu ntice, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_max_element_coordinate_out[i]:
            failure = True
            print("NOK")
            print("Pro vstup \"{}\" nebyl vracen spravny vysledek"
                  .format(ib113_max_element_coordinate_in[i]))
            print("Byl vracen vysledek: \"{}\"".format(res))
            print("Byl ocekavan vysledek: \"{}\""
                  .format(ib113_max_element_coordinate_out[i]))
            break

    if not failure:
        print("OK")


ib113_count_zeros_in = ([[2, 0, 4], [4, 5, 0]], [[0], [0], [3]],
                        [[4, 0, 3], [3, 3, 0], [0, 2, 2]], [[3, 5, 4]])
ib113_count_zeros_out = (2, 2, 3, 0)


def ib113_test_count_zeros():
    print("Testovani funkce count_zeros: ", end="")
    failure = False

    for i in range(len(ib113_count_zeros_in)):
        res = count_zeros(ib113_count_zeros_in[i])
        if not isinstance(res, int):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu cele cislo, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_count_zeros_out[i]:
            failure = True
            print("NOK")
            print("Pro vstup \"{}\" nebyl vracen spravny vysledek"
                  .format(ib113_count_zeros_in[i]))
            print("Byl vracen vysledek: \"{}\"".format(res))
            print("Byl ocekavan vysledek: \"{}\""
                  .format(ib113_count_zeros_out[i]))
            break

    if not failure:
        print("OK")


ib113_transpose_matrix_in = ([[2, 0, 4], [4, 5, 0]], [[0], [0], [3]],
                             [[4, 0, 3], [3, 3, 0], [0, 2, 2]], [[3, 5, 4]])
ib113_transpose_matrix_out = ([[2, 4], [0, 5], [4, 0]], [[0, 0, 3]],
                              [[4, 3, 0], [0, 3, 2], [3, 0, 2]],
                              [[3], [5], [4]])


def ib113_test_transpose_matrix():
    print("Testovani funkce transpose_matrix: ", end="")
    failure = False

    for i in range(len(ib113_transpose_matrix_in)):
        res = transpose_matrix(ib113_transpose_matrix_in[i])
        if not isinstance(res, list):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu seznam, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_transpose_matrix_out[i]:
            failure = True
            print("NOK")
            print("Pro vstup \"{}\" nebyl vracen spravny vysledek"
                  .format(ib113_transpose_matrix_in[i]))
            print("Byl vracen vysledek: \"{}\"".format(res))
            print("Byl ocekavan vysledek: \"{}\""
                  .format(ib113_transpose_matrix_out[i]))
            break

    if not failure:
        print("OK")


ib113_detect_adjacent_zeros_in = ([[2, 0, 4], [4, 0, 5]], [[0], [0], [3]],
                                  [[0], [3], [0]], [[3, 0, 0]],
                                  [[4, 0, 3], [3, 3, 0], [1, 2, 2]],
                                  [[4, 3, 0], [0, 3, 3], [1, 2, 0]])
ib113_detect_adjacent_zeros_out = (True, True, False, True, True, False)


def ib113_test_detect_adjacent_zeros():
    print("Testovani funkce detect_adjacent_zeros: ", end="")
    failure = False

    for i in range(len(ib113_detect_adjacent_zeros_in)):
        res = detect_adjacent_zeros(ib113_detect_adjacent_zeros_in[i])
        if not isinstance(res, bool):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu boolean, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_detect_adjacent_zeros_out[i]:
            failure = True
            print("NOK")
            print("Pro vstup \"{}\" nebyl vracen spravny vysledek"
                  .format(ib113_detect_adjacent_zeros_in[i]))
            print("Byl vracen vysledek: \"{}\"".format(res))
            print("Byl ocekavan vysledek: \"{}\""
                  .format(ib113_detect_adjacent_zeros_out[i]))
            break

    if not failure:
        print("OK")


ib113_unique_check_in = ([[1, 5, 6, 5, 4, 9], [1, 5, 6, 3, 9]])
ib113_unique_check_out = (False, True)


def ib113_test_unique_check():
    print("Testovani funkce unique_check: ", end="")
    failure = False

    for i in range(len(ib113_unique_check_in)):
        res = unique_check(ib113_unique_check_in[i])
        if not isinstance(res, bool):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu boolean, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_unique_check_out[i]:
            failure = True
            print("NOK")
            print("Pro vstup \"{}\" nebyl vracen spravny vysledek"
                  .format(ib113_unique_check_in[i]))
            print("Byl vracen vysledek: \"{}\"".format(res))
            print("Byl ocekavan vysledek: \"{}\""
                  .format(ib113_unique_check_out[i]))
            break

    if not failure:
        print("OK")


ib113_dict_sum_in = ([{'a': 100, 'b': 200, 'c': 300}, {'x': 1000}])
ib113_dict_sum_out = (600, 1000)


def ib113_test_dict_sum():
    print("Testovani funkce dict_sum: ", end="")
    failure = False

    for i in range(len(ib113_dict_sum_in)):
        res = dict_sum(ib113_dict_sum_in[i])
        if not isinstance(res, int):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu int, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_dict_sum_out[i]:
            failure = True
            print("NOK")
            print("Pro vstup \"{}\" nebyl vracen spravny vysledek"
                  .format(ib113_dict_sum_in[i]))
            print("Byl vracen vysledek: \"{}\"".format(res))
            print("Byl ocekavan vysledek: \"{}\""
                  .format(ib113_dict_sum_out[i]))
            break

    if not failure:
        print("OK")


ib113_add_two_dictionaries_in = ([({'a': 100, 'b': 200, 'c': 300},
                                   {'a': 300, 'b': 200, 'd': 400})])
ib113_add_two_dictionaries_out = [{'a': 400, 'b': 400, 'd': 400, 'c': 300}]


def ib113_test_add_two_dictionaries():
    print("Testovani funkce add_two_dictionaries: ", end="")
    failure = False

    for i in range(len(ib113_add_two_dictionaries_in)):
        res = add_two_dictionaries(ib113_add_two_dictionaries_in[i][0],
                                   ib113_add_two_dictionaries_in[i][1])
        if not isinstance(res, dict):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu dict, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_add_two_dictionaries_out[i]:
            failure = True
            print("NOK")
            print("Pro vstup \"{}\" nebyl vracen spravny vysledek"
                  .format(ib113_add_two_dictionaries_in[i]))
            print("Byl vracen vysledek: \"{}\"".format(res))
            print("Byl ocekavan vysledek: \"{}\""
                  .format(ib113_add_two_dictionaries_out[i]))
            break

    if not failure:
        print("OK")


ib113_unique_values_in = ([{'a': 5, 'b': 5, 'c': 4},
                           {'a': 1, 'b': 5, 'c': 1, 'd': 5},
                           {'a': 1, 'b': 5, 'c': 1, 'd': 1}])
ib113_unique_values_out = ([4, 5], [1, 5], [1, 5])


def ib113_test_unique_values():
    print("Testovani funkce unique_values: ", end="")
    failure = False

    for i in range(len(ib113_unique_values_in)):
        res = unique_values(ib113_unique_values_in[i])
        if not isinstance(res, list):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu list, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_unique_values_out[i]:
            failure = True
            print("NOK")
            print("Pro vstup \"{}\" nebyl vracen spravny vysledek"
                  .format(ib113_unique_values_in[i]))
            print("Byl vracen vysledek: \"{}\"".format(res))
            print("Byl ocekavan vysledek: \"{}\""
                  .format(ib113_unique_values_out[i]))
            break

    if not failure:
        print("OK")


# Zde muzete vkladat vlastni testy
if __name__ == '__main__':
    ib113_test_count_zeros()
    print()
    ib113_test_max_element_coordinate()
    print()
    ib113_test_column_max_sum()
    print()
    ib113_test_transpose_matrix()
    print()
    ib113_test_detect_adjacent_zeros()
    print()
    ib113_test_unique_check()
    print()
    ib113_test_dict_sum()
    print()
    ib113_test_add_two_dictionaries()
    print()
    ib113_test_unique_values()
    print()
