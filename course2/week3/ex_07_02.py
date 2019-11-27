fname = input('Enter a file name: ')
fhandle = open(fname, 'r')

line_count = 0
sum = 0
for line in fhandle:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        line_count = line_count + 1
        column_index = line.find(':')
        value = line[column_index + 2:]
        fvalue = float(value)
        sum = sum + fvalue

if line_count != 0:
    avg = sum / line_count
else:
    avg = sum

# print('Average spam confidence: %.8f' % avg) # 8 decimal point precision
print('Average spam confidence:', avg)
