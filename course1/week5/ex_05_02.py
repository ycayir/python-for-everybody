min = None
max = None

while True:
    entry = input('Enter a number: ')
    if entry == 'done':
        break
    try:
        num = int(entry)
        if min is None or min > num:
            min = num
        if max is None or max < num:
            max = num
    except Exception as e:
        print('Invalid input')
        continue

print(min, max)
