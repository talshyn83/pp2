from datetime import datetime

date1 = datetime(2025, 2, 15, 14, 30, 0) 
date2 = datetime(2025, 2, 15, 16, 45, 30) 

time_difference = date2 - date1

seconds_difference = time_difference.total_seconds()

print("Difference in seconds:", seconds_difference)