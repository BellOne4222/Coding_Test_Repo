import sys

n,m,k = map(int,sys.stdin.readline().split())

graph = [[0]* n for _ in range(m)]

for _ in range(k):

  r,c = map(int,sys.stdin.readline().split())
  
  sticker_graph = [[0]*c for _ in range(r)]
  
  for sticker in range(r):
    sticker_graph[sticker] = list(map(int, sys.stdin.readline().split()))
  
  print(sticker_graph)  

    
