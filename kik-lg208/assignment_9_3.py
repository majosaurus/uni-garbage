from unicodedata import *

def unicode_printing(char_list, code_or_char):
    if code_or_char == "char":
        for char in char_list:
            print(char, name(char))
        return 0
    else:
        for code in char_list:
            print(hex(ord(code)), name(code))
        return 0


def main():
    char_hex = ["\uAA65", "\U0001004C", "\u02A4", "\u0E15", "\u0F04", 
            "\U0001D209", "\U0001F71D", "\u16A4", "\U0001D2E0", "\u306E"]
    unicode_char = ["ŵ", "Φ", "Ӫ", "ʔ", "‱"]
    
    unicode_printing(char_hex, "char")
    unicode_printing(unicode_char, "code")

main()

