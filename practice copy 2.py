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
    
    
    
o_idx= 0
i_idx = 0

while True:
    if outer[o_idx] != inner[0]:
        o_idx += 1
        passing += 1
    else:
        break


compare = outer[o_idx:]
for k in range(len(compare)):
    if outer[o_idx] == inner[i_idx]:
        o_idx += 1
        i_idx += 1
    else:
        passing += 1
        o_idx += 1


print(passing)