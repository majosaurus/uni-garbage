number = int(input("Enter a number and see how to inflect the following Russian noun correctly: "))

last_digit = number % 10

case = ""
sg_pl = ""


if number % 10 == 1 and number != 11:
    case = "Nominative"

else:
    case = "Genitive"

if (number % 10 == 1 or number % 10 == 2 or number % 10 == 3 or number % 10 == 4) and \
        (number % 100 != 12 and number % 100 != 13 and number % 100 != 14):
    sg_pl = "singular"

else:
    sg_pl = "plural"

print(case, sg_pl)
