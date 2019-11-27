t1 = ['a', 'b', 'z', 'f']
t2 = ['d', 'f', 'e', 'y', 'k']

print('t1:', t1)
print('t2:', t2)

t3 = t1.append('j')
print("\nt3 = t1.append('j')")
print('t1:', t1)
print('t3:', t3)

t1.extend(t2)
print('\nt1.extend(t2)')
print('t1:', t1)
print('t2:', t2)

t1.sort()
print('\nt1.sort()')
print('t1:', t1)
print('\npop(3):', t1.pop(3))
print('t1:', t1)

del t1[2]
print("\ndel t1[2]")
print('t1:', t1)

del t1[1:4]
print("\ndel t1[1:4]")
print('t1:', t1)

t2.remove('e')
print("\nt2.remove('e')")
print('t2:', t2)
