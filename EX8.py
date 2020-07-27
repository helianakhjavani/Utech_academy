def calday(year, month, day):
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

    caldays = sum(montharray[: month-1]) + day
    return caldays

print(calday(2020,12,5))
