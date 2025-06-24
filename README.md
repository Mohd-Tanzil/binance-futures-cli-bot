# Binance Futures CLI Trading Bot 💹

A lightweight command-line bot for placing and managing Binance Futures Testnet orders.  
Built in Python, this tool allows users to trade directly via the terminal using Binance Futures API.

---

## 🚀 Features Implemented

 Place orders (MARKET, LIMIT, STOP_MARKET, TAKE_PROFIT_MARKET)  
 Cancel all open orders for a given symbol  
 Track order status by order ID  
 Smart prompts for user inputs  
 CLI-based menu navigation  
 Secure API handling via `.gitignore`  
 Clean and readable output format  
✅ Bonus features implemented that were **not required**:
- Order Status Tracker
- Cancel Open Orders
- Clean UI enhancements with menu flow

---

## ⚙️ Tech Stack

- Python 3
- `python-binance` library
- Binance Futures Testnet
- Logging & error handling
- Git version control

---

## 🧠 How It Works

1. Clone the repo:
   ```bash
   git clone https://github.com/Mohd-Tanzil/binance-futures-cli-bot.git
   cd binance-futures-cli-bot
   ```
2. Install dependencies:
   ```bash
   pip install python-binance
   ```
3. Add your API credentials:
   ```bash
   API_KEY = "your_api_key_here"
   API_SECRET = "your_api_secret_here"
   ```
4. Run the bot:
   ```bash
   python bot.py
   ```
 ## Sample CLI Demo
   ```bash
   📈 Welcome to Binance Futures Testnet CLI Bot

   Menu:
   1. Place Order
   2. Cancel Open Orders
   3. Track Order Status
   4. Exit
   ```
## 🖼️ Screenshots

### 🟢 Bot Starting View  
![Bot Starting View](screenshots/Screenshot%202025-06-24%20184027.png)

### ⚙️ Bot Working Status  
![Bot Working Status](screenshots/Screenshot%202025-06-24%20184147.png)

### ✅ Execution Status  
![Execution Status](screenshots/Screenshot%202025-06-24%20184308.png)
