# Exercise 5: This program records the domain name (instead of the
# address) where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program, print
# out the contents of your dictionary.
# python schoolcount.py
#
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

handle = open('../../files/mbox-short.txt')

counts = dict()

for line in handle:
    line = line.strip()
    if not line.startswith('From'): continue
    words = line.split()
    if len(words) < 2: continue
    email = words[1]
    emailParts = email.split('@')
    domain = emailParts[1]
    counts[domain] = counts.get(domain, 0) + 1

print(counts)
