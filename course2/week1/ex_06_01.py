# Exercise 1: Write a while loop that starts at the last character in the
# string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.

fruit = 'banana'

index = len(fruit) - 1
while index >= 0:
    print(fruit[index])
    index = index - 1
