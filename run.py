# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# https://www.blackjackapprenticeship.com/how-to-play-blackjack/#:~:text=Blackjack%20is%20played%20with%20a,%2CK)%20count%20as%2010.

import random
import time

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
        time.sleep(print_delay)
        print("1 Casino has to Aces. First counts 11 second 1")
    if sum(casino_cards) == 21:
        time.sleep(print_delay)
        print("CASINO WINS! BLACK JACK!")
        casino_points = casino_points + 1
        time.sleep(print_delay)
        print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
        return 
    time.sleep(print_delay)
    print(f"The sum of casino cards is {sum(casino_cards)} and of player cards {sum(player_cards)}")

    if sum(casino_cards) > sum(player_cards):
        time.sleep(print_delay)
        print(f"CASINO SUM: {sum(casino_cards)} PLAYER SUM {sum(player_cards)}")
        time.sleep(print_delay)
        print("CASINO SUM > PLAYER SUM. CASINO WINS!")
        time.sleep(print_delay)
        casino_points = casino_points + 1
        time.sleep(print_delay)
        print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
        return
  
    while sum(casino_cards) < 17:
        time.sleep(print_delay)
        print("CASINO SUM < 17. CASINO TAKE A  NEW CARD!")
        casino_cards.append(random.choice(unlimitted_deck))
        print(casino_cards)
        if sum(casino_cards) >21:
            time.sleep(print_delay)
            print("CASINO SUM > 21. PLAYER WINS!")
            player_points = player_points + 1
            time.sleep(print_delay)
            print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
            return
        if sum(casino_cards) == 21:
            time.sleep(print_delay)
            print("CASINO BLACK JACK ! CASINO WINS!")
            casino_points = casino_points + 1
            time.sleep(print_delay)
            print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
            return
        if sum(casino_cards) > sum(player_cards):
            time.sleep(print_delay)
            print("CASINO SUM > PLAYER SUM. CASINO WINS!")
            casino_points = casino_points + 1
            time.sleep(print_delay)
            print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
            return
 
    if sum(casino_cards) > sum(player_cards):
        time.sleep(print_delay)
        print("CASINO SUM > PLAYER SUM. CASINO WINS!")
        casino_points = casino_points + 1
        time.sleep(print_delay)
        print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
        return

    if sum(casino_cards) < sum(player_cards):
        time.sleep(print_delay)
        print("CASINO SUM < PLAYER SUM. PLAYER WINS!")
        player_points = player_points + 1
        time.sleep(print_delay)
        print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
        return

    if sum(casino_cards) == sum(player_cards):
        time.sleep(print_delay)
        print("CASINO SUM = PLAYER SUM. DRAW!")
        time.sleep(print_delay)
        print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
        return


def player_start_first_playing():
    '''
    This action helps to player to make his first move and win or loss
    '''
    global player_cards, player_points, casino_points
    if sum(player_cards) == 21:
        time.sleep(print_delay)
        print("PLAYER SUM 21. BLACK JACK! PLAYER WINDS!")
        player_points = player_points + 1
        time.sleep(print_delay)
        print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
        return player_points
    if sum(player_cards) == 22:
        player_cards[1] = 1
        time.sleep(print_delay)
        print("PLAYER HAS TWO ACES. SECOND COUNTS AS  1")
    print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
    time.sleep(print_delay)
    print(f"YOU HAVE {len(player_cards)} cards. The cards VALUES ARE:")
    for card in player_cards:
        print(f"    {card}")
    time.sleep(print_delay)
    print(f"PLAYER SUM {sum(player_cards)}")
    time.sleep(print_delay)
    print(f"CASINO FIRST CARD {casino_cards[0]}")
    time.sleep(print_delay)
    print("DO YOU WANT ADDITIONAL CARD? PRESS '1' FOR YES, '0' FOR No")

    valid_entry = False

    while not valid_entry:
        user_response_str = input("ENTER A NUMBER: ")
        # print(user_response_str)
        # print(type(user_response_str))
        if user_response_str.isnumeric():
            user_response = int(user_response_str)
            # print(type(user_response))
            # print(user_response)
            if user_response == 0 or user_response == 1:
                valid_entry = True
            else:
                time.sleep(print_delay)
                print("PLEASE ENTER VALID ENTRY '0' OR '1'")

        else:
            time.sleep(print_delay)
            print("PLEASE ENTER VALID ENTRY  '0' or '1'")

    print(user_response)
    while user_response == 1:
        player_cards.append(random.choice(unlimitted_deck))
        print(player_cards)
        if sum(player_cards) == 21:
            time.sleep(print_delay)
            print("PLAYER SUM = 21. PLAYER WON!")
            time.sleep(print_delay)
            print("BLACK JACK !")
            player_points = player_points + 1
            time.sleep(print_delay)
            print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
            return player_points
        if sum(player_cards) > 21:
            time.sleep(print_delay)
            print("PLAYER SUM > 21. CASINO WON")
            time.sleep(print_delay)
            print(f"PLAYER SUM {sum(player_cards)}")
            casino_points = casino_points + 1
            time.sleep(print_delay)
            print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
            return player_points    
        if sum(player_cards) < 21:
            time.sleep(print_delay)
            print(f"YOU HAVE {len(player_cards)} cards. The cards VALUES ARE:")
            for card in player_cards:
                time.sleep(print_delay)
                print(f"    {card}")   
            time.sleep(print_delay)
            print(f"The sum of the cards is {sum(player_cards)}")
            time.sleep(print_delay)
            print(f"CASINO FIRST CARD {casino_cards[0]}")
            time.sleep(print_delay)
            print("DO YOU WANT ADDITIONAL CARD? PRESS '1' FOR YES, '0' FOR No")

        valid_entry = False

        while not valid_entry:
            user_response_str = input("ENTER NUMBER: ")
            # print(user_response_str)
            # print(type(user_response_str))
            if user_response_str.isnumeric():
                user_response = int(user_response_str)
                if user_response == 0 or user_response == 1:
                    valid_entry = True
                else:
                    time.sleep(print_delay)
                    print("PLEASE ENTER VALID ENTRY '0' OR  '1'")

            else:
                time.sleep(print_delay)
                print("PLEASE ENTER VALID ENTRY '0' OR '1'")
        
    if user_response == 0:
        time.sleep(print_delay)
        print('CASINO STARTS PLAYING!')
        casino_start_first_playing()



def main():
    global player_points, casino_points, print_delay
    player_points = 0
    casino_points = 0
    game = 1
    print_delay = 1
    while True:
        print("-------------------------------------------------")
        time.sleep(print_delay)
        print("-------------------------------------------------")
        time.sleep(print_delay)
        print("Hello Player. Welcome to BlackJac")
        time.sleep(print_delay)
        print("The game has 10 rounds")
        time.sleep(print_delay)
        print("Result of each round and overall results are going to be saved in Excel")
        time.sleep(print_delay)
        input("Press any key to continue: ")
        while game < 10:
            print("NEW ROUND STARTS")
            print(f"ROUND {game}")
            time.sleep(print_delay)
            newgame()
            casino_gets_two_cards()
            player_gets_two_cards()
            player_start_first_playing()
            print("-------------------------------------------------")
            time.sleep(print_delay)
            print("-------------------------------------------------")
            time.sleep(print_delay)
            game = game+1
        time.sleep(print_delay)
        print("After 10 rounds the score is ")
        time.sleep(print_delay)
        print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
        if player_points > casino_points:
            time.sleep(print_delay)
            print("player won a game of 10 rounds")
        elif player_points < casino_points:
            time.sleep(print_delay)
            print("Casino won a game of 10 rounds")
        else:
            time.sleep(print_delay)
            print("Draw!")
        time.sleep(print_delay)
        input("TO PLAY BLACK JACK AGAIN PRESS  ANY KEY: ")
        player_points = 0
        casino_points = 0
        game = 1

main()


