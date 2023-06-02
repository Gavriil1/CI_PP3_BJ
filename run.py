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
    # print("------------------------------------------------------------------------")
    # print("New Game function starts here")
    global unlimitted_deck
    unlimitted_deck = [2,3,4,5,6,7,8,10,10,10,10,11]
    # print(f" function 0: unlimted deck is {unlimitted_deck}")
    global player_cards
    player_cards = [] 
    global casino_cards
    casino_cards = []
    # print(f"function 0. player_cards array {player_cards} and casino_cards {casino_cards}")
    # print(f"function 0: player_pints {player_points} and casino points {casino_points}")


# newgame()


# Page 1
# Giving two cards two casiono and hiding 1


def casino_gets_two_cards():
    '''
    Function assign two random numbers from the deck to cassion array.
    '''
    # print("------------------------------------------------------------------------")
    # print("casino_gets_two_cards(): starts here")
    global casino_cards
    # Giving first two cards to  casino
    casino_cards.append(random.choice(unlimitted_deck))
    casino_cards.append(random.choice(unlimitted_deck))
    # casino_cards = [2, 2]
    # print(f"casino array is {casino_cards}")
    # print(f"1st card of casino is hidden. Second card is: {casino_cards[1]}")
    # return casino_cards


#casino_gets_two_cards()


# Page 2
# Giving two cards two player.


def player_gets_two_cards():
    '''
    Assign tow random numbers from unlimitted deck to player array
    '''
    #print("------------------------------------------------------------------------")
    #print("plaer_gets_two_cards(): starts here")
    global player_cards
    # Giving first two cards to  casino
    player_cards.append(random.choice(unlimitted_deck))
    player_cards.append(random.choice(unlimitted_deck))
    # player_cards = [11,2]
    #print(f"player array {player_cards}")
    #print(f"sum of the array is {sum(player_cards)}")
    # return player_cards
    

#player_gets_two_cards()



def casino_start_first_playing():
    '''
        This action 
    '''

    #print("------------------------------------------------------------------------")
    # print("casino_start_first_playing(): starts here")
    # print("casino_start_first_playing starts here")
    global casino_cards, casino_points, player_points
    # print(f"casino cards are {casino_cards}")
    # print(f"The sum of casino cards is {sum(casino_cards)}")
    if sum(casino_cards) == 22:
        # print(f" first value is {casino_cards[0]} second value {casino_cards[1]}")
        casino_cards[1] = 1
        print("Since casino have to aces and sum of them is 22, the second Ace counts as 1")
        # print(f" first value is {player_cards[0]} second value {player_cards[1]}")
    if sum(casino_cards) == 21:
        print("CASINO WINS! BLACK JACK!")
        casino_points = casino_points + 1
        print(f"Score Player: {player_points} Casino: {casino_points}")
        return casino_points
    
    print(f"The sum of casino cards is {sum(casino_cards)} and of player cards {sum(player_cards)}")

    if sum(casino_cards) > sum(player_cards):
        print(f"cards sum of the casino: {sum(casino_cards)} sum of the plaer cards {sum(player_cards)}")
        print("Casiono SUmo of cards is higher that of a player. Casion won")
        print("Casino won this round")
        casino_points = casino_points + 1
        print(f"The score is player: {player_points} casino: {casino_points}")
        # return casino_points
    while sum(casino_cards) < 17:
        print("I am taking new card")
        casino_cards.append(random.choice(unlimitted_deck))
        print(casino_cards)
        if sum(casino_cards) >21:
            print("Casino sum is over 21. Casino lost player won")
            player_points = player_points + 1
            print(f"The score is player: {player_points} casino: {casino_points}")
            #return player_points
        if sum(casino_cards) == 21:
            print("Casino sum is  21. Casino won player lost")
            casino_points = casino_points + 1
            print(f"The score is player: {player_points} casino: {casino_points}")
            #return casino_points
        if sum(casino_cards) > sum(player_cards):
            print("Casino sum is  iver player sum. Casino won player lost")
            casino_points = casino_points + 1
            print(f"The score is player: {player_points} casino: {casino_points}")
            #return casino_points
 
    if sum(casino_cards) > sum(player_cards):
        print("Casino sum is  iver player sum. Casino won player lost")
        casino_points = casino_points + 1
        print(f"The score is player: {player_points} casino: {casino_points}")
        # return casino_points
    if sum(casino_cards) < sum(player_cards):
        print("Casino sum is  lower than  player sum. Player won player lost")
        player_points = player_points + 1
        print(f"The score is player: {player_points} casino: {casino_points}")
        # return player_points  
    if sum(casino_cards) == sum(player_cards):
        print("Draw")
        print(f"The score is player: {player_points} casino: {casino_points}")
        # return player_points  
    

# casino_start_first_playing()

def player_start_first_playing():
    '''
    This action helps to player to make his first move and win or loss
    '''
    # print("------------------------------------------------------------------------")
    # print("plaer_gets_two_cards(): starts here")
    # print("player_start_first_playing starts here")
    global player_cards, player_points, casino_points
    # print(f"sum of the array is {player_cards}")
    # print(f"sum of the array is {sum(player_cards)}")
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
    print(f"casino first card is {casino_cards[0]}")
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
                # print(type(user_response))
                # print(user_response)
                if user_response == 0 or user_response == 1:
                    valid_entry = True
                else:
                    print("Please enter valid entry '0' or '1'")

            else:
                print("Please enter valid entry '0' or '1'")
        
    if user_response == 0:
        print('Start casino play!')
        casino_start_first_playing()


#player_start_first_playing()


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


def main2():
    newgame()
    casino_gets_two_cards()
    player_gets_two_cards()
    player_start_first_playing()
    print("adddddddddddddddddddddddddddd")


# main2()