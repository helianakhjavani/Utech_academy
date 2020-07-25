
def fib(arg):
    if arg == 0:
        return 0
    elif arg ==1:
        return 1
    else:
        return (fib(arg-1) + fib(arg-2))

print(fib(7))
