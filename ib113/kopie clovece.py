from random import randint, randint


def game(length, output=True):
    position = 1
    round_count = 0

    if length > 2:
        while True:
            round_count += 1
            print(round_count, "round:", end=" ")
            dice_number = randint(1, 6)

            while dice_number % 6 == 0:
                print(dice_number, end=" ")
                dice_number = randint(1, 6)

                if dice_number == 5:
                    position += 0

                else:
                    position += 6

            if dice_number == 5:
                print(dice_number, end=" ")
                position += 0

            else:
                position += dice_number
                print(dice_number, end=" ")

            if position > length:
                print("Byl by prehozen cil")
                print("-> New position:", position)

            else:
                print("-> New position:", position)

            if position == length:
                break
    else:
        print("Delka hracicho planu neni dostatecne dlouha.")
        return 0

    return round_count

game(30)
