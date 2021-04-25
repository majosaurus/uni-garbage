from random import randint


def odd_cube(limit):
    number = 1
    total = 0
    number_of_throws = 0

    if number_of_throws < limit:
        while number % 2 == 1:
            number = randint(1, 6)
            total = total + number
            number_of_throws += 1
            print(number, end=" ")

    print()
    print("Pocet hodu:", number_of_throws)
    print("Prumer hodu:", total / number_of_throws)

    return total


odd_cube(4)
