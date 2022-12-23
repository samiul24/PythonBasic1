n = [1,2,3,4,5]
m = [6,7,8,9,10]

def myFunc(x,y):
    return x+y

x = map(lambda x,y : myFunc(x,y), n,m)
print(x)
print(list(x))