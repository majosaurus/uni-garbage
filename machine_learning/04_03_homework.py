import numpy
from nltk.cluster import KMeansClusterer, euclidean_distance
import nltk, random, math
from nltk.util import ngrams
from collections import defaultdict, Counter

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

words = ["dog", "cat", "house", "building", "garden", "one", "two", "three", 
            "obviously", "slowly", "naturally", "blue", "green", "black",
            "white", "run", "walk", "jump", "eat", "sleep", "sing", "talk"]

word_vectors = [normalize(context_vector[word]) for word in words]

# In this example we cluster four two-dimensional vectors:
vectors = [numpy.array(f) for f in word_vectors]

# Test k-means using the Euclidean distance metric, 2 means and repeat
# clustering 10 times with random seeds                                                    
n_clusters = 5
clusterer = KMeansClusterer(n_clusters, euclidean_distance, repeats=10)
clusters = clusterer.cluster(vectors, assign_clusters=True, trace=True)
# In the above method call you can set trace=False eventually


clusters_again = { key: [] for key in range(n_clusters) }

for i in range(len(clusters)):
    clusters_again[clusters[i]].append(words[i])

for key in clusters_again:
    print("Cluster #", key, ": ", ", ".join(val for val in clusters_again[key]) , sep="")


# I used n_clusters = 5 because I have nouns, adjectives, numerals, adverbs, and verbs.
# Once I was able to get all the words correct except for 'cat' (in adverbs cluster) and 
# 'obviously' (in numerals cluster). The numerals were always grouped together, the nouns
# almost always as well. This clustering method has problems with adverbs, they were almost
# never correct. Verbs varied from one run of the program to another, sometimes they appeared
# all in one cluster, sometimes they were spread among 2-3 different clusters. 
# I noticed an interesting thing: for some reason, if adjectives weren't grouped together 
# correctly, they appeared more likely with 'dog', and if adverbs weren't grouped correctly,
# they appeared more likely with 'cat'.
# 
# This is the best result I got:
# Cluster #0: cat, slowly, naturally
# Cluster #1: run, walk, jump, eat, sleep, sing, talk
# Cluster #2: dog, house, building, garden
# Cluster #3: blue, green, black, white
# Cluster #4: one, two, three, obviously

