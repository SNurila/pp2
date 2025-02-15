from datetime import *
x = datetime.now()

ago = x - timedelta(days=5)
print(ago.strftime("%a"))
