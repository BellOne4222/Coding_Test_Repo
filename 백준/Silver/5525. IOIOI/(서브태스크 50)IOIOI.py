# 서브태스크 50점 solve
# 서브테스크 2는 1000000 * 1000000이기 때문에 통과할 수 없다.

import sys

# n을 입력으로 받음: 'IO' 패턴을 얼마나 반복할 것인지
n = int(sys.stdin.readline().rstrip())

# 문자열 패턴 'IO'를 생성
p = ""
for i in range((2 * n) + 1):
    if i % 2 == 0:
        p += "I"
    else:
        p += "O"

# m을 입력으로 받음: 대상 문자열 s의 길이
m = int(sys.stdin.readline().rstrip())

# s를 입력으로 받음: 'IO' 패턴을 찾을 문자열
s = sys.stdin.readline().rstrip()

# 패턴이 등장한 횟수를 저장하는 변수
p_cnt = 0

# 문자열 s를 순회하면서 패턴 p와 일치하는 부분을 찾음
for i in range(m - len(p) + 1):
    # s에서 패턴 p의 길이만큼 문자열을 추출하여 비교
    compare = s[i:i + len(p)]
    if compare == p:  # 추출한 부분과 패턴 p가 일치하면
        p_cnt += 1  # 일치하는 패턴이 발견되었으므로 카운트 증가

# 패턴 p가 문자열 s에서 몇 번 나타났는지 출력
print(p_cnt)