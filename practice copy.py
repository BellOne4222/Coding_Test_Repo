import sys
from collections import deque

def bfs(s,t,kick):
    q = deque()
    q.append((s,t,kick))
    
    while q:
        me, opponent, kicks = q.popleft()
        
        if me <= opponent:
            q.append((me*2,opponent+3,kicks+1))
            q.append((me+1,opponent,kicks+1))
            
            if me == opponent:
                return kicks 
    

c = int(sys.stdin.readline())

for _ in range(c):
    kick = 0
    s,t = map(int, sys.stdin.readline().split())
    print(bfs(s,t,kick))

