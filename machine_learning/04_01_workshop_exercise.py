import nltk, random, math
from nltk.util import ngrams
from collections import defaultdict, Counter

n = 3
text = list(nltk.corpus.brown.words())
vocabulary = set(text)
brown_ngrams = list(ngrams(text, n))

# Compute the position of the middle word in an n-gram (this is the focus word)
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

# Normalize a vector so that the Euclidean length is 1
def normalize(a):
    total = math.sqrt(sum(x**2 for x in a))
    return [x/total for x in a]

# Compute cosine similarity
def cosine_similarity(a,b):
    return sum((x*y) for x,y in zip(a,b))

def cosine_distance(a,b):
    return 1 - cosine_similarity(a,b)

# Print the similarity between each pair of words in the given list
# Mathiasovo řešení používá dva for loopy - když si představíme slova
# jako matici, zjistíme, že jsou symetrická podle diagonály, stačí nám
# tedy koukat pouze na první půlku, abychom neprintovali duplikáty.
def pairwise_distance(words):
    pair_distance = {}
    for i in range(0, len(words)):
        for j in range(i+1, len(words)):
            pair_distance[words[i], words[j]] = \
                    cosine_distance(
                        normalize(context_vector[words[i]]),
                        normalize(context_vector[words[j]]))
    for w1, w2 in sorted(pair_distance, key=lambda p: pair_distance[p]):
        print("{:8s} {:8s} {:.3f}".format(w1, w2, pair_distance[w1, w2]))

pairwise_distance('one two three four dog cat mother beer drink eat walk run sleep'.split())

# Moje řešení, aby pairwise_distance() nevypisovalo duplicitní páry a
# slovo samo se sebou (pouze základní for loop bez printování a sortu):
"""
seen_pairs = []
    for word1 in words:
        for word2 in words:
            if (word1, word2) not in seen_pairs:
                # append additional pair, e.g. if we have (run, walk) append (walk, run)
                seen_pairs.append((word2, word1))
            if word1 != word2 and (word1, word2) not in seen_pairs:
                # print without redundant pairs
"""

# Step 1: The words doesn't make that much sense. Although numerals appear very close
# to each other, pairs such as "three mother", "three drink", or "four dog" appear
# high on the list, too.
#
# Step 7: Only increasing 5-grams to 7-grams didn't do much for me. Then I switched back
# to 5-grams and checked a context for following words only. It gave me bad results.
# Same with looking at preceding words only. I believe that by changing ngrams to 3grams,
# we can check one preceding and one following word (I tried to do it in the for loop
# with 'context = ngrams[middle_position-1] + ngrams[middle_position+1]' but it gave me
# errors) which actually worked better for my words than 5grams, 7grams or checking
# broader context.
