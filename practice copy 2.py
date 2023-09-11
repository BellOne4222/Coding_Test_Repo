a = 123
a = str(a)
b = list(a)
b.sort(reverse=True)
c = ''.join(b)
print(c)