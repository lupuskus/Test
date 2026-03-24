import yfinance as yf

def fetch_astrazeneca_stock_data():
    # Download AstraZeneca stock data
    stock_data = yf.Ticker("AZN")
    hist = stock_data.history(period="1mo")

    print("AstraZeneca Stock Data (Last Month):")
    print(hist[["Open", "High", "Low", "Close", "Volume"]])

if __name__ == "__main__":
    fetch_astrazeneca_stock_data()