# Arbitrage Opportunity Finder
This is a Python script that checks for arbitrage opportunities greater than 0.1% on USDT futures across multiple cryptocurrency exchanges.

## Overview
The script fetches the ticker prices for the BTC/USDT futures contract on the following exchanges:

Kucoin
Binance
Huobi
OKX
Coinbase
Bybit
Bitget
Bitfinex
It then calculates the potential profit from arbitrage by finding the minimum ask price and maximum bid price across all exchanges, and checks if the potential profit exceeds the threshold of 0.1%.

If an arbitrage opportunity is found, the script prints out the potential profit percentage. Otherwise, it prints out a message indicating that no arbitrage opportunity was found.

## Dependencies
This project requires the following dependencies:

Python 3.7+
CCXT library (pip install ccxt)

## Usage
To run the script, simply run python arbitrage.py in the command line.

By default, the script checks for arbitrage opportunities on the BTC/USDT futures contract with a threshold of 0.1%. You can modify the symbol and threshold variables in the script to check for other symbols or adjust the threshold.

## Authors

👤 **Peter Boro**

- - GitHub: [@peterboro](https://github.com/peterboro)

## Contributing
Feel free to contribute to this project by submitting issues or pull requests.

## 📝 License

This project is [MIT](./LICENSE.file) licensed.
