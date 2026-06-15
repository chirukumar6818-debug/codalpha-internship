# Simple Stock Portfolio Tracker

# Dictionary containing stock names and their prices
stock_prices = {
    "AAPL": 180,   # Apple
    "GOOGL": 2800, # Alphabet
    "TSLA": 250,   # Tesla
    "MSFT": 320    # Microsoft
}

# Dictionary containing the number of shares owned
portfolio = {
    "AAPL": 10,
    "GOOGL": 2,
    "TSLA": 5,
    "MSFT": 8
}

# Variable to store total investment value
total_investment = 0

print("Stock Portfolio Summary")
print("-" * 30)

# Calculate investment for each stock
for stock, shares in portfolio.items():
    price = stock_prices[stock]
    investment = price * shares
    total_investment += investment

    print(f"{stock}: {shares} shares × ${price} = ${investment}")

# Display total investment value
print("-" * 30)
print(f"Total Investment Value: ${total_investment}")