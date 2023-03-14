import ccxt

exchanges = ['kucoin', 'binance', 'huobi', 'okex', 'bybit', 'bitget', 'bitfinex']
symbol = 'BTC/USDT'
threshold = 0.001

# Initialize the exchanges
exchange_objs = [getattr(ccxt, e)() for e in exchanges]

# Fetch the ticker prices for USDT futures on each exchange
tickers = [exchange.fetch_ticker(symbol) for exchange in exchange_objs]

# Find the minimum ask price and maximum bid price across all exchanges
min_ask = min([ticker['ask'] for ticker in tickers])
max_bid = max([ticker['bid'] for ticker in tickers])

# Calculate the potential profit from arbitrage
spread = max_bid - min_ask
profit = spread / min_ask

# Check if the potential profit exceeds the threshold
if profit > threshold:
    print(f"Arbitrage opportunity found! Profit: {profit:.2%}")
else:
    print("No arbitrage opportunity found.")
