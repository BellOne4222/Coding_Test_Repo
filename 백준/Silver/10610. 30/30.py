n = str(input())

n = list(n)

n.sort(reverse = True)

num = ''.join(n)
num = int(num)

if num % 30 == 0:
    print(num)
else:
    print(-1)


    