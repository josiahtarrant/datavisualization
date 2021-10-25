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
#plt.xticks(date_time[0], date_time[18])
plt.xticks(rotation = 25)
plt.ylabel('Closing Share Price ($)', fontweight='bold')
plt.title('Apple and Google\'s share price (January 2021)')
plt.legend()
plt.show()
'''  
with open('output.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    plots.sort("Date")
    for row in plots:
        x.append(row[0])
        y.append(row[1])  
        z.append(row[2])
print(x)
print(y)
print(z)
x.sort()
y.sort()
z.sort()
plt.plot(x, y, color = 'r')
plt.plot(x, z, color = 'b')
plt.xlabel('Return to Work Strategy', fontweight='bold')
plt.ylabel('# of Companies', fontweight='bold')
plt.title('Number of tech companies using each return to work strategy')
plt.legend()
plt.show()'''
