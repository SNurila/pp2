import datetime  #Import the datetime module and display the current date

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2020, 5, 17)

print(x)