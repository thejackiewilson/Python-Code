import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates as mdates

# Function to calculate moving averages
def moving_averages(stock, days):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    hist = stock.history(interval='1d', start=start_date, end=end_date)
    hist['Close'].plot(figsize=(12,5))
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'{days} Day Moving Averages')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%A"))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    plt.plot(hist.index, hist['Close'].rolling(window=5).mean(), label='5 Day MA')
    plt.plot(hist.index, hist['Close'].rolling(window=10).mean(), label='10 Day MA')
    plt.plot(hist.index, hist['Close'].rolling(window=20).mean(), label='20 Day MA')
    plt.legend()
    plt.show()

# Function to calculate success rate
def success_rate(stock, days):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    hist = stock.history(interval='1d', start=start_date, end=end_date)
    current_price = hist['Close'][-1]
    average_close = hist['Close'].mean()
    price_change = (current_price - average_close) / average_close * 100
    if price_change > 0:
        success = 'Success'
    else:
        success = 'Failure'
    print(f'Over the past {days} days, the stock has had a {price_change:.2f}% change in price. This can be considered a {success}.')

# Get the stock information
stock = yf.Ticker("GME")

# Get the stock's historical market data
end_date = datetime.now()
start_date = end_date - timedelta(days=365)
hist = stock.history(interval='1d', start=start_date, end=end_date)

# Print the moving averages and success rate
moving_averages(stock, 365)
success_rate(stock, 365)

