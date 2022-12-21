def myFunc(a, b):
    return f"{a}, {b}"

x = map(myFunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

print(list(x))