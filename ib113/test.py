from random import randint, randint


def game(length, output=True):
    position = 1
    round_count = 0

    if length >= 2:
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


def game_analysis(length, count):
    rounds_count = 0

    for i in range(count + 1):
        rounds = game(length)
        rounds_count += rounds

    return rounds_count / count


# Vypisuje na standardni vystup prumerne delky her pro plany o velikostech
# 2-50. Pocet simovanych her nad kazdym planem je urcen paramtrem count.
# (Pokud je count nastaven na hodnotu 10, tak hra nad planem velokosti 2
# probehne 10krat, nad planem velikosti 3 take 10krat, atd.

#   :param count: pocet her, ktere se maji simulovat nad danymi plany.

# Ukazkovy vystup po zavolani game_average_length(20):
# Plan with length: 2  ->  6.35
# Plan with length: 3  ->  3.3
# Plan with length: 4  ->  7.45
# Plan with length: 5  ->  6.05
# Plan with length: 6  ->  8.3
# Plan with length: 7  ->  7.95
# Plan with length: 8  ->  6.15
# Plan with length: 9  ->  6.95
# Plan with length: 10  ->  6.1
# Plan with length: 11  ->  5.95
# Plan with length: 12  ->  8.7
# Plan with length: 13  ->  8.3

def game_average_length(count):

    for i in range(2, 51):
        average = game_analysis(i,count)
        print("Plan with length:", i, "->", average)


game_average_length(10)