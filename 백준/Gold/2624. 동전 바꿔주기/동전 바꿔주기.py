import sys
my_input = sys.stdin.readline

t = int(my_input())
k = int(my_input())
coins = [list(map(int, my_input().split())) for _ in range(k)]

result = [0] * (t + 1)
result[0] = 1

for p, n in coins:
	for i in range(t, 0, -1):
		for j in range(1, n + 1):
			answer = i - (p * j)
			if answer >= 0:
				result[i] += result[answer]

print(result[t])
