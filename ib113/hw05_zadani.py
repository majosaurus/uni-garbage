# ################################## HW5 ################################## #
"""
Pokyny:
- Deadline odevzdani: 22. 12. 23:59
- Odevzdejte jediny soubor
- Muzete si vytvaret pomocne funkce, pokud chcete.
- V pripade, ze chcete vytvaret vlastni testy, vkladete je na prislusne misto
    na konci souboru.
    - Pred odevzdanim vlastni modifikace smazte.
- Piste srozumitelny kod, pouzivejte vhodne nazvy promennych a funkci.
- Dodrzujte standard pep8.
    - Budu kontrolovat a strhavat body za jeho nedodrzeni.
- Nemente hlavicky pripravenych funkci.
- Pripadne nejasnosti muzete resit v diskuznim foru. Pokud by ale mela otazka
    obsahovat kusy kodu, nebo neco, co by mohli ostatni studenti opsat, tak
    napiste radeji email.
- Pokud nevite, jak nejaky priklad vyresit kompletne, napiste do komentare,
    co vasemu reseni chybi.
- Neopisujte. Nestoji to za to. Dostanete zaporne body a budete muset ulohu
    stejne vypracovat sami.

Implementujte uvedene funkce dle jejich dokumentace. Prvni z nich nacita
externi soubor do interni datove struktury typu slovnik a zbyvajici funkce nad
nim pracuji (pocitaji ruzne statistiky)
"""

import re

# Funkce nacte data ze souboru jmena.csv a ulozi je do slovniku. Soubor se
# musi nachazet ve stejnem adresari jako soubor s domacim ukolem. Struktura
# nacitanych dat je dana csv formatem.
# Vytvoreny slovnik ma strukturu dat ve formatu dct[jmeno][rok], kde jmeno je
# typu str a rok typu int, tj. napr. dct["ANNA"][2000] obsahuje hodnotu 1382


def load_data_to_dictionary():
    final_dict = {}
    years = []

    names = open('jmena.csv', encoding='utf8')

    for name in names:
        lst = name.split(',')

        if lst[0] == 'JMÉNO':
            for i in range(1, len(lst)):
                years.append(int(lst[i]))

        else:
            aux_dict = {}

            for j in range(0, len(years)):
                aux_dict[years[j]] = int(lst[j + 1])

            final_dict[lst[0]] = aux_dict

    return final_dict


# Naleznete n nejpopularnejsich jmen pro dany rok

# :param dct:   slovnik v jehoz datech vyhledavame vysledky
# :param n:     pocet jmen, ktera se maji vratit
# :param year:  rok ve kterem hledame nejpopularnejsi jmena

# :return       seznam obsahujici n nejpopularnejsich jmen v roce year


def n_most_popular_for_given_year(dct, n, year):
    popular = []
    current_max = 0
    person = ''

    while len(popular) != n:
        for key in dct.keys():
            if dct[key][year] > current_max and key != 'SOUČET'\
                    and key not in popular:
                current_max = dct[key][year]
                person = key

        popular.append(person)
        current_max = 0

    return popular


# Naleznete kdy bylo dane jmeno nejpopularnejsi

# :param dct:   slovnik v jehoz datech vyhledavame vysledky
# :param name:  jmeno, ktere hledame v datech.

# :return       rok (int), ve kterem bylo dane jmeno nejpopularnejsi v pripade,
#               ze se ve slovniku nachazi. Jinak vraci None


def most_popular_in_what_year(dct, name):
    most_popular = 0
    year = 0

    if name not in dct:
        return None

    for key in dct.keys():
        if key == name:
            for yrs in dct[name].keys():
                if dct[name][yrs] > most_popular:
                    most_popular = dct[name][yrs]
                    year = yrs

            return year


# Funkce nalezne rok, kdy u daneho jmena doslo k nejvetsimu vzrustu popularity.
# Tato funkce uvazuje vzrust popularity v absolutnich cislech (nikoliv
# percentualne)

# :param dct:   slovnik v jehoz datech vyhledavame vysledky
# :param name   jmeno, ktere zkoumame
# :return year  cele cislo udavajici rok, po nemz doslo k nejvetsimu vzrustu
#               popularity pro dane jmeno name


def maximal_increase(dict, name):
    var1 = 0
    max_diff = 0
    current_diff = 0

    for key in dict.keys():
        if key == name:
            for yrs in dict[name].keys():
                var2 = dict[name][yrs]

                if var1 != 0:
                    current_diff = abs(var1 - var2)

                if current_diff > max_diff and var1 < var2:
                    max_diff = current_diff
                    year = yrs - 1

                var1 = var2

            return year


# Nasledujici dve funkce jsem nebyla schopna vyresit.

# Funkce nalezne mezi kterymi lety doslo u libovolneho jmena k nejvetsimu
# procentnimu poklesu popularity. Uvazuji se jen jmena, ktera byla dany rok
# davana alespon min-occurence krat (po poklesu mohla klesnout i pod tuto
# hranici. Funkce vraci dvojici (jmeno, rok), kde rok je rok po kterem doslo
# k nejvetsimu poklesu pro dane jmeno

# :param dct:   slovnik v jehoz datech vyhledavame vysledky
# :param min_occurence  pocet vyskytu daneho jmena, tak aby mohl byt uvazovan
#                       jeho procentni pokles
# :return   (name, year, decrease), kde jmeno je typu str a rok typu int.
#           Rok je rok po kterem doslo k nejvetsimu poklesu pro dane jmeno
#           decrease je typu int a jedna se o percentuelni pokles zaokrouhleny
#           na cele cislo


def maximal_decrease(dict, min_occurence):
    return ("", 0, 0)


# Funkce nalezne a vrati seznam jmen, ktera zazila dany rok nejvetsi narust
# popularity oproti predchozimu roku v absolutnim poctu (prvni misto seznamu
# tedy bude mit jmeno jenz zazilo nejvetsi narust popularity dle poctu vyskytu
# v roce 1951 oproti roku 1950, druhe pak narust v roce 1952 oproti roku 1951,
# ...

# :param dct:   slovnik v jehoz datech vyhledavame vysledky
# :return lst   seznam obsahuji jmena ktera zazila nejvetsi narust popularity
#               oproti predchozimu roku (pocinaje rokem 1951)


def max_increase_for_each_year(dict):
    max_lst = []
    return max_lst


# Cviceni https://www.umimecesky.cz/diktaty pouziva jako interni reprezentaci
# format ulozeny v souboru diktat.txt. Napiste program, ktery pro zadani
# v tomto formatu vrati text v korektni podobe (tj. dosadi z moznosti vzdy tu
# spravnou variantu).
# Priklad:
# "Zb[i/y|01]něk se rád zab[í/ý|01]vá hrou na b[i/y|10]cí." =>
# "Zbyněk se rád zabývá hrou na bicí."
# "V zrcadle m[ě/ně|10] sleduje nějaký b[ě/je|10]s." =>
# "V zrcadle m[ě/ně|10] sleduje nějaký b[ě/je|10]s."

# Pro reseni teto ulohy jsem si vyhledala, jak rozdelit string
# pomoci vice znaku a jak ze seznamu udelat string.
def dictation(text):
    replace_lst = []
    final = ""
    text = re.split('\]|\[', text)

    for chars in text:
        if '/' in chars:
            split = re.split('\/|\|', chars)

            if '01' in split:
                replace_lst.append(split[1])

            if '10' in split:
                replace_lst.append(split[0])

    for i in range(len(text)):
        if '/' in text[i]:
            character = replace_lst.pop(0)
            text[i] = character

    return final.join(text)



########################################################################
#               Nasleduje kod testu,                                   #
########################################################################


def ib113_test_load_data_to_dictionary(dct):
    print("************* TEST LOAD DATA TO DICTIONARY *************")

    if not isinstance(dct, dict):
        print("NOK: Nebyla vracena promenna typu slovnik")
        return False

    input_data = [("IVAN", 1960), ("ANNA", 2000), ("ALENA", 1982),
                  ("DAVID", 1950), ("EVA", 2010), ("HANA", 2001),
                  ("ALENA", 1990), ("BARBORA", 1982)]
    output_data = [668, 1382, 1146, 9, 358, 504, 547, 1044]
    failure = False

    for i in range(len(input_data)):
        try:
            res = dct[input_data[i][0]][input_data[i][1]]
        except KeyError:
            print("NOK, data pravdepodobne nemaji spravnou strukturu. Nebylo "
                  "mozne ziskat data pro dotaz dictionary[%s][%d]" %
                  (input_data[i][0], input_data[i][1]))
            failure = True
            break

        if not isinstance(res, int):
            failure = True
            print("NOK, Nebyla vracena hodnota typu retezec, ale typu %s" %
                  type(res))
            failure = True
            break
        if res != output_data[i]:
            failure = True
            print("NOK: Data nemaji spravnou strukturu nebo nenacitaji data "
                  "koretne. Pro jmeno %s a rok %d byl vracem vysledek %d, ale"
                  " byl ocekavan vysledek %d" %
                  (input_data[i][0], input_data[i][1], res, output_data[i]))
            failure = True
            break

    if failure:
        return False
    print("OK")
    return True


def ib113_test_n_most_popular_for_given_year(dct):
    print("************* TEST N_MOST_POPULAR_FOR_GIVEN_YEAR *************")
    failure = False

    input_data = [(5, 1982), (10, 1982), (3, 2001)]
    output_data = [['JAN', 'PETR', 'MARTIN', 'LUCIE', 'TOMÁŠ'],
                   ['JAN', 'PETR', 'MARTIN', 'LUCIE', 'TOMÁŠ', 'JANA', 'JIŘÍ',
                    'MICHAL', 'PETRA', 'LENKA'], ['JAN', 'TOMÁŠ', 'JAKUB']]

    for i in range(len(input_data)):
        res = n_most_popular_for_given_year(dct, input_data[i][0],
                                            input_data[i][1])

        if not isinstance(res, list):
            failure = True
            print("NOK: Nebyla vracena hodnota typu list, ale typu %s" %
                  type(res))
            break
        if res != output_data[i]:
            failure = True
            print("NOK: Pro rok %d a pocet jmen %d byl vracen list %s, ale byl"
                  " ocekavan list %s" % (input_data[i][0], input_data[i][1],
                                         res, output_data[i]))
            break

    if not failure:
        print("OK")


def ib113_test_most_popular_in_what_year(dct):
    print("************* TEST MOST_POPULAR_IN_WHAT_YEAR *************")
    failure = False

    input_data = ["ABC", "DAVID", "EVA", "HANA", "ALENA", "BARBORA"]
    output_data = [None, 1979, 1955, 1956, 1955, 1993]

    for i in range(len(input_data)):
        res = most_popular_in_what_year(dct, input_data[i])

        if output_data[i] is None:
            if res is not None:
                failure = True
                print("NOK: Mela byt vracena hodnota None, ale byla vracena"
                      " jina hodnota typu %s)" % type(res))
                break
            continue

        if not isinstance(res, int):
            failure = True
            print("NOK: Pro jmeno %s nebyla vracena hodnota typu int, ale "
                  "typu %s" % (input_data[i], type(res)))
            break
        if res != output_data[i]:
            failure = True
            print("NOK: Pro jmeno %s byl vracen rok %d, ale byl ocekavan rok "
                  "%d." % (input_data[i], res, output_data[i]))
            break

    if not failure:
        print("OK")


def ib113_test_maximal_increase(dct):
    print("************* TEST MAXIMAL_INCREASE *************")
    failure = False

    input_data = ["ABC", "DAVID", "EVA", "HANA", "ALENA", "BARBORA"]
    output_data = [None, 1973, 1962, 1953, 1952, 1987]

    for i in range(len(input_data)):
        res = maximal_increase(dct, input_data[i])

        if output_data[i] is None:
            if res is not None:
                failure = True
                print("NOK: Mela byt vracena hodnota None, ale byla vracena"
                      " jina hodnota typu %s)" % type(res))
                break
            continue

        if not isinstance(res, int):
            failure = True
            print("NOK: Pro jmeno %s nebyla vracena hodnota typu int, ale "
                  "typu %s" % (input_data[i], type(res)))
            break
        if res != output_data[i]:
            failure = True
            print("NOK: Pro jmeno %s byl vracen rok %d, ale byl ocekavan rok "
                  "%d." % (input_data[i], res, output_data[i]))
            break

    if not failure:
        print("OK")


def ib113_test_maximal_decrease(dct):
    print(
        "************* TEST MAXIMAL_DECREASE *************")
    failure = False

    input_data = [50, 100, 400, 500, 1000]
    output_data = [("RADOMÍRA", 1971, 88), ("RADOMÍRA", 1971, 88),
                   ("ANETA", 2012, 63), ("ANETA", 2012, 63),
                   ("VOJTĚCH", 2012, 60)]

    for i in range(len(input_data)):
        res = maximal_decrease(dct, input_data[i])

        if not isinstance(res, tuple):
            failure = True
            print("NOK: Nebyla vracena hodnota typu tuple, ale typu %s" %
                  type(res))
            break

        if not isinstance(res[0], str) or not isinstance(res[1], int) or \
                not isinstance(res[2], int):
            failure = True
            print("NOK: Nebyla vracena hodnota typu tuple(str, int, int), ale "
                  "typu tuple(%s, %s, %s)" % (
                      type(res[0]), type(res[1]), type(res[2])))
            break

        if res[0] != output_data[i][0] or res[1] != output_data[i][1] or \
                res[2] != output_data[i][2]:
            failure = True
            print("NOK: Pro minimalne pocet jmen %d bylo vraceno jmeno %s, "
                  "rok %d a pokles %d, ale bylo ocekavano jmeno %s, rok %d "
                  "a pokles %d." % (
                      input_data[i], res[0], res[1], res[2], output_data[i][0],
                      output_data[i][1], output_data[i][2]))
            break

    if not failure:
        print("OK")


def ib113_test_max_increase_for_each_year(dct):
    print("************* TEST MAX_INCREASE_FOR_EACH_YEAR *************")
    failure = False

    output_data = ["JIŘÍ", "JIŘÍ", "ALENA", "MIROSLAV", "ZDENĚK", "JANA",
                   "LUBOŠ", "DANA", "PETR", "PETR", "IVA", "PAVEL", "PAVEL",
                   "IVANA", "PAVLÍNA", "PETRA", "MARTIN", "MARTIN", "RADEK",
                   "MARTIN", "MARTIN", "RADKA", "MAREK", "PETRA", "TOMÁŠ",
                   "PETRA", "KATEŘINA", "MICHAELA", "LUKÁŠ", "LUCIE", "LUCIE",
                   "VERONIKA", "LUKÁŠ", "JAKUB", "LUCIE", "VERONIKA", "LUCIE",
                   "TOMÁŠ", "TEREZA", "JAKUB", "DAVID", "DANIEL", "KRISTÝNA",
                   "DOMINIK", "DOMINIK", "KRISTÝNA", "TEREZA", "DOMINIK",
                   "MATĚJ", "NATÁLIE", "ELIŠKA", "ADAM", "MATĚJ", "ADAM",
                   "ADAM", "JAKUB", "ADAM", "MATYÁŠ", "MATYÁŠ", "VOJTĚCH",
                   "SOFIE", "MATYÁŠ", "NEZJIŠTĚNO"]

    res = max_increase_for_each_year(dct)
    if not isinstance(res, list):
        failure = True
        print("NOK: Nebyla vracena hodnota typu list, ale typu %s" %
              type(res))
    elif len(res) != len(output_data):
        failure = True
        print("NOK: Seznam ma delku %d ale je ocekavana delka %d" % (
            len(res), len(output_data)))
    else:
        for i in range(len(res)):
            if res[i] != output_data[i]:
                failure = True
                print(
                    "NOK: Pro rok %d bylo vraceno jmeno %s, ale bylo ocekavano"
                    " jmeno %s" % (i + 1951, res[i], output_data[i]))
                break

    if not failure:
        print("OK")


def ib113_test_dictation():
    input = [
        "Zb[i/y|01]něk se rád zab[í/ý|01]vá hrou na b[i/y|10]cí.",
        "Ob[i/y|01]čejně hraje ve svém ob[i/y|01]dlí, na B[i/y|01]stré ulici.",
        "Náb[i/y|01]tek v celém b[i/y|01]tě se otřásá, "
        "hluk přib[í/ý|01]vá a maminka se zlob[í/ý|10].",
        "Cítím se jako ob[ě/je|10]ť ranního vstávání.",
        "Budík m[ě/ně|10] do nového dne nevítá jem[ě/ně|01] a přátelsky,"
        "ale rozeřve se jako bezohledný dráb.",
        "Sm[ě/ně|10]le otevřu jedno oko, pak oči ob[ě/je|10] a je to.",
        "V[ě/je|01]zd do nového dne povolen!",
        "Venku padal[i/y|01] provaz[i/y|01] vody.",
        "Z[i/y|10]ma zalézala pod kožešinová kaťata.",
        "Pračlov[í/ý|10]čata se vracela z pralesa vymrzlá ne na kost,"
        "ale na jejich prakostičky.",
        "Jako všechny správné praděti b[i/y|01]la parádně hladová,"
        "protože naposledy jedl[i/a|01] už pradávno.",
        "Brz[i/y|01] ráno."
    ]

    output = [
        "Zbyněk se rád zabývá hrou na bicí.",
        "Obyčejně hraje ve svém obydlí, na Bystré ulici.",
        "Nábytek v celém bytě se otřásá, hluk přibývá a maminka se zlobí.",
        "Cítím se jako oběť ranního vstávání.",
        "Budík mě do nového dne nevítá jemně a přátelsky,ale rozeřve se jako "
        "bezohledný dráb.",
        "Směle otevřu jedno oko, pak oči obě a je to.",
        "Vjezd do nového dne povolen!",
        "Venku padaly provazy vody.",
        "Zima zalézala pod kožešinová kaťata.",
        "Pračlovíčata se vracela z pralesa vymrzlá ne na kost,ale na jejich "
        "prakostičky.",
        "Jako všechny správné praděti byla parádně hladová,protože naposledy "
        "jedla už pradávno.",
        "Brzy ráno."
    ]

    print("************* TEST DICTATION *************")
    failure = False
    for i in range(len(input)):
        if not isinstance(dictation(input[i]), str):
            failure = True
            print("NOK: Nebyla vracena hodnota typu str, ale typu %s" %
                  type(res))
        elif dictation(input[i]) != output[i]:
            failure = True
            print("NOK: Pro vetu {} byl vracen vysledek '{}', ale byl "
                  "ocekavan '{}'".format(input[i], dictation(input[i]),
                                         output[i]))
            break

    if not failure:
        print("OK")


# Hlavni funkce volana automaticky po spusteni programu.
if __name__ == '__main__':
    ib113_test_dictation()
    dct = load_data_to_dictionary()
    if ib113_test_load_data_to_dictionary(dct):
        ib113_test_n_most_popular_for_given_year(dct)
        ib113_test_most_popular_in_what_year(dct)
        ib113_test_maximal_increase(dct)
        ib113_test_maximal_decrease(dct)
        ib113_test_max_increase_for_each_year(dct)