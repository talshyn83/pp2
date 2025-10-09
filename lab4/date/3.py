from datetime import datetime

current_datetime = datetime.now()

clean_datetime = current_datetime.replace(microsecond=0)

print(current_datetime)
print(clean_datetime)