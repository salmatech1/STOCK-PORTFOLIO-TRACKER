
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "MSFT": 320,
    "AMZN": 125
}

portfolio = {}
n = int(input("📈 How many different stocks do you want to add? "))

for _ in range(n):
    stock = input("🔤 Enter stock symbol (e.g., AAPL): ").upper()
    if stock not in stock_prices:
        print("⚠️ We don't have data for this stock.")
        continue
    quantity = int(input(f"🔢 How many shares of {stock} do you own? "))
    portfolio[stock] = quantity

total_value = 0

print("\n📊 Your Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"• {stock}: {qty} shares × ${price} = ${value}")

print(f"\n💰 Total Investment Value: ${total_value}")

save = input("📝 Do you want to save this summary to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Your Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} × ${price} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}")
    print("✅ Portfolio saved to 'portfolio_summary.txt'")
