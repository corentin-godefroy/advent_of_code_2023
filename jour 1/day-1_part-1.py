if __name__ == "__main__":
    file = open("input.txt")
    total = 0

    while True:
        line = file.readline()

        if line == "":
            break
        if line == "\n":
            continue

        subtotal = 0

        for character in line:
            if character.isdigit():
                subtotal = 10 * int(character)
                break

        for i in range(len(line)-1, -1, -1):
            character = line[i]
            if character.isdigit():
                subtotal = subtotal + int(character)
                break

        total = total + subtotal
    print(total)
