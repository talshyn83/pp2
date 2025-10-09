from datetime import datetime, timedelta

current_date = datetime.today()
yesterday = current_date - timedelta(days=1)
today = datetime.today()
tomorrow = current_date + timedelta(days=1)

print(yesterday.strftime("%Y-%m-%d"))
print(today.strftime("%Y-%m-%d"))
print(tomorrow.strftime("%Y-%m-%d"))