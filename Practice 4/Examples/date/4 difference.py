from datetime import datetime
x = datetime.now()
y = datetime(2020 , 5 , 17)
print(f"Difference between time x and y in seconds equal: {int((x-y).total_seconds())}")
