year = int(input("enter the year"))
month = int(input("enter the month"))
day = int(input("enter the day"))
if (year % 400 == 0):
    result = True
elif (year % 100 ==0):
    result = False
elif (year % 4 ==0):
    result = True
else :
    result = False

montharray = [31,28,31,30,31,30,31,31,30,30,30,31]

if result == True :
    montharray[1] = 29

caldays = sum(montharray[: month]) + day
print(caldays , "passed from begining of the year")
