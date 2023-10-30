# 시간 복잡도 : O(N^2)

import sys

n,k = map(int,sys.stdin.readline().split(" "))

result = -100 * k

temperature = list(map(int, sys.stdin.readline().split()))

left = 0
right = k 

while True:
    if right > n:
        break
    temperatures = sum(temperature[left:right])
    if temperatures <= result:
        continue
    else:
        result = temperatures
    left += 1
    right += 1

print(result)