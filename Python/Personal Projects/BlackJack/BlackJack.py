import random

suits = ['Diamond', 'Heart', 'Spade', 'Clubs']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

deck = []
discardPile = []
dealerHand = []
playerHand = []

for suit in suits:
    for rank in ranks:
        card = {'suit': suit, 'rank': rank}
        deck.append(card)

random.shuffle(deck)

def drawRandomCard(deck):
    randomCard = None
    while randomCard not in discardPile:  # Loop until you get a card not in the discard pile
        randomCard = random.choice(deck)
        discardPile.append(randomCard)  # If not, add it to the discard pile
        break  # Break out of the loop
    return randomCard


takenCard = drawRandomCard(deck)
print(takenCard)

