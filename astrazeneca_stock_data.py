import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, name):
    # Fetch stock data
    stock_data = yf.Ticker(ticker)
    hist = stock_data.history(period="1mo")
    hist["Name"] = name
    return hist[["Name", "Open", "High", "Low", "Close", "Volume"]]

def main():
    # Fetch data for AstraZeneca and Legal & General
    azn_data = fetch_stock_data("AZN", "AstraZeneca")
    lgen_data = fetch_stock_data("LGEN.L", "Legal & General")

    # Combine data into one DataFrame
    combined_data = pd.concat([azn_data, lgen_data])

    # Print the combined data as a table
    print("Stock Data (Last Month):")
    print(combined_data)

if __name__ == "__main__":
    main()