import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd

class MovingAverageRSIStrategy:

    def __init__(self, capital, stock, start, end, short, long):
        self.data = None
        self.is_long = False
        self.short = short
        self.long = long
        self.capital = capital
        self.equity = [capital]
        self.stock = stock
        self.start = start
        self.end = end

    def download_data(self):
        stock_data = {}
        ticker = yf.download(self.stock, self.start, self.end)
        stock_data['Price'] = ticker['Close'].squeeze()
        self.data = pd.DataFrame(stock_data)

    def construct_signals(self):
        self.data['short_ma'] = self.data['Price'].ewm(span=self.short).mean()
        self.data['long_ma'] = self.data['Price'].ewm(span=self.long).mean()
        self.data['move'] = self.data['Price'] - self.data['Price'].shift(1)
        self.data['up'] = np.where(self.data['move'] > 0, self.data['move'], 0)
        self.data['down'] = np.where(self.data['move'] < 0, self.data['move'], 0)
        self.data['average_gain'] = self.data['up'].rolling(14).mean()
        self.data['average_loss'] = self.data['down'].abs().rolling(14).mean()
        relative_strength = self.data['average_gain']/self.data['average_loss']
        self.data['rsi'] = 100 - (100 / (1 + relative_strength))
        self.data.dropna(inplace=True)

    def simulate(self):
        price_when_buy = 0

        for index, row in self.data.iterrows():
            if row['short_ma'] < row['long_ma'] and self.is_long:
                self.equity.append(self.capital * row['Price'] / price_when_buy)
                self.is_long = False

            elif row['short_ma'] > row['long_ma'] and not self.is_long and row['rsi']<30:
                price_when_buy = row['Price']
                self.is_long = True

    def plot_signals(self):
        plt.figure(figsize=(12,6))
        plt.plot(self.data['Price'], label= 'Stock Price', c='black')
        plt.plot(self.data['short_ma'], label= 'Short MA', c='red')
        plt.plot(self.data['long_ma'], label= 'Long MA', c='blue')
        plt.title('Moving Average (MA) Crossover Trading Strategy with RSI')
        plt.xlabel('Date')
        plt.ylabel('Stock Price')
        plt.show()

    def plot_equity(self):
        plt.figure(figsize=(12,6))
        plt.title('Equity Curve')
        plt.plot(self.equity, label='Stock Price', c='green')
        plt.xlabel('Date')
        plt.ylabel('Actual Capital ($)')
        plt.show()

    def show_stats(self):
        print('Profit of the trading strategy: %.2f%%' % (
            (float(self.equity[-1]) - float(self.equity[0])) /
            float(self.equity[0]) * 100))
        print('Actual capital: $%.2f' % self.equity[-1])
        returns = (self.data['Price'] - self.data['Price'].shift(1)) / self.data['Price'].shift(1)
        ratio = returns.mean() / returns.std() * np.sqrt(252)   # annualised to 252 trading days
        print('Sharpe ratio %.2f' % ratio)

if __name__ == '__main__':

    start = dt.datetime(2010,1,1)
    end = dt.datetime(2020,1,1)

    model = MovingAverageRSIStrategy(100, 'IBM', start, end, 30, 200)
    model.download_data()
    model.construct_signals()
    model.plot_signals()
    model.simulate()
    model.plot_equity()
    model.show_stats()