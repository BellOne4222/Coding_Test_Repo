import sys

n,k = map(int, sys.stdin.readline().split())

table = list(map(str, sys.stdin.readline().rstrip()))     

visited = [False] * n

eaten = 0

for i in range(n):
    if table[i] == "P":
        for j in range(i-k, i+k+1):
            if 0 <= j < n:
                if table[j] == "H" and not visited[j]:
                    visited[j] = True
                    eaten += 1
                    break

print(eaten)