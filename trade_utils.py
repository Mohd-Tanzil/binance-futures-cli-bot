from binance.client import Client
from binance.enums import *
import logging

logging.basicConfig(filename='log.txt', level=logging.INFO)

def init_client(api_key, api_secret):
    return Client(api_key, api_secret, testnet=True)

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        if order_type == 'MARKET':
            order = client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side == 'buy' else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
        elif order_type == 'LIMIT':
            order = client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side == 'buy' else SIDE_SELL,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                price=price,
                quantity=quantity
            )
        elif order_type == 'STOP_MARKET':
            order = client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side == 'buy' else SIDE_SELL,
                type=ORDER_TYPE_STOP_MARKET,
                stopPrice=price,
                quantity=quantity
            )
        else:
            return "❌ Unsupported order type"
        logging.info(f"Order response: {order}")
        return f"✅ Order placed: {order['orderId']} | Status: {order['status']}"
    except Exception as e:
        logging.error(f"Error placing order: {e}")
        return f"❌ Error placing order: {e}"
