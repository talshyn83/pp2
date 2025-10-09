from datetime import datetime, timedelta

current_date = datetime.today()
days = int(input())
new_date = current_date - timedelta(days)

print(current_date.strftime("%Y-%m-%d"))
print(new_date.strftime("%Y-%m-%d"))