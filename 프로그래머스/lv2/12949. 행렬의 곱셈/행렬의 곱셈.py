# 행렬의 곱셈을 공부하고 식 그대로 구현

def solution(arr1, arr2):
    m = len(arr1) # arr1의 세로 
    k_1 = len(arr1[0]) # arr1의 가로
    k_2 = len(arr2) # arr2의 세로
    n = len(arr2[0]) # arr2의 가로
    
    # 행렬의 곱셈 : k의 값이 같을 때, 두 행렬의 곱은 (m * k) * (k * n) = m * n 이다.
    # 행렬 공부한 링크 : https://mathbang.net/562#gsc.tab=0
    result = [[0 for _ in range(n)] for _ in range(m)] # 결과는 m * n 크기의 배열이 나와야 하므로 0으로 이루어진 배열 생성
    
    for i in range(m):
        for j in range(n):
            for k in range(k_1): # 공통 k(공통 인덱스)
                result[i][j] += arr1[i][k] * arr2[k][j] # result[0][1] = arr1[0][1] * arr2[1][0]
    
    return result
            
            
    
        
    