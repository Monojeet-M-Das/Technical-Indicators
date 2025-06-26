import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import pandas as pd

def download_data(stock, start, end):
    data = {}
    ticker = yf.download(stock, start, end)
    data['Price'] = ticker['Close'].squeeze()
    return pd.DataFrame(data)

def construct_signal(data, short_period, long_period):
    data['Short EMA'] = data['Price'].ewm(span = short_period, adjust = False).mean()
    data['Long EMA'] = data['Price'].ewm(span = long_period, adjust = False).mean()

def plot_data(data):
    plt.figure(figsize=(12,6))
    plt.plot(data['Price'], label= 'Stock Price')
    plt.plot(data['Short EMA'], label= 'Short EMA', c='red')
    plt.plot(data['Long EMA'], label= 'Long EMA', c='blue')
    plt.title('Moving Average (MA) Indicators')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.show()

if __name__ == '__main__':

    start_date = datetime.datetime(2010,1,1)
    end_date = datetime.datetime(2020,1,1)

    stock_data = download_data('IBM', start= start_date, end= end_date)
    construct_signal(stock_data, 50, 200)
    stock_data.dropna(inplace=True)
    plot_data(stock_data)
