# 들어간 차와 나온차에서 나온차의 첫번째와 들어간 차의 첫번째가 같을 때까지 반복문으로 돌리고 같아 지면 그 때에서의 뒤의 차들이 들어간 차의 리스트와 같은지 비교하고 추월한 차의 수를 셌는데 실패

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