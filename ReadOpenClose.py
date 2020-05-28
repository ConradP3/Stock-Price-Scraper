import pandas
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import urllib3 as url
import certifi as cert
from datetime import datetime
import xlsxwriter
import csv


OpenPrice = []
ClosePrice = []
PERatio = []
MarketCap=[]

def get_stock_prices(name):
    http = url.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=cert.where())
    html_doc = http.request('GET', 'https://finance.yahoo.com/quote/' + name + '?p=' + name)
    # https://finance.yahoo.com/quote/AAPL?p=AAPL
    soup = BeautifulSoup(html_doc.data, 'html.parser')
    try:
        OpenPrices = soup.find('td', {"data-test":"OPEN-value"}).get_text()
        return soup.find('td', {"data-test":"OPEN-value"}).get_text()
        #<td class="Ta(end) Fw(600) Lh(14px)" data-test="OPEN-value" data-reactid="94"><span class="Trsdu(0.3s) " data-reactid="95">34.92</span></td>
    except:
        pass

def get_stock_prices_Close(name):
    http = url.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=cert.where())
    html_doc = http.request('GET', 'https://finance.yahoo.com/quote/' + name + '?p=' + name)
    #https://finance.yahoo.com/quote/AAPL?p=AAPL
    soup = BeautifulSoup(html_doc.data, 'html.parser')
    try:
        ClosePrices = soup.find('td', {"data-test":'PREV_CLOSE-value'}).get_text()
#<td class="Ta(end) Fw(600) Lh(14px)" data-test="PREV_CLOSE-value" data-reactid="88"><span class="Trsdu(0.3s) " data-reactid="89">2,351.26</span></td>
        return soup.find('td', {"data-test":'PREV_CLOSE-value'}).get_text()
    except:
        pass

def get_stock_PE(name):
    http = url.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=cert.where())
    html_doc = http.request('GET', 'https://finance.yahoo.com/quote/' + name + '?p=' + name)
    #https://finance.yahoo.com/quote/AAPL?p=AAPL
    soup = BeautifulSoup(html_doc.data, 'html.parser')
    try:
        ClosePrices = soup.find('td', {"data-test":'PE_RATIO-value'}).get_text()
        return soup.find('td', {"data-test":'PE_RATIO-value'}).get_text()
    except:
        pass
#<td class="Ta(end) Fw(600) Lh(14px)" data-test="PE_RATIO-value" data-reactid="148"><span class="Trsdu(0.3s) " data-reactid="149">116.39</span></td>


def get_stock_MC(name):
    http = url.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=cert.where())
    html_doc = http.request('GET', 'https://finance.yahoo.com/quote/' + name + '?p=' + name)
    #https://finance.yahoo.com/quote/AAPL?p=AAPL
    soup = BeautifulSoup(html_doc.data, 'html.parser')
    try:
        ClosePrices = soup.find('td', {"data-test":'MARKET_CAP-value'}).get_text()
        return soup.find('td', {"data-test":'MARKET_CAP-value'}).get_text()
    except:
        pass
#<td class="Ta(end) Fw(600) Lh(14px)" data-test="MARKET_CAP-value" data-reactid="138"><span class="Trsdu(0.3s) " data-reactid="139">1.215T</span></td>

def goto(linenum):
    global line
    line = linenum

def createSheet(row_Symbol):
    for i in range(len(row_Symbol)):
        try:
            OpenPrice.append(get_stock_prices(row_Symbol[i]))
            ClosePrice.append(get_stock_prices_Close(row_Symbol[i]))
            PERatio.append(get_stock_PE(row_Symbol[i]))
            MarketCap.append(get_stock_MC(row_Symbol[i]))
            print('close ' + get_stock_prices_Close(row_Symbol[i]))
            print('open ' + get_stock_prices(row_Symbol[i]))
            print('MC ' + get_stock_MC(row_Symbol[i]))
            print('PE Ratio ' + get_stock_PE(row_Symbol[i]))
            print(str(i) + ' data points added to PriceData.csv')
            print('Latest data from ' + str(row_Symbol[i]))
            # Print to command line
        except:
            pass

if __name__ == '__main__':

    data = pandas.read_csv("companylist.csv", header=0)
    row_Symbol = list(data.Symbol)
    Test = ['AMZN', 'TSLA','AAPL']
    df = pandas.DataFrame(data={"Symbol": row_Symbol})
    df.to_csv("./PriceData.csv", sep=',',index=False)

    # Scrapes Close and Open Price from Yahoo.com for all stocks in companylist.csv
    createSheet(row_Symbol)

    # Data from OpenPrice and ClosePrice placed into PriceData.csv

    df = pandas.read_csv("PriceData.csv")
    df["Open Price"] = pandas.DataFrame(data={"Open Price": OpenPrice})
    df['Close Price'] =  pandas.DataFrame(data={"Close Price": ClosePrice})
    df['PE Ratio'] = pandas.DataFrame(data = {'P/E Ratio': PERatio})
    df['Market Cap'] = pandas.DataFrane(data={'Market Cap': MarketCap})
    df['Date'] = datetime.now()

    df.to_csv("PriceData.csv", index=False)

    print("Data Upload Complete")
