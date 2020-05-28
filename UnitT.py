# Testing

from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib3 as url
import certifi as cert
import xlsxwriter
from datetime import datetime as dt
import datetime
from openpyxl import Workbook
from openpyxl import load_workbook


def get_stock_price_Open(name):
    http = url.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=cert.where())
    html_doc = http.request('GET', 'https://finance.yahoo.com/quote/' + name + '?p=' + name)
    #https://finance.yahoo.com/quote/AAPL?p=AAPL
    soup = BeautifulSoup(html_doc.data, 'html.parser')
    price = soup.find('span', {"data-reactid":'103'}).get_text()
    return soup.find('span', {"data-reactid":'103'}).get_text() # Not unique
#<span class="Trsdu(0.3s) " data-reactid="103">777.21</span>
#<span class="Trsdu(0.3s) " data-reactid="98">300.63</span>
def get_stock_price_Close(name):
    http = url.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=cert.where())
    html_doc = http.request('GET', 'https://finance.yahoo.com/quote/' + name + '?p=' + name)
    soup = BeautifulSoup(html_doc.data, 'html.parser')
    price = soup.find('span', {"data-reactid":'98'}).get_text()
    return soup.find('span', {"data-reactid":'98'}).get_text()
#<span class="Trsdu(0.3s) " data-reactid="98">782.58</span>


if __name__ == '__main__':

    print('Symbol | Open/Close')

    #Command Line
    print('__________________________________')
    print('TSLA')
    print('     '+ get_stock_price_Open('TSLA'))
    print('     '+ get_stock_price_Close('TSLA'))

    # from urllib.request import urlopen, Request
    # from bs4 import BeautifulSoup as interpret
    #
    # my_url = 'https://finance.yahoo.com/quote/AAPL'
    # req = Request(my_url, headers={'user-agent': 'Chrome/5.0'})
    # uClient = urlopen(req)
    # page_HTML = uClient.read()
    # uClient.close()
    #
    # page_soup = interpret(page_HTML, 'html.parser')
    #
    # str(page_soup.findAll('tr',{'class':'Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) '})[0]).split('Trsdu(0.3s) ')[1].split('data-reactid=')[1][5:11]
    # stocklist = ['AAPL','AMZN', 'TSLA']
    #
    #
    # for stock in stocklist:
    #   my_url = f'https://finance.yahoo.com/quote/{stock}'
    #   uClient = urlopen(my_url)
    #   page_HTML = uClient.read()
    #   uClient.close()
    #
    #   page_soup = BeautifulSoup(page_HTML, 'html.parser')
    #
    #   print(str(page_soup.findAll('tr',{'class':'Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) '})[0]).split('Trsdu(0.3s) ')[1].split('data-reactid=')[1][5:11])
