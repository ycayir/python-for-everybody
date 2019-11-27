# 5.2 Write a program that repeatedly prompts
# a user for integer numbers until the user
# enters 'done'. Once 'done' is entered, print out
# the largest and smallest of the numbers.
# If the user enters anything other than a valid
# number catch it with a try/except and put out an
# appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

min = None
max = None

while True:
    entry = input('Enter a number: ')
    if entry == 'done': break
    try:
        num = int(entry)
        if min is None or min > num:
            min = num
        if max is None or max < num:
            max = num
    except Exception as e:
        print('Invalid input')
        continue

print('Maximum is', max)
print('Minimum is', min)
