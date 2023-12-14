import sys  # sys 모듈을 불러옵니다.

n = int(sys.stdin.readline())  # 상자의 개수를 입력 받습니다.
boxes = list(map(int, sys.stdin.readline().split()))  # 각 상자의 크기를 리스트로 입력 받습니다.

dp_table = [1] * n  # 각 상자마다 최소한 1개는 넣을 수 있으므로 1로 초기화합니다.

for i in range(n):  # 모든 상자에 대해 반복합니다.
    for j in range(i):  # 현재 상자 이전의 상자들을 확인합니다.
        if boxes[i] > boxes[j]:  # 현재 상자를 이전 상자에 넣을 수 있는지 확인합니다.
            dp_table[i] = max(dp_table[i], dp_table[j] + 1)  # 현재 상자까지의 최대 개수와 새로운 상자를 넣었을 때의 개수를 비교하여 최대값을 저장합니다.

print(max(dp_table))  # 저장된 값 중 최대값을 출력합니다.