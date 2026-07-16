from binance.client import Client
from .logging_config import logger
TESTNET_URL="https://testnet.binancefuture.com"
class BinanceClient:
    def __init__(self, api_key, api_secret):
        self.client=Client(api_key, api_secret)
        self.client.FUTURES_URL=TESTNET_URL
        logger.info("Connected to Binance Futures Testnet")
    def get_client(self):
        return self.client
