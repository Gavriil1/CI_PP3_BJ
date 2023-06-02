# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# https://www.blackjackapprenticeship.com/how-to-play-blackjack/#:~:text=Blackjack%20is%20played%20with%20a,%2CK)%20count%20as%2010.

import random

def newgame():
    '''
    Set variables for the game
    '''
    global unlimitted_deck
    unlimitted_deck = [2,3,4,5,6,7,8,10,10,10,10,11]
    global player_cards
    player_cards = [] 
    global casino_cards
    casino_cards = []


def casino_gets_two_cards():
    '''
    Function assign two random numbers from the deck to cassion array.
    '''
 
    global casino_cards
    casino_cards.append(random.choice(unlimitted_deck))
    casino_cards.append(random.choice(unlimitted_deck))


def player_gets_two_cards():
    '''
    Assign tow random numbers from unlimitted deck to player array
    '''
    global player_cards
    player_cards.append(random.choice(unlimitted_deck))
    player_cards.append(random.choice(unlimitted_deck))


def casino_start_first_playing():
    '''
        This action 
    '''
    global casino_cards, casino_points, player_points
    if sum(casino_cards) == 22:
        casino_cards[1] = 1
        print("1 Casino has to Aces. First counts 11 second 1")
    if sum(casino_cards) == 21:
        print("CASINO WINS! BLACK JACK!")
        casino_points = casino_points + 1
        print(f"2 SCORE PLAYER: {player_points} CASINO: {casino_points}")
        return 
        
    print(f"3 The sum of casino cards is {sum(casino_cards)} and of player cards {sum(player_cards)}")

    if sum(casino_cards) > sum(player_cards):
        print(f"4 CASINO SUM: {sum(casino_cards)} PLAYER SUM {sum(player_cards)}")
        print("5 CASINO SUM > PLAYER SUM. CASINO WINS!")
        casino_points = casino_points + 1
        print(f"6 SCORE PLAYER: {player_points} CASINO: {casino_points}")
        return
  
    while sum(casino_cards) < 17:
        print("7 CASINO SUM < 17. CASINO TAKE A  NEW CARD!")
        casino_cards.append(random.choice(unlimitted_deck))
        print(casino_cards)
        if sum(casino_cards) >21:
            print("8 CASINO SUM > 21. PLAYER WINS!")
            player_points = player_points + 1
            print(f"9 SCORE PLAYER: {player_points} CASINO: {casino_points}")
            return
        if sum(casino_cards) == 21:
            print("10 CASINO BLACK JACK ! CASINO WINS!")
            casino_points = casino_points + 1
            print(f"11 SCORE PLAYER: {player_points} CASINO: {casino_points}")
            return
        if sum(casino_cards) > sum(player_cards):
            print("12 CASINO SUM > PLAYER SUM. CASINO WINS!")
            casino_points = casino_points + 1
            print(f"13 SCORE PLAYER: {player_points} CASINO: {casino_points}")
            return
 
    if sum(casino_cards) > sum(player_cards):
        print("14 CASINO SUM > PLAYER SUM. CASINO WINS!")
        casino_points = casino_points + 1
        print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
        return

    if sum(casino_cards) < sum(player_cards):
        print("15 CASINO SUM < PLAYER SUM. PLAYER WINS!")
        player_points = player_points + 1
        print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
        return

    if sum(casino_cards) == sum(player_cards):
        print("16 CASINO SUM = PLAYER SUM. DRAW!")
        print(f"17 SCORE PLAYER: {player_points} CASINO: {casino_points}")
        return


def player_start_first_playing():
    '''
    This action helps to player to make his first move and win or loss
    '''
    global player_cards, player_points, casino_points
    if sum(player_cards) == 21:
        print("PLAYER SUM 21. BLACK JACK! PLAYER WINDS!")
        player_points = player_points + 1
        print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
        return player_points
    if sum(player_cards) == 22:
        player_cards[1] = 1
        print("PLAYER HAS TWO ACES. SECOND COUNTS AS  1")
    print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
    print(f"YOU HAVE {len(player_cards)} cards. The cards VALUES ARE:")
    for card in player_cards:
        print(f"    {card}")
    print(f"PLAYER SUM {sum(player_cards)}")
    print(f"CASINO FIRST CARD {casino_cards[0]}")
    print(" DO YOU WANT ADDITIONAL CARD? PRESS '1' FOR YES, '0' FOR No")

    
    valid_entry = False

    while not valid_entry:
        user_response_str = input("Enter a number: ")
        # print(user_response_str)
        # print(type(user_response_str))
        if user_response_str.isnumeric():
            user_response = int(user_response_str)
            # print(type(user_response))
            # print(user_response)
            if user_response == 0 or user_response == 1:
                 valid_entry = True
            else:
                print("Please enter valid entry '0' or '1'")

        else:
            print("Please enter valid entry '0' or '1'")

    print(user_response)
    while user_response == 1:
        player_cards.append(random.choice(unlimitted_deck))
        print(player_cards)
        if sum(player_cards) == 21:
            print("The player won this round because sum of his cards is 21")
            print("Black Jack !")
            player_points = player_points + 1
            print(f"The score is player: {player_points} casino: {casino_points}")
            return player_points
        if sum(player_cards) > 21:
            print("The sum of the cards is above 21. Casino Won")
            print(f"the sum of the cards is {sum(player_cards)}")
            casino_points = casino_points + 1
            print(f"The score is player: {player_points} casino: {casino_points}")
            return player_points    
        if sum(player_cards) < 21:
            print(f"Player, you have {len(player_cards)} cards. The cards have the following values")
        for card in player_cards:
            print(f"    {card}")
        print(f"The sum of the cards is {sum(player_cards)}")
        print(f" Do you want additional card? Please press '1' for yes and '0' for No")

        valid_entry = False

        while not valid_entry:
            user_response_str = input("Enter a number: ")
            print(user_response_str)
            print(type(user_response_str))
            if user_response_str.isnumeric():
                user_response = int(user_response_str)
                if user_response == 0 or user_response == 1:
                    valid_entry = True
                else:
                    print("Please enter valid entry '0' or '1'")

            else:
                print("Please enter valid entry '0' or '1'")
        
    if user_response == 0:
        print('Start casino play!')
        casino_start_first_playing()



def main():
    global player_points
    player_points = 0
    global casino_points
    k=1
    casino_points = 0
    while k < 10:
        print(f"ROUND {k}")
        newgame()
        casino_gets_two_cards()
        player_gets_two_cards()
        player_start_first_playing()
        print("adddddddddddddddddddddddddddd")
        print("adddddddddddddddddddddddddddd")
        print("adddddddddddddddddddddddddddd")
        print("adddddddddddddddddddddddddddd")
        k = k+1
        


main()


