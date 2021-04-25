from random import randint, random

# Napiste funkci, ktera bude provadet hazeni obycejnou sestistennou kostkou
# tak dlouho dokud nepadne liche cislo, pricemz jednotlive hody vypisujte na
#  jeden radek. Pote funkce vrati celkovy soucet vsech hozenych hodu.
def even_turn():
    number = 1
    total = 0
    number_of_throws = 0

    while number % 2 == 1:
        number = randint(1, 6)
        total = total + number
        number_of_throws += 1
        print(number, end=" ")

        print()
        print("Pocet hodu:", number_of_throws)
        print("Prumer hodu:", total / number_of_throws)

        return total


print("\nVysledek =", even_turn())
print("\nVysledek =", even_turn())
print("\nVysledek =", even_turn())


# Ve funkci vypiste pocet hozeni kostkou a prumer hodu
def even_turn2():
    return 0  # TODO


print("\nVysledek =", even_turn2())
print("\nVysledek =", even_turn2())
print("\nVysledek =", even_turn2())


# Prestante hazet, pokud hody prekroci hranici danou novym parametrem limit
# Nastavte, ze prvnich first hodu muze padnout i liche cislo
def even_turn3(limit, first):
    return 0  # TODO


print("\nVysledek =", even_turn3(10, 3))
print("\nVysledek =", even_turn3(15, 4))
print("\nVysledek =", even_turn3(100, 5))


# Napiste funkci divisors_count(n), ktera vrati pocet delitelu cisla n
def divisors_count(n):
    divisors_found = 0

    for i in range(1, n + 1):
        if n % i == 0:
            divisors_found += 1

    return divisors_found


# Napiste funkci is_prime(n), ktera vrati True pokud je cislo n prvocislo,
# jinak False
def is_prime(n):
    return divisors_count(n) == 2


# Napiste funkci kth_prime(k), ktera vrati k-te prvocislo.
def kth_prime(k):
    count = 0
    num = 0

    if count == num:
        while count <= num:
            is_prime(k)
            count += 1

    return num


# Napiste funkci, ktera vygeneruje a vypise count nahodnych cisel v intervalu
# [lower, upper], pricemz jednotlive hody vypisujte na jeden radek. Nasledne
# vypise nejmensi, nejvetsi a prumerne cislo.
def dice_freq(count, lower, upper):
    return 0


dice_freq(10, 1, 16)

# Opilec na ceste domu
# Opilec je na puli cesty mezi domovem a hospodou, kazdy krok udela nahodne
# jednim smerem. Napiste funkci, ktera bude simulovat opilcuv pohyb. Jejimy
# parametry budou vzdalenost mezi domovem a hospodou a pocet kroku do
# opilcova usnuti (tj. maximalni delka simulace). Simulace skonci bud tehdy,
# kdyz opilec dojede domu nebo do hospody, pripadne po vycerpani poctu kroku.

# Ukazka vystupu:
# home . . . . . * . . . . pub
# home . . . . * . . . . . pub
# home . . . * . . . . . . pub
# home . . . . * . . . . . pub
# home . . . * . . . . . . pub
# home . . . . * . . . . . pub
# home . . . * . . . . . . pub
# home . . * . . . . . . . pub
# home . * . . . . . . . . pub
# home * . . . . . . . . . pub
# home . . . . . . . . . . pub
# Got home!


# Upravte funkci z predchozi prikladu tak, aby nevypisovala stav opilce
# (napriklad pridanim volitelneho parametru output a zapodminkovanim vypisu)
# a aby vracela True dojde-li opilec domu a False pokud ne.


def drunkman_simulator(size, steps, output=False):
    pass  # TODO


drunkman_simulator(10, 10)


# Nasledne napiste funkci, ktera provede simulaci opilce count krat a vypise
# procentualni uspesnost dojiti domu.


def drunkman_analysis(size, steps, count):
    pass  # TODO


drunkman_analysis(10, 100, 100)
print()


########################################################################
#               Nasleduje kod testu                                    #
########################################################################

ib113_divisors_in = (1, 5, 42, 127, 1024)
ib113_divisors_out = (1, 2, 8, 2, 11)


def ib113_test_divisors_count():
    print("Testovani funkce divisors_count: ", end="")
    failure = False

    for i in range(len(ib113_divisors_in)):
        res = divisors_count(ib113_divisors_in[i])
        if not isinstance(res, int):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu int, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_divisors_out[i]:
            failure = True
            print("NOK")
            print("Pro hodnotu {} nebyl vracen spravny vysledek"
                  .format(ib113_divisors_in[i]))
            print("Byl vracen vysledek: {}".format(res))
            print("Byl ocekavan vysledek: {}".format(ib113_divisors_out[i]))
            break

    if not failure:
        print("OK")


ib113_is_prime_in = (1, 2, 3, 42, 127)
ib113_is_prime_out = (False, True, True, False, True)


def ib113_test_is_prime():
    print("Testovani funkce is_prime_count: ", end="")
    failure = False

    for i in range(len(ib113_is_prime_in)):
        res = is_prime(ib113_is_prime_in[i])
        if not isinstance(res, int):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu int, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_is_prime_out[i]:
            failure = True
            print("NOK")
            print("Pro hodnotu {} nebyl vracen spravny vysledek"
                  .format(ib113_is_prime_in[i]))
            print("Byl vracen vysledek: {}".format(res))
            print("Byl ocekavan vysledek: {}".format(ib113_is_prime_out[i]))
            break

    if not failure:
        print("OK")


ib113_kth_prime_in = (1, 2, 10, 100)
ib113_kth_prime_out = (2, 3, 29, 541)


def ib113_test_kth_prime():
    print("Testovani funkce kth_prime_count: ", end="")
    failure = False

    for i in range(len(ib113_kth_prime_in)):
        res = kth_prime(ib113_kth_prime_in[i])
        if not isinstance(res, int):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu int, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_kth_prime_out[i]:
            failure = True
            print("NOK")
            print("Pro hodnotu {} nebyl vracen spravny vysledek"
                  .format(ib113_kth_prime_in[i]))
            print("Byl vracen vysledek: {}".format(res))
            print("Byl ocekavan vysledek: {}".format(ib113_kth_prime_out[i]))
            break

    if not failure:
        print("OK")


# Zde muzete vkladat vlastni testy
if __name__ == '__main__':
    ib113_test_divisors_count()
    print()
    ib113_test_is_prime()
    print()
    ib113_test_kth_prime()
