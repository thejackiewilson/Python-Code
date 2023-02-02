import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from datetime import date, timedelta, datetime

stock = yf.Ticker("AAP")
fig = plt.figure()
ax = fig.add_subplot(111)

# Get the stock's historical market data
end_date = datetime.now()
start_date = end_date - timedelta(days=7)
hist = stock.history(interval='1wk', start=start_date, end=end_date)

# Convert the data to a pandas DataFrame
df = pd.DataFrame(hist)

# Calculate the stock's average closing price
average_close = df['Close'].mean()

# Get the stock's current price
print(hist)
current_price = hist.iloc[-1]['Close']

# Calculate and print the moving averages
moving_avg_20 = hist['Close'].rolling(window=20).mean()
moving_avg_50 = hist['Close'].rolling(window=50).mean()

#Calculate the success rate
success_rate = 0
if current_price > moving_avg_20[-1] and current_price > moving_avg_50[-1]:
    success_rate = 100
elif current_price < moving_avg_20[-1] and current_price < moving_avg_50[-1]:
    success_rate = 0
else:
    success_rate = 50


# Calculate the stock's price change percentage
price_change = (current_price - average_close) / average_close * 100

# Print the results
print("Stock:", stock.info['longName'])
print("Average Closing Price:", average_close)
print("Current Price:", current_price)
print("Price Change: {:.2f}%".format(price_change))
print("20-day Moving Average:", moving_avg_20[-1])
print("50-day Moving Average:", moving_avg_50[-1])
print("Success Rate: ", success_rate, "%")

# Plot the stock's closing price over time
ax.xaxis.set_major_locator(MaxNLocator(integer=True, prune='both'))
ax.yaxis.set_major_locator(MaxNLocator(integer=True, prune='both'))
plt.xticks(rotation=90)
plt.plot(df['Close'])
plt.xlabel('Yearly')
plt.ylabel('Closing Price')
plt.title(stock.info['longName'] + ' Closing Price')
plt.show()
