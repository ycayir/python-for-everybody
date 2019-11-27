handle = open('../files/mbox-short.txt')

# create empty dictionary
histogram = dict() # key: word, value: number of occurance

for line in handle:
    line = line.strip()   # remove white charaters
    # print('debug (line):', line)
    words = line.split()
    for word in words:
        # print('debug (word):', word)
        histogram[word] = histogram.get(word, 0) + 1

bigCount = None
bigWord = None
for k,v in histogram.items():
    if bigCount is None or v > bigCount:
        bigCount = v
        bigWord = k

print(bigWord, bigCount)
