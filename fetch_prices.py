import requests
import json
import os
from datetime import datetime

# Your portfolio
HOLDINGS = [
    # Stocks
    {"symbol": "BABA", "quantity": 119},
    {"symbol": "BNTX", "quantity": 4},
    {"symbol": "NNDM", "quantity": 1300},
    {"symbol": "OTLY", "quantity": 161},
    {"symbol": "BNGO", "quantity": 1},
    {"symbol": "BMBL", "quantity": 42},
    {"symbol": "BYDDY", "quantity": 400},
    {"symbol": "CLOV", "quantity": 400},
    {"symbol": "EVEX", "quantity": 200},
    {"symbol": "EXAS", "quantity": 117},
    {"symbol": "FSLY", "quantity": 128},
    {"symbol": "HYLN", "quantity": 105},
    {"symbol": "KNDI", "quantity": 600},
    {"symbol": "LAZR", "quantity": 6},
    {"symbol": "OGN", "quantity": 1},
    {"symbol": "PYPL", "quantity": 61},
    {"symbol": "PTON", "quantity": 125},
    {"symbol": "QS", "quantity": 750},
    {"symbol": "RIVN", "quantity": 20},
    {"symbol": "SNSE", "quantity": 25},
    {"symbol": "SHOP", "quantity": 70},
    {"symbol": "TDOC", "quantity": 20},
    {"symbol": "TWLO", "quantity": 80},
    {"symbol": "TWST", "quantity": 35},
    {"symbol": "VTRS", "quantity": 153},
    {"symbol": "ADYEN.AS", "quantity": 12},
    {"symbol": "ASML.AS", "quantity": 19},
    {"symbol": "HAL.AS", "quantity": 20},
    {"symbol": "AF.PA", "quantity": 70},
    {"symbol": "ALO.PA", "quantity": 60},
    {"symbol": "BCART.BR", "quantity": 1300},
    {"symbol": "TUI1.DE", "quantity": 17},
    {"symbol": "GLPG.BR", "quantity": 50},
]

CRYPTO = [
    {"symbol": "bitcoin", "quantity": 0.064103}
]

def fetch_stock_prices():
    """Fetch stock prices using Financial Modeling Prep API"""
    api_key = os.environ.get('FMP_API_KEY', 'PYg3qNmBoOYHuRnnUGEBd32s0JtBdIIj')
    prices = {}
    
    # Fetch US stocks in batch
    us_stocks = [h['symbol'] for h in HOLDINGS if '.' not in h['symbol']]
    if us_stocks:
        symbols = ','.join(us_stocks)
        url = f"https://financialmodelingprep.com/api/v3/quote/{symbols}?apikey={api_key}"
        
        try:
            response = requests.get(url, timeout=10)
            data = response.json()
            
            if isinstance(data, list):
                for quote in data:
                    if quote.get('symbol') and quote.get('price'):
                        prices[quote['symbol']] = quote['price']
        except Exception as e:
            print(f"Error fetching US stocks: {e}")
    
    # Fetch European stocks individually
    eu_stocks = [h['symbol'] for h in HOLDINGS if '.' in h['symbol']]
    for symbol in eu_stocks:
        try:
            url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={api_key}"
            response = requests.get(url, timeout=10)
            data = response.json()
            
            if isinstance(data, list) and len(data) > 0 and data[0].get('price'):
                prices[symbol] = data[0]['price']
        except Exception as e:
            print(f"Error fetching {symbol}: {e}")
    
    return prices

def fetch_crypto_prices():
    """Fetch crypto prices using CoinGecko API"""
    prices = {}
    
    try:
        ids = ','.join([c['symbol'] for c in CRYPTO])
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
        
        response = requests.get(url, timeout=10)
        data = response.json()
        
        for crypto in CRYPTO:
            symbol = crypto['symbol']
            if symbol in data and 'usd' in data[symbol]:
                prices[symbol] = data[symbol]['usd']
    except Exception as e:
        print(f"Error fetching crypto: {e}")
    
    return prices

def main():
    print("Fetching stock prices...")
    stock_prices = fetch_stock_prices()
    
    print("Fetching crypto prices...")
    crypto_prices = fetch_crypto_prices()
    
    # Combine all prices
    all_prices = {**stock_prices, **crypto_prices}
    
    # Create output data
    output = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "prices": all_prices,
        "holdings": HOLDINGS,
        "crypto": CRYPTO
    }
    
    # Write to JSON file
    with open('prices.json', 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"Updated prices for {len(all_prices)} symbols")
    print(f"Timestamp: {output['timestamp']}")

if __name__ == "__main__":
    main()
