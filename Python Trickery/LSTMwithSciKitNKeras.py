import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import LSTM, Dense
from datetime import timedelta, datetime

# Get the stock information
stock = yf.Ticker("AAPL")

# Get the stock's historical market data
end_date = datetime.now()
start_date = end_date - timedelta(days=365)
hist = stock.history(interval='1d', start=start_date, end=end_date)

# Create a new DataFrame with necessary data
df = pd.DataFrame({'date': hist.index, 'close': hist['Close']})
print (df.columns)
df['Close']

# Create a feature array
X = np.array(df.close)
# Create a target array
y = np.array(df.close)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest Regression
# Create a RandomForestRegressor model
rf = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model using the training data
rf.fit(X_train.reshape(-1,1), y_train)

# Make predictions using the test data
rf_predictions = rf.predict(X_test.reshape(-1,1))

# Print out the predictions
print(rf_predictions)

# LSTM
# Reshape data for LSTM
X_train = X_train.reshape(X_train.shape[0], 1, 1)
X_test = X_test.reshape(X_test.shape[0], 1, 1)

# Create a LSTM model
model = Sequential()
model.add(LSTM(50, input_shape=(1, 1)))
model.add(Dense(1))

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Train the model
model.fit(X_train, y_train, epochs=100, batch_size=1, verbose=2)

# Make predictions
lstm_predictions = model.predict(X_test)

# Print out the predictions
print(lstm_predictions)
