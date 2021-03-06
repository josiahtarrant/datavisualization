import pandas as pd

a = pd.read_csv("AAPLCS.csv")
b = pd.read_csv("GOOGCS.csv")
b = b.dropna(axis=1)
merged = a.merge(b, on='Date')
merged.to_csv("output.csv", index=False)

import matplotlib.pyplot as plt
import csv
  
x = []
y = []
z = []

from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates
import numpy as np

data = pd.read_csv('output.csv')
data["Date"] = pd.to_datetime(data["Date"])
data.sort_values("Date", inplace=True)
date_time = data["Date"]
AAPL = data["Adj Close_x"]
GOOG = data["Adj Close_y"]
plt.plot_date(date_time, AAPL, color = 'b', linestyle='solid', label = 'AAPL')
plt.plot_date(date_time, GOOG, color = 'g', linestyle='solid', label = 'GOOG')

plt.xlabel('Return to Work Strategy', fontweight='bold')
plt.xticks(rotation = 25)
plt.ylabel('Closing Share Price ($)', fontweight='bold')
plt.title('Apple and Google\'s share price (January 2021)')
plt.legend()
plt.show()