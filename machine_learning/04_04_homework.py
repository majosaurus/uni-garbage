import numpy as np
from nltk.cluster import KMeansClusterer, euclidean_distance
import nltk, random, math
from nltk.util import ngrams
from collections import defaultdict, Counter
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy

n = 3
text = list(nltk.corpus.brown.words())
vocabulary = set(text)
brown_ngrams = list(ngrams(text, n))
middle_position = n // 2

# Dimensionality of vectors. Normally this is a large number, but for demonstration purposes we use a smaller number.
d = 100
m = 5

index_vector = { word: [1]*m + [0]*(d-m) for word in vocabulary }

for word in index_vector:
    random.shuffle(index_vector[word])

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

# Normalize a vector by dividing it by its length (= magnitude) (Step 4)
def normalize(a):
    total = math.sqrt(sum(x**2 for x in a))
    return [x/total for x in a]

words = ["dog", "cat", "house", "building", "one", "two", "three", "obviously", "naturally", 
            "slowly", "blue", "green", "black", "white", "run", "walk", "jump", "eat", "sleep"]
word_vectors = []

for word in words:
    word_vectors.append(normalize(context_vector[word]))

Z = hierarchy.linkage(word_vectors, method='complete', metric='euclidean')

plt.figure(tight_layout=True)

dn = hierarchy.dendrogram(Z, labels=words, leaf_rotation=90.0)

plt.savefig('dendrogram.png')


# Task 1:
# 2 clusters: one four two three, talk, took, see, hear, watch, walk, run
#             mouse, cat, dog, house
# 3 clusters: one four two three, talk, took, see, hear, watch, walk, run
#             mouse
#             cat, dog, house
# 4 clusters: one, four, two, three
#             talk, look, see, hear, watch, walk, run
#             mouse
#             cat, dog, house
# 5 clusters: one, four, two, three
#             talk, look, see, hear, watch, walk, run
#             mouse
#             cat
#             dog, house
