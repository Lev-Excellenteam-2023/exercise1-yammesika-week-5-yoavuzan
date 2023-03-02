import random

SHAPES = ["Club", "Diamond", "Heart", "Spade"]
all_cards = []
players = {1: [], 2: [], 3: [], 4: []}


def main():
    for i in range(1, 14):# create deck of cards
        for j in range(0, 4):
            all_cards.append((i, SHAPES[j]))

    random.shuffle(all_cards) #shuffle all the cards

    for i in range(0, 52): #Divide into 4 players
        player = random.randint(1, 4)
        players[player].append(all_cards[i])

    max_len = max(len(players[1]), len(players[2]), len(players[3]), len(players[4]))#find the winner
    count = 0
    for i in range(1, 5):
        if len(players[i]) == max_len:
            count = count + 1
            winner = i

    print("The winner is player number:", winner) if count == 1 \
        else print("Sorry but we do'nt have winner this time")


if __name__ == '__main__':
    main()
