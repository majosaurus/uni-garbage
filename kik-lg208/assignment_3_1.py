import random

secret_number = random.randint(1, 100)
guess = 0

while(secret_number != guess):
    guess = int(input("Your guess? "))

    if secret_number - guess > 20:
        print("Not even close!")

    if secret_number - guess > 10 and secret_number - guess <= 20:
        print("Getting there...")

    if secret_number - guess > 5 and secret_number - guess <= 10:
        print("Almost there!")

    if secret_number - guess <= 5:
        print("Very close!")

    if secret_number == guess:
        print("Correct! Congratulations!")
