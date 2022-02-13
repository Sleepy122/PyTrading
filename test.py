import alpaca_trade_api as tradeapi
import secretsConfig as secrets



ALPACA_BASE_URL = "https://api.alpaca.markets/paper-api.alpaca.markets";


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

runner = PythonTradingBot()
runner.run()
