# dir() function returns a list of attributes and methods of any object
x = dict()
print('<<< DICTIONARY >>>')
print(dir(x), '\n')

y = list()
print('<<< LIST >>>')
print(dir(y), '\n')

z = tuple()
print('<<< TUPLES >>>')
print(dir(z), '\n')

# sorted() function
d = {'a':10, 'c': 3, 'b':20}
print(d.items())
print(sorted(d.items())) # returns key order sorted
