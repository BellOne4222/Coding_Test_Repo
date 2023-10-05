# 사용자로부터 정수 n을 입력 받습니다.
n = int(input())

# 탑의 높이를 입력 받아 리스트로 저장합니다.
towers = list(map(int, input().split()))

# 높이 순서대로 탑을 저장할 스택을 초기화합니다.
stack = []

# 결과 리스트를 초기화하고 모든 요소를 0으로 채웁니다.
result = [0 for i in range(n)]

# 각 탑에 대한 처리를 수행합니다.
for i in range(n):
    # 스택에 요소가 있으면서 스택의 가장 위 탑의 높이가 현재 탑보다 높을 때까지 반복합니다.
    while stack:
        if stack[-1][1] > towers[i]:
            # 스택의 가장 위 탑이 현재 탑을 수신하면 결과 리스트에 해당 인덱스를 저장하고 반복을 종료합니다.
            result[i] = stack[-1][0] + 1
            break
        else:
            # 스택의 가장 위 탑이 현재 탑을 수신하지 못하면 스택에서 제거합니다.
            stack.pop()
    
    # 현재 탑을 스택에 추가합니다. 스택에는 현재 탑의 인덱스와 높이를 저장합니다.
    stack.append([i, towers[i]])

# 결과 리스트를 문자열로 변환하여 출력합니다.
print(" ".join(map(str, result)))