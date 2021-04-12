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


documents = read_tagged_sents()
random.shuffle(documents)
size = int(len(documents) * 0.9)
train_set, test_set = documents[:size], documents[size:]


default_tagger = nltk.DefaultTagger('NOUN')
unigram_tagger = nltk.UnigramTagger(train_set)
bigram_tagger = nltk.BigramTagger(train_set)
trigram_tagger = nltk.TrigramTagger(train_set)
print('Default Tagger Accuracy', default_tagger.evaluate(test_set))
print('Unigram Tagger Accuracy:', unigram_tagger.evaluate(test_set))
print('Bigram Tagger Accuracy:', bigram_tagger.evaluate(test_set))
print('Trigram Tagger Accuracy:', trigram_tagger.evaluate(test_set))

print()

t0 = nltk.DefaultTagger('NOUN')
t1 = nltk.UnigramTagger(train_set, backoff=t0)
t2 = nltk.BigramTagger(train_set, backoff=t1)
t3 = nltk.TrigramTagger(train_set, backoff=t2)
print('Unigram Backoff Accuracy:', t1.evaluate(test_set))
print('Bigram Backoff Accuracy:', t2.evaluate(test_set))
print('Trigram Backoff Accuracy:', t3.evaluate(test_set))

print()

t4 = nltk.DefaultTagger('NOUN')
t5 = nltk.UnigramTagger(train_set, backoff=t0, cutoff=2)
t6 = nltk.BigramTagger(train_set, backoff=t1, cutoff=3)
t7 = nltk.TrigramTagger(train_set, backoff=t2, cutoff=5)
print('Unigram Backoff Cutoff Accuracy:', t5.evaluate(test_set))
print('Bigram Backoff Cutoff Accuracy:', t6.evaluate(test_set))
print('Trigram Backoff Cutoff Accuracy:', t7.evaluate(test_set))

print()

untag_sents = []
for i in range(5):
    untag_sents.append(nltk.tag.untag(test_set[i]))

tagged_sents_t2 = []
tagged_sents_t7 = []
for sent in untag_sents:
    tagged_sents_t2.append(t2.tag(sent))
    tagged_sents_t7.append(t7.tag(sent))

print('Bigram Backoff sentences:\n')
for s in tagged_sents_t2:
    print(s)

print('\nTrigram Backoff Cutoff sentences:\n')
for s in tagged_sents_t7:
    print(s)


# I was surprised that the DefaultTagger isn't the worst of all the taggers. In my 
# case, the worst tagger was the TrigramTagger followed by the BigramTagger. Simple 
# UnigramTagger performed quite well - around 76%.
#
# The taggers with back-off all performed very good - around 87%. The BigramTagger
# with back-off worked the best. I supposed the TrigramTagger with back-off would
# perform even better, but apparently one extra word doesn't help that much. I also
# tried TrigramTagger with backoff=t1 (UnigramTagger) but with no effect at all.
#
# Cut-off didn't help that much either. The UnigramTagger with both back-off and
# cut-off performs worse than the UnigramTagger with back-off only. For BigramTagger
# and TrigramTagger, the accuracy remains almost the same.
#
# I couldn't decide if the BigramTagger with back-off or the TrigramTagger with back-off
# and cut-off works better. Depending on the random shuffle, one performed better than
# the other but with a very small difference, so I decided to print the tagged sentences
# of both.
#
#
# I will compare the POS tagger from exercise 3.1 to the BigramTagger with back-off.
# They both work similarly - they take a context into account. However, the POS tagger
# from exercise 3.1 operates with suffixes and prefixes and previous words, and is still
# not able to perform better than the "simple" BigramTagger with back-off. The tagger from
# exercise 3.1 has accuracy around 85%, the BigramTagger around 87%. I don't know how 
# nltk's BigramTagger works, if it uses something like a featureset too, but I would
# expect the 3.1 POS tagger to perform better with all these features and words taken
# into account.

