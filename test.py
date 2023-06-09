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


#print(data)
player_point = scores.col_values(2)
casino_points = scores.col_values(3)
print(player_point)
print(casino_points)
player_point.pop(0)
casino_points.pop(0)
player_point = [int(x) for x in player_point]
casino_points = [int(x) for x in casino_points]
print(player_point)
print(casino_points)
print(sum(player_point)/len(player_point))
print(sum(casino_points)/len(casino_points))
player_percentage = round(sum(player_point)/len(player_point) * 100, 2)
casino_percentage = round(sum(casino_points)/len(casino_points)*100, 2)
print(player_percentage)
print(casino_percentage)
print(player_percentage + casino_percentage)
print(100 - player_percentage - casino_percentage)
drawpercentage = round(100 - player_percentage - casino_percentage, 2)
print("The propability player to win is :", player_percentage, "%")
print("The propability casino to win:", casino_percentage, "%")
print("The propability for a draw is", drawpercentage, "%")


def get_last_5_entries_sales1():
    """
    Collects columns of data from sales worksheet, collecting
    the last 5 entries for each sandwich and returns the data
    as a list of lists.
    """
    player_point = SHEET.worksheet("sales")
    print(sales)
    '''
    cheese_hum = sales.col_values(1)
    tom_moz = sales.col_values(2)
    print(cheese_hum)
    print(tom_moz)
    cheese_hum.pop(0)
    tom_moz.pop(0)
    print(cheese_hum)
    print(tom_moz)
    cheese_hum = [int(x) for x in cheese_hum]
    tom_moz = [int(x) for x in tom_moz]
    print(cheese_hum)
    print(tom_moz)
    print(sum(cheese_hum)/len(cheese_hum))
    print(sum(tom_moz)/len(tom_moz))
    return
    '''

#get_last_5_entries_sales1()
    