"""The program asks for two strings. It prints all characters and its
occurences of both strings. If the character occurs in both of the strings,
an asterisk is shown next to the character."""

def count_occurences(string):
    """The function counts occurences of characters in a string. It stores
    them in a dictionary. Keys are the characters, values are the occurences."""

    occurences = {}

    for letter in string:
        if letter not in occurences:
            occurences[letter] = 1

        else:
            occurences[letter] += 1
    
    return occurences


def merge_occurences(first_dict, second_dict):
    """The function combines the occurences of the characters of both strings into 
    the first dictionary."""

    for key, value in second_dict.items():
        if key not in first_dict:
            first_dict[key] = value
        else:
            first_dict[key] += value

    return first_dict


def sort_occurences(dictionary):
    """The function sorts keys in the dictionary in aplhabetical order. It returns
    list of keys."""
    
    sorted_list = []
    sorted_list = sorted(dictionary)
    return sorted_list


def common_characters(first_string, second_string):
    """The function compares two strings and returns a list of their common
    characters."""

    common = []

    for i in range(len(first_string)):
        for j in range(len(second_string)):
            if first_string[i] == second_string[j]:
                common.append(first_string[i])
    
    return common


def print_output(dictionary, sorted_list, common_list):
    """The function outputs character, the number of its occurences
    in both strings. If the character occurs in both strings, an asterisk
    is shown at the end."""

    for character in sorted_list:
        if character in common_list:
            print(character, dictionary[character], "*")

        else:
            print(character, dictionary[character])

    return 0


def main():
    """Main function asking for input and calling the above functions."""

    first = input("Enter first string: ")
    second = input("Enter second string: ")

    first_occur = count_occurences(first)
    second_occur = count_occurences(second)
    common_chars = common_characters(first, second)
    merged_dict = merge_occurences(first_occur, second_occur)
    sorted_list = sorted(merged_dict)
    
    print_output(merged_dict, sorted_list, common_chars)
    
main()
