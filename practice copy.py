import sys

n,m = map(int,sys.stdin.readline().split())

blueray = list(map(int,sys.stdin.readline().split())) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

rng = n // m

left = blueray[:rng]
mid = blueray[rng:(n-rng)]
right = blueray[(n-rng):]

print(left, mid, right)