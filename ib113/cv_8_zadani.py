# Naprogramujte funkci bubble_sort(lst), kde lst je seznam hodnot
# Vyuzijte testovaci vypisy pred kazdou iteraci cyklu pro kontrolu prubehu
# razeni


def bubble_sort(lst):
    is_sorted = False

    while not is_sorted:
        print(lst)
        is_sorted = True

        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                is_sorted = False


print("Bubble sort")
test = [9, 8, 4, 6, 1]
bubble_sort(test)
print("Final:", test)


# Naprogramujte funkci selection_sort(lst), kde lst je seznam hodnot
# Vyuzijte testovaci vypisy pred kazdou iteraci cyklu pro kontrolu prubehu
# razeni


def selection_sort(lst):

    for i in range(len(lst)):
        min_num_index = minimum(lst)
        lst.insert(i, lst[min_num_index])
        print(lst)


def minimum(lst):
    min_num_index = 0

    for i in range(len(lst)):
        min_num_index = i

        for j in range(i + 1, len(lst)):
            if lst[min_num_index] > lst[j]:
                min_num_index = j

    return min_num_index


print("Selection sort")
TEST = [9, 8, 4, 6, 1]
selection_sort(TEST)
print("Final:", TEST)

# Naprogramujte funkci insertion_sort(lst), kde lst je seznam hodnot
# Vyuzijte testovaci vypisy pred kazdou iteraci cyklu pro kontrolu prubehu
# razeni


def insertion_sort(lst):
    pass  # TODO


print("Insertion sort")
TEST = [9, 8, 4, 6, 1]
insertion_sort(TEST)
print("Final:", TEST)
