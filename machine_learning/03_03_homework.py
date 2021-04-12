import nltk, random
from nltk.tag import hmm

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

documents = read_tagged_sents()
random.shuffle(documents)
size = int(len(documents) * 0.9)
train_set, test_set = documents[:size], documents[size:]

trainer = hmm.HiddenMarkovModelTrainer()
tagger = trainer.train_supervised(train_set)

print('Hidden Markov Models Accuracy:', tagger.evaluate(test_set))
print()
print('Five tagged sentences:')

def tag_five_sentences(sentences):
    tagged = []
    for sent in sentences:
        sent = nltk.tag.untag(sent)
        tagged.append(tagger.tag(sent))
    return tagged

tag_sents = tag_five_sentences(test_set[:5])
for sent in tag_sents:
    print(sent)


# HMM performs much worse than most of the n-gram taggers and sequential Naïve Bayes Tagger.
# It gave me only 40-50% accuracy. Few times only 30%.
#
#
#   I. One might think that HMM will work better than the other algorithms because it checks
#      the current word we're tagging in the moment with probability distribution over all
#      possible tags. HMM doesn't pick a tag with highest probability separately, but it
#      takes a combined probability of tags for a whole tagged sentence and picks one
#      sentence with the highest probability. The model is very mathematical and statistical,
#      so that may be why people would trust it more and expect better performance. It makes 
#      you feel "HMM knows what it's doing".
#
#  II. The problem of the worse performance could happen because of ambiguity. If we have
#      lots of ambiguous words in the sentence with higher probability of one tag than the
#      other, HMM could still tag it wrong. Or complex or compound words could be tagged
#      wrongly, too. It can also depend on the train set, if the train set is not variable 
#      enough, HMM can't perform well on the test set. The last thing coming to my mind is
#      HMM relying on the current state only, not considering previous context. 
#
# III. The actual situation is HMM is working worse than the other taggers.
#
#  IV. Maybe Finnish is too complicated and we have a small dataset to train HMM accurately.
#      I have also read usually you have to adjust HMM's parameters for the given problem
#      which we didn't do in this exercise. We have lots of tags to choose from and it can
#      be overwhelming to choose the right ones from all the combinations.
