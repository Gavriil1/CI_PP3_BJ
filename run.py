# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# https://www.blackjackapprenticeship.com/how-to-play-blackjack/#:~:text=Blackjack%20is%20played%20with%20a,%2CK)%20count%20as%2010.

import random

# First array.
print("hi how are you")
unlimitted_deck = [2,3,4,5,6,7,8,10,10,10,10,11]
print(unlimitted_deck)
player_cards = []
casino_cards = []

random_number = random.choice(unlimitted_deck)

print(random_number)

# Giving first two cards to player and casino
player_cards.append(random.choice(unlimitted_deck))
player_cards.append(random.choice(unlimitted_deck))

print("Hhere are players cards")
print(player_cards)