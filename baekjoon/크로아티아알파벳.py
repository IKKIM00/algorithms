s = str(input())

cro_alph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in cro_alph:
    while i in s:
        s = s.replace(i, '!')
print(len(s))
