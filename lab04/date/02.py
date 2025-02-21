from datetime import datetime, timedelta
today = datetime.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print(yesterday.strftime('%Y-%m-%d'))
print(today.strftime('%Y-%m-%d'))
print(tomorrow.strftime('%Y-%m-%d'))

