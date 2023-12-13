import sys  # sys 모듈을 불러옵니다.

t = int(sys.stdin.readline())  # 테스트 케이스의 개수를 입력 받습니다.

for _ in range(t):  # 각 테스트 케이스에 대해 반복합니다.
    dp_table = [0] * 101  # 동적 프로그래밍 테이블을 초기화합니다. 최대 크기는 100까지이므로 101개의 공간을 만듭니다.
    n = int(sys.stdin.readline())  # 현재 테스트 케이스의 N 값을 입력 받습니다.

    # 처음 5개의 값을 미리 설정합니다.
    dp_table[1] = 1 # dp_table[1]
    dp_table[2] = 1 # dp_table[1]
    dp_table[3] = 1 # dp_table[1]
    dp_table[4] = 2 # dp_table[1] + dp_table[3]
    dp_table[5] = 2 # dp_table[4]

    # 만약 N이 6보다 작으면 미리 설정된 값에서 해당 값을 가져와 출력합니다.
    if n < 6:
        print(dp_table[n])
    else:
        # N이 6 이상인 경우, 동적 프로그래밍을 사용하여 값을 계산합니다.
        for i in range(6, n + 1):  # 6부터 N까지의 값을 계산합니다.
            dp_table[i] = dp_table[i - 5] + dp_table[i - 1]  # 주어진 규칙에 따라 값을 갱신합니다.

        print(dp_table[n])  # 결과 값을 출력합니다.