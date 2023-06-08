# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# https://www.blackjackapprenticeship.com/how-to-play-blackjack/#:~:text=Blackjack%20is%20played%20with%20a,%2CK)%20count%20as%2010.


from datetime import datetime
import random
import time
import gspread
from google.oauth2.service_account import Credentials



SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('blackjack')


# log file variables
logs = SHEET.worksheet('logfile')
logs_u = SHEET.worksheet("logfile")
logs_data = logs.get_all_values()
tstamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
logs_u.append_row([tstamp, "This is my timestamp"])

# Player Score variables
scores = SHEET.worksheet('scores')
scores_to_update = SHEET.worksheet("scores")
print('ooooooooooooooooooooooooooooooo')


def newgame():
    '''
    Set variables for the game
    '''
    global unlimitted_deck
    unlimitted_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
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
    logs_u.append_row([tstamp, f"Casino gets two cards {casino_cards}"])


def player_gets_two_cards():
    '''
    Assign tow random numbers from unlimitted deck to player array
    '''
    global player_cards
    player_cards.append(random.choice(unlimitted_deck))
    player_cards.append(random.choice(unlimitted_deck))
    logs_u.append_row([tstamp, f"Player gets two cards {player_cards}"])


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
        # logfile
        logs_u.append_row([tstamp, "Casino wins Bj"])
        # score record
        scores_to_update.append_row([tstamp, 0, 1])
        return
    time.sleep(print_delay)
    print(f"Casino SUM {sum(casino_cards)} Player Sum {sum(player_cards)}")

    if sum(casino_cards) > sum(player_cards):
        time.sleep(print_delay)
        print(f"CASINOSUM: {sum(casino_cards)} PLAYER SUM {sum(player_cards)}")
        time.sleep(print_delay)
        print("CASINO SUM > PLAYER SUM. CASINO WINS!")
        time.sleep(print_delay)
        casino_points = casino_points + 1
        time.sleep(print_delay)
        print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
        # score record
        scores_to_update.append_row([tstamp, 0, 1])
        logs_u.append_row([tstamp, "Casino Wins. Casino Sum > Player Sum"])
        return

    while sum(casino_cards) < 17:
        time.sleep(print_delay)
        print("CASINO SUM < 17. CASINO TAKE A  NEW CARD!")
        casino_cards.append(random.choice(unlimitted_deck))
        print(casino_cards)
        if sum(casino_cards) > 21:
            time.sleep(print_delay)
            print("CASINO SUM > 21. PLAYER WINS!")
            player_points = player_points + 1
            # score record
            scores_to_update.append_row([tstamp, 1, 0])
            logs_u.append_row([tstamp, "Casino SUm > 21 player wins"])
            time.sleep(print_delay)
            print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
            return
        if sum(casino_cards) == 21:
            time.sleep(print_delay)
            print("CASINO BLACK JACK ! CASINO WINS!")
            casino_points = casino_points + 1
            # score record:
            scores_to_update.append_row([tstamp, 0, 1])
            logs_u.append_row([tstamp, "Casino wins. BJ!"])
            time.sleep(print_delay)
            print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
            return
        if sum(casino_cards) > sum(player_cards):
            time.sleep(print_delay)
            print("CASINO SUM > PLAYER SUM. CASINO WINS!")
            casino_points = casino_points + 1
            scores_to_update.append_row([tstamp, 0, 1])
            logs_u.append_row([tstamp, "casinosum>playersum casino wins"])
            time.sleep(print_delay)
            print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
            return

    if sum(casino_cards) > sum(player_cards):
        time.sleep(print_delay)
        print("CASINO SUM > PLAYER SUM. CASINO WINS!")
        casino_points = casino_points + 1
        # score record
        scores_to_update.append_row([tstamp, 0, 1])
        logs_u.append_row([tstamp, "Casino wins. casinosum>playersum"])
        time.sleep(print_delay)
        print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
        return

    if sum(casino_cards) < sum(player_cards):
        time.sleep(print_delay)
        print("CASINO SUM < PLAYER SUM. PLAYER WINS!")
        player_points = player_points + 1
        time.sleep(print_delay)
        scores_to_update.append_row([tstamp, 1, 0])
        logs_u.append_row([tstamp, "player wins playersum>casinosum"])
        print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
        return

    if sum(casino_cards) == sum(player_cards):
        time.sleep(print_delay)
        print("CASINO SUM = PLAYER SUM. DRAW!")
        logs_u.append_row([tstamp, "Draw"])
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
        # score record
        scores_to_update.append_row([tstamp, 1, 0])
        logs_u.append_row([tstamp, "Player won a game because of BJ"])
        return player_points
    if sum(player_cards) == 22:
        player_cards[1] = 1
        time.sleep(print_delay)
        logs_u.append_row([tstamp, "Player has two Aces.Changing second to 1"])
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
        user_response_str = input("ENTER A NUMBER:\n ")
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
        logs_u.append_row([tstamp, f"Player gets an additonal card"])
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
            # score record
            scores_to_update.append_row([tstamp, 1, 0])
            logs_u.append_row([tstamp, "BJ player wins"])
            return player_points
        if sum(player_cards) > 21:
            time.sleep(print_delay)
            print("PLAYER SUM > 21. CASINO WON")
            time.sleep(print_delay)
            print(f"PLAYER SUM {sum(player_cards)}")
            casino_points = casino_points + 1
            time.sleep(print_delay)
            print(f"SCORE PLAYER: {player_points} CASINO: {casino_points}")
            # score record
            scores_to_update.append_row([tstamp, 0, 1])
            logs_u.append_row([tstamp, " Player Sum >21 casino wins"])
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
            user_response_str = input("ENTER NUMBER:\n")
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
        logs_u.append_row([tstamp, "Player pressed 0. Casiono starts"])
        time.sleep(print_delay)
        print('CASINO STARTS PLAYING!')
        casino_start_first_playing()


def main():
    global player_points, casino_points, print_delay
    logs_u.append_row([tstamp, "The games starts"])
    player_points = 0
    casino_points = 0
    game = 1
    print_delay = 1
    logs_u.append_row([tstamp, f"Set variables for the game"])
    while True:
        print("-------------------------------------------------")
        time.sleep(print_delay)
        print("-------------------------------------------------")
        time.sleep(print_delay)
        print("Hello Player. Welcome to BlackJac")
        time.sleep(print_delay)
        print("The game has 10 rounds")
        time.sleep(print_delay)
        print("Result of each round are saved in Excel")
        time.sleep(print_delay)
        input("Press any key to continue:\n ")
        logs_u.append_row([tstamp, "Player pressed key to start a game"])
        while game < 10:
            logs_u.append_row([tstamp, "New Round starts"])
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
            logs_u.append_row([tstamp, "Player Won the entire game"])
        elif player_points < casino_points:
            time.sleep(print_delay)
            print("Casino won a game of 10 rounds")
            logs_u.append_row([tstamp, "Casino Won the entire game"])
        else:
            time.sleep(print_delay)
            print("Draw!")
            logs_u.append_row([tstamp, "Casino - Player Draw"])
        time.sleep(print_delay)
        input("TO PLAY BLACK JACK AGAIN PRESS  ANY KEY:\n")
        player_points = 0
        casino_points = 0
        game = 1


main()
