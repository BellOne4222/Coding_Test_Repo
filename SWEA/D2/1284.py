# 1284 수도 요금 경쟁

# 한 달간 수도 사용량 : W
# A사 : 1L당 P => W = W * P
# B사 : R리터 이하: 기본요금 Q + 초과하면 1L당 S => (1) W <= R : Q, (2) W > R : Q + S * (W - R) 

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    A = (W * P)
    if W <= R:
        B = Q
    elif W > R:
        B = (Q + S * (W - R))
    if A > B:
        answer = B
    else:
        answer = A
    print("#{} {}".format(test_case, answer))
