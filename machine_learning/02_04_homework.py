import nltk, random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = [w for w, f in all_words.most_common(1000)]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)

desired_outcome = [c for (d, c) in test_set]
test = classifier.classify_many(f for (f, c) in test_set)

cm = nltk.ConfusionMatrix(desired_outcome, test)
print(cm.pretty_format(sort_by_count=False, show_percents=True, truncate=9))


# The upper right cell says how many negative reviews were marked as positive by our
# Naïve Bayes classifier. 
#
# There is also the lower left cell which says the opposite - how many positive reviews 
# were marked as negative by our classifier (false negative). I tried running the program 
# few times and false negatives always occured more than false positives.
#
# We could say it is false positive according to True and False Positives and Negatives 
# table. The NLTK Book suggests, false positives are irrelevant items that were 
# incorrectly identified as relevant. For our Movie Reviews case, I would argue it is 
# not exactly true. There is no relevant and irrelevant item for inspecting semantics 
# of a review. It is either positive or negative, but both types of information are 
# important to us. It is an error, still, but not in terms of (ir)relevancy.
