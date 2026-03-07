# # Write a Python program to subtract five days from current date.
# from datetime import date, timedelta
# # Before subtract
# result = date.today()
# print(f"Currect date {result}")
# # After
# result = date.today() - timedelta(days=5)
# print(f"Subtracted five days {result}")

# # Write a Python program to print yesterday, today, tomorrow.
# from datetime import date, timedelta
# # Today
# today = date.today()
# # Yesterday
# yesterday = today - timedelta(days=1)
# # Tomorrow
# tomorrow = today + timedelta(days=1)
# print(f"Yesterday: {yesterday}")
# print(f"Today: {today}")
# print(f"Tomorrow: {tomorrow}")

# # Write a Python program to drop microseconds from datetime.
# from datetime import datetime, timedelta
# # The datetime contains year, month, day, hour, minute, second, and microsecond.
# x = datetime.now()
# print(x.strftime("%Y-%B-%d %H:%M:%S"))

# Write a Python program to calculate two date difference in seconds.
from datetime import datetime
x = datetime.now()
y = datetime(2020 , 5 , 17)
print(f"Difference between time x and y in seconds equal: {int((x-y).total_seconds())}")
