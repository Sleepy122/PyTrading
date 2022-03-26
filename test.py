from typing_extensions import Self
import alpaca_trade_api as tradeapi
import secretsConfig as secrets
import pandas as pd
import matplotlib.pyplot as plt
import requests
import numpy as np
from math import floor
from termcolor import colored as cl
import schedule
import time




ALPACA_BASE_URL = "https://paper-api.alpaca.markets"


class PythonTradingBot :
    def __init__(self) :
        self.alpaca = tradeapi.REST(secrets.ALPACA_API_KEY,secrets.ALPACA_API_SECRET, ALPACA_BASE_URL,api_version="v2")
# test
    def run(self) :
        print("testing getting Microsoft Trade")
        bar_group = self.alpaca.get_barset("QQQ", "day", limit=5)
        for bar in bar_group:
            print(bar)
        print("Got Microsoft Trade?")

    def buyShares(self,rsiIndicator) :
        print("the rsi indicator was : ",rsiIndicator, " setting it to 25 for instant buy")
        rsiIndicator = 25
        if(rsiIndicator < 30):
            order_confirmation = self.alpaca.submit_order(
                symbol='BNGO',
                side='buy',
                type='market',
                qty='1',
                time_in_force='day',
            )
            print(order_confirmation)
            print("Stock was bought")
        elif(rsiIndicator > 70) :
            #Test this code
            self.alpaca.cancel_all_orders()
            share_amount = self.alpaca.close_position("BNGO",{'percentage': 100})
            print ("Stock was sold")
        else:
            print("Stock was held")

        



#####____________________________________________________________________ALPHA

plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (20, 10)

def get_historical_data(symbol, start_date = None):
    api_key = secrets.ALPHA_VANTAGE_API_KEY
    ## ENTIRE OUTPUT??? how much data is this???
    api_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}&outputsize=full'
    raw_df = requests.get(api_url).json()

    df = pd.DataFrame(raw_df[f'Time Series (Daily)']).T
    df = df.rename(columns = {'1. open': 'open', '2. high': 'high', '3. low': 'low', '4. close': 'close', '5. volume': 'volume'})
    for i in df.columns:
        df[i] = df[i].astype(float)
    df.index = pd.to_datetime(df.index)
    # df = df.iloc[::-1].drop(['7. dividend amount', '8. split coefficient'], axis = 1)
    if start_date:
        df = df[df.index >= start_date]
    return df

ibm = get_historical_data('BNGO', '2020-01-01')
ibm

#**************** RSI
def get_rsi(close, lookback):
    ret = close.diff()
    up = []
    down = []
    for i in range(len(ret)):
        if ret[i] < 0:
            up.append(0)
            down.append(ret[i])
        else:
            up.append(ret[i])
            down.append(0)
    up_series = pd.Series(up)
    down_series = pd.Series(down).abs()
    up_ewm = up_series.ewm(com = lookback - 1, adjust = False).mean()
    down_ewm = down_series.ewm(com = lookback - 1, adjust = False).mean()
    rs = up_ewm/down_ewm
    rsi = 100 - (100 / (1 + rs))
    rsi_df = pd.DataFrame(rsi).rename(columns = {0:'rsi'}).set_index(close.index)
    rsi_df = rsi_df.dropna()
    return rsi_df[3:]

ibm['rsi_14'] = get_rsi(ibm['close'], 14)
ibm = ibm.dropna()
# rsi_14 has an array of indicators by day
alpha_vantage_RSI = ibm['rsi_14'][0]

#_____________________________________________Buying or selling stock



def runbot(t) :
    runner = PythonTradingBot()
    runner.buyShares(alpha_vantage_RSI)
    return

schedule.every().day.at("12:50").do(runbot, 'Running trade its 12:50')

while True:
    schedule.run_pending()
    print("waiting 1 min ", time.localtime())
    time.sleep(60)



