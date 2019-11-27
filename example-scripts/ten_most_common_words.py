fname = input('Enter a file name:')
if len(fname) == 0:
    fname = '../files/clown.txt'
fhandle = open(fname)

counts = dict()
for line in fhandle:
    line = line.strip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()

lst = sorted([(v,k) for k,v in counts.items()], reverse=True)
# previous line can be re-written like this
# for k,v in counts.items():
#     newtup = (v,k)
#     lst.append(newtup)
# lst = sorted(lst, reverse=True)

for v,k in lst[:10]:
    print(k, v)
