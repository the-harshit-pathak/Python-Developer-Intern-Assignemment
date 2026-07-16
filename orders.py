from .validators import validate_order
from .logging_config import logger
class OrderManager:
    def __init__(self,client): self.client=client
    def place_order(self,symbol,side,order_type,quantity,price=None):
        validate_order(symbol,side,order_type,quantity,price)
        try:
            if order_type.upper()=="MARKET":
                order=self.client.futures_create_order(symbol=symbol,side=side,type="MARKET",quantity=quantity)
            else:
                order=self.client.futures_create_order(symbol=symbol,side=side,type="LIMIT",quantity=quantity,price=price,timeInForce="GTC")
            logger.info(order)
            return order
        except Exception as e:
            logger.error(str(e)); raise
