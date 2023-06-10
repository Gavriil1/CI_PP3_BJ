# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# https://www.blackjackapprenticeship.com/how-to-play-blackjack/#:~:text=Blackjack%20is%20played%20with%20a,%2CK)%20count%20as%2010.


from datetime import datetime
import random
import time
import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore, Back, Style
colorama.init()




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
player_points = 0
casino_points = 1

print(Fore.BLACK + "Hello world")
print(Fore.RED + "Hello world")
print(Fore.GREEN + "Hello world")
print(Fore.YELLOW + "Hello world")
print(Fore.MAGENTA + "Hello world")
print(Fore.CYAN + "Hello world")
print(Fore.WHITE + "Hello world")