def text():
    print("Let's use some functions!")

def dash():
    print("-"*25)

def slash():
    print("/"*25)

def backslash():
    print("\\"*25)

def asterisk():
    print("* "*13)

'''Function prints a "box" consisting of rows as following: dashes, slashes, backslashes,
slashes, backslashes, dashes.'''
def box():
    for i in range(6):
        if i == 0 or i == 5:
            dash()

        if i % 2 == 1 and i != 5:
            slash()

        if i % 2 == 0 and i != 0:
            backslash()

'''Function prints final pattern. On the first and the last row it prints "Let's use some functions!" text.
On every odd row it prints a "box" pattern from the earlier function. In between those three "boxes" it prints 
a row of asterisks.'''
def carpet():
    for i in range(7):
        if i == 0 or i == 6:
            text()

        if i % 2 == 1:
            box()

        if i % 2 == 0 and i != 0 and i != 6:
            asterisk()

carpet()
