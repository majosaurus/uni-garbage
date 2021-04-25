def russian_inflection():
    number = int(input("Enter a number to find out how to inflect following Russian noun correctly: "))

    last_digit = number % 10

    if last_digit == 1:
        print("Nominative singular")
        return 0

    if last_digit == 2 or last_digit == 3 or last_digit == 4:
        last_two_digits = number % 100

        if last_two_digits == 12 or last_two_digits == 13 or last_two_digits == 14:
            print("Genitive plural")
            return 0

        print("Genitive singular")
        return 0

    print("Genitive plural")
    return 0

russian_inflection()


