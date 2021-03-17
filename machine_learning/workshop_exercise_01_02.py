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

words = ['attribution', 'confabulation', 'elocution', 'sequoia', 'tenacious', 'unidirectional']
vsequences = sorted(''.join(char for char in word if char in 'aeiyou') for word in words)
print(vsequences)
