# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# https://www.blackjackapprenticeship.com/how-to-play-blackjack/#:~:text=Blackjack%20is%20played%20with%20a,%2CK)%20count%20as%2010.

import random

# Page 0
# Choose cards 
def newgame():
    print("New Game function starts here")
    global unlimitted_deck
    unlimitted_deck = [2,3,4,5,6,7,8,10,10,10,10,11]
    print(f" function 0: unlimted deck is {unlimitted_deck}")
    player_cards = [] 
    global casino_cards
    casino_cards = []
    print(f"function 0. player_cards array {player_cards} and casino_cards {casino_cards}")
    player_points = 0
    casino_points = 0
    print(f"function 0: player_pints {player_points} and casino points {casino_points}")

newgame()

print("------------------------------------------------------------------------")

# Page 1
# Giving two cards two casiono and hiding 1
def casino_gets_two_cards():
    # Giving first two cards to  casino
    casino_card_one = casino_cards.append(random.choice(unlimitted_deck))
    casino_card_two = casino_cards.append(random.choice(unlimitted_deck))

    print(f" casino array is {casino_cards}")
    print(f"1st card of casino is hidden. Second card is: {casino_cards[1]}")

casino_gets_two_cards()


# Page 2
# Giving two cards two player.
def player_gets_two_cards():
    # Giving first two cards to  casino
    player_card_one = player_cards.append(random.choice(unlimitted_deck))
    player_card_two = player_cards.append(random.choice(unlimitted_deck))
    print(player_card_one)
    print(player_card_two)")

player_gets_two_cards():

'''
# Giving first two cards to player 


    print(f"The player cards are{player_cards}")
    print(f"Total sum of your cards is {player_cards[0]+player_cards[1]} ")


'''
'''
if player_cards[0]+player_cards[1] == 21:
    print("Player Won")
    player_points = player_points + 1
    print(f"score is player: {player_points} casino {casino_points = 0}")
    pass
'''