# Applying discount to every item
prices = [10, 60, 25, 80, 15, 100]
index = 0

while index < len(prices):
    price = prices[index]
    index += 1
    if price < 50:
        continue
    discounted = price * 0.9  # 10% off
    print(f"Discounted price: ${discounted}")
