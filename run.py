# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# https://www.blackjackapprenticeship.com/how-to-play-blackjack/#:~:text=Blackjack%20is%20played%20with%20a,%2CK)%20count%20as%2010.

import random

# Page 0
# Choose cards 


def newgame():
    '''
    Set variables for the game
    '''
    print("New Game function starts here")
    global unlimitted_deck
    unlimitted_deck = [2,3,4,5,6,7,8,10,10,10,10,11]
    print(f" function 0: unlimted deck is {unlimitted_deck}")
    global player_cards
    player_cards = [] 
    global casino_cards
    casino_cards = []
    print(f"function 0. player_cards array {player_cards} and casino_cards {casino_cards}")
    global player_points
    player_points = 0
    global casino_points
    casino_points = 0
    print(f"function 0: player_pints {player_points} and casino points {casino_points}")


newgame()

print("------------------------------------------------------------------------")
# Page 1
# Giving two cards two casiono and hiding 1


def casino_gets_two_cards():
    '''
    Function assign two random numbers from the deck to cassion array.
    '''

    # Giving first two cards to  casino
    casino_cards.append(random.choice(unlimitted_deck))
    casino_cards.append(random.choice(unlimitted_deck))
    #casino_cards = [11, 10]
    print(f"casino array is {casino_cards}")
    print(f"1st card of casino is hidden. Second card is: {casino_cards[1]}")
    return casino_cards


casino_gets_two_cards()

print("------------------------------------------------------------------------")
# Page 2
# Giving two cards two player.


def player_gets_two_cards():
    '''
    Assign tow random numbers from unlimitted deck to player array
    '''
    global player_cards
    # Giving first two cards to  casino
    player_cards.append(random.choice(unlimitted_deck))
    player_cards.append(random.choice(unlimitted_deck))
    # player_cards = [11,11]
    print(f"player array {player_cards}")
    print(f"sum of the array is {sum(player_cards)}")
    return player_cards
    

player_gets_two_cards()
print("----------------------------------------------------------------------")




def player_start_first_playing():
    '''
    This action helps to player to make his first move and win or loss
    '''
    print("Start player_start_first_playing()")
    global player_cards, player_points, casino_points
    print(f"sum of the array is {player_cards}")
    print(f"sum of the array is {sum(player_cards)}")
    if sum(player_cards) == 21:
        print("The player won this round")
        player_points = player_points + 1
        print(f"The score is player: {player_points} casino: {casino_points}")
        return player_points
    if sum(player_cards) == 22:
        # print(f" first value is {player_cards[0]} second value {player_cards[1]}")
        player_cards[1] = 1
        # print(f" first value is {player_cards[0]} second value {player_cards[1]}")
        print("Since you have to aces and sum of them is 22, the second Ace counts as 1")
    print(f"Player, you have {len(player_cards)} cards. The cards have the following values")
    for card in player_cards:
        print(f"    {card}")
    print(f"The sum of the cards is {sum(player_cards)}")
    print(f" Do you want additional card? Please press '1' for yes and '0' for No")
# player_cards, player_points, casino_points
    
    valid_entry = False

    while not valid_entry:
        user_response_str = input("Enter a number: ")
        print(user_response_str)
        print(type(user_response_str))
        if user_response_str.isnumeric():
            user_response = int(user_response_str)
            print(type(user_response))
            print(user_response)
            if user_response == 0 or user_response == 1:
                 valid_entry = True
            else:
                print("Please enter valid entry '0' or '1'")

        else:
            print("Please enter valid entry '0' or '1'")






    '''
    while not is_numeric:
        print("Hey I am numeric loop")
        if user_response_str.isnumeric():
            is_numeric = True
        else: 
            print("Input is not valid, press enter 0 or 1")
            user_response_str = input("Enter a number: ")

    user_response = int(user_response_str)
    

    while user_response != 0 and user_response != 1:
        print("hey I am 0 or 1 loop")
        print("Invalid input. Please enter 0 or 1.")
        user_response = int(input("Enter a number (0 or 1): "))
    '''
    print(user_response)


player_start_first_playing()



