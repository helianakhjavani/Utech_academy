class Time:
    Hour = 0
    Minute= 0
    Second = 0
    def __init__(arg, h=0, m=0, s=0):
        arg.Hour = h
        arg.Minute = m
        arg.Second = s

        
    def __str__(arg):
        return  str(arg.Hour) + ":" + str(arg.Minute) + ":" + str(arg.Second)

    
    def __repr__(arg):
        return  str(arg.Hour) + ":" + str(arg.Minute) + ":" + str(arg.Second)
    def __add__(arg, other):
        second = arg.Second + other.Second
        minute = arg.Minute + other.Minute
        hour = arg.Hour + other.Hour
        if second >=60:
            minute += (second // 60)
            second = second%60
        if minute >=60:
            hour += (minute // 60)
            minute = minute%60           
        return Time(hour,minute,second)

    
    def __sub__(arg, other):
        argval = arg.Hour*3600 + arg.Minute*60 + arg.Second
        otherval = other.Hour*3600 + other.Minute*60 + other.Second
        if argval > otherval:
            return Time(arg.Hour - other.Hour , arg.Minute - other.Minute, arg.Second - other.Second)
        else:
            return(other.Hour - arg.Hour , other.Minute - arg.Minute, other.Second - arg.Second)
        

    def __eq__(arg, other):
        if arg.Hour == other.Hour and arg.Minute == other.Minute and arg.Second == other.Second:
            return "True"
        else:
            return "False"

        
    def __gt__(arg, other):
        
        argval = arg.Hour*3600 + arg.Minute*60 + arg.Second
        otherval = other.Hour*3600 + other.Minute*60 + other.Second
        if argval > otherval:
            return "True"
        else:
            return "False"

    def __lt__(arg, other):
        
        argval = arg.Hour*3600 + arg.Minute*60 + arg.Second
        otherval = other.Hour*3600 + other.Minute*60 + other.Second
        if argval > otherval:
            return "False"
        else:
            return "True"
        


