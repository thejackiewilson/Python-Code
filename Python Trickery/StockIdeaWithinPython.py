import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta, datetime

stock = yf.Ticker("AAPL")

# Get the stock's historical market data
end_date = datetime.now()
start_date = end_date - timedelta(days=1)
hist = stock.history(interval='1d', start=start_date, end=end_date)

# Convert the data to a pandas DataFrame
df = pd.DataFrame(hist)

# Calculate the stock's average closing price
average_close = df['Close'].mean()

# Get the stock's current price
print(hist)
current_price = hist.iloc[-1]['Close']

# Calculate the stock's price change percentage
price_change = (current_price - average_close) / average_close * 100

# Print the results
print("Stock:", stock.info['longName'])
print("Average Closing Price:", average_close)
print("Current Price:", current_price)
print("Price Change: {:.2f}%".format(price_change))

# Plot the stock's closing price over time
plt.plot(df['Close'])
plt.xlabel('Year')
plt.ylabel('Closing Price')
plt.title(stock.info['longName'] + ' Closing Price')
plt.show()
