from datetime import date, timedelta
result = date.today()
print(f"Currect date {result}")
five_days_earlier = date.today() - timedelta(days=5)
print(f"Subtracted five days {five_days_earlier}")

