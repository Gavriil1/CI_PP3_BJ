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
logs_to_update = SHEET.worksheet("logfile")
logs_to_update.append_row([datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "This is my timestamp"])

# Player Score variables
scores = SHEET.worksheet('scores')
scores_to_update = SHEET.worksheet("scores")

# Get the values from the existing row A
existing_row_a = scores.row_values(1)  # Assuming row A is the first row (index 1)

# Append new values to columns B and C
new_values_b_c = [datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "This is my timestamp"]
scores_to_update.append_row([existing_row_a[0], *new_values_b_c])






# new file