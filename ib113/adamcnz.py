def find_longest_word(words_list):
    longest_word = ""

    for word in words_list:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

def magic(lst):
    for i in range(len(a)-1):
        if a[i] > a[i + 1]:
            a[i + 1] = a[i]
            a[i] = a[i + 1]
    print(a)

magic([3, 7, 5, 1, 8])