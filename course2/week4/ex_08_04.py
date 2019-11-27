fh = open('../files/romeo.txt')

t = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        # print('debug:', word)
        if word not in t:
            t.append(word)

t.sort()
print(t)
