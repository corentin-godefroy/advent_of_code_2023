if __name__ == "__main__":
    input = open("input.txt")
    lines = input.readlines()
    red_limit = 12
    green_limit = 13
    blue_limit = 14
    total = 0
    for line in lines:
        game_set = line.split(": ")
        game_number = int(game_set[0].removeprefix("Game "))
        sets = game_set[1].split("; ")

        impossible = False
        for set in sets:
            pairs = set.split(", ")
            for pair in pairs:
                print("\"" + pair + "\"")
                pair = pair.split(" ")
                number = int(pair[0])
                color = pair[1].removesuffix("\n")

                if color == "red" and number <= red_limit:
                    red_number = number
                elif color == "green" and number <= green_limit:
                    green_number = number
                elif color == "blue" and number <= blue_limit:
                    blue_number = number
                else:
                    impossible = True
                    break

        if not impossible:
            total += game_number
            print("Numéro ajouté : " + str(game_number))


    print(total)

