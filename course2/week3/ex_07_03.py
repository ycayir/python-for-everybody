fname = input('Enter a file name: ')
if fname == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit()

try:
    fhandle = open(fname, 'r')
except:
    print('File cannot be opened:', fname)
    exit()

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
