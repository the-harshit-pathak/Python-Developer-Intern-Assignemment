def validate_order(symbol,side,order_type,quantity,price=None):
    side=side.upper(); order_type=order_type.upper()
    if side not in ["BUY","SELL"]: raise ValueError("Invalid side")
    if order_type not in ["MARKET","LIMIT"]: raise ValueError("Invalid order type")
    if quantity<=0: raise ValueError("Quantity must be >0")
    if order_type=="LIMIT" and (price is None or price<=0):
        raise ValueError("Price required for LIMIT")
