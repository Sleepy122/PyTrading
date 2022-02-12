from alpaca_trade_api.stream import Stream
from alpaca_trade_api.common import URL

async def trade_callback(t):
    print('trade', t)


async def quote_callback(q):
    print('quote', q)


# Initiate Class Instance
stream = Stream("6471159df356db467b5301ca1598859f",
                "484202e887c2d3d382cf676830bdb406309b6a0a",
                base_url=URL('https://paper-api.alpaca.markets'),
                data_feed='iex')  # <- replace to SIP if you have PRO subscription
# subscribing to event

streamOutput = stream.subscribe_quotes(quote_callback, 'IBM')
stream.subscribe_trades(trade_callback, 'AAPL')




stream.run()