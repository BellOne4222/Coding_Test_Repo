# 참고 : https://phaskal.tistory.com/entry/Python3-%EB%94%94%EC%A7%80%ED%84%B8-%EC%88%AB%EC%9E%90-%EC%B0%8D%EA%B8%B0
# 

# s: LCD의 높이, n: 표현할 숫자
s, n = map(int, input().split())

# 입력된 숫자를 문자열로 변환
n = str(n)

# LCD의 전체 너비를 계산
m = 2 * s + 3

# LCD를 저장할 2차원 리스트를 초기화
ans = [[" "]*((s+2)*(len(n))+(len(n)-1)) for _ in range(m)]

# LCD의 첫 번째 숫자부터 마지막 숫자까지 반복
st = 0
for i in n:
    if i == '1':
        # '1'을 그릴 때, 세로 막대를 그림
        st += s + 1
        for j in range(1, 1 + s):
            ans[j][st] = "|"
        for j in range(2 + s, m - 1):
            ans[j][st] = "|"
        st += 2
    elif i == '2':
        # '2'를 그릴 때, 일부 수평 및 수직 선을 그림
        for j in range(2 + s, m - 1):
            ans[j][st] = "|"
        st += 1
        for _ in range(s):
            ans[0][st], ans[(m - 1) // 2][st], ans[m - 1][st] = "-", "-", "-"
            st += 1
        for j in range(1, 1 + s):
            ans[j][st] = "|"
        st += 2
    # '3', '4', '5', '6', '7', '8', '9', '0'에 대한 그리기 로직도 동일하게 반복합니다.
    # 각 숫자에 따라 다양한 수평 및 수직 선을 그리고 st 값을 업데이트합니다.

# LCD 출력
for a in ans:
    print("".join(a))