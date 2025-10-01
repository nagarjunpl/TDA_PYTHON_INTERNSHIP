import requests
import pandas as pd
import matplotlib.pyplot as plt

# 🔑 Replace with your Alpha Vantage API key
API_KEY = "YOUR_API_KEY"

def stock_tracker():
    # Step 1: Ask for stock symbol
    symbol = input("Enter stock symbol (e.g., AAPL, INFY, TCS): ").upper()
    
    # Step 2: Build API URL
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}&outputsize=compact"
    
    # Step 3: Fetch data
    response = requests.get(url)
    data = response.json()
    
    if "Time Series (Daily)" not in data:
        print("❌ Error fetching data. Check symbol or API limit.")
        return
    
    # Step 4: Convert to DataFrame
    daily_data = data["Time Series (Daily)"]
    df = pd.DataFrame(daily_data).T  # transpose
    df.columns = ["Open", "High", "Low", "Close", "Volume"]
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    df = df.astype(float)
    
    # Step 5: Display last 5 days
    print("\n📊 Last 5 Days Stock Data:")
    print(df.tail())
    
    # Step 6: Save to CSV
    df.to_csv(f"{symbol}_history.csv")
    print(f"\n✅ Saved stock history to {symbol}_history.csv")
    
    # Step 7: Plot closing price
    plt.figure(figsize=(10,5))
    plt.plot(df.index, df["Close"], label="Closing Price", color="blue")
    plt.title(f"{symbol} - Stock Price (Daily)")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.show()

# Run the tracker
stock_tracker()
