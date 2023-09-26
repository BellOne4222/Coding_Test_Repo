# 나온차의 인덱스와 들어간 차의 인덱스를 같은 차 이름을 비교를 해서 들어간 차의 인덱스가 나온 차의 인덱스보다 크거나 같으면 -> 위치가 바뀌었으면 추월했다고 생각해서 구현했지만 실패

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