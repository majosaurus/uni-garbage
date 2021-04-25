vowels = ["a", "e", "i", "y", "o", "u"] # global variable used in functions

def infinitive(verb):
    """Function returns infinitive form of a verb"""
    return verb


def third_singular(verb):
    """Function returns third singular present form of a 
    verb. It takes exceptions and alternations into
    account"""

    if verb[-1] in ["s", "x", "z", "o"]:
        return verb + "es"

    if verb[-2:] in ["ch", "sh"]:
        return verb + "es"

    if verb[-2] not in vowels and verb[-1] == "y":
        return verb[:-1] + "ies"

    return verb + "s"    


def past_participle(verb):
    """Functions returns past participle form of a 
    verb. It takes some exceptions and alternations
    into account. However it does not take irregular
    verbs into account."""

    if verb[-2] not in vowels and verb[-1] == "y":
        return verb[:-1] + "ied"

    if verb[-1] == "e":
        return verb + "d"
    
    vow_count = 0
    for letter in verb:
        if letter in vowels:
            vow_count += 1

    if vow_count == 1 and (verb[-2] in vowels and verb[-1] not in vowels):
        if verb[-1] in ["h", "j", "w", "x"]:
            return verb + "ed"
        return verb + verb[-1] + "ed"

    return verb + "ed"


def gerund(verb):
    """Function returns gerund form of a verb. It takes 
    exeptions and alternations into account"""

    if verb[-2:] == "ie":
        return verb[:-2] + "ying"

    if verb[-1] == "e" and verb[-2] != "e":
        return verb[:-1] + "ing"

    vow_count = 0
    for letter in verb:
        if letter in vowels:
            vow_count += 1

    if vow_count == 1 and (verb[-2] in vowels and verb[-1] not in vowels):
        if verb[-1] in ["h", "j", "w", "x"]:
            return verb + "ing"
        return verb + verb[-1] + "ing"

    return verb + "ing"


def main():
    """Main function asks a user to enter an English verb to inflect.
    Then it prints the verb's infinitive, third singular present form,
    past participle, and gerund. It does not take irregular verbs into
    account. Also verbs containing two syllables with the stress on the
    second syllable are not inflected correctly."""

    verb = " "
    print("Hello!")

    while verb != "":
        verb = input("Enter an English verb to inflect: ").lower()
        
        if verb:
            print("Infinitive:", infinitive(verb))
            print("3sg Present:", third_singular(verb))
            print("Past participle:", past_participle(verb))
            print("Gerund:", gerund(verb))
    
    print("Goodbye!")

main()
