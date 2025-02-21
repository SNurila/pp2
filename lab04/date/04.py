from datetime import datetime

date1 = datetime(2024, 2, 20)
date2 = datetime(2024, 2, 25)

difference = date2 - date1
print(difference.total_seconds())