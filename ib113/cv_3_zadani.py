# Napiste funkci digit_sum(n), ktera vrati ciferny soucet cisla n.
def digit_sum(num):
    result = 0
    aux_variable = 0

    while num > 0:
        aux_variable = num % 10
        num = (num - aux_variable) // 10
        result = result + aux_variable

    return result


print(digit_sum(0))              # 0
print(digit_sum(274))            # 13
print(digit_sum(123456789))      # 45
print()


# Napiste funkci repeated_digit_sum(n), ktera opakovane vypocita ciferny
# soucet cisla n. Ze ziskaneho ciferneho souctu opet vypocita ciferny soucet
# (pokud se jedna o viceciferny soucet) a tento postup opakuje dokud nezbude
# jednociferne cislo, ktere vrati. Ke svemu reseni vyuzijte predchozi funkci.
def repeated_digit_sum(num):
    result = digit_sum(num)
    return digit_sum(result)


print(repeated_digit_sum(123))               # 6
print(repeated_digit_sum(123456789))         # 9
print(repeated_digit_sum(99989788879879))    # 7
print()


# Pomoci textove grafiky vykreslete vyplneny ctverec o strane 5
def print_full_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end=" ")
        print()


print_full_square(5)
print()


# Pomoci textove grafiky vykreslete prazdny ctverec o strane 5
def print_empty_square(size):
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()


print_empty_square(5)
print()


# Pomoci textove grafiky vykreslete sachovnici o velikosti 8x8
def chessboard(size):
    for i in range(1, size + 1):
        if i % 2 == 1:
            for j in range(size):
                if j % 2 == 0:
                    print("#", end=" ")
                else:
                    print(".", end=" ")
            print()
        else:
            for k in range(size):
                if k % 2 == 0:
                    print(".", end=" ")
                else:
                    print("#", end=" ")
            print()


chessboard(8)
print()


# Vypiste soucet prvnich N cisel pocinaje jednickou (pro jednicku vraci 1,
# pro dvojku 3, pro trojku 6, pro ctyrku 10, ...)
def sum_first_n(num):
    result = 0

    for i in range(1, num + 1):
        result += i

    return result


########################################################################
#               Nasleduje kod testu                                    #
########################################################################

ib113_divisors_in = (1, 2, 3, 4, 111, 1000)
ib113_divisors_out = (1, 3, 6, 10, 6216, 500500)


def ib113_test_sum_first_n():
    print("Testovani funkce sum_first_n: ", end="")
    failure = False

    for i in range(len(ib113_divisors_in)):
        res = sum_first_n(ib113_divisors_in[i])
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


# Zde muzete vkladat vlastni testy
if __name__ == '__main__':
    ib113_test_sum_first_n()
