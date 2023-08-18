# 회전과 최솟값을 반환하는데 중점을 둔 문제라 heapq도 생각을 하여서 다른 풀이도 참고

import heapq

def solution(rows, columns, queries):
    answer = []
    
    #rowsXcolmns 배열 만들기
    arr = [[0]*(columns+1) for _ in range(rows+1)]
    
    num = 1
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            arr[i][j] = num
            num += 1
	
    #시계 방향으로 1칸 회전 명령 시행
    for r1, c1, r2, c2 in queries:
    	#위치가 변한 숫자들을 담을 배열
        nums = []
        #가장 첫 번째 숫자 temp에 저장하기
        temp = arr[r1][c1]
        
        #(r2, c1) -> (r1, c1)로 값 이동
        for r in range(r1, r2):
            arr[r][c1] = arr[r+1][c1]
            heapq.heappush(nums, arr[r+1][c1])
            
        #(r2, c2) -> (r2, c1)로 값 이동
        for c in range(c1, c2):
            arr[r2][c] = arr[r2][c+1]
            heapq.heappush(nums, arr[r2][c+1])
            
        #(r1, c2) -> (r2, c2)로 값 이동
        for r in range(r2, r1, -1):
            arr[r][c2] = arr[r-1][c2]
            heapq.heappush(nums, arr[r-1][c2])
            
        #(r1, c1) -> (r1, c2)로 값 이동
        for c in range(c2, c1+1, -1):
            arr[r1][c] = arr[r1][c-1]
            heapq.heappush(nums, arr[r1][c-1])
        arr[r1][c1+1] = temp
        heapq.heappush(nums, temp)
        
        #Min heap에서 pop하여 가장 작은 수 answer에 담아주기
        answer.append(heapq.heappop(nums))   
    
    return answer

#시간복잡도 = O(n), 공간복잡도 = O(n)