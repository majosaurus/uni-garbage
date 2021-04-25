# Napiste funkci, ktera vam vrati retezec s pismeny usporadanymi pozpatku.
def reverse(text):
    reversed_text = ""

    for character in text:
        reversed_text = character + reversed_text

    return reversed_text


reverse("abcd")


# HESLOJETAJEMNO


# Mezi kazda dve pismena daneho textu vlozte dodany text (jako novy parametr
# funkce)
def reverse_for_dummies(text, rubbish):
    text = reverse(text)
    encrypted_text = ""

    for character in text:
        encrypted_text += character + rubbish

    return encrypted_text


print(reverse_for_dummies('', 'X'))
# <prazdny retezec>
print(reverse_for_dummies('ONMEJATEJOLSEH', 'X'))
# HXEXSXLXOXJXEXTXAXJXEXMXNXO
print()


# Napiste funkci, ktera vrati novy retezec, ve kterem bylo kazde pismenko
# zdvojeno.
# duplication("PYTHON") => PPYYTTHHOONN


def duplication(text):
    doubled_text = ""

    for character in text:
        doubled_text += character * 2

    return doubled_text


duplication("ABCD")


# Napiste funkci, ktera dostane dva retezce a vrati ty znaky, ktere jsou na
# shodnych pozicich stejne.
# string_intersection('ZIRAFA', 'KARAFA') => RAFA
# string_intersection('PES', 'KOCKA') => (prazdny retezec)


def string_intersection(left, right):
    identical_chars = ""

    if len(left) > len(right):
        minimum = len(right)
    else:
        minimum = len(left)

    for i in range(minimum):
        left_char = ord(left[i])
        right_char = ord(right[i])

        if left_char == right_char:
            identical_chars += (chr(left_char))

    return identical_chars


# Napiste funkci, ktera vrati, zda je retezec palindromem. Palindromem je
# takove slovo ci veta, ktera ma pri cteni v libovolnem smeru stejny vyznam,
# napriklad nepotopen ci jelenovi pivo nelej (mezery muzete ignorovat).
# palindrom("JELENOVIPIVONELEJ") => True


def palindrom(text):
    text.upper()
    text_len = len(text)

    for i in range(text_len):
        front_char = text[i]
        back_char = text[text_len - 1 - i]

        if front_char != back_char:
            return False

    return True


palindrom("jelenovipivonelej")


# Kazdy znak A-Z ma hodnotu 1-26 (diakritiku a velikost pismen pro tento
# priklad ignorujte). Napiste funkci, ktera spocita a vrati hodnotu vlozeneho
# retezce (slova).
# word_value("AHOJ") => 34
def word_value(text):
    ORD_VAL = 64  # ordinalni hodnota A = 65, tj. odectenim 64 dostaneme A = 1
    text.upper()
    total = 0

    for character in text:
        total += ord(character) - ORD_VAL

    return total


########################################################################
#               Nasleduje kod testu                                    #
########################################################################

ib113_duplication_in = ("", "a", "PYTHON", "tESt")
ib113_duplication_out = ("", "aa", "PPYYTTHHOONN", "ttEESStt")


def ib113_test_duplication():
    print("Testovani funkce duplication: ", end="")
    failure = False

    for i in range(len(ib113_duplication_in)):
        res = duplication(ib113_duplication_in[i])
        if not isinstance(res, str):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu str, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_duplication_out[i]:
            failure = True
            print("NOK")
            print("Pro vstup \"{}\" nebyl vracen spravny vysledek"
                  .format(ib113_duplication_in[i]))
            print("Byl vracen vysledek: \"{}\"".format(res))
            print("Byl ocekavan vysledek: \"{}\""
                  .format(ib113_duplication_out[i]))
            break

    if not failure:
        print("OK")


ib113_string_intersection_in = (("ZIRAFA", "KARAFA"), ("PES", "KOCKA"),
                                ("", ""), ("AB", "AB"), ("KOCKA", "PES"))
ib113_string_intersection_out = ("RAFA", "", "", "AB", "")


def ib113_test_string_intersection():
    print("Testovani funkce string_intersection: ", end="")
    failure = False

    for i in range(len(ib113_string_intersection_in)):
        res = string_intersection(ib113_string_intersection_in[i][0],
                                  ib113_string_intersection_in[i][1])
        if not isinstance(res, str):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu str, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_string_intersection_out[i]:
            failure = True
            print("NOK")
            print("Pro vstupy \"{}\" a \"{}\" nebyl vracen spravny vysledek"
                  .format(ib113_string_intersection_in[i][0],
                          ib113_string_intersection_in[i][1]))
            print("Byl vracen vysledek: \"{}\"".format(res))
            print("Byl ocekavan vysledek: \"{}\"".format(
                ib113_string_intersection_out[i]))
            break

    if not failure:
        print("OK")


ib113_palindrom_in = ("JELENOVIPIVONELEJ", "", "AB", "ABA", "AAA", "BBC")
ib113_palindrom_out = (True, True, False, True, True, False)


def ib113_test_palindrom():
    print("Testovani funkce palindrom ", end="")
    failure = False

    for i in range(len(ib113_palindrom_in)):
        res = palindrom(ib113_palindrom_in[i])
        if not isinstance(res, bool):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu bool, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_palindrom_out[i]:
            failure = True
            print("NOK")
            print("Pro hodnotu \"{}\" nebyl vracen spravny vysledek"
                  .format(ib113_palindrom_in[i]))
            print("Byl vracen vysledek: {}".format(res))
            print("Byl ocekavan vysledek: {}".format(ib113_palindrom_out[i]))
            break

    if not failure:
        print("OK")


ib113_word_value_in = ("A", "", "AHOJ", "AAA")
ib113_word_value_out = (1, 0, 34, 3)


def ib113_test_word_value():
    print("Testovani funkce word_value: ", end="")
    failure = False

    for i in range(len(ib113_word_value_in)):
        res = word_value(ib113_word_value_in[i])
        if not isinstance(res, int):
            failure = True
            print("NOK")
            print("Nebyla vracena hodnota typu int, "
                  "ale typu {}".format(type(res)))
            break
        if res != ib113_word_value_out[i]:
            failure = True
            print("NOK")
            print("Pro vstup \"{}\" nebyl vracen spravny vysledek"
                  .format(ib113_word_value_in[i]))
            print("Byl vracen vysledek: {}".format(res))
            print("Byl ocekavan vysledek: {}".format(ib113_word_value_out[i]))
            break

    if not failure:
        print("OK")


# Zde muzete vkladat vlastni testy
if __name__ == '__main__':
    ib113_test_duplication()
    print()
    ib113_test_string_intersection()
    print()
    ib113_test_palindrom()
    print()
    ib113_test_word_value()
