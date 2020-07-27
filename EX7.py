
def Fib(arg):
    if arg<=0: 
        print("invalid") 
    elif arg==1:
        return 0
    elif arg==2:
        return 1
    else:
        return Fib(arg-1)+Fib(arg-2)
    

def FibinList(arg):
    L= []
    for i in range(1,arg+1):
        L.append(Fib(i))
    return L


print(FibinList(7))
        
