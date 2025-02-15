import datetime

x = datetime.datetime.now()

print(x.strftime("%B"))  #Display the name of the month

print(x.strftime("%a")) #Weekday, short version
print(x.strftime("%A")) #Weekday, full version
print(x.strftime("%w")) #Weekday as a number 0-6, 0 is Sunday
print(x.strftime("%d")) #Day of month 01-31
print(x.strftime("%b")) #Month name, short version
print(x.strftime("%m")) #Month as a number 01-12
print(x.strftime("%y")) #Year, short version, without century
print(x.strftime("%Y")) #Year, full version
print(x.strftime("%H")) #Hour 00-23
print(x.strftime("%p")) #AM/PM
print(x.strftime("%M")) #Minute 00-59
print(x.strftime("%S")) #Second 00-59
print(x.strftime("%f")) #Microsecond 000000-999999
print(x.strftime("%j")) #Day number of year 001-366
print(x.strftime("%U")) #Week number of year, Sunday as the first day of week, 00-53
print(x.strftime("%W")) #Week number of year, Monday as the first day of week, 00-53
print(x.strftime("%c")) #Local version of date and time
print(x.strftime("%C")) #century
print(x.strftime("%x")) #Local version of date
print(x.strftime("%X")) #Local version of time
print(x.strftime("%%")) #A % character
print(x.strftime("%G")) #ISO 8601 year
print(x.strftime("%u")) #ISO 8601 weekday (1-7)
print(x.strftime("%V")) #ISO 8601 weeknumber (01-53)