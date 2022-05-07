from typing_extensions import Self
import alpaca_trade_api as tradeapi
import secretsConfig as secrets
import pandas as pd
import matplotlib.pyplot as plt
import requests
import numpy as np
from math import floor
from termcolor import colored as cl
import time




ALPACA_BASE_URL = "https://paper-api.alpaca.markets"

class Alpaca :
    def __init__(self) :
        self.alpaca = tradeapi.REST(secrets.ALPACA_API_KEY,secrets.ALPACA_API_SECRET, ALPACA_BASE_URL,api_version="v2")

    def buyShares(self,rsiIndicator,currentStock) :
        print("the rsi indicator for "+currentStock+" was : ",rsiIndicator )
        if(rsiIndicator < 30):
            order_confirmation = self.alpaca.submit_order(
                symbol=currentStock,
                side='buy',
                type='market',
                qty='100',
                time_in_force='day',
            )
            print(order_confirmation)
            print(currentStock + " was bought")
        elif(rsiIndicator > 70) :
            #Test this code
            self.alpaca.cancel_all_orders()
            try:
                self.alpaca.close_position(currentStock)
            except:
                print("We didn't own " + currentStock)
            
            print (currentStock + " was sold")
        else:
            print(currentStock + " was held")