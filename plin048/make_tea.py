def make_tea():
    kettle = 0
    celsius = 0
    waiting = 0
    
    tea = choose_tea()
    cups = cups_wanted()
    water = water_needed(cups)
    teaspoons = tea_needed(tea, cups)
    degrees = degrees_needed(tea)
    time = time_needed(tea)

    # prepare the cups
    cups_prepared = [0 for i in range(cups)]
    
    # pour the amount of water we need into a kettle
    while kettle != water:
        kettle += 1

    # bring to boil
    while celsius != 100:
        celsius += 1
    
    # cool the water (green or white tea)
    if tea == "green" or tea == "white":
        while celsius != degrees:
            celsius -= 1
    
    # add tea
    kettle += teaspoons

    # steep tea (in minutes)
    while waiting != time:
        waiting += 1

    # remove tea
    kettle -= teaspoons

    # pour into the cups
    for i in range(len(cups_prepared)):
        while cups_prepared[i] != 250: # 1 cup = 250 ml
            cups_prepared[i] += 1
            kettle -= 1

    return cups_prepared


# choose type of tea from list
def choose_tea():
    tea_types = ["green", "black", "white", "herbal"] # list of teas to choose from

    print("Choose your tea:")

    for i in range(len(tea_types)):
        print(i + 1, tea_types[i], end=" ")
    
    tea = int(input())

    return tea_types[tea - 1]


# calculates how many teaspoons of tea you'll need depending on number of cups given
def tea_needed(tea, cups):
    if tea == "green" or tea == "white" or tea == "herbal":
        return cups * 1
    
    if tea == "black":
        return float(cups) * 0.5


# calculates how much water you'll need depending on number of cups given
def water_needed(cups):
    return cups * 250 # 1 cup = 250 ml


# asks how many cups you want
def cups_wanted():
    print("How many cups do you want?")

    cups = int(input())
    return cups

# returns temperature of water (Celsius)
def degrees_needed(tea):
    if tea == "green":
        return 70
    
    if tea == "black":
        return 100

    if tea == "white":
        return 80

    if tea == "herbal":
        return 100


# steep time in minutes
def time_needed(tea):
    if tea == "green":
        return 2
    
    if tea == "black":
        return 5

    if tea == "white":
        return 3

    if tea == "herbal":
        return 1   

print(make_tea())