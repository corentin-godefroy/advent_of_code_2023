if __name__ == "__main__":
    input = open("input.txt").readlines()
    total = 0
    for card in input:
        wins = 0
        card = card.split(": ")[1]
        line = card.split("|")
        win_numbers = line[0].split()
        numbers = line[1].split()
        for win_number in win_numbers:
            for number in numbers:
                if int(win_number) == int(number):
                    wins += 1
        total += round(2**(wins-1))
    print(total)