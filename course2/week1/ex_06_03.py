# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)
#
# Exercise 3: Encapsulate this code in a function named count, and gen-
# eralize it so that it accepts the string and the letter as arguments.

def counter(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count = count + 1
    return count

print(counter('banana', 'a'))
