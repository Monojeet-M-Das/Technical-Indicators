import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import pandas as pd
import numpy as np

def download_data(stock, start, end):
    data = {}
    ticker = yf.download(stock, start, end)
    data['Price'] = ticker['Close'].squeeze()
    return pd.DataFrame(data)


if __name__ == '__main__':

    start = datetime.datetime(2015,1,1)
    end = datetime.datetime(2020,1,1)
    stock_data = download_data('IBM', start, end)
    
    stock_data['return'] = np.log(stock_data['Price'] / stock_data['Price'].shift(1))
    stock_data['move'] = stock_data['Price'] - stock_data['Price'].shift(1)

    # average; then the 0 values do not count
    stock_data['up'] = np.where(stock_data['move'] > 0, stock_data['move'], 0)
    stock_data['down'] = np.where(stock_data['move'] < 0, stock_data['move'], 0)
    
    # Relative Strength
    stock_data['average_gain'] = stock_data['up'].rolling(14).mean()
    stock_data['average_loss'] = stock_data['down'].abs().rolling(14).mean()

    RS = stock_data['average_gain']/stock_data['average_loss']

    stock_data['rsi'] = 100 - (100 / (1 + RS))

    stock_data.dropna(inplace=True)
    print(stock_data)
    plt.plot(stock_data['rsi'])
    plt.show()
