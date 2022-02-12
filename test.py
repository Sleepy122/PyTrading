import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import REST, TimeFrame

ALPACA_BASE_URL = "https://api.alpaca.markets/paper-api.alpaca.markets";


class PythonTradingBot :
    def __init__(self) :
        self.alpaca = tradeapi.REST("PKDA6OSQVESW7FIH53SA","XXCSnmOr3hdOKkCMIe9k1PtWvKxIC4Dp2OpzfnuK", ALPACA_BASE_URL,api_version="v2")

    def run(self) :
        print("testing getting Microsoft Trade")
        bar_group = self.alpaca.get_barset("QQQ", "day", limit=5)
        for bar in bar_group:
            print(bar)
        print("Got Microsoft Trade?")

runner = PythonTradingBot()
runner.run()

# api = REST("6471159df356db467b5301ca1598859f","484202e887c2d3d382cf676830bdb406309b6a0a", ALPACA_BASE_URL,api_version="v2")
# def process_bar(bar):
#     # process bar
#     print(bar)

# bar_iter = api.alpaca.ge("AAPL", TimeFrame.Hour, "2021-06-08", "2021-06-08", adjustment='raw')
# for bar in bar_iter:
#     process_bar(bar)
