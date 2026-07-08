#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# YOUR CODE HERE
"""
x The column Weighted_Price should be removed
xRename the column Timestamp to Date
xConvert the timestamp values to date values
xIndex the data frame on Date
xMissing values in Close should be set to the previous row value
xMissing values in High, Low, Open should be set to the same row's Close value
xMissing values in Volume_(BTC) and Volume_(Currency) should be set to 0
Plot the data from 2017 and beyond at daily intervals and group the values of the same day such that:
High: max
Low: min
Open: mean
Close: mean
Volume(BTC): sum
Volume(Currency): sum
Return the transformed pd.DataFrame before plotting.
"""
# remove weighted price
df = df.drop(columns=["Weighted_Price"])

# rename timestamp to date
df = df.rename(columns={"Timestamp": "Date"})

# Convert timestamp values to data values
df['Date'] = pd.to_datetime(df['Date'], unit='s')

# index hte dataframe on Date
df = df.set_index('Date')

# fill missing close values with previous rows
df['Close'] = df['Close'].ffill()

# fill missing HIgh, Low, Open with Close values
cols_to_fill = ["High", "Low", "Open"]
df[cols_to_fill] = df[cols_to_fill].T.fillna(df["Close"]).T

# Set missing Volume values to 0
df = df.fillna(value={'Volume_(BTC)': 0, 'Volume_(Currency)': 0})

# filter for 2017, resample & aggregate
df_transformed = df.loc['2017'].resample('D').agg({
    'High': 'max',
    'Low': 'min',
    'Open': 'mean',
    'Close': 'mean',
    'Volume_(BTC)': 'sum',
    'Volume_(Currency)': 'sum'
})

# Plotting
df_transformed.plot()
plt.show()
