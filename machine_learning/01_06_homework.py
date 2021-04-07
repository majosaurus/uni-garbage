import nltk, re, string


def normalization(user_input):
    """ Remove punctuation and tokenize the text """
    
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    user_input = regex.sub('', user_input)
    return user_input.split()


def two_syllable_words():
    """ Find two-syllable words in CMU Pronouncing Dictionary """
    
    entries = nltk.corpus.cmudict.entries()
    # a syllable must contain a vowel, the following list contains all different vowel sounds
    vowels = re.compile(r'AA|AE|AH|AO|AW|AX|AXR|AY|EH|ER|EY|IH|IX|IY|OW|OY|UH|UW|UX|AX-H')
    
    words = []
    for word in entries:
        phon_count = 0
        for phon in word[1]:
            if re.match(vowels, phon): # if the phon is a vowel
                phon_count += 1
        if phon_count == 2: # if there are two vowels in the word, append it to a list
            words.append(word[0])
    
    return words


def main():
    user_input = input("Enter English text: ").lower()
    user_input = normalization(user_input)
    two_syllable = two_syllable_words()
    matches = [w for w in user_input if w in two_syllable]
    print("Following two-syllable words were found:", end=' ')
    print(', '.join(w for w in matches))


main()

