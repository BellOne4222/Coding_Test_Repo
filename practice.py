n = int(input())

inner = dict()
outer = dict()

inner_name = []

passing = 0



for i in range(1, 2*n+1):
    if i <= n:
        inner_car = input()
        inner_name.append(inner_car)
        inner[inner_car] = i
    else:
        outer_car = input()
        outer[outer_car] = i-n
    
    
    

for k in range(len(inner_name)):
    if inner[inner_name[k]] >= outer[inner_name[k]]:
        passing += 1

print(passing)