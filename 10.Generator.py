def myFunc(x):
    for i in range(x):
        print(i)
        yield i
        len(i)

n = myFunc(5)
next(n)
next(n)
next(n)
next(n)
next(n)
next(n)
next(n)