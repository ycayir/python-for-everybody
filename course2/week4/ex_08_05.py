fh = open('../files/mbox-short.txt')

count = 0
for line in fh:
    line = line.rstrip()   # Remove white spaces
    words = line.split()
    # Guardian in a compound statement
    if len(words) < 2 or not line.startswith('From '): continue
    count = count + 1
    print(words[1])

print('There were %d lines in the file with From as the first word' % count)
