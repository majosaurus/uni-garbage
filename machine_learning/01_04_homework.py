# You need to find all three-word phrases in the corpus of the following structure:

#    The first word must be "beyond" (after lower-casing).
#    The second word must be a determiner or an article, such as "the" or "any".
#    The third word must be a noun, such as "doubt" or "town's".

import nltk
from nltk.corpus import brown


def find_beyond():
    """ Find 'beyond phrases' and return list of tuples"""
    tagged = brown.tagged_words(tagset='universal')

    phrases = []
    count = 0
    for (word, tag) in tagged:
        if word.lower() == 'beyond':
            if tagged[count+1][1] == 'DET':
                if tagged[count+2][1] == 'NOUN':
                    phrase = (word.lower(), tagged[count+1][0].lower(), tagged[count+2][0].lower())
                    if phrase not in phrases:
                        phrases.append(phrase)
        count += 1
    
    return sorted(phrases)


def main():
    phrases = find_beyond()
    print('Number of phrases found:', len(phrases))
    print('Phrases:', end=' ')
    print(', '.join(' '.join(p for p in p) for p in phrases))


main()
