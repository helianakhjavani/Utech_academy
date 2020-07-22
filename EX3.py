year = int(input("enter the year"))
if (year % 400 == 0):
    result = True
elif (year % 100 ==0):
    result = False
elif (year % 4 ==0):
    result = True
else :
    result = False

if result == True:
    print(year, "is a Leap yeat")
else :
    print(year, "is not a Leap yeat")
   

