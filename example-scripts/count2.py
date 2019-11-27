import string

handle = open('../files/romeo-full.txt')

counts = dict()
for line in handle:
    line = line.strip()
    # print('original:\t', line)
    line = line.translate(line.maketrans('','',string.punctuation))
    # print('translated:\t', line)
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# for k,v in counts.items():
#     print(k,v)
print(counts)
