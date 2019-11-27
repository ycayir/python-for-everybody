fname = input('Enter a file name: ')
fhandle = open(fname, 'r')

for line in fhandle:
    line = line.rstrip()
    print(line.upper())
