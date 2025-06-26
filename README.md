📈 Technical Indicators in Python

This repository contains Python implementations of popular technical indicators and trading strategies used in financial markets. Each script demonstrates the use of indicators such as Moving Averages and the Relative Strength Index (RSI) to analyze and visualize historical stock data, as well as simulate simple trading strategies.

📂 Contents
1. SMA_implementation.py

Implements Simple Moving Averages (SMA) with short and long windows.

    Uses rolling() mean to compute SMAs.

    Visualizes price along with short and long SMAs.

    Uses IBM stock data from 2010 to 2020.

2. EMA_implementation.py

Implements Exponential Moving Averages (EMA).

    Uses ewm() for smoothing and responsiveness.

    Plots stock price, short-term EMA, and long-term EMA.

    Demonstrates smoothing-based trend analysis.

3. MA_crossover_implementation.py

Implements a Moving Average Crossover Strategy.

    Uses short and long EMAs.

    Simulates a long-only trading strategy.

    Tracks equity curve and prints final profit and capital.

    Based on MSFT stock from 2010 to 2020.

4. RSI_implementation.py

Implements the Relative Strength Index (RSI).

    Computes RSI using rolling averages of price gains/losses.

    Plots RSI values over time.

    Uses IBM data from 2015 to 2020.

5. RSI_MA_implementation.py

Implements a combined RSI + MA crossover strategy.

    Entry signal: Short MA crosses above Long MA and RSI < 30.

    Exit signal: Short MA crosses below Long MA.

    Tracks capital growth and plots equity curve.

    Outputs performance metrics and Sharpe ratio.

🛠 Requirements

    Python 3.x

    Libraries:

        pandas

        numpy

        matplotlib

        yfinance

Install required libraries using:

pip install pandas numpy matplotlib yfinance

🚀 Getting Started

To run any script:

python filename.py

For example:

python SMA_implementation.py

📊 Sample Output

Each script provides:

    Stock price plots with overlaid indicators.

    (For strategies) Equity curves and performance metrics.

📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
🙌 Acknowledgements

Stock data provided by Yahoo Finance via the yfinance API.
