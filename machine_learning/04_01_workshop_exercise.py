import nltk, random, math
from nltk.util import ngrams
from collections import defaultdict, Counter

n = 5
text = list(nltk.corpus.brown.words())
vocabulary = set(text)
brown_ngrams = list(ngrams(text, n))
brown_ngrams[:8]

# neighbors['focus']['context'] will contain the number of times the word 'context' occurs in the same n-gram as 'focus'
neighbors = defaultdict(Counter)

# Compute the position of the middle word in an n-gram (this is the focus word)
middle_position = n // 2

# For each n-gram, add the cooccurrence statistics:
for ngram in brown_ngrams:
    # This is the focus word
    focus = ngram[middle_position]
    # These are all the words _except_ the focus word
    context = ngram[:middle_position] + ngram[middle_position+1:]
    for word in context:
        neighbors[focus][word] += 1
"""
# Now we can answer the original question:
print(', '.join('"%s"' % word for word,_ in neighbors['four'].most_common(10)))
print(', '.join('"%s"' % word for word,_ in neighbors['five'].most_common(10)))
print(', '.join('"%s"' % word for word,_ in neighbors['dog'].most_common(10)))
print()
"""
# Return the number of overlapping words in the top 100 list of contexts
def top100_similarity(word1, word2):
    return len({word for word,_ in neighbors[word1].most_common(100)} &
               {word for word,_ in neighbors[word2].most_common(100)})

# Print the similarity between each pair of words in the given list
def pairwise_similarity(words):
    for word1 in words:
        for word2 in words:
            print('%-8s %-8s %4d' % (word1, word2, top100_similarity(word1, word2)))
"""
pairwise_similarity('three four dog'.split())
print()
"""
# Dimensionality of vectors. Normally this is a large number, but for demonstration purposes we use a smaller number.
d = 5
# We represent a vector using a list of float values.
def random_vector():
    return [random.random() for _ in range(d)]

index_vector = { word: random_vector() for word in vocabulary }

[index_vector[word] for word in 'four five dog'.split()]

# Start with zero vectors
context_vector = { word: [0.0]*d for word in vocabulary }
# Add vector b to vector a and store the result in a:
# a <- a + b
def add_vector(a, b):
    for i,x in enumerate(b):
        a[i] += x
# This is almost exactly the same as we did earlier,
# except now we modify the context_vector object instead of the neighbors object.
for ngram in brown_ngrams:
    # This is the focus word
    focus = ngram[middle_position]
    # These are all the words _except_ the focus word
    context = ngram[:middle_position] + ngram[middle_position+1:]
    for word in context:
        add_vector(context_vector[focus], index_vector[word])

[context_vector[word] for word in 'four five dog'.split()]

# Normalize a vector so that the sum of its elements is 1
# We also round the result to 3 decimals, so it looks prettier when we print it,
# but this is not necessary.
def normalize(a):
    total = sum(a)
    return [round(x/total, 3) for x in a]

[normalize(context_vector[word]) for word in 'four five dog'.split()]

# Compute the Euclidean distance between vectors a and b
def euclidean(a, b):
    return math.sqrt(sum((x-y)*(x-y) for x,y in zip(a,b)))

# Print the similarity between each pair of words in the given list
def pairwise_distance(words):
    seen_pairs = []
    for word1 in words:
        for word2 in words:
            if (word1, word2) not in seen_pairs:
                # append additional pair, e.g. if we have (run, walk) append (walk, run)
                seen_pairs.append((word2, word1))
            if word1 != word2 and (word1, word2) not in seen_pairs:
                # print without redundant pairs
                print('%-8s %-8s %.3f' % (word1, word2, euclidean(
                    normalize(context_vector[word1]),
                    normalize(context_vector[word2]))))

pairwise_distance('three four dog cat mother drink eat work'.split())

# Add discussion ex. 1
