# ################################## HW1 ################################## #
"""
Pokyny:
- Deadline odevzdani: 6. 10. 2019 23:59
- Odevzdejte jediny soubor
- Muzete si vytvaret pomocne funkce, pokud chcete.
    - V teto uloze to neni potreba.
- V teto uloze je _zakazano_ pouzivat retezce a seznamy
- V pripade, ze chcete vytvaret vlastni testy, vkladete je na prislusne misto
    na konci souboru.
    - Pred odevzdanim vlastni modifikace smazte.
- Piste srozumitelny kod, pouzivejte vhodne nazvy promennych a funkci.
- Dodrzujte standard pep8 pomoci pycodestyle.
    - Budu kontrolovat a strhavat body za jeho nedodrzeni.
- Nemente hlavicky pripravenych funkci.
- Pripadne nejasnosti muzete resit v diskuznim foru. Pokud by ale mela otazka
    obsahovat kusy kodu, nebo neco, co by mohli ostatni studenti opsat, tak
    napiste radeji email.
- Pokud nevite, jak nejaky priklad vyresit kompletne, napiste do komentare,
    co vasemu reseni chybi.
- Neopisujte. Nestoji to za to. Dostanete zaporne body a budete muset ulohu
    stejne vypracovat sami.
"""


# Implementujte funkci, ktera bude vracet celou cast prumeru vsech lichych
# delitelu kladneho celeho cisla n. Napriklad pro 25 bude vracet 10, protoze
# lisi delitele cisla 25 jsou 1, 5, 25 a cela cast jejich prumeru je 31 // 3,
# tedy 10.


#   :param n:   Kladne cele cislo, jehoz liche delitele hledame
#   :return:    Hodnota obsahuji celou cast prumeru vsech lichych delitelu
#               cisla n
def odd_divisors_average(n):
    null = 0
    divisors_found = 0
    total = 0

    if n == 0 or n < 0:
        print("Nelze")

    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 1:
            total = i + null
            null = total
            divisors_found = divisors_found + 1

    average = total // divisors_found

    return average


# Implementujte funkci vypisujici k-ty prvek tribonacciho rady. Tribonacciho
# rada zacina hodnotami 0, 1 a 1 a kazda dalsi hodnota je souctem tri
# predchozich hodnot. Rada tedy pokracuje hodnotami 2, 4, 7, 13, 24, ...
# Na vstupu muzete ocekavat cela cisla vetsi nez nula.

#    :param position:   Poradi prvku tribonaciho rady, ktery hledame
#    :return:           Hodnota position-teho prvku tribonacciho rady
def tribonacci(position):
    a = 0
    b = 1
    c = 1
    total = 0

    if position > 3:
        for i in range(position - 3):
            total = a + b + c
            a = b
            b = c
            c = total
        return total

    if position == 1:
        return a

    if position == 2:
        return b

    if position == 3:
        return c


# Implementujte funkci, ktera urci pocet cifer cisla v desitkove soustave
# vetsich nebo rovno danemu limitu. Napr. pro hodnotu 905 a limit 5 vrati hodnotu 2.

#   :param n:   Kladne cele cislo v desitkove soustave, ktere zkoumame na
#               pocet cifer vetsich nez limit
#   :pamam limit: Limit pro cifry, ktere se maji spocitat
#   :return:    Pocet cifer cisla n, ktera jsou vetsi nebo rovna hodnote limit
def number_of_digits(n, limit):
    digits_quantity = 0

    while n > 0:
        aux_variable = n % 10
        if aux_variable >= limit:
            digits_quantity = digits_quantity + 1
        n = (n - aux_variable) // 10

    return digits_quantity


# Implementujte funkci, ktera obrati poradi cifer v danem cisle. Muzete
# predpokladat, ze vstupni cislo nekonci nulou. Napriklad cislo 12345 je
# prevedeno na cislo 54321.

#   :param num:   Cislo, ktere ma byt prevedeno, a ktere nekonci cifrou 0.
#   :return:    Cislo obsahujici cifry v opacnem poradi nez zadane cislo num.
def revert_number(num):
    result = 0

    while num > 0:
        aux_variable = num % 10
        num = (num - aux_variable) // 10
        result = (result + aux_variable) * 10

    return result // 10


# Implementujte funkci, ktera prevede cislo z desitkove soustavy do binarni.
# Napriklad 21 je prevedeno na 10101.

#   :param n:   Cislo v desitkove soustave typu int
#   :return:    Cislo v binarni soustave pomoci typu int
def from_dec_to_bin(n):
    binary = 0
    power = 0

    while n > 0:
        binary = binary + ((n % 2) * 10 ** power)
        n = n // 2
        power = power + 1

    return binary


########################################################################
#               Nasleduje kod testu                                    #
########################################################################

ib113_odd_entries = (1, 2, 3, 4, 8, 9, 25, 75, 99, 100)
ib113_odd_results = (1, 1, 2, 1, 1, 4, 10, 20, 26, 10)


def ib113_test_odd_divisor():
    print("Testovani funkce odd_divisors: ", end="")
    failure = False

    for i in range(len(ib113_odd_entries)):
        res = odd_divisors_average(ib113_odd_entries[i])
        if not isinstance(res, int):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu int, ale typu {}".
                  format(type(res)))
            break
        if res != ib113_odd_results[i]:
            failure = True
            print("NOK")
            print("Pro hodnotu {} nebyl vracen spravny vysledek".
                  format(ib113_odd_entries[i]))
            print("Byl navracen vysledek: {}".format(res))
            print("Byl ocekavan vysledek: {}".format(ib113_odd_results[i]))
            break

    if not failure:
        print("OK")


ib113_tribonacci_entries = (1, 2, 3, 4, 5, 6, 7, 8, 15, 25)
ib113_tribonacci_results = (0, 1, 1, 2, 4, 7, 13, 24, 1705, 755476)


def ib113_test_tribonacci():
    print("\nTestovani funkce tribonacci: ", end="")
    failure = False

    for i in range(len(ib113_tribonacci_entries)):
        res = tribonacci(ib113_tribonacci_entries[i])
        if not isinstance(res, int):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu int, ale typu {}".
                  format(type(res)))
            break
        if res != ib113_tribonacci_results[i]:
            failure = True
            print("NOK")
            print("Pro hodnotu {} nebyl vracen spravny vysledek".
                  format(ib113_tribonacci_entries[i]))
            print("Byl navracen vysledek: {}".format(res))
            print("Byl ocekavan vysledek: {}".
                  format(ib113_tribonacci_results[i]))
            break

    if not failure:
        print("OK")


ib113_number_of_digits_entries = (1, 15, 999, 1000, 99499, 150070)
ib113_number_of_digits_results = (0, 1, 3, 0, 4, 2)


def ib113_test_number_of_digits():
    print("\nTestovani funkce number_of_digits: ", end="")
    failure = False

    for i in range(len(ib113_number_of_digits_entries)):
        res = number_of_digits(ib113_number_of_digits_entries[i], 5)
        if not isinstance(res, int):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu int, ale typu {}".
                  format(type(res)))
            break
        if res != ib113_number_of_digits_results[i]:
            failure = True
            print("NOK")
            print("Pro hodnotu {} nebyl vracen spravny vysledek".
                  format(ib113_number_of_digits_entries[i]))
            print("Byla vracena hodnota: {}".format(res))
            print("Byla ocekavana hodnota: {}"
                  .format(ib113_number_of_digits_results[i]))
            break

    if not failure:
        print("OK")


ib113_test_revert_number_entries = (11, 501, 153, 123456789, 535, 987654321)
ib113_test_revert_number_results = (11, 105, 351, 987654321, 535, 123456789)


def ib113_test_revert_number():
    print("\nTestovani funkce revert_number: ", end="")
    failure = False

    for i in range(len(ib113_test_revert_number_entries)):
        res = revert_number(ib113_test_revert_number_entries[i])
        if not isinstance(res, int):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu int, ale typu {}".
                  format(type(res)))
            break
        if res != ib113_test_revert_number_results[i]:
            failure = True
            print("NOK")
            print("Pro vstup {} nebyl vracen spravny vysledek".
                  format(ib113_test_revert_number_entries[i]))
            print("Byl vracen vysledek: \"{}\"".format(res))
            print("Byla ocekavan vysledek: \"{}\"".
                  format(ib113_test_revert_number_results[i]))
            break

    if not failure:
        print("OK")


ib113_from_dec_to_bin_entries = (0, 1, 2, 3, 7, 8, 9, 16, 21, 1024, 2047)
ib113_from_dec_to_bin_results = (0, 1, 10, 11, 111, 1000, 1001, 10000, 10101,
                                 10000000000, 11111111111)


def ib113_test_from_dec_to_bin():
    print("\nTestovani funkce from_dec_to_bin: ", end="")
    failure = False

    for i in range(len(ib113_from_dec_to_bin_entries)):
        res = from_dec_to_bin(ib113_from_dec_to_bin_entries[i])
        if not isinstance(res, int):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu int, ale typu {}".
                  format(type(res)))
            break
        if res != ib113_from_dec_to_bin_results[i]:
            failure = True
            print("NOK")
            print("Pro hodnotu {} nebyl vracen spravny vysledek"
                  .format(ib113_from_dec_to_bin_entries[i]))
            print("Byla vracena hodnota: \"{}\"".format(res))
            print("Byla ocekavana hodnota: \"{}\"".
                  format(ib113_from_dec_to_bin_results[i]))
            break

    if not failure:
        print("OK")


if __name__ == '__main__':
    # Zde muzete vkladat vlastni testy
    ib113_test_odd_divisor()
    ib113_test_tribonacci()
    ib113_test_number_of_digits()
    ib113_test_revert_number()
    ib113_test_from_dec_to_bin()
