
import ccxt
import tkinter as tk
from tkinter import messagebox
import time

exchange = ccxt.binance({
    'apiKey': 'abrakadabraka',
    'secret': 'phonenahellohello',
    'enableRateLimit': True,
})

symbol = 'BTC/USDT'

def get_price():
    try:
        ticker = exchange.fetch_ticker(symbol)
        return ticker['last']
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch price: {str(e)}")
        return None

def get_balance(asset):
    try:
        balance = exchange.fetch_balance()
        return balance['free'].get(asset, 0)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch balance: {str(e)}")
        return 0

def buy(amount):
    try:
        price = get_price()
        if price is None:
            return
        order = exchange.create_market_buy_order(symbol, amount)
        messagebox.showinfo("Success", f"Bought {amount} BTC at {price} USDT")
    except Exception as e:
        messagebox.showerror("Error", f"Buy failed: {str(e)}")

def sell(amount):
    try:
        price = get_price()
        if price is None:
            return
        order = exchange.create_market_sell_order(symbol, amount)
        messagebox.showinfo("Success", f"Sold {amount} BTC at {price} USDT")
    except Exception as e:
        messagebox.showerror("Error", f"Sell failed: {str(e)}")

def auto_trade():
    while True:
        price = get_price()
        if price is None:
            time.sleep(60)
            continue
        
        btc_balance = get_balance('BTC')
        usdt_balance = get_balance('USDT')
        
       
        if price < 50000 and usdt_balance > 100:
            buy_amount = 100 / price  
            buy(buy_amount)
        elif price > 60000 and btc_balance > 0.001:
            sell(0.001)  # Sell 0.001 BTC
        
        time.sleep(60)  # Check every minute

# UI Setup
root = tk.Tk()
root.title("Bitcoin Trading Bot")

# Labels
price_label = tk.Label(root, text="Current Price: Loading...")
price_label.pack()

btc_balance_label = tk.Label(root, text="BTC Balance: Loading...")
btc_balance_label.pack()

usdt_balance_label = tk.Label(root, text="USDT Balance: Loading...")
usdt_balance_label.pack()

# Update function for labels
def update_labels():
    price = get_price()
    if price:
        price_label.config(text=f"Current Price: {price} USDT")
    
    btc_balance = get_balance('BTC')
    btc_balance_label.config(text=f"BTC Balance: {btc_balance}")
    
    usdt_balance = get_balance('USDT')
    usdt_balance_label.config(text=f"USDT Balance: {usdt_balance}")
    
    root.after(10000, update_labels)  

# Buttons
update_button = tk.Button(root, text="Update Balances", command=update_labels)
update_button.pack()

amount_entry = tk.Entry(root)
amount_entry.pack()
amount_entry.insert(0, "0.001")  # Default amount

buy_button = tk.Button(root, text="Buy BTC", command=lambda: buy(float(amount_entry.get())))
buy_button.pack()

sell_button = tk.Button(root, text="Sell BTC", command=lambda: sell(float(amount_entry.get())))
sell_button.pack()

# Start auto trading in background (comment out if not needed)
# import threading
# threading.Thread(target=auto_trade, daemon=True).start()

# Initial update
update_labels()

root.mainloop()
