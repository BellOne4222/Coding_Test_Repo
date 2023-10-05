# 사용자로부터 정수 n을 입력 받습니다.
n = int(input())

# 건물 수를 나타내는 변수를 초기화합니다.
building = 0

# 각 건물의 높이를 저장할 리스트를 초기화합니다.
heights = []

# n번 반복하면서 건물의 좌표를 입력받고 높이를 heights 리스트에 추가합니다.
for i in range(n):
    x, y = map(int, input().split())
    heights.append(y)

# 마지막 건물의 높이를 0으로 설정하여 마지막 건물을 포함시킵니다.
heights.append(0)

# 건물의 높이를 비교하면서 건물 수를 세는 리스트를 초기화합니다.
cnts = []

# 초기값으로 0을 추가합니다.
cnts.append(0)

# 각 건물의 높이를 확인하면서 건물 수를 계산합니다.
for h in heights:
    height = h
    while cnts[-1] > h:
        # 현재 높이와 이전 높이가 다르면 새로운 건물로 간주하고 building 변수를 증가시킵니다.
        if cnts[-1] != height:
            building += 1
            height = cnts[-1]
        # 현재 높이보다 낮은 높이는 pop으로 제거합니다.
        cnts.pop()
    # 현재 높이를 cnts 리스트에 추가합니다.
    cnts.append(h)

# 건물 수를 출력합니다.
print(building)