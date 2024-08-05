H, W = map(int, input().split())
N = int(input())
stickers = [tuple(map(int, input().split())) for _ in range(N)]

max_area = 0

for i in range(N):
    for j in range(i + 1, N):
        R1, C1 = stickers[i]
        R2, C2 = stickers[j]

        for (r1, c1) in [(R1, C1), (C1, R1)]:
            for (r2, c2) in [(R2, C2), (C2, R2)]:
                if (r1 + r2 <= H and max(c1, c2) <= W) or (c1 + c2 <= W and max(r1, r2) <= H):
                    max_area = max(max_area, r1 * c1 + r2 * c2)
                if (r1 + c2 <= H and max(c1, r2) <= W) or (c1 + r2 <= W and max(r1, c2) <= H):
                    max_area = max(max_area, r1 * c1 + r2 * c2)
                if (c1 + r2 <= H and max(r1, c2) <= W) or (r1 + c2 <= W and max(c1, r2) <= H):
                    max_area = max(max_area, r1 * c1 + r2 * c2)
                if (c1 + c2 <= H and max(r1, r2) <= W) or (r1 + r2 <= W and max(c1, c2) <= H):
                    max_area = max(max_area, r1 * c1 + r2 * c2)

print(max_area)
