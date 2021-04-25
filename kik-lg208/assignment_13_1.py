from nltk import word_tokenize

def tokenize(filename):
    """Split the text into token using word_tokenize from NLTK"""

    raw = open(filename, "r")
    raw = raw.read()
    tokens = word_tokenize(raw)
    return tokens


def compute_frequencies(tokens):
    """Compute token frequencies and store them into a dictionary"""

    frequencies = {}

    for token in tokens:
        if token in frequencies:
            frequencies[token] += 1
        else:
            frequencies[token] = 1
    
    return frequencies


def alphabetical(dictionary):
    """Sort the dictionary alphabetically and print the tokens"""

    print("Aplhabetical order")
    print("==================")

    for token in sorted(dictionary.keys()):
        print(token)


def decreasing(dictionary):
    """Order the dictionary by frequency (DESC) and print key-value pairs"""

    print("\nOrdered by frequency")
    print("====================")

    for token in sorted(dictionary, key=dictionary.get, reverse=True): 
        # the sort iterates over the dictionary keys, using the number of word occurrences as a sort key
        print(token, dictionary[token])
        

def length(dictionary):
    """Order the dictionary by tokens' length and print key-value pairs"""

    print("\nOrdered by length")
    print("=================")
    
    len_dict = {} # make a new dictionary with tokens as keys and their len as values

    for token in dictionary.keys():
        if token not in len_dict.keys():
            len_dict[token] = len(token)

    for tok in sorted(len_dict, key=len_dict.get, reverse=True):
        print(tok, len_dict[tok]) # sort the dict and print key-value pairs



def main():
    filename = input("Enter your input file: ")

    if filename[-4:] != ".txt":
        print("NotTxtError: The provided file is not .txt")
    else:
        try:
            tokens = tokenize(filename)
            frequencies = compute_frequencies(tokens)
            alphabetical(frequencies)
            decreasing(frequencies)
            length(frequencies)
        except FileNotFoundError:
            print("FileNotFoundError: The file does not exist")

main()
