import nltk, random, math
from nltk.util import ngrams
from collections import defaultdict, Counter
from nltk.corpus import gutenberg

files = gutenberg.fileids()

vocabulary = [word.lower() for word in gutenberg.words()]
vocabulary = set(vocabulary)

# Dimensionality of vectors. 
d = 100  # Size of index and context vectors
m = 5    # Number of non-zero components in index vectors

# Add vector b to vector a and store the result in a:
# a <- a + b
def add_vector(a, b):
    for i,x in enumerate(b):
        a[i] += x

# Start with zero index vectors
# Put ones in m random positions in the index vectors (Step 5)
index_vector = { word: [1]*m + [0]*(d-m) for word in vocabulary }

for word in index_vector:
    random.shuffle(index_vector[word])

# Start with zero context vectors
context_vector_words = { word: [0.0]*d for word in vocabulary }

for book in files:
    for word in gutenberg.words(book):
        add_vector(context_vector_words[word.lower()], index_vector[word.lower()])

context_vector = {}
for book in files:
    book_context = [0.0]*d
    for word in gutenberg.words(book):
        add_vector(book_context, index_vector[word.lower()])
    context_vector[book] = book_context

# Normalize a vector so that the Euclidean length is 1
def normalize(a):
    total = math.sqrt(sum(x**2 for x in a))
    return [x/total for x in a]

# Compute cosine similarity
def cosine_similarity(a,b):
    return sum((x*y) for x,y in zip(a,b))

def cosine_distance(a,b):
    return 1 - cosine_similarity(a,b)

# Print the similarity between each pair of words in the given list.
# Sort the distances in ascending order (Step 3) without printing
# distances between a word and itself and withot printing distances
# that were already printed (Step 2):
def sorted_pairwise_distance(words):
    pairdists = {}
    for i in range(0, len(words)):
        for j in range(i + 1, len(words)): # Note the range of j
            pairdists[words[i], words[j]] = cosine_distance(
                 normalize(context_vector[words[i]]),
                normalize(context_vector[words[j]]))
    for pair in sorted(pairdists, key=lambda p: pairdists[p]):
        print("{:30s} {:30s} {:.3f}".format(pair[0], pair[1], pairdists[pair]))

# Investigate distances between words of different part of speech (Step 1):
sorted_pairwise_distance(
    "austen-emma.txt austen-persuasion.txt austen-sense.txt bible-kjv.txt blake-poems.txt bryant-stories.txt burgess-busterbrown.txt carroll-alice.txt chesterton-ball.txt chesterton-brown.txt chesterton-thursday.txt edgeworth-parents.txt melville-moby_dick.txt milton-paradise.txt shakespeare-caesar.txt shakespeare-hamlet.txt shakespeare-macbeth.txt whitman-leaves.txt".split())


# Tragedies show up as close relatives (but it might be because Shakespeare is the author). Poems 
# also appear to be relatively close (score 0.016). Stories for children are closely related, too.
# Although a lot of them are surprisingly also related to Moby Dick. And Alice in Wonderland is not
# as closely related to the other children stories as other books. Also, it appears that Austen's
# work is somehow related to children books, too. I don't know all these books, but I think books
# of the same genre appear as close relatives.
#
# Books by the same author are the most similar to each other of all other books. It is true for all
# books by the same author. First I got Chesterton, then Austen, then Shakespeare.
#
# The closest book to King James Bible are Poems by William Blake (score 0.024)
#
# The furthest book to King James Bible are Alice's Adventures in Wonderland by Lewis Carroll (score 0.061)
#
# The beginnings of all the three books are different, so I don't see the correlation here. Maybe Blake
# uses similar words and topics in his work as are in the Bible. Also the language could be similar because
# Blake lived just a century after the Bible was published. On the other hand, Alice's Adventures in Wonderland
# are 'very young' compared to the Bible, Carroll probably already uses a different language and the story
# doesn't contain anything biblical at all. Carroll also uses lots of words he came up with on his own, so this
# could be the reason.
