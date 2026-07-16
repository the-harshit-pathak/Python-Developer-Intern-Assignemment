import argparse
from bot.client import BinanceClient
from bot.orders import OrderManager
API_KEY="YOUR_API_KEY"
API_SECRET="YOUR_SECRET_KEY"
p=argparse.ArgumentParser()
p.add_argument("--symbol",required=True)
p.add_argument("--side",choices=["BUY","SELL"],required=True)
p.add_argument("--type",choices=["MARKET","LIMIT"],required=True)
p.add_argument("--quantity",type=float,required=True)
p.add_argument("--price",type=float)
a=p.parse_args()
client=BinanceClient(API_KEY,API_SECRET).get_client()
resp=OrderManager(client).place_order(a.symbol,a.side,a.type,a.quantity,a.price)
print(resp)
