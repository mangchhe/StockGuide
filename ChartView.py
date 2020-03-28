import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from openpyxl import load_workbook

class CharView:

    def __init__(self):

        style.use('ggplot')

        self.start = dt.datetime(dt.datetime.today().year-1,dt.datetime.today().month,dt.datetime.today().day)
        self.end = dt.datetime(dt.datetime.today().year,dt.datetime.today().month,dt.datetime.today().day)
        self.df = 0

    def read_stock_data(self, companyName):

        # Open : 개장가 High : 고가 Low : 저가 Close : 마감가 Volume : 거래량
        self.df = web.DataReader(self.get_code(companyName), 'yahoo', self.start, self.end)
        self.df['10ma'] = self.df['Adj Close'].rolling(window=10, min_periods = 0).mean()
        print(self.df)

    def view_stock_data(self):

        ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
        ax2 = plt.subplot2grid((6,1), (5,0), rowspan=5, colspan=1)

        ax1.plot(self.df.index, self.df['Adj Close'])
        ax1.plot(self.df.index, self.df['10ma'])
        ax2.bar(self.df.index, self.df['Volume'])

        plt.show()

    def get_code(self, companyName):

        wb = load_workbook('상장법인목록' + '.xlsx', data_only=True)
        ws = wb['목록']

        for row in ws.rows:
            if row[0].value == companyName:
                return row[1].value + '.KS'

        return 0

if __name__ == '__main':

    charView = CharView()
    charView.read_stock_data('삼성전자')
    charView.view_stock_data()