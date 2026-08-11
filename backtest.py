import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download("AAPL", start="2019-01-01", end="2024-01-01")

#Moving Average columns
data["MA20"] = data["Close"].rolling(window=20).mean()
data["MA50"] = data["Close"].rolling(window=50).mean()

#Plot Moving Averages
plt.plot(data["Close"], label="Close")
plt.plot(data["MA20"], label="MA20")
plt.plot(data["MA50"], label="MA50")
plt.legend()
plt.savefig("output/ma_chart.png")