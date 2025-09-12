import datetime

now = datetime.datetime.now()
print("Now:", now)                # 2025-09-12 16:25:47.123456
print("Today:", datetime.date.today())  # 2025-09-12


# Extracting components
birthday = datetime.date(2003, 5, 15)   # (year, month, day)
print("Birthday:", birthday)

custom_time = datetime.time(14, 30, 45)  # (hour, minute, second)
print("Custom time:", custom_time)


# Current date and time
now = datetime.datetime.now()

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
