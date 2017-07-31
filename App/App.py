import datetime
import pandas_datareader.data as web



stock_tickers = []


while True:
    stock_ticker = input("Please input a valid product identifier, or DONE if finished:")
    if stock_ticker == "DONE":
        break
    else:
        stock_tickers.append(stock_ticker)


q = web.get_quote_google(stock_tickers)

print(q)
