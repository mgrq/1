a = ['a', 'b', 'c']
b = ['a', 'b', 'd']
c = []
for i in a:
    if i in b:
        c.append(i)

print(c)

dic = {'name': 'vasya', 'old': '25'}
print(dic.get('old'))

# 3 задача
x = {'a': 4, 'b': 6, 't': 9, 'f': 2, 'i': 7}
x_sort = list(x.items())
x_sort.sort(key = lambda i: i[1])  # по возрастанию
print(x_sort)
x_sort.sort(key = lambda i: i[1], reverse=True)  # по убыванию
print(x_sort)

# 4 задача
d1 = {'a': 1, 'b': 2}
d2 = {'c': 5, 'e': 3, 'f': 0}
d3 = {'h': 1, 'r': 9}
d = {}
for i in d1,d2,d3:
    d.update(i.items())
print(d)


