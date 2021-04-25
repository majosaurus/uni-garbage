"""The program opens a file and counts how many lines, words, and 
characters are present in the file. It prints the output."""


def line_count(txt):
    """The function counts how many lines are there in the file."""

    lines_total = 0

    for line in txt:
        lines_total += 1

    return lines_total


def word_count(txt):
    """The function counts how many words are there in the file."""

    words = 0
    
    for line in txt:
        line = line.split()
        words += len(line)

    return words


def character_count(txt):
    """The function counts how many characters are there in the file."""

    characters = 0

    for line in txt:
        characters += len(line)

    return characters

    
def main():
    """The main function calls the above functions and prints the output."""

    try:
        txt = input("Enter a file name: ")
        for i in range(3): # opening the file 3 times because single opening and
                           # storing the file in the variable did not worked, 
                           # only first function got counted, the following
                           # two returned 0s
            t = open(txt, "r")
            if i == 0:
                lines = line_count(t)
            if i == 1:
                words = word_count(t)
            if i == 2:
                characters = character_count(t)
        print("The file contains", lines, "lines,", words, "words, and", characters, "characters.")

    except FileNotFoundError:
        print("FileNotFoundError: the file does not exist or is located somewhere else")

main()
