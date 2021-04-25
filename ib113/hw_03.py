# Pyramida
def pyramid(n):
    symbol = 0
    for i in range(1, n + 1):
        for j in range(1, (n - i) + 1):
            print(" ", end=" ")

        while symbol != ((2 * i) - 1):
            print("#", end=" ")
            symbol += 1

        symbol = 0
        print()


pyramid(6)


# Napiste funkci make_fancy(text, n),ktera vypise text sikmo
# a navic n-krat za sebou.
def make_fancy(text, n):
    space_count = 0

    for i in range(len(text)):
        print(" " * space_count, end="")

        for j in range(n):
            print(text[i], end=" ")

        space_count += 1
        print()


# Napiste funkci censorship(text), ktera vrati zadany retezec text,
# ve kterem nahradi kazde druhe pismeno za X.
def censorship(text):
    censored_text = ""

    for i in range(len(text)):
        if i % 2 == 0:
            censored_text += text[i]
        if i % 2 == 1:
            censored_text += "X"

    return censored_text


# Napište funkci alphabet(n), která vypíše prvních n písmen anglické abecedy.
# Pokud je n větší jak 26, písmena jsou vypisována opakovaně.
def alphabet(n):
    letter = ord("A")  # 65

    for i in range(1, n + 1):
        if letter > ord("Z"):
            letter = ord("A")

        print(chr(letter))
        letter += 1


# Napište funkci first_letters(text), která vypíše první
# písmena slov ze zadaného řetězce text.
def first_letters(text):
    split_text = text.split()

    for i in range(len(split_text)):
        print(split_text[i], end="")


# Napište funkci zigzag(text), vypíše zadaný text 'cik-cak' na dva řádky
# s prázdnými místy vyznačenými tečkami (viz ukázkový výstup).
# P.R.U.I.E
# .A.D.B.C.
def zigzag(text):
    for i in range(2):
        if i % 2 == 0:
            print(text[i])
        if i % 2 == 1:
            print(".")


# Napište funkci five_multiples(num_list), která vezme seznam čísel
# num_list a vrátí seznam těch čísla ze seznamu, která jsou dělitelná
# pěti (v původním pořadí).
def five_multiples(num_list):
    five_list = []

    for number in num_list:
        if number % 5 == 0:
            five_list.append(number)

    return five_list


five_multiples([3, 5, 25, 4, 7, 49, 35, 12])


# Napište funkci nonzero_product(numbers), která pro zadaný seznam čísel
# numbers vrátí součin všech nenulových čísel v seznamu.
def nonzero_product(numbers):
    aux_variable = 1

    for num in numbers:
        if num != 0:
            aux_variable = aux_variable * num

    return aux_variable


# Napište funkci every_second_number(num_list), která ze zadaného seznamu čísel
# num_list vypíše každé druhé číslo (počínaje prvním).
def every_second_number(num_list):
    for i in range(len(num_list)):
        if i % 2 == 0:
            print(num_list[i])


# Napište funkci unique(mylist), která vrátí seznam obsahující každý prvek
# ze seznamu mylist právě jedenkrát (v pořadí prvních výskytů v původním seznamu).
def unique(mylist):
    unique_list = []

    for num in mylist:
        if num not in unique_list:
            unique_list.append(num)

    return unique_list


# Napište funkci find_longest_word(words_list),
# která vrátí nejdelší slovo ze zadaného seznamu slov words_list.
# Pokud je nejdelších slov více, vrátí to z nich, které je v seznamu uvedeno jako první.
def find_longest_word(words_list):
    longest_word = ""

    for word in words_list:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


# Napište funkci max_pair_sum(num_list), která pro zadaný seznam kladných
# čísel num_list vypočítá nejvyšší součet dvou po sobě jdoucích čísel.
def max_pair_sum(num_list):
    aux_number = 0
    current_sum = 0
    max_sum = 0

    for num in num_list:
        if num == aux_number + 1 or num == aux_number - 1:
            current_sum = num + aux_number

        if current_sum > max_sum:
            max_sum = current_sum

        aux_number = num

    return max_sum


# Napište funkci check_sudoku(row), která zkontroluje, zda v zadaný řádek
# čísel row obsahuje každé číslo od 1 do 9 právě jedenkrát (a nic jiného).
def check_sudoku(row):
    check_list = []

    if len(row) > 9 or len(row) < 9:
        return False

    for i in range(len(row)):
        if row[i] in check_list:
            return False

        check_list.append(row[i])

    return True


def big_frame(word_list):
    longest_word = ""

    for i in range(len(word_list)):
        if len(word_list[i]) > len(longest_word):
            longest_word = word_list[i]


big_frame(["Ahoj", "Brno"])


# Napište funkci decide(symbol1, symbol2), která rozhodne,
# kdo vyhrál ve hře kámen-nůžky-papír. Tahy jsou zadány prvními
# písmeny (symbol1, symbol2). Funkce má za úkol vypsat písmeno
# odpovídající tahu, který vítězí, nebo text 'Remiza'.
def decide(symbol1, symbol2):
    if symbol1 == symbol2:
        print("Remiza")

    if symbol1 == "K":
        if symbol2 == "N":
            print("K")
        if symbol2 == "P":
            print("P")

    if symbol1 == "N":
        if symbol2 == "K":
            print("K")
        if symbol2 == "P":
            print("N")

    if symbol1 == "P":
        if symbol2 == "K":
            print("P")
        if symbol2 == "N":
            print("N")


# Vypiste pismeno E
def letter_e(width):
    print("#" * width)
    for i in range(width // 2):
        print("#")
    print("#" * width)
    for i in range(width // 2):
        print("#")
    print("#" * width)


# Upravte funkci cross(n), aby vykreslovala ze znaků '#' kříž šířky n
def cross(n):
    for i in range(1, (3 * n) + 1):
        for j in range(1, (3 * n) + 1):
            if n < j <= 2 * n or n < i <= 2 * n:
                print("#", end="")
            else:
                print(".", end="")
        print()


# Napište funkci greatest_common_divisor(a, b), která pro zadaná čísla a, b
# vrátí jejich největšího společného dělitele.
def greatest_common_divisor(a, b):
    divisor = 0

    if a > b:
        smaller_num = b
    else:
        smaller_num = a

    for i in range(1, smaller_num + 1):
        if a % i == 0 and b % i == 0:
            divisor = i

    return divisor


# Napište funkci print_primes(n), která vypíše prvních n prvočísel
# (prvočíslo je přirozené číslo, které je dělitelné pouze jedničkou
# a sebou samým).
def print_primes(n):
    number_of_nums = 0
    num = 2

    while number_of_nums != n:
        if is_prime(num):
            print(num)
            number_of_nums += 1

        num += 1


def is_prime(num):
    counter = 0

    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1

            if counter > 2:
                return False

    return True


# Napište funkci factorize(n), která rozloží zadané číslo
# n na součin prvočísel (ve vzestupném pořadí).
def factorize(n):
    dividend = n
    divisor = 2
    div = []

    while not is_prime(dividend):
        if is_divisible(dividend, divisor):
            dividend //= divisor


def is_prime(num):
    counter = 0

    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1

            if counter > 2:
                return False

    return True


def is_divisible(num, divisor):
    if num % divisor == 0 and divisor > 0:
        return True

    return False

