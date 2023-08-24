def solution(triangle):
    triangle = triangle[::-1]
    # 	[[4, 5, 2, 6, 5], [2, 7, 4, 4], [8, 1, 0], [3, 8], [7]]
    
    for i in range(len(triangle)):
        for j in range(len(triangle[i])-1):
            triangle[i+1][j] = max((triangle[i][j] + triangle[i+1][j]) , (triangle[i][j+1] + triangle[i+1][j]))
    
    return triangle[len(triangle)-1][0]
            
            
        
    