# Validating budget and expenses
expenses = [100, 250, 50, 1500, 300]
budget = 1000
total = 0

for item in expenses:
    if total + item > budget:
        print("Budget exceeded! Stopping here.")
        break
    total += item
    print(f"Current total: ${total}")
