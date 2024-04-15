#program to convert year, months, weeks, days, hours, minutes, seconds.
# year = int
# days  = int(input("Enter the days : "))
# hours  = int(input("Enter the days : ")*3600)
# minutes  = int(input("Enter the days : ") *60)
# seconds  = int(input("Enter the days : "))
# time = days + hours + minutes + seconds
# print("Total seconds is ", time)

days = int ( input ('enter number of days: ') )
year = days / 365
days = days % 365
month = days // 30
days = days % 30
week = days // 7
days = days % 7
print(year, 'Year', month, 'Month', week, 'Week', days, 'Days')