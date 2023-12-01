import math

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0
}

if __name__ == "__main__":
    file = open("input.txt")
    total = 0

    while True:
        line = file.readline()

        if line == "":
            break
        if line == "\n":
            continue

        last_position_left = math.inf
        last_position_right = -1
        subtotal_left = 0
        subtotal_right = 0

        for text_number in numbers:
            # Recherche du "chiffre" à gauche qu'il soit en digit ou écrit
            new_position_left = line.find(str(text_number))
            if new_position_left != -1 and last_position_left > new_position_left:
                last_position_left = new_position_left
                subtotal_left = 10 * numbers[text_number]

            # Recherche du "chiffre" à droite qu'il soit en digit ou écrit
            new_position_right = line.rfind(str(text_number))
            if new_position_right != -1 and last_position_right < new_position_right:
                last_position_right = new_position_right
                subtotal_right = numbers[text_number]

        total = total + subtotal_left + subtotal_right

    print(total)
