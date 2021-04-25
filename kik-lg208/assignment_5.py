""" Assignment 5 """

# Below there are functions for each of the operations that the
# user can perform on the lists

def print_list(namelist):
    """ Print all items in 'namelist'

        NB: the namelist variable from the main program is passed as
        an argument to the print_list function; otherwise the function
        would not "see" the name list
    """
    if len(namelist) > 0:
        for i in range(0, len(namelist)):
            print("Item", i, ":", namelist[i])
    else:
        print("List is empty.")

def add_to_list(namelist):
    """ Append a name to 'namelist'

        NB: again the namelist variable from the main program is
        passed as an argument to the add_to_list function.  The
        function modifies the value of namelist, so the function needs
        to return the new value to the main program.  Otherwise the
        main program would not "see" the change.
    """
    name = input("Type in a name to add: ")
    namelist.append(name)
    return namelist # return modified value

    # NB: Lists are passed as arguments to functions *by reference*,
    # which means that there is actually only one copy of the list in
    # memory, so any changes to the namelist inside this function will
    # change the original list in the main program.  Returning the value
    # is not necessary in this case.
    #
    # However, you could use another, temporary list variable in your
    # function, such as:
    #
    # new_list = namelist
    # new_list.append(name)
    # namelist = new_list
    #
    # In this case, you would need to return the modified namelist,
    # because the connection to the original list would be lost.
    # Because you might be using some technique like that in the
    # functions that you will add to this program, we will be
    # consistent, and return the namelist always when it is modified
    # by the function.

def remove_from_list(namelist):
    """ Remove all occurrences of a name from 'namelist'
    """
    del_name = input("What name would you like to remove: ")
    if del_name in namelist:
        while del_name in namelist:
            item_number = namelist.index(del_name)
            del namelist[item_number]
    else:
        print(del_name, "was not found.")
    return namelist

def change_item_in_list(namelist):
    """ Change all occurrences of a name in 'namelist' to another name
    """
    old_name = input("What name would you like to change: ")
    if old_name in namelist:
        new_name = input("What is the new name: ")
        if new_name != old_name:
            while old_name in namelist:
                item_number = namelist.index(old_name)
                namelist[item_number] = new_name
        else:
            print("The new name is the same as the old name.")
    else:
        print(old_name, "was not found.")
    return namelist

# TODO: You need to add your functions here -->

def sort_aplhabetically(namelist):
    if len(namelist) > 0:
        namelist.sort()

    else:
        print("The list is empty. Nothing to sort.")

    return namelist


def reverse_list(namelist):
    if len(namelist) > 0:
        namelist.reverse()

    else:
        print("The list is empty. Nothing to reverse.")

    return namelist


def prepend_name(namelist):
    name = input("Type in a name to prepend: ")
    namelist.insert(0, name)
    return namelist


def longest_name(namelist):
    longest = []
    longest_char = 0

    if len(namelist) > 0:
        for name in namelist:
            if len(name) > longest_char:
                longest = []
                longest.append(name)
                longest_char = len(name)

            if len(name) == longest_char:
                if name not in longest:
                    longest.append(name)
        
        print("The longest name contains", longest_char, "characters.")
        print("The longest name(s) is/are:")

        for names in longest:
            print(names)
    
    else:
        print("The list is empty. No name to show.")

    return namelist


def duplicate(namelist):
    duplicate_list = []

    if len(namelist) > 0:
        for name in namelist:
            duplicate_list.append(name)
            duplicate_list.append(name)

    else:
        print("The list is empty. Nothing to duplicate.")

    return duplicate_list


def drop_every_second(namelist):
    if len(namelist) > 0:
        del namelist[1::2]

    else:
        print("The list is empty. Nothing to drop.")

    return namelist

# <-- Added functions go here

# The main program keeps asking the user for input until the user selects
# Q, which means "Quit"

# TODO: You need to change the main function such that it covers the new operations
# asked for in the assignment.

def main():
    """ Main program that runs the menu loop
    """

    # Initially, namelist is the empty list:
    namelist = []  # NB: this namelist variable exists inside the main program only;
                   # it has the same name as the local variables used in the functions,
                   # but it is another variable!

    menu_item = "0"
    while menu_item != "Q" and menu_item != "q":
        print()            
        print("--------------------")
        print("1. Print the list")
        print("2. Add a name to the list")
        print("3. Remove a name from the list")
        print("4. Change an item in the list")
        print("5. Sort list into alphabetical order")
        print("6. Reverse list")
        print("7. Prepend a name to the list")
        print("8. Find longest name(s) in the list")
        print("9. Duplicate items in the list")
        print("10. Drop every second item from the list")
        print("Q. Quit")
        menu_item = input("Pick an item from the menu: ")
        print()
        if menu_item == "1":
            print_list(namelist)
        elif menu_item == "2":
            namelist = add_to_list(namelist)
            # On the line above namelist gets a nw value, which is
            # the old value of namelist with a new item added to the
            # end of the list (similarly below)
        elif menu_item == "3":
            namelist = remove_from_list(namelist)
        elif menu_item == "4":
            namelist = change_item_in_list(namelist)
        elif menu_item == "5":
            namelist = sort_aplhabetically(namelist)
        elif menu_item == "6":
            namelist = reverse_list(namelist)
        elif menu_item == "7":
            namelist = prepend_name(namelist)
        elif menu_item == "8":
            namelist = longest_name(namelist)
        elif menu_item == "9":
            namelist = duplicate(namelist)
        elif menu_item == "10":
            namelist = drop_every_second(namelist)
        elif menu_item != "Q" and menu_item != "q":
            print("No such item in the menu.")

    print("Goodbye")
                
main() # Call the main function
