from random import randint, randint


def game(length, output=True):
    position = 1
    round_count = 0

    if length > 2:
        while True:
            move = 0
            round_count += 1
            print(round_count, "round:", end=" ")
            dice_number = randint(1, 6)
            print(dice_number, end=" ")
            move += dice_number

            while move % 6 == 0:
                next_number = randint(1, 6)
                print(next_number, end=" ")
                move += next_number
                if next_number == 5:
                    move = 5

            if move == 5:
                move = 0

            position += move

            if position > length:
                position -= move
                print("Byl by prehozen cil")

            print("-> New position:", position)

            if position == length:
                print("Game ended in round:", round_count)
                return round_count

    else:
        print("Delka hracicho planu neni dostatecne dlouha.")
        return None


def average(length, num_of_tests):

    i = 0
    round_count = 0

    while i < num_of_tests:
        
        num_of_rounds = game(length)
        round_count += num_of_rounds
        i+=1;

    average = round_count / num_of_tests
    print("Average number of rounds is: ", average)
    return average

average(50, 50)
