# Exercise 4: Add code to the above program (ex_09_03.py) to figure out who has the
# most messages in the file. After all the data has been read and the dic-
# tionary has been created, look through the dictionary using a maximum
# loop (see Chapter 5: Maximum and minimum loops) to find who has
# the most messages and print how many messages the person has.
#
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
#
# Enter a file name: mbox.txt
# zqian@umich.edu 195

handle = open('../../files/mbox-short.txt')

counts = dict()
for line in handle:
    line = line.strip()
    words = line.split()
    if len(words) < 2 or not line.startswith('From'):
        continue;
    email = words[1]
    counts[email] = counts.get(email, 0) + 1

biggestEmail = 0
biggestCount = 0
for k,v in counts.items():
    if v > biggestCount:
        biggestEmail = k
        biggestCount = v

print(biggestEmail, biggestCount)
