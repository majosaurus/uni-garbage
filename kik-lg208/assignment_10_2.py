"""The program takes a Finnish text and modifies the spelling using 
regular expressions. The modified text is lowercased."""

import re

def rules(inp, out):
    finnish = open(inp, "r")
    output = open(out, "w")

    for line in finnish:
        line = line.lower()
        line = re.sub(r'([a-zäö])(?=\1)', r'', line) # two identical letters in a row are reduced to one
        line = re.sub(r'ks', r'x', line) # ks becomes x
        line = re.sub(r'ts', r'z', line) # ts becomes z
        line = re.sub(r'(k)(u(a|e|i|o|u|ä|ö|y))', r'q\2', line) # k followed by two vowels becomes q
        line = re.sub(r'k', r'c', line) # otherwise k becomes c
        line = re.sub(r'j', r'i', line) # j becomes i
        line = re.sub(r'(ä|ö)', 'e', line) # ä and ö become e
        output.write(line)

    finnish.close()
    output.close()

    return 0


def main():
    inp = input("Enter input file: ")
    out = input("Enter output file: ")

    if inp[-4:] != ".txt": # if the file is not .txt
        print("NotTextFileError: File is not .txt file.")
        return 1 # skip following code

    try:
        rules(inp, out)
        print("Modifying spelling and writing to file", out)
        print("Done!")

    except FileNotFoundError:
        print("FileNotFoundError: The input file does not exist.")


main()
