

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
# Imports
import argparse
import csv
from datetime import datetime, date, timedelta
import pandas as pd

#initialize products list
#productlist = []





#def main():

#write CSV files:
with open ("bought.csv", mode='w') as csvfile:
    writer=csv.writer(csvfile, delimiter=",", lineterminator='\n')
    writer.writerow(["product_name","buy_date","buy_price","expiration_date"])
    writer.writerow(["bread", "2023-02-12", "2", "2023-02-15"])
    writer.writerow(["beer", "2023-02-12", "1", "2023-10-12"])
    writer.writerow(["cheese", "2023-02-12", "7", "2023-03-12"])
    writer.writerow(["milk", "2023-02-12", "1", "2023-03-02"])
    writer.writerow(["whiskas", "2023-02-12", "2", "2023-05-12"])
    print("Ok")
df=pd.read_csv("bought.csv")
print(df)

#How to append bought.csv items to inventory.csv?


with open ("sold.csv", mode="w") as csvfile:
    writer=csv.writer(csvfile, delimiter=",", lineterminator='\n')
    writer.writerow(["bought_id", "sell_date", "sell_price"])
    writer.writerow(["bread", "2023-02-13", "3"])
    writer.writerow(["beer", "2023-02-13", "2"])
    writer.writerow(["cheese", "2023-02-13", "9"])
    writer.writerow(["milk", "2023-02-13", "2"])
    writer.writerow(["whiskas", "2023-02-13", "3"])
    print("Beterrrr")

#create inventory.csv, and write products from bought.csv to inventory.csv.
with open ("inventory.csv", mode="w") as csvfile:
    writer=csv.writer(csvfile, delimiter=",", lineterminator='\n')
    writer.writerow(["product_name", "count", "buy_price", "expiration_date"])
    print(writer.writerow)

#Alles van bought.csv moet in inventory.csv, en alles van sold.csv moet uit inventory.csv,
#net als dat alle expired products uit inventory.csv moeten.

#Dus ook eerst nog een expired functie schrijven.



#Using pandas
#work on the csv data with pandas, ad to inventory etc

#HIER OPSCHRIJVEN WELKE ACTIES JE WIL ONDERNEMEN!!

#Wat je koopt op CL moet in bought.csv verschijnen, en automatisch op inventory_lijst
#komen. Dan in inventory_lijst moet alles wat verkocht wordt op CL 
# in sold.csv terechtkomen en automatisch verdwijnen van inventory_lijst.
# Ook moeten alle producten expired verdwijnen van inventory_lijst


df=pd.read_csv("bought.csv")
print(df.head())

  # using merge function by setting how='inner?

  #set the date
#fixed_date="2020-01-01"
#print(fixed_date)
today=date.today()
print("Today is:", today)
today_strf = today.strftime("%Y-%m-%d")

#looking back and forth in time, in which 1 is one day later and -1 one day back(2 is two days later etc)
yesterday = date.today() - timedelta(days=1)
print(yesterday)
tomorrow = date.today() + timedelta(days=1)
print (tomorrow)

def advance_time(number):
    advanced_date = date.today() + timedelta(days=number)
    advanced_strf = advanced_date.strftime("%Y-%m-%d")
    return advanced_strf
print(advance_time(-1989))
#open csv
    #with open (main.py.CSV, 'w', newline ='') as csvfile:



#import sys
#here you can see what s in stock
def inventory(product_name, count, buy_price, expiration_day):
        pass
#Amount of each product
def current_amount_of_each_product():
    pass
#How much each product was bought for and what its expiry date is
def bought_product(id,product_name,buy_date,buy_price,expiration_date):
    pass
#How much each product was sold for OR if it expired, the fact that it did
def sold_product(id,bought_id,sell_date,sell_price):
    pass
def revenue():
#(sell_price * number of sold units)
    pass
def profit():
     #(remainings of revenue after costs)
    pass
def main():
#def append_data(file_path):
    pass
#write commandline tool w argpsarser
#parser=argparse.ArgumentParser(" a command-line tool that a supermarket will use to keep track of their inventory.")
parser=argparse.ArgumentParser (description="Supermarket tool to keep track of inventory")
#parser.add_argument("advancetime")
#create subparsers
subparser = parser.add_subparsers(dest = "command")
#define arguments 
#"create parser for "advanced_time"
#parser.add_argument("--advanced_time", type=str, help="Provides the date (yy-mm-dd)")
#create parser for "buy"
#bought.csv	id,product_name,buy_date,buy_price,expiration_date
advancetime = subparser.add_parser("advancetime", help="looking back and forth in time") 
advancetime.add_argument("--back", type=int, help="Looking back in time with number of days")
advancetime.add_argument("--forth", type=int, help="Looking forth in time with number of days")
buy = subparser.add_parser("buy", help="Here you can add products to buy")
buy.add_argument("--product_name", type=str, help = "Name of product")
buy.add_argument("--buy_date", type=str, help="Date of purchase: string in %Y-%m-%d format")
buy.add_argument("--buy_price", type=float, help="Purchase price of the product")
buy.add_argument("--expiration_date", type=str, help= "date of expiration in YY-MM-DD format")

#create parser for "sold"
#id,bought_id,sell_date,sell_price
sold = subparser.add_parser("sold", help="Sold items")
sold.add_argument("--product_name", type=str, help="Sold items")
sold.add_argument ("--sell_date", type=str, help="Selling date: string in %Y-%m-%d format")
sold.add_argument ("--sell_price", type=float, help="Price of sold product")
#create parser for "inventory"
inventory=subparser.add_parser("inventory", help="Here you can see what's in stock")
inventory.add_argument("--product_name", type=str, help="Name of product")
inventory.add_argument("--count", type=int, help="Number of products")
inventory.add_argument("--buy_price", type=float, help="Purchase price of the product")
inventory.add_argument("--expiration_date", type=str, help="date of expiration in YY-MM-DD format")
#create parser for "revenue"
revenue=subparser.add_parser("revenue", help="Total amount of sales")
revenue.add_argument("--today", help="Todays revenue")
revenue.add_argument("--other date", help="Check revenue on another date, in which -1 is yesterday and 1 tomorrow etc")
#create parser for "expired"
expired = subparser.add_parser("expired", help="Here you can see expired products")
expired.add_argument("--date", type=str, help="Expiry date: string in %Y-%m-%d format" )
#create parser for "profit"
profit =subparser.add_parser("profit", help="Here you can see the profit on a certain date, in which -1 is yesterday and 1 tomorrow etc" )
profit.add_argument("--today", help="Todays profit")
profit.add_argument("--other date", help="Check profit on another date, in which -1 is yesterday and 1 tomorrow etc")
#parser.add_argument
args=parser.parse_args()








if __name__ == "__main__":
    main()
