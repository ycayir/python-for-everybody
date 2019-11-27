text = "X-DSPAM-Confidence:    0.8475";

index_of_colon = text.find(':')
number = text[index_of_colon+1:]

fnumber = float(number)
print(fnumber)
