import nltk, random
from nltk.corpus import movie_reviews
from nltk.util import bigrams


documents = [(list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = [w for w, f in all_words.most_common(1000)]


# Naïve Bayes Classifier with the standard feature extraction
def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

def classifier1():
    featuresets = [(document_features(d), c) for (d,c) in documents]
    train_set, test_set = featuresets[100:], featuresets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)

    print('Standard Naïve Bayes Classifier accuracy:', nltk.classify.accuracy(classifier, test_set))
    classifier.show_most_informative_features(30)
    print('\n')


# Naïve Bayes Classifier with first 30 words of a document feature extraction
def document_begins(document):
    document_words = set(document)
    features = {}
    for word in document_words:
        features['begins({})'.format(word)] = (word in document_words)
    return features

def classifier2():
    featuresets = [(document_begins(d[:30]), c) for (d,c) in documents]
    train_set, test_set = featuresets[100:], featuresets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    
    print('First 30 words of a review Bayes accuracy:', nltk.classify.accuracy(classifier, test_set))
    classifier.show_most_informative_features(30)
    print('\n')


# Naïve Bayes Classifier with last 30 words of a document feature extraction
def document_ends(document):
    document_words = set(document)
    features = {}
    for word in document_words:
        features['ends({})'.format(word)] = (word in document_words)
    return features

def classifier3():
    featuresets = [(document_ends(d[-30:]), c) for (d,c) in documents]
    train_set, test_set = featuresets[100:], featuresets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)

    print('Last 30 words of a review Bayes accuracy:', nltk.classify.accuracy(classifier, test_set))
    classifier.show_most_informative_features(30)
    print('\n')


# Naïve Bayes Classifier with bigrams feature extraction
def document_bigrams(document):
    document_words = set(document)
    features = {}
    for bigram in document_words:
        features['bigram({} {})'.format(bigram[0], bigram[1])] = (bigram in document_words)
    return features

def classifier4():
    bigrams_doc = [(list(bigrams(d)),c) for (d,c) in documents]
    featuresets = [(document_bigrams(d), c) for (d,c) in bigrams_doc]
    train_set, test_set = featuresets[100:], featuresets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)

    print('Bigrams Bayes accuracy:', nltk.classify.accuracy(classifier, test_set))
    classifier.show_most_informative_features(30)
    print('\n')


# Naïve Bayes Classifier with first and last 30 words of a document feature extraction
def document_mix(document):
    begin_words = set(document[:30])
    end_words = set(document[-30:])
    features = {}
    for word in begin_words:
        features['begins({})'.format(word)] = (word in begin_words)
    for word in end_words:
        features['ends({})'.format(word)] = (word in begin_words)
    return features

def classifier5():
    featuresets = [(document_mix(d), c) for (d,c) in documents]
    train_set, test_set = featuresets[100:], featuresets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)

    print('First 30 and last 30 words of a review Bayes accuracy:', nltk.classify.accuracy(classifier, test_set))
    classifier.show_most_informative_features(30)


def main():
    classifier1()
    classifier2()
    classifier3()
    classifier4()
    classifier5()

main()
