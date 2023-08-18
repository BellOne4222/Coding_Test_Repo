# k가 sequence 안에 있으면 바로 안에 있는 k의 인덱스를 출력하고, 없으면 2개, 3개 늘려가면서 숫자를 인덱스 슬라이싱으로 합하면서 합이 k와 같은 인덱스 들을 반환하는 로직
# 시간 복잡도가 O(N^3)으로 시간 초과 실패...

def solution(sequence, k):
    s_idx, e_idx = 0, 0
    if k not in sequence:
        sums = 0
        a = 1
        check = []
        
        for i in range(len(sequence)-a):
            for j in range(a, len(sequence)):
                sums = sum(sequence[i:j+1])
                if sums == k:
                    if check and len(check[0]) > len(sequence[i:j+1]):
                        check.pop()
                        check.append(sequence[i:j+1])
                        s_idx, e_idx = i, j
                    elif len(check) == 0:
                        check.append(sequence[i:j+1])
                        s_idx, e_idx = i, j
                        
    else:
        s_idx = sequence.index(k)
        e_idx = sequence.index(k)
        
    return [s_idx, e_idx]