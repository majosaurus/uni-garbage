import nltk, random

def read_tagged_sents():
    tagged_sents = []
    try:
        with open('fi-ud-train.pos-tagged.txt', "r", encoding="UTF-8") as gs_file:
            line = gs_file.readline().lower()
            while line != "":
                tagged_sents.append([nltk.tag.str2tuple(wt) for wt in line.split()])
                line = gs_file.readline().lower()
    except OSError:
        print("Error reading file.")
        sys.exit()
    return tagged_sents

def pos_features(sentence, i, history):
     features = {"suffix(1)": sentence[i][-1:],
                 "suffix(2)": sentence[i][-2:],
                 "suffix(3)": sentence[i][-3:],
                 "suffix(4)": sentence[i][-4:],
                 "prefix(1)": sentence[i][:3],
                 "prefix(2)": sentence[i][:2],
                 "prefix(3)": sentence[i][:1]}
     if i == 0:
         features["prev-prev-word"] = "<START>"
         features["prev-prev-tag"] = "<START>"
         features["prev-word"] = "<START>"
         features["prev-tag"] = "<START>"
     elif i == 1:
         features["prev-prev-word"] = "<START>"
         features["prev-prev-tag"] = "<START>"
         features["prev-word"] = sentence[i-1]
         features["prev-tag"] = history[i-1]
     else:
         features["prev-prev-word"] = sentence[i-2]
         features["prev-prev-tag"] = history[i-2]
         features["prev-word"] = sentence[i-1]
         features["prev-tag"] = history[i-1]
     return features

class ConsecutivePosTagger(nltk.TaggerI):

    def __init__(self, train_sents):
        train_set = []
        for tagged_sent in train_sents:
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                featureset = pos_features(untagged_sent, i, history)
                train_set.append( (featureset, tag) )
                history.append(tag)
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)

    def tag(self, sentence):
        history = []
        for i, word in enumerate(sentence):
            featureset = pos_features(sentence, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence, history)

documents = read_tagged_sents()
random.shuffle(documents)
size = int(len(documents) * 0.9)
train_set, test_set = documents[:size], documents[size:]
tagger = ConsecutivePosTagger(train_set)

print('\nAccuracy:', tagger.evaluate(test_set), '\n')

def five_test_sentences(test_set):
    untag_sent = []
    for i in range(5):
        untag_sent.append(nltk.tag.untag(test_set[i]))
    return untag_sent

def tag_five_sentences(untag_sents):
    tagged_sents = []
    for sent in untag_sents:
        tagged_sents.append(list(tagger.tag(sent)))
    return tagged_sents

untag_sents = five_test_sentences(test_set)
tagged_sents = tag_five_sentences(untag_sents)

for sent in tagged_sents:
    print(sent, '\n')

def show_featureset(tagged_sents):
    for tagged_sent in tagged_sents:
        untagged_sent = nltk.tag.untag(tagged_sent)
        history = []
        for i, (word, tag) in enumerate(tagged_sent):
            featureset = pos_features(untagged_sent, i, history)
            print(featureset)
            history.append(tag)
        print()
    return 0

features = show_featureset(tagged_sents)


# I was suprised that taking one more previous word into consideration
# didn't improve the performance at all. Usually, this ConsecutivePosTagger
# gives me accuracy around 70% and it remained the same after looking at
# two previous words. However, when I added 4th suffix, the performace
# improved by cca 7%. Then I added 3letter prefixes and the accuracy
# rised to cca 85%.
#
# I think it is a good score and it works well with Finnish which operates
# with lots of affixes. Combined together with previous context the tagger
# can make better decisions. I think it is a simple idea but it works
# surprisingly well. On the other hand, I would like to know if there's
# any explanation why this tagger works better for English than Finnish?
# I would also like to try this tagger out with Czech and see the performance.
#
# The ConsecutivePosTagger works better than the RegexpTagger. Mine RegexpTagger
# was around 51% accurate on the particular text we used in the exercise which is
# not much. The RegexpTagger relies on the rules a lot and it doesn't take
# context into consideration. If it doesn't have any rule to tag the word, it 
# tags it as a noun without any probability taken into the decision. I would
# also say these two taggers aren't directly comparable. In RegexpTagger, we
# simply look for patterns in each word and if they are found in the word,
# we give the word the first tag it matches the pattern for. But in
# ConsecutivePosTagger we don't simply use a suffix as a tag indicator. We
# train our model using Naïve Bayes algorithm, so we can base the decision
# on statistics.
