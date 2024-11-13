#Fetching the data from yfinance

import yfinance as yf
import pandas as pd

# getting data from yfinance using a function that takes in the stock name and the time period
def get_stock_data():

    # specifying the data types
    start = input('Enter the start date in the format YYYY-MM-DD: ')
    start = pd.to_datetime(start)
    end = input('Enter the end date in the format YYYY-MM-DD: ')
    end = pd.to_datetime(end)

    stock_name = str(input('Enter the stock name: '))
    stock_name = str(stock_name.upper()) # we want the stock name to be a string else throw an error

    stock = yf.download(stock_name, start, end)
    return stock

# calling the function
stock = get_stock_data()
print(stock)
