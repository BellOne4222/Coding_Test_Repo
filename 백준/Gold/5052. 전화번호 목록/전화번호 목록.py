import sys

t = int(sys.stdin.readline())  # 테스트 케이스의 개수 t를 입력받습니다.

for _ in range(t):  # 각 테스트 케이스에 대해 반복합니다.
  n = int(sys.stdin.readline())  # 전화번호의 수 n을 입력받습니다.
  
  cases = []  # 전화번호를 저장할 리스트를 초기화합니다.
  for i in range(n):  # n개의 전화번호에 대해 반복하며
    cases.append(sys.stdin.readline().rstrip())  # 각 전화번호를 리스트에 추가합니다.
  
  cases.sort()  # 전화번호 목록을 사전순으로 정렬합니다.
  
  flag = "YES"  # 일관성 있는 목록인지 여부를 저장할 변수입니다. 초기값은 "YES"로 설정합니다.
  
  for j in range(n-1):  # 정렬된 목록에서 인접한 전화번호를 비교합니다.
    # 현재 전화번호가 다음 전화번호의 접두어인 경우
    if cases[j] == cases[j+1][:len(cases[j])]:
      flag = "NO"  # 일관성이 없으므로 flag를 "NO"로 변경하고
      break  # 더 이상 검사할 필요가 없으므로 반복을 종료합니다.
  
  print(flag)  # 최종 결과를 출력합니다. (일관성 있는 목록인 경우 "YES", 아닌 경우 "NO")
