from datetime import date, timedelta


today = date.today()
yesterday = date.today() - timedelta(1)

print(today.strftime('%Y-%m-%d'))
print(yesterday.strftime('%Y-%m-%d'))
