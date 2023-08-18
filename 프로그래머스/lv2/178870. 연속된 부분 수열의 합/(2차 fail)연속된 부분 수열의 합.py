# 1차와 비슷한 로직에 누적합과 구간합 방식으로 누적합 배열을 만들어서 구간합의 결과를 배열에 넣어서 결과를 반환하는 방식으로 구현하였으나 시간 복잡도가 O(N^2)으로 시간 초과로 인해 실패...

def solution(sequence, k):
    s_idx, e_idx = 0, 0
    if k not in sequence:
        check = []
        n = len(sequence)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + sequence[i - 1]

        for i in range(n):
            for j in range(i + 1, n + 1):
                if prefix_sum[j] - prefix_sum[i] == k:
                    if check and len(check[0]) > j - i:
                        check.pop()
                        check.append(sequence[i:j])
                        s_idx, e_idx = i, j - 1
                    elif len(check) == 0:
                        check.append(sequence[i:j])
                        s_idx, e_idx = i, j - 1
    else:
        s_idx = sequence.index(k)
        e_idx = sequence.index(k)

    return [s_idx, e_idx]
    