from typing_extensions import Self
import alpaca_trade_api as tradeapi
import secretsConfig as secrets
import Utilities.AlpacaUtilites as AlpacaU
import Utilities.AlphaVantageUtilities as AlphaU
import pandas as pd
import matplotlib.pyplot as plt
import requests
import numpy as np
from math import floor
from termcolor import colored as cl
import time

for stock in secrets.STOCK_LIST:
    rsiIndicator = AlphaU.get_rsi(stock)
    AlpacaU.Alpaca().buyShares(rsiIndicator,stock)
#    return

# schedule.every().day.at("09:00").do(runbot, 'Running trade its 09:00')

#while True:
#    schedule.run_pending()
#    print("waiting 1 min ", time.localtime())
#    time.sleep(60)



