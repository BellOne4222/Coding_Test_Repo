import sys

# 사용자로부터 입력을 받습니다.
a, p = map(int, sys.stdin.readline().split())

# 중복을 제외한 수들을 담을 리스트를 생성하고 초기값인 a를 추가합니다.
non_duplicate = [a]

# 수열을 생성하는 과정입니다.
while True:
    duplicate = str(non_duplicate[-1])  # 리스트의 마지막 요소를 문자열로 변환합니다.
    compare = 0
    # 각 자리의 숫자를 P번 곱하여 합을 구합니다.
    for i in duplicate:
        compare += int(i) ** p
    # 이미 나온 값이라면 반복을 멈춥니다.
    if compare in non_duplicate:
        break
    non_duplicate.append(compare)  # 중복되지 않은 값이면S 리스트에 추가합니다.

# 반복되는 부분을 제외하고 남는 수들의 개수를 출력합니다.
print(non_duplicate.index(compare))