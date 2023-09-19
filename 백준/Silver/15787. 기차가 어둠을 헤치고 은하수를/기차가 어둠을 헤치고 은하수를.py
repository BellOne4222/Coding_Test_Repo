from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())   # n: 기차 수, m: 명령 수
order = list(tuple(map(int, input().split())) for _ in range(m))

train = [deque(0 for _ in range(20)) for _ in range(n)]
for i in range(m):
  if order[i][0] == 1:
    train[order[i][1]-1][order[i][2]-1] = 1
  elif order[i][0] == 2:
    train[order[i][1]-1][order[i][2]-1] = 0
  elif order[i][0] == 3:
    train[order[i][1]-1].rotate(1)
    train[order[i][1]-1][0] = 0
  else:
      train[order[i][1]-1].rotate(-1)
      train[order[i][1]-1][-1] = 0

output_train = []
for i in range(n):
  if train[i] not in output_train:
    output_train.append(train[i])

print(len(output_train))