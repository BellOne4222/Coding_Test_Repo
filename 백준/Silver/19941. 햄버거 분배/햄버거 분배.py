import sys

# 첫 줄에서 N(식탁의 길이)과 K(햄버거를 선택할 수 있는 거리)를 입력받습니다.
n, k = map(int, sys.stdin.readline().split())

# 두 번째 줄에서 식탁의 상태를 문자열로 입력받아 리스트로 변환합니다.
table = list(map(str, sys.stdin.readline().rstrip()))

# 햄버거가 먹혔는지를 기록하는 리스트를 초기화합니다. 초기에는 모든 값이 False로 설정됩니다.
eaten_burger = [False] * n

# 햄버거를 먹은 사람의 수를 저장하는 변수입니다.
eaten_people = 0

# 식탁의 각 위치를 순회합니다.
for i in range(n):
    # 현재 위치에 사람이 있는 경우에만 아래 코드를 실행합니다.
    if table[i] == "P":
        # 사람의 위치 i에서 거리가 K 이하인 모든 위치를 확인합니다.
        for j in range(i - k, i + k + 1):
            # j가 식탁의 범위를 벗어나지 않도록 체크합니다.
            if 0 <= j < n:
                # 해당 위치에 햄버거가 있고, 아직 먹히지 않은 경우에만 햄버거를 먹습니다.
                if table[j] == "H" and not eaten_burger[j]:
                    # 해당 위치의 햄버거가 먹혔음을 기록합니다.
                    eaten_burger[j] = True
                    # 햄버거를 먹은 사람의 수를 증가시킵니다.
                    eaten_people += 1
                    # 한 사람이 먹을 수 있는 햄버거는 하나이므로, 더 이상 탐색하지 않고 탈출합니다.
                    break

# 최종적으로 먹을 수 있는 햄버거의 최대 수를 출력합니다.
print(eaten_people)
