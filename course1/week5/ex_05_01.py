count = 0
total = 0
avg = 0

while True:
    entry = input('Enter a number: ')
    if entry == 'done':
        break
    try:
        total = int(entry) + total
    except Exception as e:
        print('Invalid input')
        continue
    count = count + 1

if count != 0:
    avg = total / count

print(total, count, avg)
