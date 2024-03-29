# 참고 : https://dev-scratch.tistory.com/m/133

import sys
input = sys.stdin.readline

def rotate(s):
    # 스티커를 시계 방향으로 90도 회전시키는 함수
    s = zip(*s[::-1])
    return [list(e) for e in s]

def put(sticker):
    # 스티커를 노트북에 붙일 수 있는지 확인하고, 붙일 수 있다면 노트북에 붙이는 함수
    sr, sc = len(sticker), len(sticker[0])

    for x in range(n - sr + 1):
        for y in range(m - sc + 1):
            if compare(x, y, sr, sc, sticker):
                # 스티커를 붙일 수 있는 위치를 찾았다면, 실제로 붙임
                for sx in range(sr):
                    for sy in range(sc):
                        laptop[x + sx][y + sy] += sticker[sx][sy]
                return True

    return False

def compare(x, y, sr, sc, sticker):
    # 스티커를 특정 위치에 붙일 수 있는지 없는지를 확인하는 함수
    for sx in range(sr):
        for sy in range(sc):
            if laptop[x + sx][y + sy] == sticker[sx][sy] == 1:
                # 노트북과 스티커가 겹치는 부분이 있으면 False 반환
                return False

    return True

n, m, k = map(int, input().split())

laptop = [[0] * m for _ in range(n)] # 노트북을 0으로 초기화
stickers = [] # 스티커들을 저장할 리스트

for _ in range(k):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    stickers.append(sticker) # 스티커 정보 입력 받기

for sticker in stickers:
    for i in range(4):
        if put(sticker):
            # 스티커를 붙일 수 있으면 다음 스티커로 넘어감
            break
        sticker = rotate(sticker) # 스티커를 회전시키고 다시 시도

cnt = sum(map(sum, laptop)) # 노트북에 붙은 스티커의 총 칸 수 계산

print(cnt) # 결과 출력