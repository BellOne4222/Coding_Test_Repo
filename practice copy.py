import sys

# 테스트 케이스 수를 입력받는다.
t = int(sys.stdin.readline())

# 테스트 케이스마다 반복
for _ in range(t):
    
    # n과 m 값을 입력받는다. n은 배열 A의 크기, m은 배열 B의 크기
    n, m = map(int, sys.stdin.readline().split())
    
    # 배열 A와 B를 각각 입력받는다.
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    b = list(map(int, sys.stdin.readline().rstrip().split()))
    
    # 배열 B를 오름차순으로 정렬하여 이진 탐색이 가능하도록 준비한다.
    b.sort()
    
    # 결과를 저장할 변수 초기화
    result = 0
    
    # 배열 A의 각 요소에 대해 가장 가까운 B의 값을 찾는다.
    for num in a:
        start = 0
        end = m - 1
        
        # 이진 탐색을 통해 num에 가장 가까운 값을 찾는다.
        while start < end:
            mid = (start + end) // 2
            
            # 중간 값이 num보다 작거나 같으면 start를 오른쪽으로 옮긴다.
            if b[mid] <= num:
                start = mid + 1
            else:
                # 중간 값이 num보다 크다면 end를 왼쪽으로 옮긴다.
                end = mid
        
        # 이진 탐색이 끝난 후 가장 가까운 값이 결정된다.
        # 여기서 start는 num보다 큰 첫 번째 값을 가리킨다.
        if start == 0:
            # start가 0이라면 num보다 작은 값이 없으므로 b[0]이 가장 가까운 값이다.
            result += b[0]
        else:
            # num과 b[start] 또는 b[start-1] 중 어느 값이 더 가까운지 결정한다.
            if num - b[start - 1] > b[start] - num:
                result += b[start]
            else:
                result += b[start - 1]
    
    # 각 테스트 케이스에 대해 구한 결과를 출력한다.
    print(result)
        
            
        
             
        
    
    
    