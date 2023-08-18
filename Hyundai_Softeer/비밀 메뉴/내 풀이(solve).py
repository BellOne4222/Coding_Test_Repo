import sys

m, n, k = map(int, input().split())

secret_menu = list(map(int, input().split()))

user = list(map(int, input().split()))

if len(secret_menu) > len(user): #비밀 메뉴 조작 보다 사용자 조작이 더 길면 normal 반환
    ans = "normal"

for i in range(len(user)):
    if user[i:m+i] == secret_menu: # 비밀 메뉴 조작 수만큼 사용자 조작 리스트에서 잘라서 비교를 하며 같은 구간이 있으면 secret 반환하고 아니면 normal 반환
        ans = "secret"
        break
    else:
        ans = "normal"

print(ans)

# 비밀 메뉴 조작 수만큼 사용자 조작 리스트에서 잘라서 비교를 하며 같은 구간이 있으면 secret 반환하고 아니면 normal, 비밀 메뉴 조작 보다 사용자 조작이 더 길면 normal 반환