from datetime import datetime
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

sales = SHEET.worksheet('logfile')

data = sales.get_all_values()

print(data)



print("Please enter sales data from the last market.")
print("Data should be six numbers, separated by commas.")
print("Example: 10,20,30,40,50,60\n")
# data_str = input("Enter your data here:\n")
# sales_data = data_str.split(",")
sales_data  = '2' ,'1','2' 
print(sales_data)
worksheet_to_update = SHEET.worksheet("logfile")
data1 = worksheet_to_update.get_all_values()
print(data1)

worksheet_to_update.append_row(sales_data)
dd = "Hellow how are you"
print("---------------------------------")
# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)
print("---------------------------------")
print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "This is my timestamp")
kk = now.strftime("%d/%m/%Y %H:%M:%S")
worksheet_to_update.append_row([kk,"dd"])
worksheet_to_update.append_row([datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "This is my timestamp"])
#print("worksheet updated succesfully")



