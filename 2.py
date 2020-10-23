a = ['a', 'b', 'c']
b = ['a', 'b', 'd']
c = []
for i in a:
    if i in b:
        c.append(i)

print(c)