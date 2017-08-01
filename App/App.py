import csv
import datetime
import matplotlib.pyplot as plt
from matplotlib import style



filename_import = 'data/Tickers.csv'
column = 'Ticker'

data = []

reader = csv.reader(open( filename_import, 'rU'), delimiter=',', dialect='excel')
hrow = next(reader)
idx = hrow.index(column)
for row in reader:
 data.append( row[idx] )


#get the beginning year of the data pulled
year = int(input('Enter the year of how far the data should go back:'))
month = int(input('Enter the month, in numbers, of how far the data should go back:'))
day = int(input('Enter the day of the month of how far the data should go back:'))
date1 = datetime.date(year, month, day)


End_date = datetime.datetime.now()

import pandas_datareader as pdr
from datetime import datetime

Stock_prices = pdr.get_data_yahoo(symbols=data, start=date1, end=End_date)
print(Stock_prices['Adj Close'])



final_data = Stock_prices['Adj Close']
final_data.plot()
plt.show()

final_data.to_csv("data/Stock_prices.csv")
