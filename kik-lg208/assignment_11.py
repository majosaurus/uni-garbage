"""This program works as a simple segmentation and tokenization tool. It reads a text file
and then outputs the text, one sentence per line, all tokens separated by space. Tokens are:
words, abbreviations ('e.g.', 'Mr.', 'Mrs.', and 'U.S.A.' types), abbreviated forms of verbs (isn't),
punctuation, quotes, brackets, numbers ('55', '55.5', '55,5', '55,000.55', and '55,000.55' types),
numbers together with currencies or percentage signs."""


import re

def prepare_raw(data):
    """Read file, remove file's newline characters and replace them by space. Then split
    the text using space."""

    data = open(data, "r")
    raw = data.read()
    raw = raw.replace("\n", " ")
    raw = raw.split(" ")
    raw = raw[:-1] # used because of standard behaviour of .split() method 
                   # which appends an empty string at the end of the list
    data.close()
    return raw


def newline_char(raw):
    """Append newline characters at the end of the sentences."""

    abbr = re.compile(r'\b(?:[A-Za-z]\.)+|\b(?:[A-Z][a-z]{1,2}\.)+|(?:[A-Z]\.)+') # matches abbreviations such as e.g., Dr., Mrs., or U.S.A.
    end_punct = re.compile(r'(\.|\?|\!)$') # matches .?! punctuation marks (at the end of sentences)
    end_br = re.compile(r'[\.\?\!]+[\)\'"]$') # matches .?! punctuation inside brackets and quotation marks

    for i in range(len(raw)):
       if (re.search(end_punct, raw[i]) or re.search(end_br, raw[i])) and not re.search(abbr, raw[i]):
            raw[i] = raw[i] + "\n"
    return raw


def sentence_list(raw):
    """Makes a list of lists. Each inner list contains a sentence."""

    sentence_per_line = []
    sent = []
    
    for part in raw:
        if part[-1:] != "\n": # append the inner token to the sentence
            sent.append(part)
    
        else:
            sent.append(part[:-1]) # append the last word of the sentence to the sentence
                                   # without the newline character
            sentence_per_line.append(sent) # append the whole sentence to the list of all sentences
            sent = [] # reset the variable for next sentence
    
    return sentence_per_line


def tokenize(sentence_per_line):
    """Tokenize the sentences according to the rules mentioned below."""

    abbr = re.compile(r'\b(?:[A-Za-z]\.)+|\b(?:[A-Z][a-z]{1,2}\.)+|(?:[A-Z]\.)+') # matches abbreviations such as e.g., Dr., Mrs., or U.S.A.
    numbers = re.compile(r'(\d+[.,]?\d+)+') # matches decimal numbers with decimal period, or comma, or both (e.g. 2,000.3)
    end_punct = re.compile(r'(\.|\?|\!)$') # matches .?! punctuation marks (for the end of sentences)
    end_br = re.compile(r'[\.\?\!]+[\)\'"]$') # matches .?! punctuation inside brackets and quotation marks
    brq_front = re.compile(r'^[\"\[\(\{\']') # matches brackets and quotation marks at the beginning of the word
    brq_back = re.compile(r'[\"\]\)\}\']$') # matches brackets and quotations marks at the end of the word

    for lst in sentence_per_line:
        for tok in lst:
            if re.search(end_punct, tok) and len(tok) > 1 and not re.search(abbr, tok):
                token1 = tok[:-1] # separate the word from the punctuation mark
                end = tok[-1] # the punctuation mark itself
                lst.remove(tok) # remove the last word
                lst.append(token1) # append the separated word instead
                lst.append(end) # append the separated punctuation instead

            elif re.search(r'\,$', tok) and len(tok) > 1:
                where = lst.index(tok) # keep an index where to put the comma
                token1 = tok[:-1] # the word itself
                end = tok[-1] # the comma itself
                lst.remove(tok) # remove the last word
                lst.insert(where, token1) # insert the word at the index
                lst.insert(where+1, end) # insert the comma after the word

            elif re.search(end_br, tok) and len(tok) > 1: # search for punctuation inside brackets
                token1 = tok[:-2] # word
                end1 = tok[-2] # punctuation
                end2 = tok[-1] # ending bracket
                lst.remove(tok) # remove the last word
                lst.append(token1) # append the separated word instead
                lst.append(end1) # append the separated punctuation mark
                lst.append(end2) # append the separated bracket
        
            elif re.search(brq_front, tok) and len(tok) > 1: # front brackets or quotations
                where = lst.index(tok) # where to insert (it can be in the middle of the sentence)
                token2 = tok[1:]
                brq = tok[0]
                lst.remove(tok)
                lst.insert(where, brq) # we first want to insert the front bracket or quotation
                lst.insert(where+1, token2) # then insert the word
        
            elif re.search(brq_back, tok) and len(tok) > 1: # back brackets or quotations
                where = lst.index(tok) # where to insert
                token1 = tok[:-1]
                brq = tok[-1]
                lst.remove(tok)
                lst.insert(where, token1) # here we want the word first
                lst.insert(where+1, brq) # and the bracket or the quote last

    return sentence_per_line


def main():
    try:
        inp = input("Enter a text to tokenize: ")
        
        if inp[-4:] != ".txt": # the file needs to be .txt
            print("NotTxtFileError: Enter a .txt file.")
            return 1
        
        raw = prepare_raw(inp)
        newline_appended = newline_char(raw)
        sentence_per_line = sentence_list(newline_appended)
        tokens = tokenize(sentence_per_line)

        for sentences in tokens: # print tokens divided by space
            for toks in sentences:
                print(toks, end=" ")
            print()

        return 0

    except FileNotFoundError:
        print("FileNotFoundError: Enter an existing file.")

main()
