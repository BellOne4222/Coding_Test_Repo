n = int(input())

inner = []
outer = []

passing = 0



for i in range(1, 2*n+1):
    if i <= n:
        inner_car = input()
        inner.append(inner_car)

    else:
        outer_car = input()
        outer.append(outer_car)
    
    
    
for j in range(n):
    if outer[j] != inner[0]:
        passing += 1
        inner.remove(outer[j])
    else:
        inner.pop(0)


print(passing)