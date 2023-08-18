# 연산의 나머지는 나머지들의 연산이다라는 아이디어를 사용해 solve

import sys

K, P, N = map(int, sys.stdin.readline().split())

virus = K * pow(P, N, 1000000007)

final_virus = virus % 1000000007

print(final_virus)