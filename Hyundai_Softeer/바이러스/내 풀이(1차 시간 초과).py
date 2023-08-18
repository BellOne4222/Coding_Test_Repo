import sys

K, P, N = map(int,sys.stdin.readline().split())

virus = K * (pow(P, N))

ans = virus % 1000000007

print(ans)