def get_number(number_line, coord):
    number_line = list(number_line)
    while number_line[coord].isdigit():
        coord -= 1
    coord += 1
    number = 0
    while number_line[coord].isdigit():
        number *= 10
        number += int(number_line[coord])
        number_line[coord] = "."
        coord += 1
    return number, number_line

if __name__ == "__main__":
    input = open("input.txt")
    schematic = input.readlines()
    total = 0
    for line in range(len(schematic)):
        for column in range(len(schematic[line]) - 1):
            if not schematic[line][column].isdigit() and schematic[line][column] != ".":
                """regarder en :
                -1,-1  -1, 0 -1,+1
                 0,-1   sym   0,+1
                +1,-1, +1, 0 +1,+1
                si c'est un chiffre, alors récupérer le nombre qu'il compose,
                l'ajouter et le remplacer par des espaces (important pour pas avoir de doublons)
                """
                print(line)
                if line < len(schematic) and column > 0 and schematic[line + 1][column - 1].isdigit():
                    number = 0
                    coord_x, coord_y = line + 1, column - 1
                    number, schematic[coord_x] = get_number(schematic[coord_x], coord_y)
                    total += number
                if line < len(schematic) and schematic[line + 1][column].isdigit():
                    number = 0
                    coord_x, coord_y = line + 1, column
                    number, schematic[coord_x] = get_number(schematic[coord_x], coord_y)
                    total += number
                if  line < len(schematic) and column < len(schematic[line + 1]) - 1 and schematic[line + 1][column + 1].isdigit():
                    number = 0
                    coord_x, coord_y = line + 1, column + 1
                    number, schematic[coord_x] = get_number(schematic[coord_x], coord_y)
                    total += number
                if schematic[line][column - 1].isdigit() and column > 0:
                    number = 0
                    coord_x, coord_y = line, column - 1
                    number, schematic[coord_x] = get_number(schematic[coord_x], coord_y)
                    total += number
                if  column < len(schematic[line]) - 1 and schematic[line][column + 1].isdigit():
                    number = 0
                    coord_x, coord_y = line, column + 1
                    number, schematic[coord_x] = get_number(schematic[coord_x], coord_y)
                    total += number
                if schematic[line - 1][column - 1].isdigit() and line > 0 and column > 0:
                    number = 0
                    coord_x, coord_y = line - 1, column - 1
                    number, schematic[coord_x] = get_number(schematic[coord_x], coord_y)
                    total += number
                if line > 0 and schematic[line - 1][column].isdigit():
                    number = 0
                    coord_x, coord_y = line - 1, column
                    number, schematic[coord_x] = get_number(schematic[coord_x], coord_y)
                    total += number
                if line > 0 and column < len(schematic[line]) - 1 and schematic[line - 1][column + 1].isdigit():
                    number = 0
                    coord_x, coord_y = line - 1, column + 1
                    number, schematic[coord_x] = get_number(schematic[coord_x], coord_y)
                    total += number

    print(total)