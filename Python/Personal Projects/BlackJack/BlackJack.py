import random

suits = ['Diamond', 'Heart', 'Spade', 'Clubs']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

deck = []

for suit in suits:
    for rank in ranks:
        card = {'suit': suit, 'rank': rank}
        deck.append(card)

for i in deck:
    print(i['rank'])