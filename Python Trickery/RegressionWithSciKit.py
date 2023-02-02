import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from datetime import datetime, timedelta
import yfinance as yf
import matplotlib.dates as mdates
import matplotlib.pyplot as plt 


# Get the stock information
stock = yf.Ticker("AAPL")


# Get the stock's historical market data
end_date = datetime.now()
start_date = end_date - timedelta(days=365)
hist = stock.history(interval='1d', start=start_date, end=end_date)

# Create a new DataFrame with necessary data
df = pd.DataFrame({'date': hist.index, 'close': hist['close']})

# Create a feature array
X = np.array(df.date).reshape(-1,1)
# Create a target array
y = np.array(df.close)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a LinearRegression model
model = LinearRegression()

# Train the model using the training data
model.fit(X_train, y_train)

# Make predictions using the test data
predictions = model.predict(X_test)

# Print out the predictions
print(predictions)

# Plot the predictions against the actual values
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, predictions, color='blue', linewidth=3)

# Add labels and formatting to the plot
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%A"))
plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator())
plt.gcf().autofmt_xdate()

# Show the plot
plt.show()
