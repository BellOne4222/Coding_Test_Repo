# 1926 간단한 369 게임

T = int(input())
hypen = ["3", '6', '9']
ans = ''
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    cnt = 0
    num = str(test_case) # 숫자들을 문자열 변환
    for i in num:
        if i in hypen: # i가 369 중 하나이면
            cnt += 1 
    if cnt == 0: # cnt가 0이면 369가 아니므로 ans에 숫자 출력
        ans += num
    else:
        for _ in range(0, cnt): # cnt 개수 만큼
            ans += '-' # 하이픈 출력
    ans += ' ' # 공백

print(ans)
    