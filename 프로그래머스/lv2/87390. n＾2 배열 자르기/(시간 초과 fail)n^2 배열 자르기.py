# 시간 초과로 실패
# 문제 설명 그대로 구현을 했지만 n 범위 자체가 시간 초과가 날 수 있는 범위였습니다...
# 시간 복잡도 :  O(n^2 + right - left)

def solution(n, left, right):
    
    
    # 1: n행 n열 크기의 비어있는 2차원 배열을 만듭니다.
    grid = [[0 for _ in range(n)] for _ in range(n)]
    
    # 2: i = 1, 2, 3, ..., n에 대해서, 다음 과정을 반복합니다. 1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
    for i in range(n): # (i,j) 경우 i와 j 중 큰 값으로 해당 칸의 값으로 변경, 같은 경우 i 값으로 변경
        for j in range(n):
            if i > j:
                grid[i][j] = i+1
            elif i < j:
                grid[i][j] = j+1
            else:
                grid[i][j] = i+1
    
    # 3: 1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.
    new_arr = []
    
    for i in grid:
        new_arr += i
    
    # 4: 새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지웁니다.
    result = new_arr[left:right+1]
    
    return result