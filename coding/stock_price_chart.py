# filename: stock_price_chart.py
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

# Define the ticker symbols for NVDA and TESLA
tickers = ["NVDA", "TSLA"]

# Retrieve the historical stock price data
data = yf.download(tickers, start="2021-01-01", end="2021-12-31")

# Filter the data for year-to-date (YTD)
start_date = pd.Timestamp('2021-01-01')
end_date = pd.Timestamp.now().normalize()
ytd_data = data.loc[start_date:end_date, "Close"]

# Convert DataFrame to numpy array
ytd_data_np = ytd_data.to_numpy()

# Plot the chart
plt.figure(figsize=(10, 6))
plt.plot(ytd_data.index, ytd_data_np[:, 0], label="NVDA")
plt.plot(ytd_data.index, ytd_data_np[:, 1], label="TESLA")
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.title("NVDA and TESLA Stock Price Change YTD")
plt.legend()
plt.grid(True)
plt.show()