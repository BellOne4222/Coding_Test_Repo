def check_secret_menu(M, N, K, secret_buttons, user_buttons):
    # 비밀 메뉴 조작법의 길이가 사용자의 버튼 조작보다 길면 정상적인 식권이 발매된다
    if M > N:
        return "normal"
    
    # 비밀 메뉴 조작법과 첫 번째 윈도우의 부분 리스트를 비교하여 일치 여부를 확인한다
    window = user_buttons[:M]
    if window == secret_buttons:
        return "secret"
    
    # 슬라이딩 윈도우를 이용하여 비밀 메뉴 조작법과 일치하는지 확인한다
    for i in range(N - M):
        # 윈도우를 오른쪽으로 한 칸 이동하고, 새로 추가된 버튼을 비교한다
        window.pop(0)
        window.append(user_buttons[i + M])
        if window == secret_buttons:
            return "secret"
    
    # 비밀 메뉴 조작법과 일치하는 부분을 찾지 못했으면 정상적인 식권이 발매된다
    return "normal"

# 입력 받기
M, N, K = map(int, input().split())
secret_buttons = list(map(int, input().split()))
user_buttons = list(map(int, input().split()))

# 비밀 메뉴 확인
result = check_secret_menu(M, N, secret_buttons, user_buttons)
print(result)