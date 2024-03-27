import sys

n = int(sys.stdin.readline())

line_lst = []

for _ in range(n):
  cur_line = list(map(int, sys.stdin.readline().split()))
  
  if not line_lst:
    line_lst.append(cur_line)
    
  else:
    if line_lst[-1][1] >= cur_line[0]:
      if cur_line[1] > line_lst[-1][1]:
        line_lst[-1][1] = cur_line[1]
      else:
        continue
    else:
      line_lst.append(cur_line)
  
total_length = 0

for i in line_lst:
  total_length += (abs(i[1]-i[0]))

print(total_length)