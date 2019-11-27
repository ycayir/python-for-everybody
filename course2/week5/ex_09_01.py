# Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
#
# Write a program that reads the words in words.txt and stores them as
# keys in a dictionary. It doesn’t matter what the values are. Then you
# can use the in operator as a fast way to check whether a string is in the
# dictionary.

handle = open('../files/words.txt')

dwords = dict()
for line in handle:
    line = line.strip()
    # print('debug:', line)
    words = line.split()
    for word in words:
        dwords[word] = word

print('Does words exist?')
print('or:', 'or' in dwords.keys())
print('goose:', 'goose' in dwords.keys())
