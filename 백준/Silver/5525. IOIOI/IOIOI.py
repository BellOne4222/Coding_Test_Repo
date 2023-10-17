# 참고 : https://aia1235.tistory.com/30

import sys

# n을 입력으로 받음: 'IOI' 패턴이 몇 번 반복되는지 찾을 때 사용
n = int(sys.stdin.readline().rstrip())

# m을 입력으로 받음: 문자열 s의 길이
m = int(sys.stdin.readline().rstrip())

# s를 입력으로 받음: 'IOI' 패턴을 찾을 대상 문자열
s = sys.stdin.readline().rstrip()

# 인덱스 초기화
idx = 0

# 'IOI' 패턴을 찾은 횟수
count = 0

# 최종 결과 (n 개의 'IOI' 패턴이 연속으로 등장한 횟수)
result = 0

# 문자열을 순회하면서 'IOI' 패턴을 찾음
while idx < (m - 1):
    # 'IOI' 패턴을 찾았을 때
    if s[idx:idx + 3] == 'IOI':
        count += 1
        idx += 2  # 'I' 다음 'O'로 바로 이동
        if count == n:
            result += 1  # n 개의 'IOI' 패턴이 연속으로 등장
            count -= 1  # 다음 패턴 검사를 위해 count 초기화
    else:
        idx += 1  # 'IOI' 패턴이 아닌 경우, 다음 인덱스로 이동
        count = 0  # 연속 패턴을 찾던 중에 끊겼으므로 count 초기화

# 최종 결과 출력
print(result)