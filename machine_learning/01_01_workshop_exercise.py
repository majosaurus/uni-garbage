#Write a Python program, in which you rewrite the following loop as a list comprehension:
#
#>>> sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
#>>> result = []
#>>> for word in sent:
#...     word_len = (word, len(word))
#...     result.append(word_len)
#>>> print(result)
#[('The', 3), ('dog', 3), ('gave', 4), ('John', 4), ('the', 3), ('newspaper', 9)]

sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
result = [(w, len(w)) for w in sent]
print(result)
