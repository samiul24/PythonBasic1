# List of strings
l = ['sat', 'bat', 'cat', 'mat']

#https://realpython.com/python-map-function/
#for loop vs map python
# map() can listify the list of strings individually
test = list(map(list, l))
print(test)
