b = input().lower()
c = {}
for i in b:
    if i in c: c[i] += 1
    else: c[i] = 1

ma = max(c.values())

if list(c.values()).count(ma) != 1: print('?')
else:
    for i in c:
        if c[i] == ma: print(i.upper())