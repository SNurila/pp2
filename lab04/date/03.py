from datetime import datetime
now = datetime.now()
x = now.replace(microsecond=0)
print(x)
