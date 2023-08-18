def check_secret_menu(M, N, secret_buttons, user_buttons):
    # 비밀 메뉴 조작법의 길이가 사용자의 버튼 조작보다 길면 정상적인 식권이 발매된다
    if M > N:
        return "normal"
    
    # 모든 가능한 부분 리스트를 생성하여 비밀 메뉴 조작법과 일치하는지 확인한다
    for i in range(N - M + 1):
        for j in range(M):
            if user_buttons[i + j] != secret_buttons[j]:
                break
        else:
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