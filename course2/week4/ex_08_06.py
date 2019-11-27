t = list()

while True:
    number = input('Enter a number: ')
    if number == 'done': break
    try:
        number = float(number)
    except:
        print('%s is not a number. Try again!' % number)
        continue
    t.append(number)

if len(t) != 0:
    print('Maximum: ', max(t))
    print('Minimum: ', min(t))
else:
    print('No value entered. Play again :)')
