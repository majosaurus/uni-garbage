#Write a Python program, in which you rewrite the following nested loop as a nested list comprehension:
#
#>>> words = ['attribution', 'confabulation', 'elocution',
#...          'sequoia', 'tenacious', 'unidirectional']
#>>> vsequences = set()
#>>> for word in words:
#...     vowels = []
#...     for char in word:
#...         if char in 'aeiou':
#...             vowels.append(char)
#...     vsequences.add(''.join(vowels))
#>>> print(sorted(vsequences))
#['aiuio', 'eaiou', 'eouio', 'euoia', 'oauaio', 'uiieioa']

"""
words = ['attribution', 'confabulation', 'elocution', 'sequoia', 'tenacious', 'unidirectional']
vsequences = set()
for word in words:
    vowels = []
    for char in word:
        if char in 'aeiou':
            vowels.append(char)
    print(vowels)
    vsequences.add(''.join(vowels))
    print(vsequences)
print(vsequences)
print(sorted(vsequences))
"""
words = ['attribution', 'confabulation', 'elocution', 'sequoia', 'tenacious', 'unidirectional']
sequences = set()
t = [{c for c in words for c in c if c in 'aeiyou'} for c in words]
print(t)
t = [[''+c for c in w if c in 'aeiyou'] for w in words]
print(t)
t = [c for c in words for c in c if c in 'aeiyou']
print(t)
