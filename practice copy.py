import sys

n = int(sys.stdin.readline())  # 선분의 개수 N을 입력받습니다.

line_lst = []  # 선분을 저장할 리스트입니다.

for _ in range(n):
  cur_line = list(map(int, sys.stdin.readline().split()))  # 현재 선분의 시작점과 끝점을 입력받습니다.
  
  if not line_lst:  # 선분 리스트가 비어있다면, 현재 선분을 리스트에 추가합니다.
    line_lst.append(cur_line)
    
  else:
    if line_lst[-1][1] >= cur_line[0]:  # 현재 선분의 시작점이 마지막에 저장된 선분의 끝점보다 작거나 같으면, 겹치는 부분이 있습니다.
      if cur_line[1] > line_lst[-1][1]:  # 현재 선분의 끝점이 마지막에 저장된 선분의 끝점보다 크다면, 끝점을 업데이트합니다.
        line_lst[-1][1] = cur_line[1]
      else:  # 그렇지 않으면, 현재 선분은 완전히 포함되므로 추가 작업 없이 계속합니다.
        continue
    else:  # 겹치지 않는 새로운 선분이면, 리스트에 추가합니다.
      line_lst.append(cur_line)
  
total_length = 0  # 선분들의 총 길이를 저장할 변수입니다.

for i in line_lst:  # 최종적으로 겹치지 않는 선분들만 남게 됩니다. 이 선분들의 길이를 합산합니다.
  total_length += (abs(i[1]-i[0]))  # 각 선분의 길이(끝점 - 시작점)를 총 길이에 더합니다.

print(total_length)  # 선분들의 총 길이를 출력합니다.

  

    
