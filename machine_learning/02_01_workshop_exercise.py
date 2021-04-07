# 1. Show the 30 most informative features from the Naïve Bayes classifier.
# 2. Run your program a few times at this point. Since the training and test 
#    sets are created randomly, the results vary from one run of the program 
#    to another. Do you see much variation in the results?
# 3. Add another classifier, a Decision Tree classifier to your program. 
#    Use the same data sets and feature extraction as for the Naïve Bayes classifier.
# 4. Have your program print the accuracy obtained by the Decision Tree classifier, too.
# 5. Have your program print the "pseudocode" for the rules it has learned. Use an appropriate depth.
# 6. Add comments into your program, where you discuss which classifier performs better. Also 
#    discuss the most informative features of the Naïve Bayes classifier and the rules of the 
#    Decision Tree classifier. Do they make sense?
# 7. Warning: Running the Decision Tree classifier may be slow. One run may take 5 minutes or more. 
#    Make an additional experiment, where you reduce the number of features. Don't use the 2000 most 
#    frequent words, but a much smaller value. Add a comment to your program how the two classifiers 
#    now perform compared to each other. When you submit your code, leave the smaller value for the 
#    number of features in your code.
# 8. Repeat your experiment a few times to verify that your observations are consistent and not 
#    because of random fluctuation.

import nltk, random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = [w for w, f in all_words.most_common(500)]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
Bclassifier = nltk.NaiveBayesClassifier.train(train_set)
Tclassifier = nltk.DecisionTreeClassifier.train(train_set)

print('Naïve Bayes Classifier accuracy: ', nltk.classify.accuracy(Bclassifier, test_set))
Bclassifier.show_most_informative_features(30)

print('Decision Tree Classifier accuracy: ', nltk.classify.accuracy(Tclassifier, test_set))
print('Pseudocode\n', Tclassifier.pseudocode(depth=4))


# Naive Bayes works performs better in this type of task. Even though it sometimes chooses
# inadequate informative features, it still was able to perform between 0,73-0,86 accuracy. Decision
# Tree was able to get only 0,57-0,71 accuracy. (2000 most common words)
# I tried both smaller (500) and bigger (5000) datasets, but it didn't have much impact on the accuracy. 
# Naïve Bayes was still more accurate than Decision Tree.
#
# The most informative features made sense when having bigger dataset. When I used 500 most common
# words, things such as punctuation (',', '=') and stop words ('as', 'in', 'it') started
# appearing in the most informative features. Also the (pos : neg =) numbers were much lower.
# When using 2000 most common words, the choice of words was better, but words such as 'mulan', 
# 'jedi', 'seagal', and 'hanks' still appeared marking the review positive. Also, sometimes things 
# like marking 'terrific' positive happened (on the other hand it can be positive in horror movie reviews).
#
# Decision Tree almost always started decisions based on a word 'bad'. The bigger the dataset the better
# the decisions were. Unfortunately, it was never enough to perform similar to or even better as 
# Naïve Bayes. With bigger data, it would almost always pick adjectives to make the decisions.
# With smaller data, nouns as 'america', 'family', or 'school' appeared. Also, using smaller
# data, the decisions stopped making sense, such as marking review containing 'worst' and 
# 'present' as positive, or review containing 'bad' and 'political' but not 'similar' and 
# 'perfect' as positive. Or it would mark if 'bad' == 'True' or if 'bad' == 'False' both
# 'pos' for example. Using big dataset didn't have much impact speaking about accuracy (I tried 
# it with 5000 word_features and training set of 1000). Naive Bayes was still more that 20% more accurate. 
# It may need even bigger dataset to make up the rules correctly and not over fit them.
