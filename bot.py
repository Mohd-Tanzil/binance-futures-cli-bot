import logging
from binance.client import Client
from binance.enums import *
from keys import API_KEY, API_SECRET

# Setup logging
logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
client = Client(API_KEY, API_SECRET, testnet=True)

def get_price(order, order_type):
    import time
    if order_type in [ORDER_TYPE_MARKET, "STOP_MARKET", "TAKE_PROFIT_MARKET"]:
        time.sleep(1)  # Short delay to let trade execution happen
        trades = client.futures_account_trades(symbol=order['symbol'])
        for t in reversed(trades):
            if str(t['orderId']) == str(order['orderId']):
                return t['price']
        return "N/A"
    else:
        return order.get('price', 'N/A')


def track_order(symbol, order_id):
    try:
        status = client.futures_get_order(symbol=symbol, orderId=order_id)
        print("\n📊 Order Status Tracker")
        print(f"🔸 Symbol: {status['symbol']}")
        print(f"🔸 Order ID: {status['orderId']}")
        print(f"🔸 Status: {status['status']}")
        print(f"🔸 Filled Qty: {status['executedQty']}")
        print(f"🔸 Avg Price: {status.get('avgFillPrice', 'N/A')}")
    except Exception as e:
        print(f"❌ Error fetching order status: {e}")

def cancel_open_orders(symbol):
    try:
        client.futures_cancel_all_open_orders(symbol=symbol)
        print(f"🚫 All open orders for {symbol} have been cancelled.")
    except Exception as e:
        print(f"❌ Error cancelling open orders: {e}")

def place_order():
    symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
    side = input("Buy or Sell? ").upper()
    order_type = input("Order type (MARKET / LIMIT / STOP_MARKET / TAKE_PROFIT_MARKET): ").upper()
    quantity = input("Quantity: ")

    try:
        params = {
            "symbol": symbol,
            "side": SIDE_BUY if side == "BUY" else SIDE_SELL,
            "quantity": quantity,
        }

        if order_type == "MARKET":
            params["type"] = ORDER_TYPE_MARKET

        elif order_type == "LIMIT":
            price = input("Enter price: ")
            params["price"] = price
            params["timeInForce"] = TIME_IN_FORCE_GTC
            params["type"] = ORDER_TYPE_LIMIT

        elif order_type == "STOP":
           stop_price = input("Enter stop price: ")
           price = input("Enter price: ")
           params["stopPrice"] = stop_price
           params["price"] = price
           params["timeInForce"] = TIME_IN_FORCE_GTC
           params["type"] = "STOP_MARKET"


        elif order_type in ["STOP_MARKET", "TAKE_PROFIT_MARKET"]:
            stop_price = input("Enter stop price: ")
            params["stopPrice"] = stop_price
            params["type"] = order_type
            params["timeInForce"] = TIME_IN_FORCE_GTC



        order = client.futures_create_order(**params)
        filled_price = get_price(order, params["type"])

        print("\n✅ Order placed successfully!")
        print(f"🔹 Symbol: {order['symbol']}")
        print(f"🔹 Side: {order['side']}")
        print(f"🔹 Type: {order['type']}")
        print(f"🔹 Quantity: {float(order['origQty']):.2f}")
        print(f"🔹 Price: {filled_price}")
        print(f"🔹 Order ID: {order['orderId']}")
        print(f"🔹 Status: {order['status']}")

        return symbol, order['orderId']

    except Exception as e:
        print(f"❌ Error placing order: {e}")
        return None, None

def main():
    while True:
        print("\n📈 Welcome to Binance Futures Testnet CLI Bot")
        print("\nMenu:")
        print("1. Place Order")
        print("2. Cancel Open Orders")
        print("3. Track Order Status")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            symbol, order_id = place_order()
        elif choice == "2":
            symbol = input("Enter symbol to cancel all open orders (e.g. BTCUSDT): ").upper()
            cancel_open_orders(symbol)
        elif choice == "3":
            symbol = input("Enter symbol of the order: ").upper()
            order_id = input("Enter Order ID to track: ")
            track_order(symbol, order_id)
        elif choice == "4":
            print("👋 Exiting bot. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
