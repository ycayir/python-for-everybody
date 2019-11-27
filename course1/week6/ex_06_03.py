def count(letter, word):
    counter = 0;
    for char in word:
        if (char == letter):
            counter = counter + 1
    return counter


word = 'banana'

print(count('a', word))
