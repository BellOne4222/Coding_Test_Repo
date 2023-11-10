import sys

n,m = map(int,sys.stdin.readline().split())

board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

print(board)