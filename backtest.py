import yfinance as yf

data = yf.download("AAPL", start="2019-01-01", end="2024-01-01")

#Moving Average columns
data["MA20"] = data["Close"].rolling(window=20).mean()
data["MA50"] = data["Close"].rolling(window=50).mean()