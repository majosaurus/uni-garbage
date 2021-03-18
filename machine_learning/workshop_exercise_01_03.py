from nltk.corpus import brown

news_tagged = brown.tagged_words(categories='news', tagset='brown')
nouns = [(word.lower(), tag) for (word, tag) in news_tagged if tag.startswith('NNS')]
verbs = [(word.lower(), tag) for (word, tag) in news_tagged if tag.startswith('VBZ')]

results = []

for (word, tag) in verbs:
    for (word2, tag2) in nouns:
        if word == word2 and word not in results:
            results.append(word)

results = sorted(results)

print('Number of words found:', len(results))
print('Words:', ', '.join(sorted(results)))
