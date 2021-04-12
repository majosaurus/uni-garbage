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

def tag_five_sentences(sentences):
    tagged = []
    for sent in sentences:
        sent = nltk.tag.untag(sent)
        tagged.append(tagger.tag(sent))
    return tagged

documents = read_tagged_sents()
random.shuffle(documents)
size = int(len(documents) * 0.9)
train_set, test_set = documents[:size], documents[size:]

# Create a frequency dictionary of words appearing in the train_set
# Words are keys and frequencies are values
words_freq = {}
for sent in train_set:
    for words in sent:
        if words[0] in words_freq:
            words_freq[words[0]] += 1
        else:
            words_freq[words[0]] = 1

# Replace words with low frequencies with '<UNK>' in the train_set
# I chose words occuring 20 times in the train_set because it gave
# me the best results. I am also using a dictionary instead of a list
# because dictionaries are quicker to iterate over.
unk_candidates = {}
for word in words_freq:
    if words_freq[word] == 20:
        unk_candidates[word] = 1

for sent in train_set:
    for i, word in enumerate(sent):
        if word[0] in unk_candidates:
            sent.pop(i)
            sent.insert(i, ('<UNK>', word[1]))

# If there's a word in test_set which is not present in train_set, replace
# it with '<UNK>'. Make a dictionary called originals to store a tuple 
# (original word<UNK>, tag) as a value and a tuple (sentence_index, word_index)
# as a key. This weird dictionary helps me print the five tagged sentences
# easily and correctly according to the assignment instructions.
# Count all words straight away in the test_set for computing relative 
# frequency of out-of-vocabulary words later in the code.
originals = {}
all_words = 0
for i, sent in enumerate(test_set):
    all_words += len(sent)
    for j, word in enumerate(sent):
        if word[0] not in words_freq:
            sent.pop(j)
            sent.insert(j, ('<UNK>', word[1])), 
            originals[(i, j)] = (word[0]+'<UNK>', word[1])


trainer = hmm.HiddenMarkovModelTrainer()
tagger = trainer.train_supervised(train_set)
print('\nHidden Markov Models Accuracy:', tagger.evaluate(test_set))

print('\nFive tagged sentences:')
tag_sents = tag_five_sentences(test_set[:5])

# Print five sentences tagged by the HMM. Replace <UNK> words with
# their originals followed by the tag <UNK> (e.g. 'car<UNK>')
for i, sent in enumerate(tag_sents):
    for j, word in enumerate(sent):
        if word[0] == '<UNK>':
            sent.pop(j)
            sent.insert(j, originals[(i, j)])
    print(sent)

# Divide the number of <UNK>s with the total number of words in the test set
# to obtain relative frequency of out-of-vocabulary words
print('\nRelative frequency of out-of-vocabulary words:', len(originals)/all_words)


# I was able to get accuracy of around 83% only. Which is still impressive because
# "the normal" HMM performs poorly (40-50%). However, I don't fully understand
# why is it possible for this HMM with <UNK>s perform so much better than the
# original one. I'm just impressed. The HMM now works almost as good as the BigramTagger.
#
# I cannot discuss how well this HMM predicts the out-of-vocab words since I don't 
# speak Finnish. I think it can tag proper nouns quite good but otherwise I can't
# tell anything. I could translate the sentences with Google Translate but it still
# doesn't work well with Finnish so I don't want to draw any conclusions out of it.
# I guess I just have to give up on the last 0.3 points :-)
