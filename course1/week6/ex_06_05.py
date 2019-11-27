str = 'X-DSPAM-Confidence:0.8475'

colon_index = str.find(':')

c = str[colon_index+1:]
fc = float(c)

print(fc)
