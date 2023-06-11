# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# https://www.blackjackapprenticeship.com/how-to-play-blackjack/#:~:text=Blackjack%20is%20played%20with%20a,%2CK)%20count%20as%2010.


from datetime import datetime
import time
import random
import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore
colorama.init(autoreset=True)


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


def welcome_page():
    '''
    welcome message of the game
    '''
    Y = Fore.YELLOW
    print(Fore.GREEN + "Welcome to: ")
    print(Y + "####                                   #")                      
    print(Y + "#   # #      ##    ####  #    #        #   ##    ####  #    # ")
    print(Y + "#   # #     #  #  #    # #   #         #  #  #  #    # #   # ") 
    print(Y + "####  #    #    # #      ####          # #    # #      ####   ")
    print(Y + "#   # #    ###### #      #  #      #   # ###### #      #  #   ")
    print(Y + "#   # #    #    # #    # #   #     #   # #    # #    # #   #  ")
    print(Y + "####  #### #    #  ####  #    #     ###  #    #  ####  #    # ")


def manual():
    '''
    the function prints rules of the game
    '''
    print("1) Player and Casino receives two random cards from the deck]")
    print("")
    time.sleep(print_delay)
    print("2) Player can see both his cards and only one card of the casino")
    time.sleep(print_delay)
    print("3) If sum of the cards is over 21 casino/player loses the round")
    time.sleep(print_delay)
    print("4) If the sum of the card is 21, casino/player wins the round.")
    time.sleep(print_delay)
    print("5) If sum < 21 for both players and noone wants to take additional")
    print("card, we compaire sums of participants to define a winner.")
    time.sleep(print_delay)
    print("6) After receiving cards the player may ask for additional card.")
    time.sleep(print_delay)
    print("7) If player does not take additional card, casino takes a card")
    time.sleep(print_delay)
    print("if 'Casino SUM' <= 'Player SUM' and if 'Casino SUM' < 17.")
    time.sleep(print_delay)
    print("If it is the case, casino takes additional card.  If the above")
    time.sleep(print_delay)
    print("statement is not true, casino does not take any additional card.")
    time.sleep(print_delay)
    input("To start a game please press any key")


def start_game():
    '''
    This function starts interaction with a user.
    It informs the user about number of rounds.
    Informes him that results are going to be saved to excel.
    User chooses if he wants to read a manual or start a game
    '''
    print("- "*34)
    time.sleep(print_delay)
    print("- "*34)
    time.sleep(print_delay)
    print(Fore.GREEN + "Hello Player. Welcome to BlackJac")
    time.sleep(print_delay)
    print(Fore.BLUE + "The game has 10 rounds")
    time.sleep(print_delay)
    print(Fore.MAGENTA + "Result of each round are saved in Excel")
    time.sleep(print_delay)
    show_man = input("Ppress 0 to read game manual. Press 1 to start a game\n")
    if show_man == "0":
        manual()

def newgame():
    '''
    Function Sets varialbles to start a new round
    '''
    global unlimitted_deck
    unlimitted_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    global player_cards
    player_cards = []
    global casino_cards
    casino_cards = []


def casino_gets_two_cards():
    '''
    Function assigns two random numbers from the deck to Casino
    '''

    global casino_cards
    casino_cards.append(random.choice(unlimitted_deck))
    casino_cards.append(random.choice(unlimitted_deck))
    logs_u.append_row([tstamp, f"Casino gets two cards {casino_cards}"])


def player_gets_two_cards():
    '''
    Function assigns tow random numbers from unlimitted deck to player array
    '''
    global player_cards
    player_cards.append(random.choice(unlimitted_deck))
    player_cards.append(random.choice(unlimitted_deck))
    logs_u.append_row([tstamp, f"Player gets two cards {player_cards}"])


def casino_start_first_playing():
    '''
        When player rejcects to take a new card this function starts.
        It checkes if "casino sum" > "player sum" if it trues casino wins.
        Otherwise, we check if "casino sum" <17. and if this a case, casino 
        takes a new card and do the same estimation again.
    '''
    global casino_cards, casino_points, player_points
    if sum(casino_cards) == 22:
        casino_cards[1] = 1
        time.sleep(print_delay)
        print(Fore.BLUE + "Casino has two Aces. First counts 11 second 1")
    if sum(casino_cards) == 21:
        time.sleep(print_delay)
        print(Fore.RED + "CASINO WINS! BLACK JACK!")
        casino_points = casino_points + 1
        time.sleep(print_delay)
        print(Fore.RED + f"PLAYER:{player_points} CASINO:{casino_points}")
        # logfile
        logs_u.append_row([tstamp, "Casino wins Bj"])
        # score record
        scores_to_update.append_row([tstamp, 0, 1])
        return
    time.sleep(print_delay)
    print(f"Casino SUM {sum(casino_cards)} Player Sum {sum(player_cards)}")

    if sum(casino_cards) > sum(player_cards):
        time.sleep(print_delay)
        print(Fore.MAGENTA + "CASINO SUM > PLAYER SUM. CASINO WINS!")
        time.sleep(print_delay)
        casino_points = casino_points + 1
        time.sleep(print_delay)
        print(Fore.RED + f"PLAYER:{player_points} CASINO:{casino_points}")
        # score record
        scores_to_update.append_row([tstamp, 0, 1])
        logs_u.append_row([tstamp, "Casino Wins. Casino Sum > Player Sum"])
        return

    while sum(casino_cards) < 17:
        time.sleep(print_delay)
        print(Fore.YELLOW + "CASINO SUM < 17. CASINO TAKE A  NEW CARD!")
        casino_cards.append(random.choice(unlimitted_deck))
        print(casino_cards)
        if sum(casino_cards) > 21:
            time.sleep(print_delay)
            print(Fore.GREEN + "CASINO SUM > 21. PLAYER WINS!")
            player_points = player_points + 1
            # score record
            scores_to_update.append_row([tstamp, 1, 0])
            logs_u.append_row([tstamp, "Casino SUm > 21 player wins"])
            time.sleep(print_delay)
            print(Fore.RED + f"PLAYER:{player_points} CASINO:{casino_points}")
            return
        if sum(casino_cards) == 21:
            time.sleep(print_delay)
            print(Fore.CYAN + "CASINO BLACK JACK ! CASINO WINS!")
            casino_points = casino_points + 1
            # score record:
            scores_to_update.append_row([tstamp, 0, 1])
            logs_u.append_row([tstamp, "Casino wins. BJ!"])
            time.sleep(print_delay)
            print(Fore.RED + f"PLAYER:{player_points} CASINO:{casino_points}")
            return
        if sum(casino_cards) > sum(player_cards):
            time.sleep(print_delay)
            print(Fore.MAGENTA + "CASINO SUM > PLAYER SUM. CASINO WINS!")
            casino_points = casino_points + 1
            scores_to_update.append_row([tstamp, 0, 1])
            logs_u.append_row([tstamp, "casinosum>playersum casino wins"])
            time.sleep(print_delay)
            print(Fore.RED + f"PLAYER:{player_points} CASINO:{casino_points}")
            return

    if sum(casino_cards) > sum(player_cards):
        time.sleep(print_delay)
        print(Fore.MAGENTA + "CASINO SUM > PLAYER SUM. CASINO WINS!")
        casino_points = casino_points + 1
        # score record
        scores_to_update.append_row([tstamp, 0, 1])
        logs_u.append_row([tstamp, "Casino wins. casinosum>playersum"])
        time.sleep(print_delay)
        print(Fore.RED + f"PLAYER:{player_points} CASINO:{casino_points}")
        return

    if sum(casino_cards) < sum(player_cards):
        time.sleep(print_delay)
        print(Fore.CYAN + "CASINO SUM < PLAYER SUM. PLAYER WINS!")
        player_points = player_points + 1
        time.sleep(print_delay)
        scores_to_update.append_row([tstamp, 1, 0])
        logs_u.append_row([tstamp, "player wins playersum>casinosum"])
        print(Fore.RED + f"PLAYER:{player_points} CASINO:{casino_points}")
        return

    if sum(casino_cards) == sum(player_cards):
        time.sleep(print_delay)
        print(Fore.CYAN + "CASINO SUM = PLAYER SUM. DRAW!")
        logs_u.append_row([tstamp, "Draw"])
        time.sleep(print_delay)
        print(Fore.RED + f"PLAYER:{player_points} CASINO:{casino_points}")
        return


def player_start_first_playing():
    '''
    The function show to the player his card and 1 card of the casino.
    Player decides if he wants to take a new card. If he wants to take 
    a new card , a new card assigned to him. 
    If player rejects to take a card, casino starts playing
    '''
    global player_cards, player_points, casino_points
    if sum(player_cards) == 21:
        time.sleep(print_delay)
        print(Fore.GREEN + "PLAYER SUM 21. BLACK JACK! PLAYER WINS!")
        player_points = player_points + 1
        time.sleep(print_delay)
        print(Fore.RED + f"PLAYER:{player_points} CASINO:{casino_points}")
        # score record
        scores_to_update.append_row([tstamp, 1, 0])
        logs_u.append_row([tstamp, "Player won a game because of BJ"])
        return player_points
    if sum(player_cards) == 22:
        player_cards[1] = 1
        time.sleep(print_delay)
        logs_u.append_row([tstamp, "Player has two Aces.Changing second to 1"])
        print(Fore.YELLOW + "PLAYER HAS TWO ACES. SECOND COUNTS AS  1")
    print(Fore.RED + f"PLAYER:{player_points} CASINO:{casino_points}")
    time.sleep(print_delay)
    print(Fore.CYAN + f"YOU HAVE {len(player_cards)} CARDS. THE CARDS ARE:")
    for card in player_cards:
        print(Fore.CYAN + f"    {card}")
    time.sleep(print_delay)
    print(Fore.GREEN + f"PLAYER SUM {sum(player_cards)}")
    time.sleep(print_delay)
    print(Fore.MAGENTA  + f"CASINO FIRST CARD IS {casino_cards[0]}")
    time.sleep(print_delay)
    print("DO YOU WANT ADDITIONAL CARD? PRESS '1' FOR YES, '0' FOR No")

    valid_entry = False

    while not valid_entry:
        user_response_str = input(Fore.RED + "ENTER A NUMBER:\n ")
        if user_response_str.isnumeric():
            user_response = int(user_response_str)
            if user_response == 0 or user_response == 1:
                valid_entry = True
            else:
                time.sleep(print_delay)
                print(Fore.RED + "PLEASE ENTER VALID ENTRY '0' OR '1'")

        else:
            time.sleep(print_delay)
            print(Fore.RED + "PLEASE ENTER VALID ENTRY  '0' or '1'")


    while user_response == 1:
        logs_u.append_row([tstamp, f"Player gets an additonal card"])
        player_cards.append(random.choice(unlimitted_deck))
        # print(player_cards)
        if sum(player_cards) == 21:
            time.sleep(print_delay)
            print("PLAYER SUM = 21. PLAYER WON!")
            time.sleep(print_delay)
            print("BLACK JACK !")
            player_points = player_points + 1
            time.sleep(print_delay)
            print(Fore.RED + f"PLAYER:{player_points} CASINO:{casino_points}")
            scores_to_update.append_row([tstamp, 1, 0])
            logs_u.append_row([tstamp, "BJ player wins"])
            return player_points
        if sum(player_cards) > 21:
            print(player_cards)
            time.sleep(print_delay)
            print("PLAYER SUM > 21. CASINO WON")
            time.sleep(print_delay)
            print(f"PLAYER SUM {sum(player_cards)}")
            casino_points = casino_points + 1
            time.sleep(print_delay)
            print(Fore.RED + f"PLAYER:{player_points} CASINO:{casino_points}")
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
        print(Fore.YELLOW + 'CASINO STARTS PLAYING!')
        print(Fore.CYAN + "CASINO'S CARDS ARE: ")
        print(casino_cards)
        casino_start_first_playing()

def stats():
    """
    Collects columns of data from sales worksheet, collecting
    the last 5 entries for each sandwich and returns the data
    as a list of lists.
    """
    global scores
    player_point = scores.col_values(2)
    casino_points = scores.col_values(3)
    player_point.pop(0)
    casino_points.pop(0)
    player_point = [int(x) for x in player_point]
    casino_points = [int(x) for x in casino_points]
    player_percentage = round(sum(player_point)/len(player_point) * 100, 2)
    casino_percentage = round(sum(casino_points)/len(casino_points)*100, 2)
    drawpercentage = round(100 - player_percentage - casino_percentage, 2)
    print(Fore.GREEN + "The stats are: ")
    print(Fore.GREEN + f"PLAYER'S PROPABILITY TO WIN :{player_percentage}%")
    print(Fore.GREEN + f"CASINO'S PROPABILITY TO WIN:{casino_percentage}%")
    print(Fore.GREEN + f"THE PROBABILITY FOR A DRAW IS: {drawpercentage}%")


def summary():
    '''
    This function create game summary.
    Give to the user an option to see stats of the game
    Allows t the user to start a new game
    '''
    global player_points, casino_points, game
    time.sleep(print_delay)
    print(Fore.YELLOW + "After 10 rounds the score is ")
    time.sleep(print_delay)
    print(Fore.MAGENTA + f"PLAYER:{player_points} CASINO:{casino_points}")
    if player_points > casino_points:
        time.sleep(print_delay)
        print(Fore.GREEN + "Hello world""player won a game of 10 rounds")
        logs_u.append_row([tstamp, "Player Won the entire game"])
    elif player_points < casino_points:
        time.sleep(print_delay)
        print(Fore.GREEN + "Hello world""Casino won a game of 10 rounds")
        logs_u.append_row([tstamp, "Casino Won the entire game"])
    else:
        time.sleep(print_delay)
        print(Fore.GREEN + "Draw!")
        logs_u.append_row([tstamp, "Casino - Player Draw"])
    time.sleep(print_delay)
    do_stats = input("PRESS ANY KEY TO PLAY. PRESS 0 TO SEE GAME STATS:\n")
    if do_stats == "0":
        stats()
    player_points = 0
    casino_points = 0
    game = 1
    print(game)


def main():
    '''
    main function. Run all other function to run a game
    '''
    global player_points, casino_points, print_delay, game
    logs_u.append_row([tstamp, "The games starts"])
    player_points = 0
    casino_points = 0
    game = 1
    print_delay = 1
    logs_u.append_row([tstamp, f"Set variables for the game"])
    welcome_page()
    while True:
        start_game()
        while game < 3:
            logs_u.append_row([tstamp, "New Round starts"])
            print(Fore.CYAN + "NEW ROUND STARTS")
            print(Fore.MAGENTA + f"ROUND {game}")
            time.sleep(print_delay)
            newgame()
            casino_gets_two_cards()
            player_gets_two_cards()
            player_start_first_playing()
            print("- "*34)
            time.sleep(print_delay)
            print("- "*34)
            time.sleep(print_delay)
            game = game+1
        summary()


main()