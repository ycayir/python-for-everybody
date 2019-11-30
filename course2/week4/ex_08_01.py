def chop(t):
    if t != None and len(t) >= 2:
        length = len(t)
        del t[0]
        del t[length-2]
    return None

def middle(t):
    if t != None and len(t) >= 3:
        length = len(t)
        return t[1:length-1]
    return None

t = [1,2,3,4,5,6]
print('t:', t)
print('chop:', chop(t))
print('t:', t)
print('middle:', middle(t))
