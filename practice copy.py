import sys  # sys 모듈을 불러옵니다.
from collections import deque

p = int(sys.stdin.readline())

board = [['*' for _ in range(3)] for _ in range(3)]

print(board)

for i in range(p):
    right_board = []
    for j in range(3):
        line = list(map(str, sys.stdin.readline().rstrip()))
        right_board.append(line)
    
    

