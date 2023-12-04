if __name__ == "__main__":
    input = open("input.txt")
    lines = input.readlines()
    total = 0
    for line in lines:
        red_number = 0
        green_number = 0
        blue_number = 0
        game_set = line.split(": ")
        game_number = int(game_set[0].removeprefix("Game "))
        sets = game_set[1].split("; ")

        for set in sets:
            pairs = set.split(", ")
            for pair in pairs:
                print(pair)
                pair = pair.split(" ")
                number = int(pair[0])
                color = pair[1].removesuffix("\n")

                if color == "red" and number > red_number:
                    red_number = number
                elif color == "green" and number > green_number:
                    green_number = number
                elif color == "blue" and number > blue_number:
                    blue_number = number


        number_to_add = red_number * green_number * blue_number
        total += number_to_add
        print("Numéro ajouté : " + str(number_to_add))

    print(total)