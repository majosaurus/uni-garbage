from math import pi, pow


# Vytvorte program pocitajici objem kvadru a objem koule
def volume_block_ball(a, b, c, r):
    volume_block = a * b * c
    print("Objem kvadru je roven:", volume_block, "cm^3")

    volume_ball = 4 / 3 * pi * r ** 3
    print("Objem koule je roven:", volume_ball, "cm^3")


# Vypiste prvnich 10 mocnin cisla 2.
# Oddelte je carkou a mezerou (za posledni cislici neni carka)
def powers(count):
    for i in range(10):
        count = 2 ** i
        print(count, end=" ")


# Vypiste prvnich 15 prvku Fibonnaciho posloupnosti.
def print_fibonnaci(count):
    a = 0
    b = 1
    print(a, b, end=" ")

    for i in range(count):
        total = a + b
        print(total, end=" ")

        a = b
        b = total


# Napiste funkci, ktera vypise prvnich 10 prvku posloupnosti, jejichz prvni
# prvky vypadaji nasledovne:
#   a) 1 -1 2 -2 3 -3 4 -4 5 -5 …
def print_alternating(length):
    for i in range(1, length + 1):
        print(i, end=" ")
        i = i * -1
        print(i, end=" ")


#   b) 1 1 2 1 2 3 1 2 3 4 …
def print_subsequence(length):
    for i in range(1, length + 1):
        for j in range(1, i):
            print(j, end=" ")


# Naleznete a vypiste vsechny delitele daneho cisla.
# Cislo zadejte pomoci promenne
def divisors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
    print(num)


# Rozsireni v pripade dostatku casu
# a) Cisla vypiste na jeden radek oddelena carkou
# b) Pro 0 a zaporna cisla vypiste chybovou hlasku


def divisors_extended(num):
    if num == 0 or num < 0:
        print("Nelze")

    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=",")
    print(num)


TESTED_NUMBER = 1586  # je to konstanta, proto UPPER_CASE
# tested_number = int(input("Zadej cislo: "))
print("Zakladni verze:")
divisors(TESTED_NUMBER)
print()
print("Rozsirena verze:")
divisors_extended(TESTED_NUMBER)
