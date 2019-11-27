# 7.2 Write a program that prompts for a file name, then opens that file and
# reads through the file, looking for lines of the form:
#
#    X-DSPAM-Confidence:    0.8475
#
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
#
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.

fname = input('Enter file name: ')
fh = open(fname, 'r')

spam_line_count = 0
total = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    spam_line_count = spam_line_count + 1
    column_index = line.find(':')
    value = line[column_index + 2:]
    fvalue = float(value)
    total = total + fvalue

if spam_line_count != 0:
    avg = total / spam_line_count
else:
    avg = total

print('Average spam confidence: %.12f' % avg)
