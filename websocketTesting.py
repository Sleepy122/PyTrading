import logging
import threading
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor
from alpaca_trade_api.stream import Stream
from alpaca_trade_api.common import URL

import secretsConfig as secrets

async def print_trade(t):
    print('trade', t)


async def print_quote(q):
    print('quote', q)


async def print_bar(bar):
    print('bar', bar)


# def consumer_thread():
# global conn
conn = Stream(secrets.ALPACA_API_KEY,
                secrets.ALPACA_API_SECRET,
                base_url=URL('https://paper-api.alpaca.markets'),
                data_feed='iex')

conn.subscribe_bars(print_quote, 'AAPL')
conn.run()


# if __name__ == '__main__':
#     logging.basicConfig(format='%(asctime)s  %(levelname)s %(message)s',
#                         level=logging.INFO)

#     pool = ThreadPoolExecutor(1)

#     while 1:
#         try:
#             pool.submit(consumer_thread)
#         except KeyboardInterrupt:
#             print("Interrupted execution by user")
#             conn.stop()
#             exit(0)
#         except Exception as e:
#             print("You goe an exception: {} during execution. continue "
#                   "execution.".format(e))
#             # let the execution continue
#             pass
