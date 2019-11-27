# create empty ditionary
# ages = dist()

# curly brackets represent dictionary
ages = {'chuck':42, 'yalcin': 43, 'ayse': 35}
print(ages)

print('number of items in the dictionary:', len(ages))

print('chuck' in  ages)

# print keys
print(list(ages))
print(ages.keys())

# print values
print(ages.values())

# print list of items (tuples)
print(ages.items())

# items() in for loop returns two iteration variables: key, value
for k,v in ages.items():
    print(k, v)

# get individual values
print(ages.get('yalcin', 0))
print(ages.get('steve', 0))
