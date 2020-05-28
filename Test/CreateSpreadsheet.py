import yfinance as yf
from datetime import datetime
import pandas as pd
import xlsxwriter



# Stocks = ['TSLA', 'AAPL', 'SPY', 'VOO', 'VXUS', 'MSFT', 'BAC', 'FB', 'CSCO', 'KO', 'T', 'DAL', 'UAL', 'CCL','F']

def CreateSheet(stockList):
    for i in range(len(Stocks)):

        data_df = yf.download(Stocks[i], start=datetime.now(), end=datetime.now())
        data_df.to_csv(Stocks[i] + '.csv')

        read_file = pd.read_csv (r'/Users/conradpereira/Desktop/StockScraper/'+Stocks[i] + '.csv')

        read_file.to_excel (r'/Users/conradpereira/Desktop/StockScraper/'+ Stocks[i] + '.xlsx', index = None, header=True)



if __name__ == '__main__':
    Stocks = ['TSLA', 'AAPL']

    CreateSheet(Stocks)
