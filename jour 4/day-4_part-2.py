import sys
def cards_win(wins, card_number):
    next_wins = wins[card_number]
    tot = 0
    for i in range(next_wins):
        if card_number + i + 1 < len(wins):
            tot += cards_win(wins, card_number + i + 1) + 1
    return tot

if __name__ == "__main__":
    input = open("input.txt").readlines()
    number_of_win_by_card = [0] * len(input)
    total = 0
    for i in range(len(input)):
        wins = 0
        card = input[i].split(": ")[1]
        line = card.split("|")
        win_numbers = line[0].split()
        numbers = line[1].split()
        for win_number in win_numbers:
            for number in numbers:
                if int(win_number) == int(number):
                    wins += 1
        number_of_win_by_card[i] = wins

    for i in range(len(number_of_win_by_card)):
        total += cards_win(number_of_win_by_card, i) + 1


    print(total)